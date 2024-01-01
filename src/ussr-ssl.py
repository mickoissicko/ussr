# Ussr/ussr.py

import os
import subprocess
import mcrcon
from flask import Flask, render_template

app = Flask(__name__)

SCRIPTS_FOLDER = r'G:\USSR\script'

def check_server_status():
    try:
        with mcrcon.MCRcon('localhost', 'root_admin', 25575) as client:
            response = client.command('/list')
            return True if 'players online' in response else False
    except Exception as e:
        print(f"Error checking server status: {e}")
        return False

@app.route('/')
def index():
    server_status = check_server_status()
    return render_template('index.html', server_status=server_status)

def execute_script(script_name):
    script_path = os.path.abspath(os.path.join(SCRIPTS_FOLDER, f'{script_name}.bat'))
    
    print(f"Executing {script_name} script. Path: {script_path}")

    process = subprocess.Popen([script_path], shell=True, creationflags=subprocess.CREATE_NEW_CONSOLE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    print(f"Script output:\n{stdout.decode('utf-8')}")
    print(f"Script error:\n{stderr.decode('utf-8')}")

    if process.returncode != 0:
        raise Exception(f"Script execution failed with return code {process.returncode}")
    
def get_online_players():
    try:
        with mcrcon.MCRcon('localhost', 'root_admin', 25575) as client:
            response = client.command('/list')
            player_list = response.split(':')[-1].strip().split(', ')
            return player_list
    except Exception as e:
        print(f"Error getting online players: {e}")
        return []

@app.route('/online_players')
def online_players():
    players = get_online_players()
    return ','.join(players)

def get_server_info():
    try:
        with mcrcon.MCRcon('localhost', 'root_admin', 25575) as client:
            response = client.command('/list')
            return response
    except Exception as e:
        print(f"Error getting server info: {e}")
        return ""

@app.route('/server_info')
def server_info():
    info = get_server_info()
    return info

@app.route('/test')
def test():
    try:
        execute_script('test')
        return "Script stopped successfully!"
    except Exception as e:
        print(f"Error stopping script: {e}")
        return "Error stopping script!"

@app.route('/start')
def start():
    execute_script('start')
    return "Script started successfully!"

@app.route('/stop')
def stop():
    try:
        execute_script('stop')
        return "Script stopped successfully!"
    except Exception as e:
        print(f"Error stopping script: {e}")
        return "Error stopping script!"

@app.route('/stop-on-website')
def stop_on_website():
    try:
        execute_script('stop')
        return "Stop script executed successfully!"
    except Exception as e:
        print(f"Error stopping script on website: {e}")
        return "Error stopping script on the website!"

@app.route('/shutdown')
def shutdown():
    try:
        execute_script('nuke')
        return "Shutdown script executed successfully!"
    except Exception as e:
        print(f"Error executing shutdown script: {e}")
        return "Error executing the shutdown script!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=443, debug=True)
