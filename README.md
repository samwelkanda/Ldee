
# Ride-My-Way API

[![Build Status](https://travis-ci.org/samwelkanda/Ride-My-Way.svg?branch=master)](https://travis-ci.org/samwelkanda/Ride-My-Way)

[![Coverage Status](https://coveralls.io/repos/github/samwelkanda/Ride-My-Way/badge.svg?branch=master)](https://coveralls.io/github/samwelkanda/Ride-My-Way?branch=master&service=github)

The API enables users to make various CRUD requests to the application by accessing the following endpoints.

## Endpoints

The v1 API contains the following API endpoints for users

### View All Ride Offers
Endpoint:
```
/api/v1/rides
```
request:GET

### View a specific ride offer
Endpoint:
```
/api/v1/rides/<ride_id>
```
request:GET

### Modify/Update a specific ride offer 
Endpoint:
```
/api/v1/rides/<ride_id>
```
request:PUT

### Create a ride offer
Endpoint:
```
/api/v1/rides/<ride_id>
```
request:POST

### View requests for a particular ride
Endpoint:
```
api/v1/rides/<ride_id>/requests
```
request:GET

### Request to join a ride
Endpoint:
```
/api/v1/<ride_id>/requests
```
request:POST

### Delete a ride
Endpoint
```
/api/v1/rides/<ride_id>
```
request:DELETE


