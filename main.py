import requests


# url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
# response = requests.get(url)
# print(response.json())

def send_message():
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": "It will rain today. Remember to bring an umbrella ☔"
    }

    response = requests.post(url, json=payload)
    response.raise_for_status()

#send_message()


MY_LAT = "51.51705273275507"
MY_LONG = "-0.1869446108280679"


# Endpoints

THREE_DAY_DATA = "https://api.openweathermap.org/data/2.5/forecast"

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "cnt": 4
}

response = requests.get(THREE_DAY_DATA,  params=weather_params)
data = response.json()

will_it_rain = False
for i in range(0,4):
    if int(data['list'][i]["weather"][0]["id"]) < 700:
        will_it_rain = True

if will_it_rain == False or will_it_rain==True:
    send_message()

