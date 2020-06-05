# ----------------------------------------------------
# Program by Osipova Tatiana
#
#------------------------------------------------------
import requests, time
from datetime import datetime

while True:
    response = requests.get('http://127.0.0.1:5000/get_messages')
    messages = response.json()['messages']

    for message in messages:
        dt = datetime.fromtimestamp(message['timestamp'])
        dt = dt.strftime('%H:%M:%S %d/%m/%Y')
        print(dt, message['username'])
        print(message['text'])
        print()

    time.sleep(1.0)
