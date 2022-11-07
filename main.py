import requests
import os
from twilio.rest import Client

open_weather_api_key = os.environ["open_weather_api_key"]
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
twilio_sid = "ACe6e5382825a13db97ad1afbaf0082a9d"
auth_token = os.environ['auth_token']

parameter = {
    "lat": 7.398980,
    "lon": 3.920400,
    "exclude": "current,minutely,daily",
    "appid": open_weather_api_key
}
client = Client(twilio_sid, auth_token)
response = requests.get(OWM_Endpoint, params=parameter)
response.raise_for_status()
data = response.json()
weather = [item["weather"][0]["id"] for item in data["hourly"][:12]]


def is_raining() -> bool:
    for num in weather:
        if num < 700:
            return True
        else:
            return False


if is_raining():
    message = client.messages.create(
        body="it will be raining today don't forget to bring an ☂",
        from_="+19206909329",
        to="+2347045905073"
    )

    print(message.sid)
