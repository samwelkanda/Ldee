
from flask import Blueprint, request, abort
from app.requests.helper import ride_required, response, get_parent_ride, response_with_ride_request
from app.models import Request

requests = Blueprint('requests', __name__)

@requests.route('/rides/<ride_id>/requests', methods=['GET'])
@ride_required
def get_requests(ride_id):
    """
    requests belonging to a ride specified by the ride_id are returned if the ride Id
    is valid
    An empty item list is returned if the ride has no requests.
    :param ride_id: ride Id
    :return: List of requests
    """
    # Get the ride
    ride = get_parent_ride(ride_id)
    if ride is None:
        return response('failed', 'ride not found', 404)

    # Make a list of requests
    if requests:
        result = []
        for request in requests:
            result.append(request.json())

@requests.errorhandler(404)
def request_not_found(e):
    """
    Custom response to 404 errors.
    :param e:
    :return:
    """
    return response('failed', 'Request not found', 404)


@requests.errorhandler(400)
def bad_method(e):
    """
    Custom response to 400 errors.
    :param e:
    :return:
    """
    return response('failed', 'Bad request', 400)