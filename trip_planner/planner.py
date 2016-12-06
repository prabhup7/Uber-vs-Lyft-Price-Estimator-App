from flask import json

import best_route
from db_and_common import app


def render_result(route_arg):
    pass


id = 0


@app.route('/trips', methods=['POST'])
def plan(arg_body=None):
    arg_body = json.loads(arg_body)
    print "inside planner.plan"

    best_others = best_route.find_best_route(arg_body)
    best_route_by_costs = [arg_body['start']]
    best_route_by_costs.extend(best_others)
    best_route_by_costs.append(arg_body['end'])
    print best_route_by_costs

    uber_report = best_route.generate_uber_report(best_route_by_costs)
    lyft_report = best_route.generate_lyft_report(best_route_by_costs)

    id += 1
    toRet = {
        "id": id,
        "start": arg_body['start'],
        "best_route_by_costs": best_others,
        "end": arg_body['end'],
        "providers": [
            uber_report,
            lyft_report
        ]
    }

    render_result(toRet)
