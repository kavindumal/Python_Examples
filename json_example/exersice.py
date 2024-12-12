# [
#     {"name": "John doe", "grade": 85},
#     {"name": "Own doe", "grade": 72},
#     {"name": "Benn doe", "grade": 90},
#     {"name": "Red doe", "grade": 65}
# ]

# You are given a json file name students.json with contain information about students and there grades. Your task is to 
# 1. Read the json file
# 2. Display the name of all students who scored above 75
# 3. Add a new student record to the file
# 4. Save the updated data back to the json file

import json

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def display_students_above_75(data):
    for student in data:
        if student['grade'] > 75:
            print(student['name'])
            
def add_new_student(data, name, grade):
    new_student = {
        'name': name,
        'grade': grade
    }
    data.append(new_student)

def save_to_json_file(file_path, data):
    with open(file_path, 'w') as file:
        json_data = json.dumps(data, indent=4)
        file.write(json_data)

def main():
    json_file_path = 'json_example/students.json'
    data = read_json_file(json_file_path)
    add_new_student(data, 'Kavindu Malshan', 80)
    save_to_json_file(json_file_path, data)
    display_students_above_75(data)
    
if __name__ == '__main__':
    main()
    
