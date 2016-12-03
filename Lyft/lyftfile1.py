import itertools

import requests
from a2m.itertools import *
from db_and_common.init_app import *

#2control over here



r = db.engine.execute('select latitude from location')
r2 = db.engine.execute('select longitude from location')

number_of_places = 6

latitudes = []

longitude = []

for i in r:
    start_lat = str(i['latitude'])
    latitudes.append(start_lat)
    #print "hi"
    #print start_lat
#print latitudes

for i in r2:
    start_lng = str(i['longitude'])
    longitude.append(start_lng)
    #print "hi"
    #print start_lng
#print longitude

pl_ind_lat_lng = {
    "location_no.": 0,
    "lats": 0,
    "lngs": 0
}

for i in range(0,6):
    pl_ind_lat_lng["location_no."] = i
    pl_ind_lat_lng["lats"] = latitudes[i]
    pl_ind_lat_lng["lngs "] = longitude[i]
    #print pl_ind_lat_lng


combo1 = list(itertools.permutations([0,1,3,4,5], 2))
#print combo1
#r i in range(0,42):
   # print combo1[i]

#print "the pairs of addresses are"
#print combo1[29]
start_location_lat = latitudes[combo1[19][0]]
start_location_lng = longitude[combo1[19][0]]
end_location_lat = latitudes[combo1[19][1]]
end_location_lng = longitude[combo1[19][1]]
#print start_location_lat
#print start_location_lng
#print end_location_lat
#print end_location_lng

estimate_cost = []

for i in range(0,20):
    #print "The pair of addresses are"
    print combo1[i]
    print i
    start_location_lat = latitudes[combo1[i][0]]
    start_location_lng = longitude[combo1[i][0]]
    end_location_lat = latitudes[combo1[i][1]]
    end_location_lng = longitude[combo1[i][1]]
    #print start_location_lat
    #print start_location_lng
    #print end_location_lat
    #print end_location_lng
    url = 'https://api.lyft.com/v1/cost'
    payload = {'start_lat': start_location_lat , 'start_lng': start_location_lng, 'end_lat': end_location_lat,'end_lng':end_location_lng}
    myheaders = {'Authorization': 'Bearer Auth Token'}
    r = requests.get(url, headers=myheaders, params=payload)
    d = json.dumps(r.json())
    json_acceptable_string = d.replace("'", "\"")
    data = json.loads(json_acceptable_string)
    cost = []
    a1 = (data["cost_estimates"][0]["estimated_cost_cents_max"]/100.0)
    b1 = (data["cost_estimates"][0]["estimated_cost_cents_min"] / 100.0)
    c1 = (a1 + b1)/2.0
    cost.append(c1)
    p = (data["cost_estimates"][1]["estimated_duration_seconds"]/60.0)
    minutes = float("{0:.2f}".format(p))
    distance = (data["cost_estimates"][1]["estimated_distance_miles"])
    result = {"id":0,

              "start":0,

              "best_route_by_costs":[],

              "providers":[
                {"name":"Lyft",
                 "total_costs_by_cheapest_car_type":0,
                 "total_duration": 0,
                 "duration_unit": "minute",
                 "total_distance": 0,
                 "distance_unit": "mile"
                 }
                ],
              "end":0
              }

    i = result["providers"][0]["total_costs_by_cheapest_car_type"] = (min(cost))
    estimate_cost.append(i)
    result["providers"][0]["total_duration"] = minutes
    result["providers"][0]["total_distance"] = distance
    print result
    print i

for i in range(0,20):
    print estimate_cost[i]

