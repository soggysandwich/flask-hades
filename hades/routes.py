from hades import app
from flask import render_template
from hades.model import Advert


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/adverts')
def list_adverts():
    advert_list = Advert.query.all()
    return render_template('adverts.html', advert_list=advert_list)


@app.route('/keywords')
def keywords():
    return render_template('keywords.html')

