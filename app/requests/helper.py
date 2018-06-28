from flask import jsonify, make_response, request, url_for
from app import app
from functools import wraps
from app.models import Request


def ride_required(f):
    """
    Decorator to ensure that a valid ride id is sent in the url path parameters
    :param f:
    :return:
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        ride_id_ = request.view_args['ride_id']
        try:
            int(ride_id_)
        except ValueError:
            return response('failed', 'Provide a valid ride Id', 401)
        return f(*args, **kwargs)

    return decorated_function


def response(status, message, status_code):
    """
    Make an http response helper
    :param status: Status message
    :param message: Response Message
    :param status_code: Http response code
    :return:
    """
    return make_response(jsonify({
        'status': status,
        'message': message
    })), status_code


def response_with_ride_request(status, request, status_code):
    """
    Http response for response with a ride request.
    :param status: Status Message
    :param request: riderequest
    :param status_code: Http Status Code
    :return:
    """
    return make_response(jsonify({
        'status': status,
        'request': request.json()
    })), status_code


def response_with_pagination(requests, previous, nex, count):
    """
    Get the ride requests with the result paginated
    :param requests: requests within the ride
    :param previous: Url to previous page if it exists
    :param nex: Url to next page if it exists
    :param count: Pagination total
    :return: Http Json response
    """
    return make_response(jsonify({
        'status': 'success',
        'previous': previous,
        'next': nex,
        'count': count,
        'requests': requests
    })), 200


def get_parent_ride( ride_id):
    """
    Query the user to find and return the ride specified by the ride Id
    :param ride_id: ride Id
    :return:
    """
    parent_ride = rides.filter_by(id=ride_id).first()
    return parent_ride