from flask import jsonify, make_response, request, url_for
from app import app
from functools import wraps
from app.models import Rides


def response(status, message, status_code):
    """
    This creates a http response helper
    :param status: Status message
    :param message: Response Message
    :param status_code: Http response code
    :return:
    """
    return make_response(jsonify({
        'status': status,
        'message': message
    })), status_code

def response_with_specific_ride(status, ride, status_code):
    """
    Http response for response with a specific ride.
    :param status: Status Message
    :param item: ride
    :param status_code: Http Status Code
    :return:
    """
    return make_response(jsonify({
        'status': status,
        'ride': ride.json()
    })), status_code

