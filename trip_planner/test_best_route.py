import urllib

import grequests
from flask import json

import key
import location_api.location_app

LYFT_BASE = "https://api.lyft.com/v1/cost"
MAX_TRIES = 3


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
    :return: {
  "uber": [{
    "name": "Uber",
    "total_costs_by_cheapest_car_type": 125,
    "currency_code": "USD",
    "total_duration": 640,
    "duration_unit": "minute",
    "total_distance": 25.05,
    "distance_unit": "mile"
  }],
  "route": [
    "/locations/1002",
    "/locations/1000",
    "/locations/1001"
  ]
}
    """
    toRet = {
        "uber": [{
            "name": "",
            "total_costs_by_cheapest_car_type": 0,
            "currency_code": "USD",
            "total_duration": 0,
            "duration_unit": "minute",
            "total_distance": 0.0,
            "distance_unit": "mile"
        }
        ],
        "route": [
        ]
    }
    print "------locations:"
    print locations
    source = int(locations['start'].split('/')[2])
    dest = int(locations['end'].split('/')[2])
    waypoints_list = []
    for loc_str in locations['others']:
        loc_id = loc_str.split('/')[2]
        waypoints_list.append(int(loc_id))

    print "----inside find_best_route()"
    print waypoints_list
    # toRet['route'] = getfromdb(source, dest, waypoints_list)
    # toRet['uber'] = get_distance()

    return toRet


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


async_list = []
toRet = {
    "name": "Lyft",
    "total_costs_by_cheapest_car_type": 0,
    "currency_code": "USD",
    "total_duration": 0.0,
    "duration_unit": "minute",
    "total_distance": 0.0,
    "distance_unit": "mile"
}


def generate_lyft_report_async(locations):
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

    url_list = []

    for i in range(0, len(locations) - 1):
        loc_str = locations[i]
        loc_id = loc_str.split('/')[2]
        resp = location_api.location_app.queryDB(loc_id)
        resp_json = json.loads(resp.data)

        loc_str_end = locations[i + 1]
        loc_id_end = loc_str_end.split('/')[2]
        resp_end = location_api.location_app.queryDB(loc_id_end)
        resp_json_end = json.loads(resp_end.data)

        query_dict = {
            "start_lat": resp_json['coordinate']['latitude'],
            "start_lng": resp_json['coordinate']['longitude'],
            "end_lat": resp_json_end['coordinate']['latitude'],
            "end_lng": resp_json_end['coordinate']['longitude']
        }
        query_str = urllib.urlencode(query_dict)
        # resp_lyft = requests.get(LYFT_BASE + query_str)
        payload = {'start_lat': query_dict['start_lat'],
                   'start_lng': query_dict['start_lng'],
                   'end_lat': query_dict['end_lat'],
                   'end_lng': query_dict['end_lng']
                   }
        auth = {'Authorization': "Bearer " + key.lyft_key}

        url_list.append(grequests.get(LYFT_BASE, headers=auth, params=payload))

    grequests.map(url_list)
    # sleep(5)

    for resp in url_list:
        print resp
        resp_json = resp.response.json()
        print json.dumps(resp_json)
        cost = resp_json["cost_estimates"][0]['estimated_cost_cents_max'] + resp_json["cost_estimates"][0][
            'estimated_cost_cents_min']
        cost = cost / 2
        cheapest_car_cost = cost
        cheapest_car_id = 0
        i = 0
        for option in resp_json["cost_estimates"]:
            cost = option['estimated_cost_cents_max'] + option['estimated_cost_cents_min']
            cost = cost / 2
            if cost < cheapest_car_cost:
                cheapest_car_id = i
            i += 1

        cheapest = resp_json["cost_estimates"][cheapest_car_id]
        cost = cheapest['estimated_cost_cents_max'] + cheapest['estimated_cost_cents_min']
        cost /= 2  # average
        toRet['total_costs_by_cheapest_car_type'] += cost
        toRet['total_distance'] += cheapest['estimated_distance_miles']
        toRet['total_duration'] += cheapest['estimated_duration_seconds']

        toRet['total_duration'] = float("%.2f" % toRet['total_duration']) / 60
        toRet['total_costs_by_cheapest_car_type'] = toRet[
                                                        'total_costs_by_cheapest_car_type'] / 100  # convert cents to USD

    print json.dumps(toRet)
    return toRet


if __name__ == '__main__':
    # locations = {
    #     "start": "/locations/1",
    #     "others": [
    #         "/locations/2",
    #         "/locations/3"
    #     ],
    #     "end": "/locations/5"
    # }
    # print json.dumps(find_best_route(locations))



    best_route = [
        "/locations/1",
        "/locations/2",
        "/locations/3",
        "/locations/4",
        "/locations/5",
        "/locations/6",
        "/locations/7",
    ]
    generate_lyft_report_async(best_route)
