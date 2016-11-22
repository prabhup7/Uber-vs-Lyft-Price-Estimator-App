import os
import requests
import json
import csv

url = 'https://api.lyft.com/v1/cost'

start_lat = '37.7772'
start_lng = '-122.4233',
end_lat = '37.7972'
end_lng = '-122.4533'

payload = {'start_lat': start_lat , 'start_lng': start_lng, 'end_lat': end_lat,'end_lng':end_lng}

myheaders = {'Authorization': '<Auth token>'}
r = requests.get(url, headers=myheaders, params=payload)
data = r.json()

cost = []
for x in range(0, 3):
 cost.append(data["cost_estimates"][0]["estimated_cost_cents_max"]/100.0)
print min(cost)

#Here in this sample it seems that the time taken by each car is same
p = (data["cost_estimates"][1]["estimated_duration_seconds"]/60.0)
minutes = float("{0:.2f}".format(p))

distance = (data["cost_estimates"][1]["estimated_distance_miles"])
#print distance

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

result["providers"][0]["total_costs_by_cheapest_car_type"] = (min(cost))
result["providers"][0]["total_duration"] = minutes
result["providers"][0]["total_distance"] = distance
print result




















































