# setup/arch.py

import os
import webbrowser

def main_menu():
    print("[1] Launch USSR")
    print("[2] Use Ngrok")

def launch_ussr():
    os.chdir('setup/')
    
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

    os.system(f"ngrok config add-authtoken {autk}")
    
    print("Starting the .sh script...")
    os.system("bash start.sh")


if __name__ == "__main__":

    while True:
        main_menu()
        choice = input("Enter your choice:  ")

        if choice == "1":
            launch_ussr()
            break
        elif choice == "2":
            print("Ngrok functionality not implemented yet.")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

