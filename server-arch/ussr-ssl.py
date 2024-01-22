# ussr-ssl.py

import subprocess
import os
import requests
from flask import Flask, render_template
import time

app = Flask(__name__)

MC_FOLDER = '/append/path/to/server/folder'
DISCORD_WEBHOOK_URL = 'your_webhook_for_server_Status'

def send_discord_message(content):
    data = {'content': content}
    requests.post(DISCORD_WEBHOOK_URL, json=data)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start')
def start():
    send_discord_message('``server starting...``')

    start_command = ['java', '-jar', '-Xms256M', '-Xmx5G', f'{MC_FOLDER}/fabric.jar']
                        # CHANGE -Xms OR -Xmx arguments to utilise RAM based on your needs
    subprocess.Popen(start_command, cwd=MC_FOLDER)

    send_discord_message('``server started``')
    return "Server started successfully!"

@app.route('/stop')
def stop():
    send_discord_message('``server stopping...``')

    stop_script_path = '/append/the/path/to/the/ussr/directory/script/stop.py'
    subprocess.Popen(['python', stop_script_path])

    time.sleep(13)

    send_discord_message('``server stopped``')
    return "Stopping server..."

backgroundpath = '/append/the/path/to/the/ussr/directory/script/backg.py'

background_process = subprocess.Popen(['python', backgroundpath])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=443, debug=True)