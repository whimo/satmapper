from keras.models import Model
from keras.layers import Input, Conv2D, MaxPooling2D, UpSampling2D
from keras.layers.normalization import BatchNormalization
from keras.layers.core import SpatialDropout2D, Activation
from keras import backend as K
from keras.layers.merge import concatenate
from keras.optimizers import Adam
import numpy as np


def preprocess_batch(batch):
    batch /= 256
    batch -= 0.5
    return batch


def dice_coef(y_true, y_pred):
    y_true_f = K.flatten(y_true)
    y_pred_f = K.flatten(y_pred)
    intersection = K.sum(y_true_f * y_pred_f)
    return (2.0 * intersection + 1.0) / (K.sum(y_true_f) + K.sum(y_pred_f) + 1.0)


def jacard_coef(y_true, y_pred):
    y_true_f = K.flatten(y_true)
    y_pred_f = K.flatten(y_pred)
    intersection = K.sum(y_true_f * y_pred_f)
    return (intersection + 1.0) / (K.sum(y_true_f) + K.sum(y_pred_f) - intersection + 1.0)


def jacard_coef_loss(y_true, y_pred):
    return -jacard_coef(y_true, y_pred)


def dice_coef_loss(y_true, y_pred):
    return -dice_coef(y_true, y_pred)


def double_conv_layer(x, size, dropout, batch_norm):
    if K.image_dim_ordering() == 'th':
        axis = 1
    else:
        axis = 3
    conv = Conv2D(size, (3, 3), padding='same')(x)
    if batch_norm is True:
        conv = BatchNormalization(axis=axis)(conv)
    conv = Activation('relu')(conv)
    conv = Conv2D(size, (3, 3), padding='same')(conv)
    if batch_norm is True:
        conv = BatchNormalization(axis=axis)(conv)
    conv = Activation('relu')(conv)
    if dropout > 0:
        conv = SpatialDropout2D(dropout)(conv)
    return conv


def unet_model(image_width, image_height, input_channels, output_channels,
               dropout=0.2, batch_norm=True):
    if K.image_dim_ordering() == 'th':
        inputs = Input((input_channels, image_height, image_width))
        axis = 1
    else:
        inputs = Input((image_height, image_width, input_channels))
        axis = 3
    filters = 32

    conv1 = double_conv_layer(inputs, filters, 0, batch_norm)
    pool1 = MaxPooling2D(pool_size=(2, 2))(conv1)

    conv2 = double_conv_layer(pool1, 2 * filters, 0, batch_norm)
    pool2 = MaxPooling2D(pool_size=(2, 2))(conv2)

    conv3 = double_conv_layer(pool2, 4 * filters, 0, batch_norm)
    pool3 = MaxPooling2D(pool_size=(2, 2))(conv3)

    conv4 = double_conv_layer(pool3, 8 * filters, 0, batch_norm)
    pool4 = MaxPooling2D(pool_size=(2, 2))(conv4)

    conv5 = double_conv_layer(pool4, 16 * filters, 0, batch_norm)
    pool5 = MaxPooling2D(pool_size=(2, 2))(conv5)

    conv6 = double_conv_layer(pool5, 32 * filters, 0, batch_norm)

    up7 = concatenate([UpSampling2D(size=(2, 2))(conv6), conv5], axis=axis)
    conv7 = double_conv_layer(up7, 16 * filters, 0, batch_norm)

    up8 = concatenate([UpSampling2D(size=(2, 2))(conv7), conv4], axis=axis)
    conv8 = double_conv_layer(up8, 8 * filters, 0, batch_norm)

    up9 = concatenate([UpSampling2D(size=(2, 2))(conv8), conv3], axis=axis)
    conv9 = double_conv_layer(up9, 4 * filters, 0, batch_norm)

    up10 = concatenate([UpSampling2D(size=(2, 2))(conv9), conv2], axis=axis)
    conv10 = double_conv_layer(up10, 2 * filters, 0, batch_norm)

    up11 = concatenate([UpSampling2D(size=(2, 2))(conv10), conv1], axis=axis)
    conv11 = double_conv_layer(up11, filters, dropout, batch_norm)

    conv_final = Conv2D(output_channels, (1, 1))(conv11)
    conv_final = Activation('sigmoid')(conv_final)

    model = Model(inputs, conv_final, name="GEO_UNET")
    return model


class GeoUNet(object):
    def __init__(self, image_width, image_height, input_channels, output_channels,
                 learning_rate=0.001, pretrained=True, weights='weights.hdf5', dropout=0.2, batch_norm=True):
        self.model = unet_model(image_width, image_height, input_channels, output_channels,
                                dropout, batch_norm)

        self.model.compile(optimizer='adam', loss=dice_coef_loss, metrics=[dice_coef])
        if pretrained:
            self.model.load_weights(weights)

    def generate_mask(self, image):
        image = image.astype(np.float32)
        image /= 256
        image -= 0.5
        return self.model.predict(image.reshape((1, 256, 256, 3))).round().reshape((256, 256))
