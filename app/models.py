# Sample data that can be accessed through the API
import datetime
import os

rides = {}
requests = {}


class Rides:
    # Methods for rides endpoints 

    
    
    @staticmethod
    def create_ride(datentime, starting, destination, seats, cost, description, driver):

        new_id = len(rides) + 1
        rides[new_id] = {"datentime": datentime,
                         "starting": starting,
                         "destination": destination,
                         "seats": seats,
                         "cost": cost,
                         "description": description,
                         "driver": driver}
        return {"msg": "Your ride has been added"}


    @staticmethod
    def get_rides():
        """Gets all rides"""

        output = []
        for ride_id in rides:
            data = {}
            data["ride_id"] = ride_id
            data["datentime"] = rides[ride_id]["datentime"]
            data["starting"] = rides[ride_id]["starting"]
            data["destination"] = rides[ride_id]["destination"]
            data["seats"] = rides[ride_id]["seats"]
            data["cost"] = rides[ride_id]["cost"]
            data["description"] = rides[ride_id]["description"]
            data["driver"] = rides[ride_id]["driver"]
            output.append(data)
        return output

    def get_ride(self, ride_id):
        """Get a specific ride"""

        if ride_id not in rides:
            return {"msg": "The ride id entered is invalid"}

        ride = rides[ride_id]
        return ride

    def request_ride(self, ride_id, pickup_location, seats, requester):
        """Request a ride"""

        requests[ride_id] = {
            "ride_id": rides[ride_id],
            'request_id': requests[-1]['request_id'] + 1,
            "seats": seats,
            "requester": requester}
        return {"msg": "You have requested this ride"}


    def get_ride_requests(self):
        """Get all requests to a ride"""

        output = []
        for ride_id in requests:
            data = {}
            data['id'] = requests[-1]['id'] + 1,
            data["ride_id"] = rides.get(ride_id),
            data["pickup_location"] = requests[ride_id]["pickup_location"]
            data["seats"] = requests[ride_id]["seats"]
            data["requester"] = requests[ride_id]["requester"]
            output.append(data)
        return output


    @staticmethod
    def delete_ride(ride_id):
        """Deleting a particular ride"""

        if ride_id not in rides:
            return {"msg": "Ride ID is Invalid"}

        del rides[ride_id]
        return {"msg": "Ride has been successfully deleted"}