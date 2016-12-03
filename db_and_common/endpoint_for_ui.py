from flask import request, json
from flask_sqlalchemy import SQLAlchemy

import location_api.location_app
from db_and_common import app

# from db_and_common.__init__ import location
BASE_URI = 'http://127.0.0.1:5009'

db = SQLAlchemy(app)


@app.route('/ui')
def parse_and_forward():
    """Parses the parameters in query string
    and posts corresponding request(s) to /v1/location (inside location_api.location_app)"""
    i = 0
    body = {}
    while (request.args.get('Location ' + (str(i))) is not None):
        print "Location " + (str(i)) + ": " + request.args.get('Location ' + (str(i)))
        name = "Location " + (str(i))
        body['name'] = name
        body['address'] = request.args.get(name).replace('+', ' ')
        body_json = json.dumps(body)
        # resp = requests.post(url=BASE_URI+'/v1/locations', json=body_json)
        resp = location_api.location_app.create(body)
        print 'resp: ' + str(resp.get_data)
        i += 1

    # call prabhu's API
    return "Hello from locationApp, Gurnoor<br/> Query: " + request.query_string + \
           "<br/> location 0: " + request.args.get('Location 0')
