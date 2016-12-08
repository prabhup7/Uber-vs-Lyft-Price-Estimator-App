import requests
from flask import json

BASE_URI = 'https://maps.googleapis.com/maps/api/geocode/json?address='
KEY_ARUN = "AIzaSyAw2jBXNkaAns3t3N2K3c1EjNBb-H5nYBQ"


def getCoordinates(inp):
    query = BASE_URI + inp.replace(' ', '+') + "&key=" + KEY_ARUN
    print "query: " + query
    response = requests.get(query)
    resp_json_payload = response.json()
    print resp_json_payload
    coord = resp_json_payload['results'][0]['geometry']['location']
    opstr = json.dumps(coord)
    print(opstr)
    # print(coord['lat'])
    print "------"
    coord['lat'] = float("%.5f" % coord['lat'])
    coord['lng'] = float("%.5f" % coord['lng'])
    print float("%.5f" % coord['lat'])
    print '====='
    return coord


if __name__ == '__main__':
    inp = '33 South third Street, San Jose'
    getCoordinates(inp=inp)
