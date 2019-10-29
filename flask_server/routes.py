from flask import render_template, url_for, flash, redirect
from flask_server import app

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title='Home')

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/login")
def login():
    return render_template('login.html', title='Login')

@app.route("/signup")
def login():
    return render_template('login.html', title='Login')
