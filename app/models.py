from app import app
import datetime


class Ride(object):
    """
    Class to represent the BucketList model
    """
   

    def __init__(self, ride_id, datentime, start, destination, seats, cost, driver:
        self.ride_id = id
        self.datentime = u'datentime'
        self.start = u'start'
        self.destination = u'destination'
        self.seats = u'seats'
        self.cost = u'cost'
        self.driver = u'driver'
        self.created_at = datetime.datetime.utcnow()

    def save(self):
        """
        Save a ride in the list
        :return:
        """
        ride = [
        {
        'id': rides[-1]['id'] + 1,
        'datentime': request.json['datentime'],
        'start': request.json['start'],
        'destination': request.json['destination'],
        'seats': request.json['seats'],
        'driver': request.json.get['driver']
        }
   ]
        rides.append(ride)

    def delete(self):
        """
        Delete a Bucket from the database
        :return:
        """
        ride = [ride for ride in rides if ride['id'] == ride_id]
        if len(ride) == 0:
            abort(404)
        rides.remove(ride[0])
    def json(self):
        """
        Json representation of the bucket model.
        :return:
        """
        return {
            'id': self.id,
            'datentime': self.datentime
            'start': self.start
            'destination': self.destination
            'seats': self.seats
            'driver': self.driver
            'createdAt': self.created_at.isoformat(),

        }

class Request(object):
    """
    Request model class
    """
    requests = [{ride_id, "pickup_location": u"pickup_location", "seats": u"seats", "requester": u"requester")}

    def __init__(self, pickup_location, seats, ride_id, requester):
        self.request_id = id
        self.pickup_location = pickup_location
        self.seats = seats
        self.requester = requester
        self.ride_id = ride_id
        self.create_at = datetime.datetime.utcnow()
            
    def save(self):
        """
        Add request to the list
        :return:
        """
        request = [
        {
        'id': requests[-1]['id'] + 1,
        'pickup_location': request.json['pickup_location'],
        'seats': request.json['seats'],
        'requester': request.json['requester'],
        }
   ]
        requests.append(requests)

