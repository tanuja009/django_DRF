# import requests
# import json

# URL="http://127.0.0.1:8000"
# data={
#     'name':'Sona',
#     'roll':105,
#     'city':'Rau'
# }
# json_data=json.dumps(data)
# r=requests.post(url=URL,data=json_data)
# data=r.json()
# print(data)

import requests
import json

URL = "http://127.0.0.1:8000"
data = [
    {
        'name': 'Sona',
        'roll': 105,
        'city': 'Rau'
    },
    {
        'name': 'Ravi',
        'roll': 106,
        'city': 'Indore'
    },
    {
        'name': 'Anita',
        'roll': 107,
        'city': 'Bhopal'
    },
    {
        'name': 'Vijay',
        'roll': 108,
        'city': 'Dewas'
    }
]

headers = {
    'Content-Type': 'application/json'
}
response = requests.post(url=URL, data=json.dumps(data), headers=headers)

if response:
    print("Data saved successfully:", response.json())
    
else:
    print("Failed to save data:", response.status_code, response.text)