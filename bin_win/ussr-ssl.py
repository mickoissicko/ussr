# bin/ussr-ssl.py

import subprocess
import os
import requests
from flask import Flask, render_template
import time

os.chdir('../bin_win')

conf_file_path = '../config/conf.txt'
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
    ngroksenpai_script_path = '../bin_win/script/ngroksenpai.py'
    subprocess.Popen(['python', ngroksenpai_script_path])

app = Flask(__name__)

DISCORD_WEBHOOK_URL_FILE = '../config/stat.txt'

def get_discord_webhook_url():
    webhook_url = None
    if os.path.exists(DISCORD_WEBHOOK_URL_FILE):
        with open(DISCORD_WEBHOOK_URL_FILE, 'r') as file:
            webhook_url = file.read().strip()
    return webhook_url

# thx chatgpt lmao
DISCORD_WEBHOOK_URL = get_discord_webhook_url()

def send_discord_message(content):
    data = {'content': content}
    requests.post(DISCORD_WEBHOOK_URL, json=data)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start')
def start():
    send_discord_message('``server starting...``')

    script_dir = os.path.dirname(os.path.abspath(__file__))
    mc_dir = os.path.join(script_dir, '../bin/.mc')
    start_command = ['java', '-jar', '-Xms256M', '-Xmx5G', os.path.join(mc_dir, 'server.jar'), 'nogui']

    try:
        subprocess.Popen(start_command, cwd=mc_dir)
        time.sleep(27)
        send_discord_message('``server started``')
        return "Server started successfully!"
    except Exception as e:
        error_message = f"Error starting server: {str(e)}"
        send_discord_message(error_message)
        return error_message

@app.route('/stop')
def stop():
    send_discord_message('``server stopping...``')
    
    stop_script_path = 'script/stop.py'
    subprocess.Popen(['python', stop_script_path])
    
    time.sleep(13)
    
    send_discord_message('``server stopped``')
    return "Stopping server..."

@app.route('/purge')
def purge():
    try:
        os.system('taskkill -f -im ngrok.exe')
    except Exception as e:
        print(f'{e}');
        os.system('taskkill -f -im ngrok')
    except Exception as e:
        print(f'Could not kill ngrok: {e}')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=443, debug=True)