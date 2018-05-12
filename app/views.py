from . import app
from flask import render_template

@app.route('/')
def index():
    with open('parsed_maps/map.txt') as map:
        return render_template('index.html', polygons=map.read())