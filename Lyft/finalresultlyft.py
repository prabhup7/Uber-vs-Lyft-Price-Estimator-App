import requests
import json
import inspect
import requests
import json

#sample inputs
data2 = ('optimized route coordinates', [[u'37.7917618', u'-122.3943405'], [u'37.3357192', u'-121.8867076'], [u'37.3253266', u'-121.9453801'], [u'37.4163855', u'-121.897841'], [u'37.3255349', u'-121.8133811']])
#data1 = ('optimized route coordinates', [[37.7917618, -122.3943405], [37.3357192, -121.8867076], [37.3253266, -121.9453801], [37.4163855, -121.897841], [37.3255349, -121.8133811]])

#print data[1][1][0]



#function to find out the lowest estimated costs,distance in miles and duration in minutes for the best route(considering data1 to be the output of the best route in this case)
def generate_lyft_report1(data1):
    a = len(data1[1])
    cost = []
    total_distance = []

    total_duration = []


    cost1 = []


    for i in range(0, a):
            start_location_lat = data1[1][i - 1][0]
            start_location_lng = data1[1][i - 1][1]
            end_location_lat = data1[1][i][0]
            end_location_lng = data1[1][i][1]
            print(" ")
            url = 'https://api.lyft.com/v1/cost'
            payload = {'start_lat': start_location_lat , 'start_lng': start_location_lng, 'end_lat': end_location_lat,'end_lng':end_location_lng}
            myheaders = {'Authorization': 'Bearer<token>'}
            r = requests.get(url, headers=myheaders, params=payload)
            d = json.dumps(r.json())
            json_acceptable_string = d.replace("'", "\"")
            data = json.loads(json_acceptable_string)
            #print data

            print data["cost_estimates"]

            result = {"id":0,

                  "start":"/locations/" + str(0),

                  "best_route_by_costs":[],

                  "providers":[
                    {"name":0,
                     "total_costs_by_cheapest_car_type":0,
                     "total_duration": 0,
                     "currency_code": "USD",
                     "duration_unit": "minute",
                     "total_distance": 0,
                     "distance_unit": "mile"
                     },


                    {"name":0,
                     "total_costs_by_cheapest_car_type":0,
                     "total_duration": 0,
                     "currency_code": "USD",
                     "duration_unit": "minute",
                     "total_distance": 0,
                     "distance_unit": "mile"
                     },


                    {"name":0,
                     "total_costs_by_cheapest_car_type":0,
                     "total_duration": 0,
                     "currency_code": "USD",
                     "duration_unit": "minute",
                     "total_distance": 0,
                     "distance_unit": "mile"
                     }
                    ],
                  "end":"/locations/" + str(a)
                  }

            for i in range(0,3):
                result["providers"][i]["name"] = data["cost_estimates"][i]["ride_type"]
                result["providers"][i][ "total_costs_by_cheapest_car_type"]
                a1 = (data["cost_estimates"][i]["estimated_cost_cents_max"] / 100.0)
                b1 = (data["cost_estimates"][i]["estimated_cost_cents_min"] / 100.0)
                c1 = (a1 + b1) / 2.0
                c2 = float("{0:.2f}".format(c1))
                cost1.append(c2)

                result["providers"][i]["total_costs_by_cheapest_car_type"] = c2
                p = (data["cost_estimates"][i]["estimated_duration_seconds"] / 60.0)
                #print p
                minutes = float("{0:.2f}".format(p))
                #print minutes
                result["providers"][i]["total_duration"] = minutes
                total_duration.append(minutes)
                distance = (data["cost_estimates"][i]["estimated_distance_miles"])
                result["providers"][i]["total_distance"] = distance
                total_distance.append(distance)
    print cost1
    print total_distance
    print total_duration



    total_costs1 = []
    sum = 0;
    sum1 = 0
    sum2 = 0
    totdist1 = 0
    totdist2 = 0
    totdist3 = 0
    totdur1 = 0
    totdur2 = 0
    totdur3 = 0

    for i in range(0,a):
        sum = sum + cost1[3*i]
        sum1 = sum1 +cost1[(3*i) + 1]
        sum2 = sum2 + cost1[(3*i) + 2]
        totdist1 = totdist1 + total_distance[3*i]
        totdist2 = totdist2 + total_distance[(3 * i) + 1]
        totdist3 = totdist3 + total_distance[(3 * i) + 2]
        totdur1 = totdur1 + total_duration[3 * i]
        totdur2 = totdur2 + total_duration[(3 * i) +1]
        totdur3 = totdur3 + total_duration[(3 * i) + 2]

    print sum
    print sum1
    print sum2
    print totdist1
    print totdist2
    print totdist3
    print totdur1
    print totdur2
    print totdur3

    finalresult = {"id":0,

                  "start":"/locations/" + str(0),

                  "best_route_by_costs":[],

                  "providers":[
                    {"name":data["cost_estimates"][0]["ride_type"],
                     "total_costs_by_cheapest_car_type":0,
                     "total_duration": 0,
                     "currency_code": "USD",
                     "duration_unit": "minute",
                     "total_distance": 0,
                     "distance_unit": "mile"
                     },


                    {"name":data["cost_estimates"][1]["ride_type"],
                     "total_costs_by_cheapest_car_type":0,
                     "total_duration": 0,
                     "currency_code": "USD",
                     "duration_unit": "minute",
                     "total_distance": 0,
                     "distance_unit": "mile"
                     },


                    {"name":data["cost_estimates"][2]["ride_type"],
                     "total_costs_by_cheapest_car_type":0,
                     "total_duration": 0,
                     "currency_code": "USD",
                     "duration_unit": "minute",
                     "total_distance": 0,
                     "distance_unit": "mile"
                     }
                    ],
                  "end":"/locations/" + str(a)
                  }

    finalresult["providers"][0]["total_costs_by_cheapest_car_type"]=sum
    finalresult["providers"][1]["total_costs_by_cheapest_car_type"] =sum1
    result["providers"][2]["total_costs_by_cheapest_car_type"] = sum2


    finalresult["providers"][0]["total_duration"] = totdur1
    finalresult["providers"][1]["total_duration"] = totdur2
    finalresult["providers"][2]["total_duration"] = totdur3

    finalresult["providers"][0]["total_distance"] = totdist1
    finalresult["providers"][1]["total_distance"] = totdist2
    finalresult["providers"][2]["total_distance"] = totdist3

    print finalresult
    return finalresult

#calling the function
generate_lyft_report1(data2)
