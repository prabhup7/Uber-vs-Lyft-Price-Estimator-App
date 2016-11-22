import os
import requests
import json

url = 'https://api.lyft.com/v1/cost'

start_lat = '37.7772'
start_lng = '-122.4233',
end_lat = '37.7972'
end_lng = '-122.4533'

payload = {'start_lat': start_lat , 'start_lng': start_lng, 'end_lat': end_lat,'end_lng':end_lng}

myheaders = {'Authorization': 'Bearer <Authorization token>'}


r = requests.get(url, headers=myheaders, params=payload)

data = json.dumps(r.json())

print data

r.status_code