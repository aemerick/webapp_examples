from flask import render_template
from flask import request, redirect, url_for
from map_app import app


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mapclick')
def mapclick():
    """
    Takes in lat and lng values from user click on the
    map, and returns user to index (where the map is located)
    while passing lat and lng as arguments, where they are
    read and saved. I highly doubt this is the best way to
    actually do this!!!
    """

    lat = request.args.get('lat','',type=float)
    lng = request.args.get('lng','',type=float)

    return redirect( url_for('index', lat=lat, lng=lng))
