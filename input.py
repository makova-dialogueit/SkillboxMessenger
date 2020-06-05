# ----------------------------------------------------
# Program by Osipova Tatiana
#
#------------------------------------------------------
import requests

username = input('Name: ')
password = input('Password: ')

while True:
    text = input('Put a text: ')

    requests.get(
        'http://127.0.0.1:5000/send_message',
        json={'username': username,
              'password': password,
              'text': text}
    )