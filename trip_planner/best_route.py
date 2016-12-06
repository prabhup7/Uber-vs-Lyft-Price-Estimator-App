def find_best_route(locations):
    """

    :param locations: {
        "start": "/locations/12345",
        "others" : [
            "/locations/1000",
            "/locations/1001",
            "/locations/1002",
        ],
        "end": "/locations/12345"
    }
    :return: [
        "/locations/1002",
        "/locations/1000",
        "/locations/1001",
    ]
    """
    # TODO: implement
    # testing data. Remove this
    return locations['others']


def generate_uber_report(best_route_by_costs):
    """
    Call Uber API for the points in best_route_by_costs.
    :param [u'/v1/locations/51', u'/v1/locations/52', u'/v1/locations/53', u'/v1/locations/54']
    :return: {
            "name" : "Uber",
            "total_costs_by_cheapest_car_type" : 125,
            "currency_code": "USD",
            "total_duration" : 640,
            "duration_unit": "minute",
            "total_distance" : 25.05,
            "distance_unit": "mile"
        }"""

    return None


def generate_lyft_report(best_route_by_costs):
    """
    Call Lyft API for the points in best_route_by_costs
    :param [u'/v1/locations/51', u'/v1/locations/52', u'/v1/locations/53', u'/v1/locations/54']
    :return: {
            "name" : "Lyft",
            "total_costs_by_cheapest_car_type" : 110,
            "currency_code": "USD",
            "total_duration" : 620,
            "duration_unit": "minute",
            "total_distance" : 25.05,
            "distance_unit": "mile"
        }
    """
    return None
