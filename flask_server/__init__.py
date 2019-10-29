from uuid import uuid4
import os
from flask import Flask

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

from flask_server import routes
