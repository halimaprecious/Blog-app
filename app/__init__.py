from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from os import path


db = SQLAlchemy()

app = Flask(__name__)

app.config['SECRET_KEY'] = 'no secrets'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app():
   
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


    #initializing flask extensions
    login_manager.init_app(app)
    db.init_app(app)



    #registering blueprints
    from .auth import auth
    app.register_blueprint(auth, url_prefix = "/")

    from .views import views
    app.register_blueprint(views,url_prefix="/")

    create_database(app)


    return app

def create_database(app):
    if not path.exists('MY-BLOG' +'blog.db'):
        db.create_all(app=app)
        print("Created database!")
