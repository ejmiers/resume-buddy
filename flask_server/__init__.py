from uuid import uuid4
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

def getSecretKey():

    # Sets a temporary key for duration of server session
    # Ideally should be manually set within terminal/CMD for permanence
    # Linux: export RESUME_BUDDY_SECRET_KEY=<key>
    # Windows: set RESUME_BUDDY_SECRET_KEY=<key>
    if not "RESUME_BUDDY_SECRET_KEY" in os.environ:
        os.environ["RESUME_BUDDY_SECRET_KEY"] = str(uuid4().hex)

    return os.environ["RESUME_BUDDY_SECRET_KEY"]

app = Flask(__name__)
app.config['SECRET_KEY'] = getSecretKey()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
db.app = app

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from flask_server import routes
