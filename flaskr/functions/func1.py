import json

def my_awesome_function():
    header_row=["Month","Issues"]
    json_data=[header_row]
    return json.dumps(json_data)