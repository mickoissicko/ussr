# setup/arch.py

import os
import platform
import webbrowser

def main_menu():
    print("SETUP PAGE -- *NIX/DARWIN")
    print("[1] Launch USSR")
    print("[2] Use Ngrok")

def clear_screen():
    system = platform.system().lower()

    if 'linux' in system or 'darwin' in system:
        os.system('clear')
    elif 'windows' in system:
        os.system('cls')
    else:
        print("Couldn't clear screen. Please stop using HelloKitty OS.")

def launch_ussr():
    clear_screen()

    if os.path.exists("token.txt"):
        with open("token.txt", "r") as file:
            autk = file.read().strip()
            print("Did you place the wrong copy-paste of the authentication token? [y/n]")
            wrong_token = input("Your answer: ").lower()
            
            if wrong_token == "y":
                os.remove("token.txt")
                print("Token deleted. Please enter your Ngrok authentication token again.")
                webbrowser.open("https://dashboard.ngrok.com/get-started/your-authtoken")
                autk = input("Your NGROK token: ")
                
                with open("token.txt", "w") as file:
                    file.write(autk)
            elif wrong_token == "n":
                pass
            else:
                print("Invalid input. Assuming 'n'. Proceeding...")
    else:
        print("Enter your Ngrok authentication token:")
        print("This is optional. If you are NOT using Ngrok, feel free to skip by pressing enter.")
        webbrowser.open("https://dashboard.ngrok.com/get-started/your-authtoken")
        autk = input("Your NGROK token: ")
       
        with open("token.txt", "w") as file:
            file.write(autk)

    os.system(f"ngrok config add-authtoken {autk}")
    
    a = os.system('ls')
    print(a)

    os.chdir('../setup/')
    print("Starting the .sh script...")
    os.system("bash start.sh")

def config_ngrok():
    clear_screen()
    
    os.chdir('archlinux/server-arch/config')

    if not os.path.isfile('conf.txt'):
        with open('conf.txt', 'w') as file:
            file.write("# conf.txt\n"
                       "#\n"
                       "# uncomment the line below to allow the app to initialise ngrok\n"
                       "# uncommenting the below line also allows the app to automatically send the ngrok urls if config'd correctly\n"
                       "# \n"
                       "# use-ngrok=True\n")
        
        print("File was not found. I recreated it and repopulated the text within.")
        response = input("Enable Ngrok? [y/n]: ").lower()
        
        if response == 'y':
            with open('conf.txt', 'r') as file:
                data = file.readlines()

            with open('conf.txt', 'w') as file:
                for line in data:
                    if '# use-ngrok=True' in line:
                        file.write('use-ngrok=True\n')
                    else:
                        file.write(line)
        elif response == 'n':
            pass
        else:
            print("Invalid response. Keeping the file as is.")
    else:
        use_ngrok_response = input("Use Ngrok? [y/n]: ").lower()
        
        if use_ngrok_response == 'y':
            with open('conf.txt', 'r') as file:
                data = file.readlines()

            with open('conf.txt', 'w') as file:
                for line in data:
                    if '# use-ngrok=True' in line:
                        file.write('use-ngrok=True\n')
                    else:
                        file.write(line)
        elif use_ngrok_response == 'n':
            with open('conf.txt', 'r') as file:
                data = file.readlines()

            with open('conf.txt', 'w') as file:
                for line in data:
                    if 'use-ngrok=True' in line:
                        file.write('# use-ngrok=True\n')
                    else:
                        file.write(line)
        else:
            print("Invalid response. Keeping the file as is.")

def create_webhook_file():
    os.chdir('archlinux/server-arch/config')
    
    if not os.path.isfile('webhook.txt'):
        with open('webhook.txt', 'w') as file:
            webhook_url = input("Enter your Discord App webhook: ")
            file.write(webhook_url)
            print("Webhook URL stored in webhook.txt")


if __name__ == "__main__":
    while True:
        main_menu()
        choice = input("Enter your choice:  ")

        if choice == "1":
            create_webhook_file()
            launch_ussr()
            break
        elif choice == "2":
            config_ngrok()
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

