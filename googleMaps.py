import requests

BASE_URI = 'https://maps.googleapis.com/maps/api/geocode/json?address='


def getCoordinates(inp):
    query = BASE_URI + inp.replace(' ', '+')
    response = requests.get(query)
    resp_json_payload = response.json()
    coord = resp_json_payload['results'][0]['geometry']['location']
    # opstr = json.dumps(coord)
    print(coord)
    # print(coord['lat'])
    return coord


if __name__ == '__main__':
    inp = '33 South third Street, San Jose'
    getCoordinates(inp=inp)
