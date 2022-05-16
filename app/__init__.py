from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate

from flask_uploads import UploadSet, configure_uploads,IMAGES
from os import path


db = SQLAlchemy()
bootstrap = Bootstrap()
photos =UploadSet('photos',IMAGES)
migrate = Migrate()


app = Flask(__name__)

app.config['SECRET_KEY'] = 'no secrets'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

#photo uploads config
app.config['UPLOADED_PHOTOS_DEST'] ='app/static/photos'

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app():
   
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    #configure uploadset
    configure_uploads(app,photos)

    #initializing flask extensions
    login_manager.init_app(app)
    db.init_app(app)
    bootstrap.init_app(app)
    migrate.init_app(app, db)





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
