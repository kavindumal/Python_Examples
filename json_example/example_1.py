import json

json_file_path = 'json_example/example_1.json'

with open(json_file_path, 'r') as file:
    data = json.load(file)
    print(data, type(data))