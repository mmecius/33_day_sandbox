import requests
import json

URL = "http://api.open-notify.org/iss-now.json"
response = requests.get(url=URL)

if response.status_code != 200:
    response.raise_for_status()

data = response.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)
print(iss_position)
