import requests
import urllib

import trip_planner.key

WEATHER_BASE = "http://api.openweathermap.org/data/2.5/weather?"

example = "http://api.openweathermap.org/data/2.5/weather?lat=37.773972&lon=-122.431297&"


def get_weathers(locations):
    toRet = {"descriptions": [],
             "icons": []
             }
    for i in range(0, len(locations)):
        query_dict = {
            "lat": locations[i]['latitude'],
            "lon": locations[i]['longitude'],
            "APPID": trip_planner.key.APPID
        }
        query_str = WEATHER_BASE + urllib.urlencode(query_dict)
        resp = requests.get(query_str).json()
        # print json.dumps(resp)
        toRet["descriptions"].append(resp["weather"][0]["description"])
        toRet["icons"].append(resp["weather"][0]["icon"])

    return toRet


if __name__ == '__main__':
    locations = [
        {
            "address": "san jose gurudwara",
            "latitude": "37.3260696",
            "longitude": "-121.7646021"
        },
        {
            "address": "pleasanton bart station",
            "latitude": "37.7016504",
            "longitude": "-121.8991813"
        },
        {
            "address": "mlk library, san jose",
            "latitude": "37.3382082",
            "longitude": "-121.8863286"
        },
        {
            "address": "33, south third street, san jose",
            "latitude": "37.3358189",
            "longitude": "-121.8877351"
        }
    ]
    get_weathers(locations)
