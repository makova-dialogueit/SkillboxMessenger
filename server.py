from flask import Flask, request
from datetime import datetime
import time

app = Flask(__name__)
server_start = datetime.now().strftime('%H:%M:%S %D/%M/%Y')
messages = [
    {'username': 'jack', 'text': 'Hello everyone', 'timestamp': time.time()},
    {'username': 'jack2', 'text': 'Hello Jack', 'timestamp': time.time()},
]

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
        'current_time_seconds': time.time()
    }

@app.route("/send_message")
def send_message():
    print()
    username = request.json['username']
    text = request.json['text']
    messages.append({'username': username, 'text': text, 'timestamp': time.time()})
    return {'ok': True}

@app.route("/get_messages")
def get_messages():
    return {
        'messages': messages
    }

app.run()