import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

MS_Endpoint = "https://www.meteosource.com/api/v1/free/point?"
api_key = API_KEY
account_sid = SID
auth_token = TOKEN

weather_params = {
    "lat": "51.5072",
    "lon": "0.1276",
    "sections": "current,daily",
    "language": "en",
    "key": api_key,
    "units": "metric"
}

response = requests.get(MS_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
temperature = weather_data["current"]["temperature"]
rainy_days = []
for day in weather_data["daily"]["data"]:
    print(day)
    if "rain" in day["summary"].lower():
        rainy_days.append(day["day"][5:])
print(rainy_days)

rota_list = ["Samriti", "Laura", "Alberto", "Esther"]
how_many_times = 0
if how_many_times % 4 == 0:
    on_rota = "Samriti"
elif how_many_times % 4 == 1:
    on_rota = "Laura"
elif how_many_times % 4 == 2:
    on_rota = "ALberto"
elif how_many_times % 4 ==3:
    on_rota = "Esther"


body = f"Dear All:\n\n" \
       f"Happy Monday! Today's temperature is {temperature} celsius." \
       f"It might rain on {','.join(x for x in rainy_days)}" \
       f"Remember to bring an umbrella☔️" \
       f"\n\nThis week's person on cleaning rota is: {on_rota}" \
       f"\nPlease make sure you : \n 1. Hoover the common areas including stairs and corridors" \
       f"\n 2. Clean the bathroom you use. " \
       f"\n 3. Any other tasks you think is necessary, for example, wiping the fridge, window edges, kitchen surfaces, etc." \
       f"\n before Sunday" \
       f"\n\nI hope you have a nice week! Whatever you are doing, I am sure you are amazing, and keep it up!☀️ " \
       f"\n\nWith ❤️\nFrom LZ"


client = Client(account_sid, auth_token)
message = client.messages \
    .create(
    body=body.replace("All","Laura"),
    from_="+447412091201",
    to="+447884570193"
)
print(message.status)




