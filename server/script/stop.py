# stop.py

import subprocess

server_address = 'localhost'
server_port = '25575'
server_password = 'root_admin'

def stop_server():
    try:
        stop_command = f'mcrcon -H {server_address} -P {server_port} -p {server_password} "/stop"'
        subprocess.run(stop_command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error stopping server: {e}")

if __name__ == "__main__":
    stop_server()