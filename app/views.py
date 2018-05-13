from . import app
from .forms import TileMap
from .coordinate_translations import deg2num, img2list, num2deg
from flask import render_template, redirect, flash
import requests
from io import BytesIO
import numpy as np
from PIL import Image
from .model import GeoUNet
import os
import cv2


@app.route('/', methods=['GET', 'POST'])
def index():
    with open('parsed_maps/map.txt') as osm_map:
        form = TileMap()
        if form.validate_on_submit():
            try:
                x, y = deg2num(float(form.lat.data), float(form.lon.data), int(form.zoom.data))
            except ValueError:
                flash('Unexpected error occurred')
                return render_template('index.html', osm_raw_polygons=osm_map.read(), dg_raw_polygons=[],
                                       bounds_coord1 = 'null', bounds_coord2 = 'null', img_src = 'null', form=form)

            url = 'https://a.tiles.mapbox.com/v4/digitalglobe.316c9a2e/' +\
            '{}/{}/{}.png'.format(int(form.zoom.data), x, y) + '?access_token=' +\
            'pk.eyJ1IjoiZGlnaXRhbGdsb2JlIiwiYSI6ImNqZGFrZ2c2dzFlMWgyd2x0ZHdmMDB6NzYifQ.9Pl3XOO82ArX94fHV289Pg'

            response = requests.get(url)
            if response.status_code == 200:

                bounds_coord1 = num2deg(x, y + 1, int(form.zoom.data))
                bounds_coord2 = num2deg(x + 1, y, int(form.zoom.data))


                with open('tmpfile.png', 'wb') as fd:
                    fd.write(response.content)

                unet = GeoUNet(256, 256, 3, 1, weights='weights.hdf5')

                the_image = cv2.imread('tmpfile.png', cv2.IMREAD_COLOR)
                print('AAAAAAAAAAAAAAAAAAAAAA', the_image.shape)

                img = unet.highlight_objects(cv2.imread('tmpfile.png', cv2.IMREAD_COLOR))
                cv2.imwrite('the_tile.png', img)

                return render_template('index.html', osm_raw_polygons=osm_map.read(),
                                       dg_raw_polygons=[], bounds_coord1 = repr(list(bounds_coord1)),
                                       bounds_coord2 = repr(list(bounds_coord2)),
                                       img_src='tile.png',
                                       form=form)
            else:
                flash('Could not fetch the tile from the tile server - perhaps, your coordinates are invalid.')

        if form.errors:
            for _, err in form.errors.items():
                flash(err[0])

        return render_template('index.html', osm_raw_polygons=osm_map.read(), dg_raw_polygons=[],
                               bounds_coord1 = 'null', bounds_coord2 = 'null', img_src = 'null', form=form)


from flask import send_from_directory
@app.route('/tile.png')
def tile():
    return send_from_directory('..', 'the_tile.png')
