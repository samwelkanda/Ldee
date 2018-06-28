# This is the package constructor for the application

import os
from flask import Flask

from config import CONFIG

# Initialize application
app = Flask(__name__, static_folder=None)

# app configuration
app_settings = os.getenv(
    'APP_SETTINGS',
    'app.config.DevelopmentConfig'
)
app.config.from_object(app_settings)

# Import the application views
from app import views

from app.rides.views import rides

app.register_blueprint(rides, url_prefix='/v1')

from app.requests.views import requests

app.register_blueprint(requests, url_prefix='/v1')