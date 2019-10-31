from flask import render_template, url_for, flash, redirect
from flask_server import app, db, bcrypt
from flask_server.forms import LogInForm, SignUpForm, ReqLookupForm
from flask_server.db_models import Users
from flask_server.req_scraper import ReqScraper
from flask_bcrypt import Bcrypt
from flask_login import login_user, current_user, logout_user
from functools import wraps
import os

# Custom decorator that checks to see if a user has been authenticated as an account
# Redirects to account login page
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            flash('You must be logged in to view this page.', 'danger')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title='Home')

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LogInForm()
    if form.validate_on_submit():
        account = Users.query.filter_by(email=form.email.data).first()
        if account and bcrypt.check_password_hash(account.passHash, form.password.data):
            login_user(account)
            flash(f'Welcome, {account.firstName}!', 'success' )
            return redirect(url_for('home'))
        elif account and not bcrypt.check_password_hash(account.passHash, form.password.data):
            flash(f'The password entered is invalid.', 'danger')
        else:
            flash(f'The account account \'{form.email.data}\' does not exist.', 'danger')

    return render_template('login.html', title='Login', form=form)

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        account = Users.query.filter_by(email=form.email.data).first()
        if account:
            flash(f'An account with this email already exists.', 'danger')
        else:

            hashedPass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

            newAccount = Users(form.firstName.data, form.lastName.data,
                               form.email.data, hashedPass)

            db.session.add(newAccount)
            db.session.commit()
            flash(f'The account was successfully created.\
                    Please check your email for a confirmation email.', 'success')
            return redirect(url_for('login'))

    return render_template('signup.html', title='Sign Up', form=form)

@app.route("/generate-resume", methods=['GET', 'POST'])
def generateResume():
    reqDict = {}
    form = ReqLookupForm()

    filepath = os.getcwd()
    if os.name == 'nt':
        filepath += "\\flask_server\\static\\req_classes.txt"
    else:
        filepath += "/flask_server/static/req_classes.txt"

    choices = []
    with open(filepath, 'r') as f:
        for line in f:
            if line != '' and line != '\n' and not line.startswith('#'):
                line = line.rstrip("\n")
                choices.append((line, line))

    form.reqClass.choices = choices

    if form.validate_on_submit():
        reqScraper = ReqScraper(form.reqURL.data, form.reqClass.data)
        reqScraper.scrape()
        return redirect(url_for('home'))

    return render_template('generate_resume.html', title='Generate Resume', form=form)


# logout signed-in users
# Redirect back to the home page
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))
