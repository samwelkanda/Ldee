# Tests for rides endpoints

import json


def test_get_rides(test_client):
    """
    Test that get request works correctly
    """
    response = test_client.get('/api/v1/rides')
    assert response.status_code == 200

def test_get_single_ride(test_client):
    """
    Test request returns correct ride with specified ID
    """

    response = test_client.get('/api/v1/rides/1')
    assert response.status_code == 200
    