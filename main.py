import requests
from twilio.rest import Client
import os


account_sid = os.environ.get('account_sid')
auth_token = os.environ.get('auth_token')


parameters = {
    'appid' : '4e86514e93eee1398fca589e03c09d8f', 
    'lat' : -16.483610, 
    'lon' : 145.465271,
    'units' : 'metric', 
    'cnt' : 4
}

response = requests.get('https://api.openweathermap.org/data/2.5/forecast', params=parameters)
response.raise_for_status()
forecast = response.json()['list'] 
 
for i in forecast:
    if (i['weather'][0]['id']) < 700:
        print('Get an umbrella')
        
        client = Client(account_sid, auth_token)
        message = client.messages\
            .create(
            body='It is going to rain today. Remenber to bring an umbrella. ☂️',
            from_='+12675507117',
            to='+573215696357',
        )
        print(message.status)
        break