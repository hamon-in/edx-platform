import json


def json_loads(json_input):
    return json.loads(json_input.decode('utf-8'))
