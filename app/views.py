from . import app
from .forms import TileMap
from .coordinate_translations import deg2num
from flask import render_template, redirect, flash
import requests


@app.route('/', methods=['GET', 'POST'])
def index():
    with open('parsed_maps/map.txt') as osm_map:
        form = TileMap()
        if form.validate_on_submit():
            try:
                x, y = deg2num(float(form.lat.data), float(form.lon.data), int(form.zoom.data))
            except ValueError:
                flash('Unexpected error occurred')
                return render_template('index.html', osm_raw_polygons=osm_map.read(), form=form)

            url = 'https://a.tiles.mapbox.com/v4/digitalglobe.316c9a2e/' +\
            '{}/{}/{}.png'.format(int(form.zoom.data), x, y) + '?access_token=' +\
            'pk.eyJ1IjoiZGlnaXRhbGdsb2JlIiwiYSI6ImNqZGFrZ2c2dzFlMWgyd2x0ZHdmMDB6NzYifQ.9Pl3XOO82ArX94fHV289Pg'

            response = requests.get(url)
            if response.status_code == 200:
                print('OK') # Success; TODO: change behavior
            else:
                flash('Could not fetch the tile from the tile server - perhaps, your coordinates are invalid.')

            return redirect('/')

        if form.errors:
            for _, err in form.errors.items():
                flash(err[0])

        return render_template('index.html', osm_raw_polygons=osm_map.read(), form=form)
