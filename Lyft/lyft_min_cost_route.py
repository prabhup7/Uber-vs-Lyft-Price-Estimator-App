




import locationApp
from locationApp import *
import requests
import json
import itertools
import a2m.itertools
import even_more_itertools
from a2m.itertools import *
#2control over here



r = db.engine.execute('select lat from location')
r2 = db.engine.execute('select longitude from location')

number_of_places = 5

latitudes = []

longitude = []

for i in r:
    start_lat = str(i['lat'])
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

for i in range(0,5):
    pl_ind_lat_lng["location_no."] = i
    pl_ind_lat_lng["lats"] = latitudes[i]
    pl_ind_lat_lng["lngs "] = longitude[i]
    #print pl_ind_lat_lng


combo1 = list(itertools.permutations([0,1,2,3,4], 2))
#print combo1[1][0]
#print combo1
#print combo1
#r i in range(0,42):
   # print combo1[i]

#start_location_lat = latitudes[combo1[0]]
#print latitudes
#start_location_lng = longitude[combo1[18][0]]
#end_location_lat = latitudes[combo1[18][1]]
#end_location_lng = longitude[combo1[18][1]]

#print "the pairs of addresses are"
#print combo1[29]
#print start_location_lat
#print start_location_lng
#print end_location_lat
#print end_location_lng

estimate_cost = []
total_duration = []
total_distance = []

for i in range(0,20):
    #print "The pair of addresses are"
    print combo1[i]
    #print combo1[i][0]
    #print combo1[i][1]
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
    myheaders = {'Authorization': 'Bearer <auth token>'}
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

    i = result["providers"][0]["total_costs_by_cheapest_car_type"] = (min(cost))
    estimate_cost.append(i)


    result["providers"][0]["total_duration"] = minutes
    #d = result["providers"][0]["total_duration"]
    total_duration.append(minutes)
    result["providers"][0]["total_distance"] = distance
    total_distance.append(distance)
    #print combo1[int(i)][0]
    #print combo1[int(i)][1]
    p = number_of_places - 1

    #print combo1[int(i)][0]
    #print combo1[int(i)][1]
    result["id"] = 200000

    p = int(i)
    #print combo1[int(1)][0]
    print result
    #print i

for i in range(0,20):
    #print estimate_cost[i]
    print total_duration[i]


combo = list(itertools.permutations([0,1,3,4,5,6], 6))
#print combo

originallist = [0,1,3,4,5]
start = [originallist[0]]

end  = originallist[-1]

list1 = []

for i in range (1, len(originallist)-1):
 list1.append(originallist[i])


#print list(itertools.permutations(list1, 3))
for i in range(0,6):
 routei = list(itertools.permutations(list1, 3))[i]
 print routei

route1 = list(itertools.permutations(list1, 3))[0]
route2 = list(itertools.permutations(list1, 3))[1]
route3 = list(itertools.permutations(list1, 3))[2]
route4 = list(itertools.permutations(list1, 3))[3]
route5 = list(itertools.permutations(list1, 3))[4]
route6 = list(itertools.permutations(list1, 3))[5]

print route1

print route2

print route3

print route4

print route5

print route6


---------------------------------------------------------------------------1
routelist1 = []

routelist2 = []

routelist3 = []

routelist4 = []

routelist5 = []

routelist6 = []

print"The possible routes are:-"

for i in range(0,3):
    routelist1.append(route1[i])
routelist1.insert(0,originallist[0])
routelist1.insert(len(routelist1),originallist[len(originallist)-1])
print routelist1


for i in range(0,3):
    routelist2.append(route2[i])
routelist2.insert(0,originallist[0])
routelist2.insert(len(routelist2),originallist[len(originallist)-1])
print routelist2

for i in range(0,3):
    routelist3.append(route3[i])
routelist3.insert(0,originallist[0])
routelist3.insert(len(routelist3),originallist[len(originallist)-1])
print routelist3

for i in range(0,3):
    routelist4.append(route4[i])
routelist4.insert(0,originallist[0])
routelist4.insert(len(routelist4),originallist[len(originallist)-1])
print routelist4

for i in range(0,3):
    routelist5.append(route5[i])
routelist5.insert(0,originallist[0])
routelist5.insert(len(routelist5),originallist[len(originallist)-1])
print routelist5

for i in range(0,3):
    routelist6.append(route6[i])
routelist6.insert(0,originallist[0])
routelist6.insert(len(routelist6),originallist[len(originallist)-1])
print routelist6



print("Considering route1")
print routelist1

result1 = {"id": 0,

     "start": "/locations/" + str(0),

    "best_route_by_costs": [],

    "providers": [
                  {"name": "Lyft",
                   "total_costs_by_cheapest_car_type": 0,
                   "total_duration": 0,
                   "currency_code": "USD",
                   "duration_unit": "minute",
                   "total_distance": 0,
                   "distance_unit": "mile"
                   }
              ],
     "end": "/locations/" + str()
              }
#p1.append(estimate_cost[0]+estimate_cost[5]+estimate_cost[10]+estimate_cost[15])
p1 = estimate_cost[0]+estimate_cost[5]+estimate_cost[10]+estimate_cost[15]
result1["providers"][0]["total_costs_by_cheapest_car_type"] = p1

#print "The total estimated costs for this route is"
#print p2
mins1 = total_duration[0]+total_duration[5] + total_duration[10] + total_duration[15]
result1["providers"][0]["total_duration"] = mins1
#print result["providers"][0]["total_duration"]
distance1 = total_distance[0]+total_distance[5]+total_distance[10]+total_distance[15]
result1["providers"][0]["total_distance"] = distance1
result1["start"] = "/locations/" + str(0)
result1["end"] = "/locations/" + str(number_of_places)
print "result1 is"
print result1


print("Considering route2")
print routelist2

result2 = {"id": 0,

     "start": "/locations/" + str(0),

    "best_route_by_costs": [],

    "providers": [
                  {"name": "Lyft",
                   "total_costs_by_cheapest_car_type": 0,
                   "total_duration": 0,
                   "currency_code": "USD",
                   "duration_unit": "minute",
                   "total_distance": 0,
                   "distance_unit": "mile"
                   }
              ],
     "end": "/locations/" + str()
              }


p2 =  estimate_cost[0]+estimate_cost[6]+estimate_cost[14]+estimate_cost[11]
result2["providers"][0]["total_costs_by_cheapest_car_type"] = p2

#print "The total estimated costs for this route is"
#print p2
mins2 = total_duration[0]+total_duration[6] + total_duration[14] + total_duration[11]
result2["providers"][0]["total_duration"] = mins2
#print result["providers"][0]["total_duration"]
distance2 = total_distance[0]+total_distance[6]+total_distance[14]+total_distance[11]
result2["providers"][0]["total_distance"] = distance2
result2["start"] = "/locations/" + str(0)
result2["end"] = "/locations/" + str(number_of_places)
print "result2 is"
print result2







print("Considering route3")
print routelist3

result3 = {"id": 0,

     "start": "/locations/" + str(0),

    "best_route_by_costs": [],

    "providers": [
                  {"name": "Lyft",
                   "total_costs_by_cheapest_car_type": 0,
                   "total_duration": 0,
                   "currency_code": "USD",
                   "duration_unit": "minute",
                   "total_distance": 0,
                   "distance_unit": "mile"
                   }
              ],
     "end": "/locations/" + str()
              }

p3 =  estimate_cost[1]+estimate_cost[9]+estimate_cost[6]+estimate_cost[15]

result3["providers"][0]["total_costs_by_cheapest_car_type"] = p3
print "The total estimated costs for this route is"
print p3
mins3 = total_duration[1]+total_duration[9] + total_duration[6] + total_duration[15]
result3["providers"][0]["total_duration"] = mins3
print result3["providers"][0]["total_duration"]

distance3 = total_distance[1]+total_distance[9]+total_distance[6]+total_distance[15]
result3["providers"][0]["total_distance"] = distance3
result3["start"] = "/locations/" + str(0)
result3["end"] = "/locations/" + str(number_of_places)
print "result3 is"
print result3



print("Considering route4")
print routelist4
result4 = {"id": 0,

     "start": "/locations/" + str(0),

    "best_route_by_costs": [],

    "providers": [
                  {"name": "Lyft",
                   "total_costs_by_cheapest_car_type": 0,
                   "total_duration": 0,
                   "currency_code": "USD",
                   "duration_unit": "minute",
                   "total_distance": 0,
                   "distance_unit": "mile"
                   }
              ],
     "end": "/locations/" + str()
              }
p4 =  estimate_cost[1]+estimate_cost[10]+estimate_cost[13]+estimate_cost[19]
result4["providers"][0]["total_costs_by_cheapest_car_type"] = p4
#print "The total estimated costs for this route is"
#print p4
mins4 = total_duration[1]+total_duration[10] + total_duration[13] + total_duration[19]
result4["providers"][0]["total_duration"] = mins4
#print result["providers"][0]["total_duration"]
distance4 = total_distance[1]+total_distance[10]+total_distance[13]+total_distance[19]
result4["providers"][0]["total_distance"] = distance4
result4["start"] = "/locations/" + str(0)
result4["end"] = "/locations/" + str(number_of_places)
print "result4 is"
print result4



print("Considering route5")
print routelist5
result5 = {"id": 0,

     "start": "/locations/" + str(0),

    "best_route_by_costs": [],

    "providers": [
                  {"name": "Lyft",
                   "total_costs_by_cheapest_car_type": 0,
                   "total_duration": 0,
                   "currency_code": "USD",
                   "duration_unit": "minute",
                   "total_distance": 0,
                   "distance_unit": "mile"
                   }
              ],
     "end": "/locations/" + str()
              }
p5 =  estimate_cost[2]+estimate_cost[13]+estimate_cost[5]+estimate_cost[11]
result5["providers"][0]["total_costs_by_cheapest_car_type"] = p2
#print "The total estimated costs for this route is"
#print p5
mins5 = total_duration[2]+total_duration[13] + total_duration[5] + total_duration[11]
result5["providers"][0]["total_duration"] = mins5
#print result["providers"][0]["total_duration"]
distance5= total_distance[2]+total_distance[13]+total_distance[5]+total_distance[11]
result5["providers"][0]["total_distance"] = distance5
result5["start"] = "/locations/" + str(0)
result5["end"] = "/locations/" + str(number_of_places)
print "result5 is"
print result5



print("Considering route6")
print routelist6
result6 = {"id": 0,

     "start": "/locations/" + str(0),

    "best_route_by_costs": [],

    "providers": [
                  {"name": "Lyft",
                   "total_costs_by_cheapest_car_type": 0,
                   "total_duration": 0,
                   "currency_code": "USD",
                   "duration_unit": "minute",
                   "total_distance": 0,
                   "distance_unit": "mile"
                   }
              ],
     "end": "/locations/" + str()
              }
p6 =  estimate_cost[2]+estimate_cost[14]+estimate_cost[9]+estimate_cost[7]
result6["providers"][0]["total_costs_by_cheapest_car_type"] = p6
#print "The total estimated costs for this route is"
#print p2
mins6 = total_duration[2]+total_duration[14] + total_duration[9] + total_duration[7]
result6["providers"][0]["total_duration"] = mins6
#print result["providers"][0]["total_duration"]
distance6 = total_distance[2]+total_distance[14]+total_distance[9]+total_distance[7]
result6["providers"][0]["total_distance"] = distance6
result6["start"] = "/locations/" + str(0)
result6["end"] = "/locations/" + str(number_of_places)
print "result6 is"
print result6






#print ("The minimum cost is  " + repr(mincost))




#def determine():
mincost = min(p1, p2, p3, p4, p5, p6)
print mincost
a = min(enumerate(['p1', 'p2', 'p3', 'p4', 'p5', 'p6']), key=lambda x, ns=locals(): ns[x[1]])[1]
print "a"
print a

if a == 'p1':
   print result1

elif a == 'p2':
   print result2

elif a == 'p3':
   print result3

elif a == 'p4':
   print result4

elif a == 'p5':
   print result5

elif a == 'p6':
   print result6

else:
   print "No route"




















