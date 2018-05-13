from . import app
from .forms import TileMap
from flask import render_template, redirect, flash

@app.route('/', methods=['GET', 'POST'])
def index():
    with open('parsed_maps/map.txt') as map:
        form = TileMap()
        if form.validate_on_submit():
            return redirect('/')

        if form.errors:
            for _, err in form.errors.items():
                flash(err[0])

        return render_template('index.html', polygons=map.read(), form=form)