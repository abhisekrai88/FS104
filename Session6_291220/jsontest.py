#load json as dictionary

import json

person = '{"name": "Abhisek", "languages": ["English", "Hindi"]}'
person_dict = json.loads(person)

print(person_dict)

print(person_dict['languages'])