from hades import app,db
from flask import render_template, redirect, url_for, flash
from hades.model import Advert, User
from hades.forms import RegisterForm, KeywordsForm


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/register', methods=["GET","POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user_create = User(
            user=form.username.data,
            email_address=form.email_address.data,
            password_hash=form.password1.data
        )

        db.session.add(user_create)
        db.session.commit()

        return redirect(url_for('list_adverts'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error on the form: {err_msg}',category='danger')

    return render_template('register.html', form=form)


@app.route('/adverts')
def list_adverts():
    advert_list = Advert.query.all()
    return render_template('adverts.html', advert_list=advert_list)


@app.route('/keywords')
def keywords():
    form = KeywordsForm()
    return render_template('keywords.html', form=form)
