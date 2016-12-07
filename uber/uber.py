import json

import requests

from model import location

places=[]
lat_dict={}
long_dict={}
lat_list=[]
long_list=[]
places_dict={}
waypoints_dict={}
str1=[]
sorted_ways_uber=[]
output_list=[]
sorted_ways_id=[]
waypoints_list=[3,4,5]
#source = start
#dest = end
source = 1
dest = 2
str2=''


def getfromdb():
    count=0
    rows = location.query.filter_by(id=source).first()
    # places_dict[source]['latitude']= rows.latitude;
    # places_dict[source]['longitude']= rows.longitude;
    places_dict[source] = {'latitude':rows.latitude,'longitude':rows.longitude}
    rows1 = location.query.filter_by(id=dest).first()
    # places_dict[dest]['latitude']= rows1.latitude
    # places_dict[dest]['longitude']= rows1.longitude
    places_dict[dest] = {'latitude':rows1.latitude,'longitude':rows1.longitude}
    print (places_dict)

    for i in range(0,(len(waypoints_list))):
        rows3 = location.query.filter_by(id=waypoints_list[i]).first()
        # waypoints_dict[rows3.id]['latitude']= rows3.latitude;
        # waypoints_dict[rows3.id]['longitude']= rows3.longitude;
        waypoints_dict[rows3.id] = {'latitude':rows3.latitude,'longitude':rows3.longitude}
    print (waypoints_dict)
    for key in waypoints_dict:
        if count<(len(waypoints_dict)-1):
            str1.append(waypoints_dict[key]['latitude']+','+waypoints_dict[key]['longitude']+'|')
        else:
            str1.append(waypoints_dict[key]['latitude']+','+waypoints_dict[key]['longitude'])
        count = count + 1
    # print str1
    str2 = ''.join(str(e) for e in str1)  
    print str2
    findwaypoints(str2)

def findwaypoints(str2):
    city ='origin='+str(places_dict[source]['latitude'])+','+str(places_dict[source]['longitude'])+'&destination='+str(places_dict[dest]['latitude'])+','+str(places_dict[dest]['longitude'])+'&waypoints=optimize:true|'+str(str2)
    print city
    url_waypoints = 'https://maps.googleapis.com/maps/api/directions/json?'+city+'&key=AIzaSyD6OzDVE_s67_JmJvfPHi28XDj8hLhaWMk'
    waypoints_response = requests.get(url_waypoints)
    print "way points route ++++++++++++++++++++++++++++++++++"
    print waypoints_response


        
    waypoints_response1= waypoints_response.json()['routes'][0]['waypoint_order']
    # waypoints_response1= waypoints_response.json()['routes'][0]
    print "way point response1",waypoints_response1
        
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
    
    sorted_ways_uber.insert(0,[places_dict[source]['latitude'],places_dict[source]['longitude']])
    for b in waypoints_response1:
        print b
        sorted_ways_uber.append([waypoints_dict[waypoints_list[b]]['latitude'],waypoints_dict[waypoints_list[b]]['longitude']])    
        sorted_ways_id.append(waypoints_list[b])
    print ("sorted id's",sorted_ways_id)

    for way in sorted_waypoint:
        for latlong in way:
            sorted_ways_uber.append(way[latlong])
    #print sorted_ways_uber    
    sorted_ways_uber.append([places_dict[dest]['latitude'],places_dict[dest]['longitude']])
    print ("optimized route coordinates",sorted_ways_uber);
    for i in range(len(sorted_ways_id)):
        output_list.append("/locations/"+str(sorted_ways_id[i]))

    print output_list
    

def get_distance():
    uber_dis_pool_distance = [] 
    uber_dis_pool_lowestimate = []
    uber_dis_xcartype_distance = []
    uber_xl_cartype_lowestimate = []
    uber_dis_xcartype_lowestimate = []
    uber_dis_pool_time = []
    uber_xl_cartype_time = []
    uber_dis_xcartype_time = []
    var= 0
    for another_value in range(1,len(sorted_ways_uber)):



            start_latitude = sorted_ways_uber[var][0]
            start_longitude = sorted_ways_uber[var][1]
            end_latitude  =  sorted_ways_uber[another_value][0]
            end_longitude = sorted_ways_uber[another_value][1]

            # print "start latitude:%d",(start_latitude)
            # print "start longitude:%d",(start_longitude)
            # print "end latitude:%d",(end_latitude)
            # print "end longitude:%d",(end_longitude)


            var = var + 1
            url_uber = 'https://api.uber.com/v1.2/estimates/price'
            parameters = {       
            'server_token': 'NgDT7eBNK2-e5TBiQ1kjN1nnGxA9xquK1XIZEg0J',
            'start_latitude':start_latitude ,
            'start_longitude':start_longitude,
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
                print ("uber pool distance",uber_dis_pool_distance)
                print ("uber pool cost",uber_dis_pool_lowestimate)
                final_uberpool_distance = sum(uber_dis_pool_distance)
                uber_dis_pool_time.append(uber_final_res['prices'][0]['duration'])
                
                # for individual_distance_pool in uber_dis_pool_distance:
                #     total_sum_distance = total_sum_distance + individual_distance_pool
                # print total_sum_distance

                # for individual_cost_pool in uber_dis_pool_estimate
                

                # uberX distance
                # uberX cost

                uber_dis_xcartype_distance.append(uber_final_res['prices'][1]['distance'])
                uber_dis_xcartype_lowestimate.append(uber_final_res['prices'][1]['low_estimate'])
                print ("uber X distance",uber_dis_xcartype_distance)
                print ("uber X cost",uber_dis_xcartype_lowestimate)

                uber_xl_cartype_lowestimate.append(uber_final_res['prices'][2]['low_estimate'])   
                #print uber_final_res['prices'][0]['distance']
            else:
                
                print "please enter distance below 100 miles"
    final_uberpool_cost = sum(uber_dis_pool_lowestimate)
    final_uberx_cost = sum(uber_dis_xcartype_lowestimate)
    final_uberxl_cost =sum(uber_xl_cartype_lowestimate)

    print ("total uberpool cost",final_uberpool_cost);
    print ("total uberx cost",final_uberx_cost);
    print ("total uber xl cost",final_uberxl_cost);

    


if __name__ == "__main__":
    getfromdb()
    get_distance()    
