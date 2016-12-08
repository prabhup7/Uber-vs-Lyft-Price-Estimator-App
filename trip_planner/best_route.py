import urllib

import grequests
import requests
from flask import json

import key
import location_api.location_app
from db_and_common.model import location

LYFT_BASE = "https://api.lyft.com/v1/cost"
MAX_TRIES = 3

places = []
lat_dict = {}
long_dict = {}
lat_list = []
long_list = []
places_dict = {}
waypoints_dict = {}
str1 = []
sorted_ways_uber = []
output_list = []
sorted_ways_id = []

# source = start
# dest = end

# waypoints_list = []
# source = 1
# dest = 2

str2 = ''


def getfromdb(source, dest, waypoints_list):
    count = 0
    rows = location.query.filter_by(id=source).first()
    # places_dict[source]['latitude']= rows.latitude;
    # places_dict[source]['longitude']= rows.longitude;
    places_dict[source] = {'latitude': rows.latitude, 'longitude': rows.longitude}
    rows1 = location.query.filter_by(id=dest).first()
    # places_dict[dest]['latitude']= rows1.latitude
    # places_dict[dest]['longitude']= rows1.longitude
    places_dict[dest] = {'latitude': rows1.latitude, 'longitude': rows1.longitude}
    print (places_dict)

    print "------inside getfromdb()"
    print waypoints_list

    for i in range(0, (len(waypoints_list))):
        rows3 = location.query.filter_by(id=waypoints_list[i]).first()
        # waypoints_dict[rows3.id]['latitude']= rows3.latitude;
        # waypoints_dict[rows3.id]['longitude']= rows3.longitude;
        waypoints_dict[rows3.id] = {'latitude': rows3.latitude, 'longitude': rows3.longitude}
    print (waypoints_dict)
    for key in waypoints_dict:
        if count < (len(waypoints_dict) - 1):
            str1.append(waypoints_dict[key]['latitude'] + ',' + waypoints_dict[key]['longitude'] + '|')
        else:
            str1.append(waypoints_dict[key]['latitude'] + ',' + waypoints_dict[key]['longitude'])
        count = count + 1
    # for i in range(0, (len(waypoints_list))):
    #     rows3 = location.query.filter_by(id=waypoints_list[i]).first()
    #     # waypoints_dict[rows3.id]['latitude']= rows3.latitude;
    #     # waypoints_dict[rows3.id]['longitude']= rows3.longitude;
    #     waypoints_dict[rows3.id] = {'latitude': rows3.latitude, 'longitude': rows3.longitude}
    # print (waypoints_dict)
    # for key in waypoints_dict:
    #     if count < (len(waypoints_dict) - 1):
    #         str1.append(waypoints_dict[key]['address'] + '|')
    #     else:
    #         str1.append(waypoints_dict[key]['address'] )
    #     count = count + 1
    # print str1
    str2 = ''.join(str(e) for e in str1)
    print str2
    print waypoints_list

    city = 'origin=' + str(places_dict[source]['latitude']) + ',' + str(
        places_dict[source]['longitude']) + '&destination=' + str(places_dict[dest]['latitude']) + ',' + str(
        places_dict[dest]['longitude']) + '&waypoints=optimize:true|' + str(str2)

    # city = 'origin=' + str(places_dict[source]['address']) \
    #        + '&destination=' + str(places_dict[dest]['address']) \
    #        + '&waypoints=optimize:true|' + str(str2)
    print city
    url_waypoints = 'https://maps.googleapis.com/maps/api/directions/json?' + city + '&key=AIzaSyD6OzDVE_s67_JmJvfPHi28XDj8hLhaWMk'

    tries = 0
    while 1:
        waypoints_response = requests.get(url_waypoints)
        print "way points route ++++++++++++++++++++++++++++++++++"
        print json.dumps(waypoints_response.json())
        if len(waypoints_response.json()['routes']) == 0:
            if tries < MAX_TRIES:
                print "No routes received. Trying again."
                tries += 1
                continue
            else:
                print "Google returned no route. Max tries reached."
                return []
        else:
            break

    waypoints_response1 = waypoints_response.json()['routes'][0]['waypoint_order']

    # waypoints_response1= waypoints_response.json()['routes'][0]
    print "way point response1", waypoints_response1
    sorted_waypoint = []

    # lat_list.insert(0,places_dict[source]['latitude'])
    # long_list.insert(0,places_dict[source]['longitude'])
    # for b in waypoints_response1:
    #     print b
    #     lat_list.append(waypoints_dict[waypoints_list[b]]['latitude'])
    #     long_list.append(waypoints_dict[waypoints_list[b]]['longitude'])
    # lat_list.append(places_dict[dest]['latitude'])
    # long_list.append(places_dict[dest]['longitude'])

    # print long_list
    # print lat_list

    # print sorted_waypoint

    sorted_ways_uber.insert(0, [places_dict[source]['latitude'], places_dict[source]['longitude']])
    for b in waypoints_response1:
        print b
        print json.dumps(waypoints_dict)
        # sorted_ways_uber.append([waypoints_dict[waypoints_list[b]]['latitude'],
        #                          waypoints_dict[waypoints_list[b]]['longitude']])
        sorted_ways_uber.append([waypoints_dict[waypoints_list[b]]['latitude'],
                                 waypoints_dict[waypoints_list[b]]['longitude']])
        sorted_ways_id.append(waypoints_list[b])
    print ("sorted id's", sorted_ways_id)

    for way in sorted_waypoint:
        for latlong in way:
            sorted_ways_uber.append(way[latlong])
    # print sorted_ways_uber
    sorted_ways_uber.append([places_dict[dest]['latitude'], places_dict[dest]['longitude']])
    print ("optimized route coordinates", sorted_ways_uber);
    for i in range(len(sorted_ways_id)):
        output_list.append("/locations/" + str(sorted_ways_id[i]))

    print output_list
    return output_list


def get_distance():
    toRet = []
    toRet_part = {
        "name": "",
        "total_costs_by_cheapest_car_type": 0,
        "currency_code": "USD",
        "total_duration": 0.0,
        "duration_unit": "minute",
        "total_distance": 0.0,
        "distance_unit": "mile"
    }

    uber_dis_pool_distance = []
    uber_dis_pool_lowestimate = []
    uber_dis_xcartype_distance = []
    uber_xl_cartype_lowestimate = []
    uber_dis_xcartype_lowestimate = []
    uber_dis_pool_time = []
    uber_xl_cartype_time = []
    uber_dis_xcartype_time = []
    var = 0
    final_uberpool_distance = None
    for another_value in range(1, len(sorted_ways_uber)):

        start_latitude = sorted_ways_uber[var][0]
        start_longitude = sorted_ways_uber[var][1]
        end_latitude = sorted_ways_uber[another_value][0]
        end_longitude = sorted_ways_uber[another_value][1]

        # print "start latitude:%d",(start_latitude)
        # print "start longitude:%d",(start_longitude)
        # print "end latitude:%d",(end_latitude)
        # print "end longitude:%d",(end_longitude)


        var = var + 1
        url_uber = 'https://api.uber.com/v1.2/estimates/price'
        parameters = {
            'server_token': 'NgDT7eBNK2-e5TBiQ1kjN1nnGxA9xquK1XIZEg0J',
            'start_latitude': start_latitude,
            'start_longitude': start_longitude,
            'end_latitude': end_latitude,
            'end_longitude': end_longitude,
        }
        # parameters = {
        # 'server_token': 'rzRLNgxRVSMbvJ5JrFX3ZiKbBcXO7vUZrNF99aB8',
        # 'start_latitude': 37.3229926,
        # 'start_longitude': -121.8832,
        # 'end_latitude': 37.3541079,
        # 'end_longitude': -121.9552356,
        # }
        uber_res = requests.get(url_uber, params=parameters)
        uber_final_res = json.loads(uber_res.text)
        print uber_final_res

        # uberpool distance
        # uberpool cost

        if 'prices' in uber_final_res:

            uber_dis_pool_distance.append(uber_final_res['prices'][0]['distance'])
            uber_dis_pool_lowestimate.append(uber_final_res['prices'][0]['low_estimate'])
            uber_dis_pool_time.append(uber_final_res['prices'][0]['duration'])
            print ("uber pool distance", uber_dis_pool_distance)
            print ("uber pool cost", uber_dis_pool_lowestimate)
            print ("uber time taken", uber_dis_pool_time)

            # for individual_distance_pool in uber_dis_pool_distance:
            #     total_sum_distance = total_sum_distance + individual_distance_pool
            # print total_sum_distance

            # for individual_cost_pool in uber_dis_pool_estimate


            # uberX distance
            # uberX cost

            uber_dis_xcartype_distance.append(uber_final_res['prices'][1]['distance'])
            uber_dis_xcartype_lowestimate.append(uber_final_res['prices'][1]['low_estimate'])
            uber_dis_xcartype_time.append(uber_final_res['prices'][0]['duration'])

            print ("uber X distance", uber_dis_xcartype_distance)
            print ("uber X cost", uber_dis_xcartype_lowestimate)

            uber_xl_cartype_lowestimate.append(uber_final_res['prices'][2]['low_estimate'])
            uber_xl_cartype_time.append(uber_final_res['prices'][0]['duration'])
            # print uber_final_res['prices'][0]['distance']
        else:

            print "please enter distance below 100 miles"
    final_uberpool_cost = sum(uber_dis_pool_lowestimate)
    final_uberx_cost = sum(uber_dis_xcartype_lowestimate)
    final_uberxl_cost = sum(uber_xl_cartype_lowestimate)
    final_uberpool_distance = sum(uber_dis_pool_distance)

    final_uberpool_time = sum(uber_dis_pool_time)
    final_uberx_time = sum(uber_dis_xcartype_time)
    final_uberxl_time = sum(uber_xl_cartype_time)

    print ("total uberpool cost", final_uberpool_cost);
    print ("total uberx cost", final_uberx_cost);
    print ("total uber xl cost", final_uberxl_cost);

    if final_uberx_cost is not None:
        toRet_uberx = toRet_part.copy()
        toRet_uberx['name'] = 'Uber X'
        toRet_uberx['total_costs_by_cheapest_car_type'] = final_uberx_cost
        toRet_uberx['total_distance'] = final_uberpool_distance
        toRet_uberx['total_duration'] = float(final_uberx_time) / 60
        toRet.append(toRet_uberx)
    if final_uberpool_cost is not None:
        toRet_uberp = toRet_part.copy()
        toRet_uberp['name'] = 'Uber Pool'
        toRet_uberp['total_costs_by_cheapest_car_type'] = final_uberpool_cost
        toRet_uberp['total_distance'] = final_uberpool_distance
        toRet_uberp['total_duration'] = float(final_uberpool_time / 60)
        toRet.append(toRet_uberp)
    if final_uberxl_cost is not None:
        toRet_uberxl = toRet_part.copy()
        toRet_uberxl['name'] = 'Uber XL'
        toRet_uberxl['total_costs_by_cheapest_car_type'] = final_uberxl_cost
        toRet_uberxl['total_distance'] = final_uberpool_distance
        toRet_uberxl['total_duration'] = float(float(final_uberxl_time) / float(60))
        toRet.append(toRet_uberxl)

    return toRet


def get_address_list(locations):
    """
    :param locations: The invoming data to fid_best_routes(). For example:
    {
        "start": "/locations/1",
        "others": [
            "/locations/2",
            "/locations/3",
            "/locations/4",
        ],
        "end": "/locations/5"
    }
    :return: list of addresses. For example [u'33 south third, san jose, california', u'33 south third, san jose, california', u'Gurdwara Sahib of San Jose ', u'1 infinite loop cupertino ca 95014', u'stanford university, palo alto, california']
    """
    toRet = []
    # parse start
    loc_id = locations['start'].split('/')[2]
    resp = location_api.location_app.queryDB(loc_id)
    resp_json = json.loads(resp.data)
    toRet.append(resp_json['address'])
    # parse others
    for loc in locations['others']:
        loc_id = loc.split('/')[2]
        resp = location_api.location_app.queryDB(loc_id)
        resp_json = json.loads(resp.data)
        toRet.append(resp_json['address'])
    # parse end
    loc_id = locations['end'].split('/')[2]
    resp = location_api.location_app.queryDB(loc_id)
    resp_json = json.loads(resp.data)
    toRet.append(resp_json['address'])
    return toRet


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
    toRet['route'] = getfromdb(source, dest, waypoints_list)
    toRet['uber'] = get_distance()

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


def generate_lyft_report(locations):
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

    toRet = {
        "name": "Lyft",
        "total_costs_by_cheapest_car_type": 0,
        "currency_code": "USD",
        "total_duration": 0.0,
        "duration_unit": "minute",
        "total_distance": 0.0,
        "distance_unit": "mile"
    }

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
        resp_lyft = requests.get(LYFT_BASE, headers=auth, params=payload).json()
        resp_json = resp_lyft
        print json.dumps(resp_lyft)

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
    toRet['total_costs_by_cheapest_car_type'] = toRet['total_costs_by_cheapest_car_type'] / 100  # convert cents to USD

    print toRet
    return toRet


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

    toRet = {
        "name": "Lyft",
        "total_costs_by_cheapest_car_type": 0,
        "currency_code": "USD",
        "total_duration": 0.0,
        "duration_unit": "minute",
        "total_distance": 0.0,
        "distance_unit": "mile"
    }
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

        toRet['total_duration'] = toRet['total_duration'] / 60
        toRet['total_costs_by_cheapest_car_type'] = int(
            toRet['total_costs_by_cheapest_car_type']) / 100  # convert cents to USD

    print json.dumps(toRet)
    return toRet


if __name__ == '__main__':
    locations = {
        "start": "/locations/1",
        "others": [
            "/locations/2",
            "/locations/3"
        ],
        "end": "/locations/5"
    }
    print json.dumps(find_best_route(locations))



    # best_route = [
    #     "/locations/1",
    #     "/locations/2",
    #     "/locations/3",
    # ]
    # generate_lyft_report(best_route)
