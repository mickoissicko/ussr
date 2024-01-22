import subprocess
import time
import os
import sys

LOCK_FILE = "run_ngrok.lock"

def check_lock_file():
    return os.path.exists(LOCK_FILE)

def create_lock_file():
    with open(LOCK_FILE, "w") as lock_file:
        lock_file.write(str(os.getpid()))

def remove_lock_file():
    if os.path.exists(LOCK_FILE):
        os.remove(LOCK_FILE)

def run_ngrok_command(region):
    command = f"ngrok tcp --region {region} 25565"
    subprocess.run(command, shell=True)

def main():
    if check_lock_file():
        print("Another instance is already running. Exiting.")
        sys.exit(1)

    create_lock_file()

    try:
        regions = ['ap', 'us', 'au', 'eu', 'in']

        for region in regions:
            run_ngrok_command(region)

        print("Waiting for 5 seconds...")
        time.sleep(5)

        subprocess.run("python drive:/path/to/ussr/script/ngroksenpai.py", shell=True)
    finally:
        remove_lock_file()

if __name__ == "__main__":
    main()