#Construct the  API Package

from flask import Blueprint

api = Blueprint('api', __name__)

from . import rides