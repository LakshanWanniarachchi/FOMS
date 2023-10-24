
from requests import post
import json

import datetime
import time
import schedule


def job():
    print("Scheduled task is running at", datetime.datetime.now())


job()
# Define the API endpoint URL
api_url = "https://www.smm-world.com/api/v1"

#Define the required parameters
api_key = "c292d86d5f7168f0cc32dce1c2904bcbc8722c12da4b5c9964f3af1fffee2f626bf46e2962af058c9608ba59efdff846"
action = "add"
service_id = 120
link = "https://soundcloud.com/user-631461695/d-rose-lil-pump"
quantity = 100

# Create the request payload
payload = {
    "key": api_key,
    "action": action,
    "service": service_id,
    "link": link,
    "quantity": quantity

}

# Send the POST request
response = post(api_url, json=payload)
print(response.status_code)

# Check the response
if response.status_code == 200:
    # Request was successful, and you can parse the JSON response
    response_data = response.json()
    print(response_data)
else:
    # Request failed
    print(f"Request failed with status code: {response.status_code}")
    print(response.text)
