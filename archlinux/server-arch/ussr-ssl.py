import os
import sys
import time
import json
import requests
import subprocess
from flask import Flask, render_template

conf_file_path = 'config/conf.txt'
use_ngrok = False

with open(conf_file_path, 'r') as conf_file:
    for line in conf_file:
        line = line.strip()
        if line.startswith('#'):
            continue
        if 'use-ngrok=True' in line:
            use_ngrok = True
            break

if use_ngrok:
    ngroksenpai_script_path = 'script/ngroksenpai.py'
    subprocess.Popen(['python', ngroksenpai_script_path])

app = Flask(__name__)

MC_FOLDER = '../.mc/'
DISCORD_WEBHOOK_URL_FILE = os.path.join('archlinux', 'server-arch', 'config', 'webhook.txt')

def get_discord_webhook_url():
    webhook_url = None
    webhook_file_path = os.path.join('archlinux', 'server-arch', DISCORD_WEBHOOK_URL_FILE)
    
    if os.path.exists(webhook_file_path):
        with open(webhook_file_path, 'r') as file:
            webhook_url = file.read().strip()

    return webhook_url

# thx chatgpt lmao
DISCORD_WEBHOOK_URL = get_discord_webhook_url()

def send_discord_message(content):
    if DISCORD_WEBHOOK_URL is not None:
        data = {'content': content}
        try:
            requests.post(DISCORD_WEBHOOK_URL, json=data)
        except requests.exceptions.RequestException as e:
            print(f"Error sending Discord message: {e}")
    else:
        print("Discord webhook URL is not available. Cannot send message.")


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start')
def start():
    send_discord_message('``server starting...``')
    
    if DISCORD_WEBHOOK_URL is not None:
        start_command = ['java', '-jar', '-Xms256M', '-Xmx5G', f'{MC_FOLDER}/fabric.jar']
        subprocess.Popen(start_command, cwd=MC_FOLDER)

        time.sleep(27)

        send_discord_message('``server started``')
        return "Server started successfully!"
    else:
        return "Error starting server: Discord webhook URL is not available. Noob. Heh."

@app.route('/stop')
def stop():
    send_discord_message('``server stopping...``')
    
    stop_script_path = 'script/stop.py'
    subprocess.Popen(['python', stop_script_path])
    
    time.sleep(13)
    
    send_discord_message('``server stopped``')
    return "Stopping server..."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=443, debug=True)