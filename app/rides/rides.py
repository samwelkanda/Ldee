from flask import Flask, jsonify, abort, make_response, request
from . import api
from app.models import rides


def get_ride_or_abort(ride_id):
    """
    Get ride with specified id or abort if not found
    """
    ride = [ride for ride in rides if ride['id'] == ride_id]
    if len(ride) == 0:
        abort(404)

    return ride


@api.route('/api/v1/rides', methods=['GET', 'POST'])
def get_rides():
    '''
    GET all rides
    '''
    if request.method == 'POST':
        data = request.json

        reqs = ['date/time', 'from', 'destination', 'seats', 'cost', 'description',
                'driver']
        for req in reqs:
            if not data or not req in data:
                abort(400)

        ride = {
            'id': len(rides)+1,
            'date/time': data['date/time'],
            'from': data['from'],
            'destination': data['destination'],
            'seats': data['seats'],
            'cost': data['cost'],
            'description': data['description'],
            'driver': data['driver'],
            'requests': []
        }

        rides[ride['id']] = ride
        return jsonify({"ride": ride}), 201
    return jsonify({'rides': rides})

@api.route('/api/v1/rides/<int:ride_id>', methods=['GET', 'PUT', 'DELETE'])
def get_specific_ride(ride_id):
    """
    GET a singe ride
    """
    ride = get_ride_or_abort(ride_id)
    if request.method == 'PUT':
        #check for keys in request data and update key
        for key in request.json.keys():
            ride[key] = request.json.get(key, ride[key])

        return jsonify({'ride':ride})

    elif request.method == 'DELETE':
        rides.pop(ride_id)
        return jsonify({}), 204

    return jsonify({'ride': ride})

@api.route('/api/v1/rides/<int:ride_id>/requests', methods=['GET', 'POST'])
def get_requests(ride_id):
    """
    Get requests for ride with ride_id
    """
    ride = get_ride_or_abort(ride_id)
    if request.method == 'POST':
        data = request.json
        requests = ride['requests']
        if requests:
            request_id = requests[-1]['id']+1
        else:
            request_id = 1
        ride_request = {
            'id': request_id,
            'pickup_location': data['pickup_location'],
            'seats': data['seats'],
            'requester': data['requester']
    }
        requests.append(ride_request)
        return jsonify({'requests': requests}), 201

    requests = ride['requests']
    return jsonify({'requests': requests})

