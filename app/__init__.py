from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_admin import Admin
from flask_mail import Mail
from flask_uploads import UploadSet, configure_uploads,IMAGES
from os import path
import os


db = SQLAlchemy()
bootstrap = Bootstrap()
photos =UploadSet('photos',IMAGES)
# migrate = Migrate()
admin = Admin()
mail = Mail()

app = Flask(__name__)
migrate = Migrate(app, db)
app.config['SECRET_KEY'] = 'no secrets'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

#email config
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.environ.get("MAIL_USERNAME")
app.config['MAIL_PASSWORD'] =  os.environ.get("MAIL_PASSWORD")
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

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
    admin.init_app(app)
    mail.init_app(app)




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
