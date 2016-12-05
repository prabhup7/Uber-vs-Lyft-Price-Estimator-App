import os
import requests
import json
from flask import jsonify
from flask import request
from flask import Flask
from model import db
from model import location
from model import createDB
from model import app as application
from djikstra import Vertex,Graph,dijkstra,shortest
import heapq


app = Flask(__name__)
places=[]
lat_dict={}
long_dict={}
lat_list=[]
long_list=[]
g= Graph()
#env $(cat .env | xargs) python 
#url = 'https://sandbox-api.uber.com/v1.2/estimates/price'
url = 'https://api.uber.com/v1.2/estimates/price'

# def get_response():
#       parameters = {
#       'server_token': os.environ['UBER_SERVER_TOKEN'],
#       'start_latitude': 21.3088619,
#       'start_longitude': -157.8086674,
#       'end_latitude': 21.2965912,
#       'end_longitude': -157.8564657,
#       }

#       response = requests.get(url, params=parameters)
#       data = json.loads(response.text)
#       #print(data)
#       process_response(data)

# def process_response(l1):
#       #crime_type = []
#       for key in l1["prices"]:
#             if(key["localized_display_name"]== "uberX"):
#                   #print "data"
#                   #distance.update({})
#                   Vertex.

        
#         #for key in data["crimes"]:
#             #crime_type.append(key["type"])


def get_places():
      try:
            #rows= location.query.filter_by().all()
            rows = location.query.with_entities(location.name,location.latitude,location.longitude)
            #rows= location.query.get()
            for key in rows:
                  places.append(key.name)
                  lat_list.append(key.latitude)
                  long_list.append(key.longitude)
                  lat_dict[key.name] = key.latitude
                  long_dict[key.name] = key.longitude
            print (places)
            print (long_dict)
            print (lat_dict)
            print (lat_list)
            print (long_list)
      except Exception,e:
		print str(e)


def build_graph():
      for i in range(0,len(places)):
            g.add_vertex(places[i])
      c= g.get_vertices()
      print (c)



def get_distance():
      try:
            for i in range(0,len(lat_list)):
                  for j in range(i+1,len(long_list)):
                        s1 = lat_list[i]
                        e1 = long_list[i]
                        s2 = lat_list[j]
                        e2 = long_list[j]
                        #print(s1,e1,s2,e2)
                        parameters = {
                              'server_token': 'NgDT7eBNK2-e5TBiQ1kjN1nnGxA9xquK1XIZEg0J',
                              'start_latitude': float(s1),
                              'start_longitude': float(e1),
                              'end_latitude': float(s2),
                              'end_longitude': float(e2),
                              }
                        response = requests.get(url, params=parameters)
                        data = json.loads(response.text)
                        #print(data)
                        if (response.status_code==422):
                              edge= "100"
                              #print (edge)
                        else:
                              for key in data["prices"]:
                                    if(key["localized_display_name"]== "uberX"):
                                          edge = int(key["low_estimate"])
                                          
                                          print (edge,places[i],places[j])
                                          g.add_edge(places[i],places[j],edge)
            
            print_graph()     

                        

      except Exception,e:
		print str(e)

def print_graph():
      print 'Graph data:'
      for v in g:
            for w in v.get_connections():
                  vid = v.get_id()
                  wid = w.get_id()
                  print '( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w))

if __name__ == "__main__":
      get_places()
      build_graph()
      get_distance()
      dijkstra(g, g.get_vertex('San Jose'), g.get_vertex('San Fransisco')) 
      target = g.get_vertex('San Fransisco')
      path = [target.get_id()]
      shortest(target, path)
      print 'The shortest path : %s' %(path[::-1])
    
