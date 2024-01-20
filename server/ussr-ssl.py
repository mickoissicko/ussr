# ussr-ssl.py

import subprocess
import os
import requests
from flask import Flask, render_template
import time

app = Flask(__name__)

MC_FOLDER = '/home/main/mc'
DISCORD_WEBHOOK_URL = 'YOUR-WEBHOOK-URL'

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
    subprocess.Popen(start_command, cwd=MC_FOLDER)
    
    time.sleep(15)
    
    send_discord_message('``server started``')
    return "Server started successfully!"

@app.route('/stop')
def stop():
    send_discord_message('``server stopping...``')
    
    stop_script_path = '/home/main/project/script/stop.py'
    subprocess.Popen(['python', stop_script_path])
    
    time.sleep(13)
    
    send_discord_message('``server stopped``')
    return "Stopping server..."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=443, debug=True)