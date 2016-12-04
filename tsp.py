#!/usr/bin/python
import MySQLdb
import json
import math

# connect
db = MySQLdb.connect(host="localhost", user="root", passwd="password",
db="my_db")

cursor = db.cursor()
locations = []
result = []
radius = 6371
distance_array = []
# execute SQL select statement
cursor.execute("SELECT * FROM LOCATION")

# commit your changes
db.commit()

# get the number of rows in the resultset
numrows = int(cursor.rowcount)
#print numrows

for i in range(0,numrows):
	row = cursor.fetchone()
	address=row[1]
	lat=row[3]
	lon=row[4]
	locations.append({'address': address, 'lat' : lat, 'lon' : lon})

def distance (temp,locations):
	for x in range(0,len(locations)):
		dlat = math.radians(float(temp["lat"])-float(locations[x]["lat"]))
		dlon = math.radians(float(temp["lon"])-float(locations[x]["lon"]))
		a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(float(temp["lat"])))*math.cos(math.radians(float(locations[x]["lat"])))*math.sin(dlon/2)*math.sin(dlon/2)
		c = 2*math.atan2(math.sqrt(a),math.sqrt(1-a))
		d = radius * c
		distance_array.append(d)
		return distance_array.index(min(distance_array))

source = locations[0]
locations.pop(0)
destination = locations[len(locations)-1]
locations.pop(len(locations)-1)
temp = source
result.append(source)
i = 0
while (i < len(locations)):
	index_next = distance(temp,locations)
	result.append(locations[index_next])
	locations.pop(index_next)
	
result.append(destination)
print result

    	



