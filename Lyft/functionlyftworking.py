import requests
import json


def cost_for_optimized_route():

    locationdetails = \
              {"address":0,

              "latitude":0,

              "longitude":0,
              }

    addresses = ['123 Main St', '101 East San Fernando Street','2855 Stevens Creek Blvd','447 Great Mall Dr','2200 Eastridge Loop #2062']

    latitudes = ['37.7917618','37.3357192','37.3253266','37.4163855','37.3255349']

    longitudes = ['-122.3943405','-121.8867076','-121.9453801','-121.897841','-121.8133811']

    cost = []
    total_duration = []
    total_distance = []
    number_of_places = len(addresses)

    #for i in range(0,len(addresses)):
    # for j in range(1,len(addresses)):

    for i in range(0,len(addresses)):
        locationdetails["address"] = addresses[i]
        locationdetails["latitude"] = latitudes[i]
        locationdetails["longitude"] = longitudes[i]
        #print locationdetails["latitude"]
        #print locationdetails
        start_location_lat = latitudes[i-1]
        start_location_lng = longitudes[i-1]
        end_location_lat = latitudes[i]
        end_location_lng = longitudes[i]
        url = 'https://api.lyft.com/v1/cost'
        payload = {'start_lat': start_location_lat , 'start_lng': start_location_lng, 'end_lat': end_location_lat,'end_lng':end_location_lng}
        myheaders = {'Authorization': 'Bearer <auth token>'}
        r = requests.get(url, headers=myheaders, params=payload)
        d = json.dumps(r.json())
        json_acceptable_string = d.replace("'", "\"")
        data = json.loads(json_acceptable_string)
        print data


        a1 = (data["cost_estimates"][0]["estimated_cost_cents_max"]/100.0)
        b1 = (data["cost_estimates"][0]["estimated_cost_cents_min"] / 100.0)
        c1 = (a1 + b1)/2.0

        p = (data["cost_estimates"][1]["estimated_duration_seconds"]/60.0)
        minutes = float("{0:.2f}".format(p))
        distance = (data["cost_estimates"][1]["estimated_distance_miles"])
        result = {"id":0,

              "start":"/locations/" + str(0),

              "best_route_by_costs":[],

              "providers":[
                {"name":"Lyft",
                 "total_costs_by_cheapest_car_type":0,
                 "total_duration": 0,
                 "currency_code": "USD",
                 "duration_unit": "minute",
                 "total_distance": 0,
                 "distance_unit": "mile"
                 }
                ],
              "end":"/locations/" + str(number_of_places)
              }



        result["providers"][0]["total_costs_by_cheapest_car_type"] = c1
        cost.append(c1)
        result["providers"][0]["total_duration"] = minutes
        total_duration.append(minutes)
        result["providers"][0]["total_distance"] = distance
        total_distance.append(distance)
        print result
        print (" ")
    print cost
    print total_distance
    print total_duration


    def sum_list(l):
        sum = 0
        for x in l:
            sum += x
        return sum
    c = sum_list(cost)
    print sum_list(cost)
    d = sum_list(total_distance)
    print sum_list(total_distance)
    td = sum_list(total_duration)
    print sum_list(total_duration)


    finalresult = {"id":0,

              "start":"/locations/" + str(0),

              "best_route_by_costs":[],

              "providers":[
                {"name":"Lyft",
                 "total_costs_by_cheapest_car_type":0,
                 "total_duration": 0,
                 "currency_code": "USD",
                 "duration_unit": "minute",
                 "total_distance": 0,
                 "distance_unit": "mile"
                 }
                ],
              "end":"/locations/" + str()
              }

    finalresult["providers"][0]["total_costs_by_cheapest_car_type"] = c
    finalresult["providers"][0]["total_duration"] = td
    finalresult["providers"][0]["total_distance"] = d
    print finalresult


cost_for_optimized_route()


