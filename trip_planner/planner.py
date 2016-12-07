from flask import json

import best_route
from db_and_common import app


def render_result(route_arg):
    # TODO: implement
    return route_arg




@app.route('/trips', methods=['POST'])
def plan(arg_body=None):
    arg_body = json.loads(arg_body)
    print "inside planner.plan"

    resp = best_route.find_best_route(arg_body)
    best_others = resp['route']
    best_route_by_costs = [arg_body['start']]
    best_route_by_costs.extend(best_others)
    best_route_by_costs.append(arg_body['end'])
    print best_route_by_costs

    # uber_report = best_route.generate_uber_report(best_route_by_costs)
    uber_report = resp['uber']
    lyft_report = best_route.generate_lyft_report(best_route_by_costs)
    toRet = {
        "start": arg_body['start'][2:],
        "best_route_by_costs": best_others,
        "end": arg_body['end'][2:],
        "providers": [
            lyft_report
        ]
    }
    toRet['providers'].extend(uber_report)

    temp = toRet['best_route_by_costs']
    toRet['best_route_by_costs'] = [toRet['start']]
    toRet['best_route_by_costs'].extend(temp)
    toRet['best_route_by_costs'].append(toRet['end'])
    print json.dumps(toRet)
    return toRet
