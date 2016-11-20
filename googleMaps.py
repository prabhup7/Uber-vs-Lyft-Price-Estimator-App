import requests
import json

BASE_URI = 'https://maps.googleapis.com/maps/api/geocode/json?address='

inp = "33 South Third Street, San Jose California"

query = BASE_URI + inp.replace(' ', '+')
response = requests.get(query)

resp_json_payload = response.json()
print(type(resp_json_payload))
print (resp_json_payload['results'])

print(resp_json_payload['results'][0]['geometry']['location'])