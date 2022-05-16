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
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password = db.Column(db.String(150),nullable = False)

class Post(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title =db.Column(db.String(100),nullable =False)
    text = db.Column(db.Text,nullable=False)
    date_created = db.Column(db.DateTime(timezone=True),default=func.now())




class Quote:
    """
    Blueprint class for quotes consumed from API
    """
    def __init__(self, author, quote):
        self.author = author
        self.quote = quote