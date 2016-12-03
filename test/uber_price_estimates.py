import json
import os

import requests

#url = 'https://sandbox-api.uber.com/v1.2/estimates/price'
url = 'https://api.uber.com/v1.2/estimates/price'

parameters = {
  'server_token': os.environ['UBER_SERVER_TOKEN'],
  'start_latitude': 21.3088619,
  'start_longitude': -157.8086674,
  'end_latitude': 21.2965912,
  'end_longitude': -157.8564657,
}

response = requests.get(url, params=parameters)

data = json.dumps( response.json(), indent=2 )

print(data)
