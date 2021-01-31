import requests
from datetime import datetime

MY_LAT = 54.687157
MY_LONG = 25.279652
URL = "http://api.open-notify.org/iss-now.json"
response = requests.get(url=URL)

if response.status_code != 200:
    response.raise_for_status()

data = response.json()
iss_longitude = float(data["iss_position"]["longitude"])
iss_latitude = float(data["iss_position"]["latitude"])
iss_position = (iss_longitude, iss_latitude)


def iss_to_my_position():
    if (iss_longitude - 5) >= iss_latitude <= (iss_longitude + 5):
        if (iss_longitude - 5) <= iss_longitude <= (iss_longitude + 5):
            return True
    else:
        return False


print(iss_to_my_position())

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get(f"https://api.sunrise-sunset.org/json?lat={MY_LAT}&lng={MY_LONG}&formatted=0")
if response.status_code != 200:
    response.raise_for_status()

data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1][:2])
sunset = int(data["results"]["sunset"].split("T")[1][:2])
time_now = datetime.now()

