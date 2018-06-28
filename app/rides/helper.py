from flask import make_response, jsonify, url_for
from app import app
from app.models import Ride


def response_for_rides():
    """
    Return the response for all rides when requested by the user.
    :return:
    """
    return make_response(jsonify({
        'status': 'success',
        'rides': rides
    }))

def response_for_ride(ride_id):
    """
    Return the response for when a single bucket when requested by the user.
    :param user_bucket:
    :return:
    """
    return make_response(jsonify({
        'status': 'success',
        'ride': ride[0]
    }))

def response_for_created_ride(status_code):
    """
    Method returning the response when a ride has been successfully created.
    :param status_code:
    :return: Http Response
    """
    return make_response(jsonify({
        'status': 'success',
        'id': ride.id,
        'from': ride.start,
        'destination': ride.destination,
        'seats': ride.seats,
        'cost': ride.cost,
        'driver': ride.driver,
        'createdAt': user_bucket.create_at,
    })), status_code


def response(status, message, code):
    """
    Helper method to make a http response
    :param status: Status message
    :param message: Response message
    :param code: Response status code
    :return: Http Response
    """
    return make_response(jsonify({
        'status': status,
        'message': message
    })), code

