from flask import render_template, url_for, flash, redirect
from flask_server import app

@app.route("/")
@app.route("/home")
def home():
    return
