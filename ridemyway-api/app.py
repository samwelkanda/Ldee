from flask import Flask, jsonify
from flask import abort
from flask import make_response

app = Flask(__name__)

rides = [
    {
        'id': 1,
        'date/time': u'01/02/2018, 08:00 AM',
        'from': u'Langata', 
        'destination': u'Nairobi West',
        'seats': 4,
        'cost': 70,
        'description': u'G-Wagon KCP 214',
        'driver': u'Paul Pogba',
    },
    {
        'id': 2,
        'date/time': u'02/14/2018, 09:00 AM',
        'from': u'Hurlingam', 
        'destination': u'Karen',
        'seats': 2,
        'cost': 100,
        'description': u'Toyota V8 KCD 777',
        'driver': u'Romelu Lukaku',
    },
    {
        'id': 3,
        'date/time': u'02/24/2018, 05:00 AM',
        'from': u'Nairobi',
        'destination': u'Mombasa',
        'seats': 3,
        'cost': 2000,
        'description': u'Audi KBX 074',
        'Driver': u'Marcus Rashford',
    },    
]

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


if __name__ == '__main__':
    app.run(debug=True)