from flask_login import UserMixin
from sqlalchemy.sql import func
from . import login_manager,db

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(150),unique = True)
    username = db.Column(db.String(150),unique = True)
    password = db.Column(db.String(150),nullable = False)
