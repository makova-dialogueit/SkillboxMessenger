# ----------------------------------------------------
# Program by Osipova Tatiana
#
#------------------------------------------------------
import requests

username = input('Name: ')

while True:
    text = input('Put a text: ')

    requests.get(
        'http://127.0.0.1:5000/send_message',
        json={'username': username, 'text': text}
    )