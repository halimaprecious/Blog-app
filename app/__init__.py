from flask import Flask


app = Flask(__name__)

def create_app():
    
    #registering blueprints
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix = "/auth")

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    return app