# This is the package constructor for the application

from flask import Flask

from isinstance.config import CONFIG

def create_app(config_name):
   
    app = Flask(__name__)
    app.config.from_object(CONFIG[config_name])

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint)

    return app