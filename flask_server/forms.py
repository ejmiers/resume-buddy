from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, Email, Optional, Length, EqualTo

class LogInForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    login = SubmitField('Login')

class SignUpForm(FlaskForm):
    firstName = StringField('First Name', validators=[DataRequired()])
    lastName = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[
        DataRequired(), Length(min=8, max=25), EqualTo('passwordConfirm', message='Passwords must match')])
    passwordConfirm = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Create Account')

class ReqLookupForm(FlaskForm):
    reqURL = StringField('Requisition URL', validators=[DataRequired()])
    reqClass = SelectField('Requisition Classification', validators=[DataRequired()])
    submit = SubmitField('Generate')
