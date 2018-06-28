from flask import Blueprint, request, abort
from app.models import Ride
from app.rides.helper import response, response_for_created_ride, response_for_rides

# Initialize blueprint
ride = Blueprint('ride', __name__)


@ride.route('/rides/', methods=['GET'])
def rideslist():
    """
    Return all the rides.
    Return an empty rides object if there are no rides
    :return:
    """
    return response_for_rides


@ride.route('/rides/', methods=['POST'])
def create_ride():
    """
    Create a ride from the sent json data.
    :return:
    """
    if request.content_type == 'application/json':
        data = request.get_json()
        reqs = ['date/time', 'from', 'destination', 'seats', 'cost', 'description',
                'driver']
        for req in reqs:
            if not data or not req in data:
                return response('failed', 'Missing name attribute', 400)
        ride = {
            'id': len(rides)+1,
            'datentime': data['datentime'],
            'start': data['start'],
            'destination': data['destination'],
            'seats': data['seats'],
            'cost': data['cost'],
            'driver': data['driver'],
        }
        rides[ride['id']] = ride
        return jsonify({"ride": ride}), 201
    return response('failed', 'Content-type must be json', 202)


@ride.route('/rides/<ride_id>', methods=['GET'])
def get_ride(ride_id):
    """
    Return a ride with the supplied Id.
    :param ride_id: ride Id
    :return:
    """
    try:
        int(ride_id)
    except ValueError:
        return response('failed', 'Please provide a valid ride Id', 400)
    else:
        return response_for_ride(ride.json())

@ride.route('/rides/<ride_id>', methods=['DELETE'])
def delete_ride(ride_id):
    """
    Deleting a ride if it exists.
    :param ride_id:
    :return:
    """
    try:
        int(ride_id)
    except ValueError:
        return response('failed', 'Please provide a valid ride Id', 400)
    ride = rides.filter_by(id=ride_id).first()
    ride.delete()
    return response('success', 'ride Deleted successfully', 200)


@ride.errorhandler(404)
def handle_404_error(e):
    """
    Return a custom message for 404 errors.
    :param e:
    :return:
    """
    return response('failed', 'ride resource cannot be found', 404)


@ride.errorhandler(400)
def handle_400_errors(e):
    """
    Return a custom response for 400 errors.
    :param e:
    :return:
    """
    return response('failed', 'Bad Request', 400)
