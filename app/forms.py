from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError

def is_float():
    message = ' - Should be a valid number.'

    def _is_float(_, field):
        try:
            float(field.data)
        except ValueError:
            raise ValidationError(field.label.text + message)

    return _is_float

def is_int():
    message = ' - Should be a valid number.'

    def _is_int(_, field):
        if not field.data.isdigit():
            raise ValidationError(field.label.text + message)

    return _is_int

def msg_data_required(fieldname):
    return DataRequired(message=fieldname + ' - This field is required.')

class TileMap(FlaskForm):
    lat = StringField('Latitude',
                      validators=[msg_data_required('Latitude'), is_float()],
                      render_kw={"placeholder": "Latitude"})

    lon = StringField('Longitude',
                      validators=[msg_data_required('Longitude'), is_float()],
                      render_kw={"placeholder": "Longitude"})

    zoom = StringField('Zoom',
                       validators=[msg_data_required('Zoom'), is_int()],
                       render_kw={"placeholder": "Zoom"})

    submit = SubmitField('Go!')