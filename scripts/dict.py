import json

my_dict = {
    'name': 'Hunter',
    'age': 30,
    'height': 69,
    'details': {
        'job': 'IT Tech',
        'degree': 'Computer Science',
        'married': 'yes'
    }
}

print(my_dict)
print(json.dumps(my_dict, indent=4))