import os
from hades import app, db
from flask import render_template, redirect, url_for, flash
from hades.model import Advert, User
from hades.forms import RegisterForm, KeywordsForm, LoginForm
from flask_login import login_user,logout_user, login_required
from google.cloud import pubsub_v1
from google.cloud import datastore
import json

credential_path= '/home/me/Projects/flask-hades/hades/scripts/hades-privatekey-publisher-serviceaccount.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path



@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user_create = User(
            user=form.username.data,
            email_address=form.email_address.data,
            password=form.password1.data
        )

        db.session.add(user_create)
        db.session.commit()

        login_user(user_create)
        flash(f'Account created successfully , you are logged in as {user_create.user}',category='success')

        return redirect(url_for('list_adverts'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error on the form: {err_msg}', category='danger')

    return render_template('register.html', form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user=User.query.filter_by(user=form.username.data).first()
        if attempted_user and attempted_user.check_password(password_to_check=form.password.data):
                login_user(attempted_user)
                flash(f'Logged in as {attempted_user.user}',category='success')
                return redirect(url_for('list_adverts'))
        else:
            flash(f'Login failed , Please check user or password is correct', category='danger')

    return render_template('login.html', form=form)


@app.route('/adverts')
@login_required
def list_adverts():

    #advert_list = Advert.query.all()
    client=datastore.Client()
    adverts_query=client.query(kind="ebay-adverts")
    adverts=list(adverts_query.fetch(limit=20))
    print(adverts[0].key.flat_path[1])

    return render_template('adverts.html', advert_list=adverts)


@app.route('/keywords',methods=["GET", "POST"])
@login_required
def keywords():
    form = KeywordsForm()
    if form.validate_on_submit():


        publisher = pubsub_v1.PublisherClient()
        topic = 'projects/hades-cloud-330810/topics/search-keywords'

        attributes = {
            'Keyword1':form.keyword1.data

        }

        data = json.dumps(attributes)
        print(f'dict to json string {data}')


        data = data.encode('utf-8')


        result = publisher.publish(topic, data)
        flash(f'Keywords scheduled ,your id is { result.result() }, Please refresh this page in a few minutes'
                ,category='info')

        return redirect(url_for('list_adverts'))

    return render_template('keywords.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out', category='info')
    return redirect(url_for('home'))
