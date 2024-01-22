import subprocess
import requests
import json
import os
import sys
import time

LOCK_FILE = "ngroksenpai.lock"

def check_lock_file():
    return os.path.exists(LOCK_FILE)

def create_lock_file():
    with open(LOCK_FILE, "w") as lock_file:
        lock_file.write(str(os.getpid()))

def remove_lock_file():
    if os.path.exists(LOCK_FILE):
        os.remove(LOCK_FILE)

def check_tunnel(curl_command, target_string):
    result = subprocess.run(curl_command, capture_output=True, text=True)
    output = result.stdout
    if target_string in output:
        return output
    return None

def send_discord_webhook(webhook_url, region, url):
    message = f"* {region} === `{url}`"
    payload = {"content": message}
    requests.post(webhook_url, json=payload)

starter_script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'starter.bat')
subprocess.Popen(['cmd', '/c', starter_script_path], shell=True)

time.sleep(8)

def main():
    if check_lock_file():
        print("Another instance is already running. Exiting.")
        sys.exit(1)

    create_lock_file()

    try:
        curl_commands = [
            "curl 127.0.0.1:4040/api/tunnels",
            "curl 127.0.0.1:4041/api/tunnels",
            "curl 127.0.0.1:4042/api/tunnels",
            "curl 127.0.0.1:4043/api/tunnels",
            "curl 127.0.0.1:4044/api/tunnels",
        ]

        target_string = "tcp://"

        discord_webhook_url = "discord_webhook_for_sending_ngrok_urls"

        region_mapping = {
            ".au": "Sydney",
            ".ap": "Singapore",
            ".in": "Mumbai",
            ".eu": "Europe",
            "": "Ohio",
        }

        for curl_command in curl_commands:
            result = check_tunnel(curl_command.split(), target_string)
            if result:
                data = json.loads(result)
                tunnel_info = data["tunnels"][0]
                public_url = tunnel_info["public_url"]

                for region_code, region_name in region_mapping.items():
                    if region_code in public_url:
                        public_url = public_url.replace("tcp://", "")
                        send_discord_webhook(discord_webhook_url, f"{region_name}", public_url)
                        break
    finally:
        remove_lock_file()

if __name__ == "__main__":
    main()