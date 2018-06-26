from flask import Flask, jsonify, abort, make_response, request
from . import api
from app.models import rides


@app.route('/ridemyway/api/v1/rides', methods=['GET'])
def get_rides():
    return jsonify({'rides': rides})

@app.route('/ridemyway/api/v1/rides/<int:ride_id>', methods=['GET'])
def get_ride(ride_id):
    ride = [ride for ride in rides if ride['id'] == ride_id]
    if len(ride) == 0:
        abort(404)
    return jsonify({'ride': ride[0]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/ridemyway/api/v1/rides', methods=['POST'])
def create_ride():
    data = request.get_json() or {}
    if 'date/time' not in data or 'from' not in data or 'destination' not in data or 'seats' not in data or 'cost' not in data:
        abort(400)
    ride = {
        'id': rides[-1]['id'] + 1,
        'date/time': request.json['date/time'],
        'from': request.json['from'],
        'destination': request.json['destination'],
        'seats': request.json['seats'],
        'cost': request.json['cost'],
        'description': request.json['description'],
        'driver': request.json['driver']
    }
    rides.append(ride)
    return jsonify({'ride': ride}), 201

@app.route('/ridemyway/api/v1/rides/<int:ride_id>/requests', methods=['GET'])
def ride_requests(ride_id):
    ride = [ride for ride in rides if ride['id'] == ride_id]
    if len(ride) == 0:
        abort(404)
    requests = ride[0]['requests']
    return jsonify({'requests': requests})

@app.route('/ridemyway/api/v1/rides/<int:ride_id>/requests', methods=['POST'])
def make_request(ride_id):
    data = request.get_json() or {}
    ride = [ride for ride in rides if ride['id'] == ride_id]
    if len(ride) == 0:
        abort(404)
    requests = ride[0]['requests']
    if 'pickup_location' not in data or 'requester' not in data:
        abort(400)
    my_request = {
        'id': requests[-1]['id'] + 1,
        'pickup_location': request.json['pickup_location'],
        'seats': request.json['seats'],
        'requester': request.json['requester']
    }
    requests.append(my_request)
    return jsonify({'my_request': my_request}), 201

@app.route('/ridemyway/api/v1/rides/<int:ride_id>', methods=['PUT'])
def update_ride(ride_id):
    ride = [ride for ride in rides if ride['id'] == ride_id]
    if len(ride) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'date/time' in request.json and type(request.json['date/time']) !=str:
        abort(400)
    if 'from' in request.json and type(request.json['from']) !=str:
        abort(400)
    if 'destination' in request.json and type(request.json['destination']) !=str:
        abort(400)
    if 'seats' in request.json and type(request.json['seats']) !=int:
        abort(400)
    if 'cost' in request.json and type(request.json['cost']) !=int:
        abort(400)
    if 'driver' in request.json and type(request.json['driver']) !=str:
        abort(400)

    ride[0]['date/time'] = request.json.get('date/time', ride[0]['date/time'])
    ride[0]['from'] = request.json.get('from', ride[0]['from'])
    ride[0]['destination'] = request.json.get('destination', ride[0]['destination'])
    ride[0]['seats'] = request.json.get('seats', ride[0]['seats'])
    ride[0]['cost'] = request.json.get('cost', ride[0]['cost'])
    ride[0]['driver'] = request.json.get('driver', ride[0]['driver'])
    ride[0]['requests'] = request.json.get('requests', ride[0]['requests'])
    return jsonify({'ride': ride[0]})

@app.route('/ridemyway/api/v1/rides/<int:ride_id>', methods=['DELETE'])
def delete_ride(ride_id):
    ride = [ride for ride in rides if ride['id'] == ride_id]
    if len(ride) == 0:
        abort(404)
    rides.remove(ride[0])
    return jsonify({'result': True})
