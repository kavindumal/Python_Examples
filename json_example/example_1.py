import json

# json_file_path = 'json_example/example_1.json'

# with open(json_file_path, 'r') as file:
#     data = json.load(file)
#     for key, value in data.items():
#         print(f"{key}: {value}")

data = {
    'name': 'John Doe',
    'age' : 30,
    'city' : 'New York',
}

with open('json_example/my_json.json', 'w') as file:
    json_data = json.dumps(data, indent=4)
    file.write(json_data)
    
# use indent = 4 to make the json data more readable with spacing