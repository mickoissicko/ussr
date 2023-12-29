# Ussr/ussr.py

import os
import subprocess
from flask import Flask, render_template

app = Flask(__name__)

SCRIPTS_FOLDER = r'G:\USSR\script'

@app.route('/')
def index():
    return render_template('index.html')

def execute_script(script_name):
    script_path = os.path.abspath(os.path.join(SCRIPTS_FOLDER, f'{script_name}.bat'))
    
    print(f"Executing {script_name} script. Path: {script_path}")

    process = subprocess.Popen([script_path], shell=True, creationflags=subprocess.CREATE_NEW_CONSOLE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    print(f"Script output:\n{stdout.decode('utf-8')}")
    print(f"Script error:\n{stderr.decode('utf-8')}")

    if process.returncode != 0:
        raise Exception(f"Script execution failed with return code {process.returncode}")

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
        return "Error stopping script on website!"

if __name__ == '__main__':
    app.run(debug=True)
