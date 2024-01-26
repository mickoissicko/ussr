# setup/win.py

import os
import webbrowser
import platform

def clear_screen():
    system = platform.system().lower()

    if 'linux' in system or 'darwin' in system:
        os.system('clear')
    elif 'windows' in system:
        os.system('cls')
    else:
        print("Couldn't clear screen. Please stop using HelloKitty OS.")

def main_menu():
    clear_screen()
    print("SETUP PAGE -- WINDOWS")
    print("[1] Launch USSR")
    print("[2] Use Ngrok")

def launch_ussr():
    clear_screen()

    path = input("\nDid you configure paths? [y/n]")

    if path == "y":
        pass
    elif path == "n":
        print("Read the guide!")
        webbrowser.open("https://mick.gdn/wiki/ussr.html")
    else:
        print("Read the guide!")
        webbrowser.open("https://mick.gdn/wiki/ussr.html")
    
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
        webbrowser.open("https://dashboard.ngrok.com/get-started/your-authtoken")
        autk = input("Your NGROK token: ")
       
        with open("token.txt", "w") as file:
            file.write(autk)

    chdir('windows/setup/')
    os.system(f"ngrok.exe config add-authtoken {autk}")
    
    print("Starting the .bat script...")
    os.system('cmd /c start.bat')

def config_ngrok():
    clear_screen()

    os.chdir('windows/server-windows/config')

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

if __name__ == "__main__":

    while True:
        main_menu()
        choice = input("Enter your choice:  ")

        if choice == "1":
            launch_ussr()
            break
        elif choice == "2":
            config_ngrok()
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

