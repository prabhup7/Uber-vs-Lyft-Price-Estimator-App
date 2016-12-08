import requests
import locationApp
from locationApp import *
import locationApp
from locationApp import *
import requests
import json
import itertools
import a2m.itertools
import even_more_itertools
from a2m.itertools import *
#2control over here

r = db.engine.execute('select address from location')


#r1 = db.engine.execute('select address from location where id = 1')
#print r1

#r6 =  db.engine.execute('select address from location where id = 6')
#print r6


r = db.engine.execute('select address from location')
#r2 = db.engine.execute('select longitude from location')

number_of_places = 5

addresslist = []


longitude = []

for i in r:
    eachaddress = str(i['address'])
    addresslist.append(eachaddress)

#print addresslist

starting_point = addresslist[0]

combo1 = list(itertools.permutations(addresslist, 2))

#for i in range(0,21):
# print combo1[i]
#print starting_point

end_point = addresslist[number_of_places -1]
#print end_point
    #print eachaddress

#print addresslist

countable_addrlist = []

for i in range(1,4):
    countable_addrlist.append(addresslist[i])


#print countable_addrlist

combo2 = list(itertools.permutations(countable_addrlist, 3))
#print combo2

#for i in range(0,6):
    #print combo2[i]

#actual route list starts from here

route1 = combo2[0]
route2 = combo2[1]
route3 = combo2[2]
route4 = combo2[3]
route5 = combo2[4]
route6 = combo2[5]

print combo1[1][0]
print combo1[1][1]

print combo1[19][0]


#print route2
#print route3
#print route4
#print route5
#print route6
#print route2
#print route3

#print combo1


distance = []
duration = []
#-------------------------------------------using the google API to retrieve the distances and duration for all combinations of routes between 5 places
for i in range(0,20):

    print combo1[i]
    BASE_URI = 'https://maps.googleapis.com/maps/api/distancematrix/json?units='
    payload = {'origins':combo1[i][0], 'destinations': combo1[i][1],'key': 'Your google api key'}
    r = requests.get(BASE_URI,params=payload)
    d = json.dumps(r.json())
    json_acceptable_string = d.replace("'", "\"")
    data = json.loads(json_acceptable_string)
#    a = d["rows"][0]["elements"][0]["distance"]["value"]
#    print a
    print data
    a = data["rows"][0]["elements"][0]["distance"]["value"]
    print i
    q = float(a) * 0.0006213
    distance.append(q)

    b = data["rows"][0]["elements"][0]["duration"]["value"]
    print b
    print float(b) / 60
    duration.append(b)

#    p = a.split(" ")
#    m =  p[0].replace(",", "")

    #print q


#print combo1
#print distance


routelist1 = []

routelist2 = []

routelist3 = []

routelist4 = []

routelist5 = []

routelist6 = []

print"The possible routes are:-"

for i in range(0,3):
    routelist1.append(route1[i])
routelist1.insert(0, addresslist[0])
routelist1.insert(len(routelist1), addresslist[len(addresslist) - 1])
print routelist1

for i in range(0,3):
    routelist2.append(route2[i])
routelist2.insert(0,addresslist[0])
routelist2.insert(len(routelist2),addresslist[len(addresslist)-1])
print routelist2

for i in range(0,3):
    routelist3.append(route3[i])
routelist3.insert(0,addresslist[0])
routelist3.insert(len(routelist3),addresslist[len(addresslist)-1])
print routelist3

for i in range(0,3):
    routelist4.append(route4[i])
routelist4.insert(0,addresslist[0])
routelist4.insert(len(routelist4),addresslist[len(addresslist)-1])
print routelist4

for i in range(0,3):
    routelist5.append(route5[i])
routelist5.insert(0,addresslist[0])
routelist5.insert(len(routelist5),addresslist[len(addresslist)-1])
print routelist5

for i in range(0,3):
    routelist6.append(route6[i])
routelist6.insert(0,addresslist[0])
routelist6.insert(len(routelist6),addresslist[len(addresslist)-1])
print routelist6

#1
print("Considering route1")
print routelist2

result1 = {"id": 0,

     "start": "/locations/" + str(1),

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
     "end": "/locations/" + str(5)
              }


p1 =  distance[0]+distance[5]+distance[10]+distance[15]
result1["providers"][0]["total_distance"] = p1
print p1
a1 =  duration[0]+duration[5]+duration[10]+duration[15]
result1["providers"][0]["total_duration"] = a1
print a1
print "result1 is"
print result1


#2
print("Considering route2")
print routelist2

result2 = {"id": 0,

     "start": "/locations/" + str(1),

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
     "end": "/locations/" + str(5)
              }


p2 =  distance[0]+distance[6]+distance[14]+distance[11]
result2["providers"][0]["total_distance"] = p2
print p2
a2 =  duration[0]+duration[6]+duration[14]+duration[11]
result1["providers"][0]["total_duration"] = a2
print a2
print "result2 is"
print result2


#3
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
     "end": "/locations/" + str(5)
              }

p3 =  distance[1]+distance[9]+distance[6]+distance[15]
result2["providers"][0]["total_distance"] = p3
print p3
a3 =  duration[1]+duration[9]+duration[6]+duration[15]
result1["providers"][0]["total_duration"] = a3
print a3
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
     "end": "/locations/" + str(5)
              }
p4 =  distance[0]+distance[6]+distance[14]+distance[11]
result2["providers"][0]["total_distance"] = p4
print p4
a4 =  duration[0]+duration[6]+duration[14]+duration[11]
result1["providers"][0]["total_duration"] = a4
print a1
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
     "end": "/locations/" + str(5)
              }
p5 =  distance[2]+distance[13]+distance[5]+distance[11]
result2["providers"][0]["total_distance"] = p5
print p5
a5 =  duration[2]+duration[13]+duration[5]+duration[11]
result1["providers"][0]["total_duration"] = a5
print a5
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
p6 =  distance[2]+distance[14]+distance[9]+distance[7]
result2["providers"][0]["total_distance"] = p6
print p6
a6 =  duration[2]+duration[14]+duration[9]+duration[7]
result1["providers"][0]["total_duration"] = a6
print a6
print "result6 is"
print result6


print("Hello Dollie")

print("According to minimum distance")

a = min(enumerate(['p1', 'p2', 'p3', 'p4', 'p5', 'p6']), key=lambda x, ns=locals(): ns[x[1]])[1]
print "The minimum total distance is"
print p6
print a
print " "
------------------------checking and retrieving the most optimized route with respect to minimum total distance
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


print("According to minimum duration")

b = min(enumerate(['a1', 'a2', 'a3', 'a4', 'a5', 'a6']), key=lambda x, ns=locals(): ns[x[1]])[1]
print "The minimum total duration is"
print a6
print b
#------------------------------------------------checking and retrieving the most estimated costs according to the least time
if b == 'a1':
   print result1

elif b == 'a2':
   print result2

elif b == 'a3':
   print result3

elif b == 'a4':
   print result4

elif b == 'a5':
   print result5

elif b == 'a6':
   print result6

else:
   print "No matches found"




