from flask_server import db, login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)

class Users(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column('id', db.Integer, primary_key=True, nullable=False, autoincrement=True)
    firstName = db.Column('first_name', db.String(50), nullable=False)
    lastName = db.Column('last_name', db.String(50), nullable=False)
    email = db.Column('email', db.String(50), nullable=False)
    passHash = db.Column('pass_hash', db.String(60), nullable=False)
    accountConfirmed = db.Column('account_confirmed', db.String(1), nullable=False, default='F')
    dateAdded = db.Column('date_added', db.String(10), default=datetime.now().strftime("%m_%d_%Y"))

    def __init__(self, firstName, lastName, email, passHash):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.passHash = passHash

    def __repr__(self):
        return f"User('{self.id}', '{self.firstName}', '{self.lastName}',"\
                        f"'{self.email}', '{self.dateAdded}')"


db.create_all()
db.session.commit()
