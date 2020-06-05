from flask import Flask, request
from datetime import datetime
import time

app = Flask(__name__)
server_start = datetime.now().strftime('%H:%M:%S %D/%M/%Y')
messages = [
    {'username': 'jack', 'text': 'Hello everyone', 'timestamp': time.time()},
    {'username': 'jack2', 'text': 'Hello Jack', 'timestamp': time.time()},
]

users = {
    'jack': '123',
    'jack2': '111',
}

@app.route("/")
def hello():
    return  'Hello, User! Its our messenger. Its status <a href="/status">status</a>'

@app.route("/status")
def status():
    return {
        'status': 'OK',
        'name': 'Skillbox Messenger',
        'server_start_time': server_start,
        'server_current_time': datetime.now().strftime('%H:%M:%S %D/%M/%Y'),
        'current_time_seconds': time.time(),
        'current_message_number': len(messages),
        'current_member_number': len(users)
    }

@app.route("/send_message")
def send_message():
    username = request.json['username']
    password = request.json['password']
    text = request.json['text']

    if username in users:
        if users[username] != password:
            return {'ok': False}
    else:
        users[username] = password

    messages.append({'username': username, 'text': text, 'timestamp': time.time()})

    # if text contains Hello, add bot Hello
    if 'Hello' in text:
        messages.append({'username': 'ThisIsBotsGreeting', 'text': 'Hello, '+ username, 'timestamp': time.time()})
    return {'ok': True}

@app.route("/get_messages")
def get_messages():
    after = float(request.args['after'])
    result = []

    for message in messages:

        if message['timestamp'] > after:
            result.append(message)

    return {
        'messages': result
    }

app.run()