# ussr-ssl.py

import subprocess
import os
from flask import Flask, render_template

app = Flask(__name__)

MC_FOLDER = '/home/main/mc'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start')
def start():
    start_command = ['java', '-jar', '-Xms256M', '-Xmx5G', f'{MC_FOLDER}/fabric.jar']
    subprocess.Popen(start_command, cwd=MC_FOLDER)
    return "Server started successfully!"

@app.route('/stop')
def stop():
    stop_script_path = '/home/main/project/script/stop.py'
    subprocess.Popen(['python', stop_script_path])
    return "Stopping server..."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)