import requests
import json

URL="http://127.0.0.1:8000"
# def post_data():
#     data={
#     'name':'sharvik',
#     'roll':110,
#     'city':'khandawa'
#     }
#     headers = {
#             'Content-Type': 'application/json'
#         }
#     json_data=json.dumps(data)
#     r=requests.post(url=URL,headers=headers,data=json_data)
#     data=r.json()
#     print(data)
# post_data()


def get_data():

    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.get(url=URL, headers=headers)

    if response:
        print("Data saved successfully:", response.json())
    else:
        print("Failed to save data:", response.status_code, response.text)





import requests
import json

def update_data():
    URL = 'https://example.com/api/update'  # Replace with your actual URL

    data = {
        "name": "Anita",
        'roll': 107,
        'city': 'delhi'
    }
    
    headers = {
        'Content-Type': 'application/json'
    }
    
    try:
        # Send the PUT request with the data
        response = requests.put(url=URL, headers=headers, data=json.dumps(data))
        
        # Check if the request was successful
        if response.ok:
            print("Data updated successfully:", response.json())
        else:
            print("Failed to update data. Status code:", response.status_code, response.text)
    
    except requests.exceptions.RequestException as e:
        # Print the exception if the request failed
        print("An error occurred:", e)

update_data()


# def patch_data(data):
#     headers = {
#        'Content-Type': 'application/json'
#      }
#     try:
    
#         # Send the PUT request with the data
#         response = requests.patch(url=URL, headers=headers, data=json.dumps(data))
        
#         # Check if the request was successful
#         if response:
#             print("Data updated successfully:", response.json())
#         else:
#             print("Failed to update data. Status code:", response.status_code)
#             print("Response text:", response.text)
#     except Exception as e:
#         print("error occured",e)

# data={
#     'id':102,
#     'name':"rohit"
# }
# patch_data(data)

# def delete_data(data):
#     headers={
#          'Content-Type': 'application/json'
#     }

    
#     try:
#         # Send the PUT request with the data
#         response = requests.delete(url=URL, headers=headers)
        
#         # Check if the request was successful
#         if response:
#             print("Data deleted successfully")
#         else:
#             print("Failed to update data. Status code:", response.status_code,response.text)
    
#     except Exception as e:
#         # Print the exception if the request failed
#         print("An error occurred:", e)
            
# data={
#     'id':105
# }
# delete_data(data)

    
    

    
