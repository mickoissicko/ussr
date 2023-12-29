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

    subprocess.Popen([script_path], shell=True, creationflags=subprocess.CREATE_NEW_CONSOLE)

@app.route('/start')
def start():
    execute_script('start')
    return "Script started successfully!"

@app.route('/stop')
def stop():
    execute_script('stop')
    return "Script stopped successfully!"

if __name__ == '__main__':
    app.run(debug=True)
