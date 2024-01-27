# root/launcher.py
import os
import platform
import webbrowser
import subprocess

def clear_screen():
    system = platform.system().lower()

    if 'linux' in system or 'darwin' in system:
        os.system('clear')
    elif 'windows' in system:
        os.system('cls')
    else:
        print("Couldn't clear screen. Please stop using HelloKitty OS.")

def setup_dependencies_win():
    clear_screen()
    print("THIS MODE IS DEPRECATED, PLEASE USE THE LAUNCHER.BAT SCRIPT!!")
    batch_script_path = '../dependencies/prerequisites.bat'
    subprocess.run([batch_script_path], shell=True)
    os.chdir('../scripts')

def setup_dependencies_arch():
    clear_screen()
    print("THIS MODE IS DEPRECATED, PLEASE USE THE LAUNCHER.SH SCRIPT!!")
    os.chdir('../dependencies')
    os.system('chmod +x install.sh')
    os.system('./install.sh')
    os.chdir('../scripts')

def ussr_for_arch():
    clear_screen()

    print("OPTIONAL: If you are not using Ngrok, feel free to use Nn to skip.")
    yesnop = input("Did you configure Ngrok token? [Y/N/Nn]")

    if yesnop.lower() == 'y':
        pass

    elif yesnop.lower() == 'n':
        webbrowser.open("https://dashboard.ngrok.com/get-started/your-authtoken")

        print("INFO: Your NGROK Authtoken is available at:")
        print("https://dashboard.ngrok.com/get-started/your-authtoken")
        ngrok_token = input("Enter NGROK authentication token: ")

        with open('../config/token.txt', 'w') as file:
            file.write(f"{ngrok_token}")

    elif yesnop.lower() == 'Nn':
        pass
    
    else:
        print("Only 'y' or 'n'. Indecisive enough?")

    clear_screen()
    print("OPTIONAL: If you are not using a webhook, feel free to use Nn to skip.")
    print("TIP: It is recommended to use a webhook if you will be using tools such as Tmux!")

    yesnop = input("Did you configure webhook URL? [Y/N/Nn]")

    if yesnop.lower() == 'y':
        pass

    elif yesnop.lower() == 'n':
        webhook_url = input("Enter webhook URL: ")

        with open('../config/webhook.txt', 'w') as file:
            file.write(f"{webhook_url}")

    elif yesnop.lower() == 'Nn':
        pass
    
    else:
        print("Only 'y' or 'n'. Indecisive enough?")

    with open('../config/token.txt', 'r') as file:
        ngrok_token = file.read().strip()
    os.system(f'ngrok config add-authtoken {ngrok_token}')
    
    os.system('chmod +x start.sh')
    os.system('./start.sh')
    os.chdir('../scripts')

def ussr_for_win():
    clear_screen()

    print("OPTIONAL: If you are not using Ngrok, feel free to use Nn to skip.")
    yesnop = input("Did you configure Ngrok token? [Y/N/Nn]")

    if yesnop.lower() == 'y':
        pass

    elif yesnop.lower() == 'n':
        webbrowser.open("https://dashboard.ngrok.com/get-started/your-authtoken")

        print("INFO: Your NGROK Authtoken is available at:")
        print("https://dashboard.ngrok.com/get-started/your-authtoken")
        ngrok_token = input("Enter NGROK authentication token: ")

        with open('../config/token.txt', 'w') as file:
            file.write(f"{ngrok_token}")

    elif yesnop.lower() == 'Nn':
        pass
    
    else:
        print("Only 'y' or 'n'. Indecisive enough?")

    clear_screen()
    print("OPTIONAL: If you are not using a webhook, feel free to use Nn to skip.")
    print("TIP: It is recommended to use a webhook if you will be using tools such as Tmux!")

    yesnop = input("Did you configure webhook URL? [Y/N/Nn]")

    if yesnop.lower() == 'y':
        pass

    elif yesnop.lower() == 'n':
        webhook_url = input("Enter webhook URL: ")

        with open('../config/webhook.txt', 'w') as file:
            file.write(f"{webhook_url}")

    elif yesnop.lower() == 'Nn':
        pass
    
    else:
        print("Only 'y' or 'n'. Indecisive enough?")

    with open('../config/token.txt', 'r') as file:
        ngrok_token = file.read().strip()

    os.chdir('../ngrok')
    os.system(f'ngrok.exe config add-authtoken {ngrok_token}')
    
    os.chdir('../bin_win')
    os.system('python ussr-ssl.py')

def mc_server():
    clear_screen()
    os.system('python ../dependencies/config.py')

def configr():
    conf_file_path = '../config/conf.txt'

    with open(conf_file_path, 'r') as file:
        lines = file.readlines()

    user_input = input("Do you want to enable NGROK? [Y/N]: ").strip().lower()

    if user_input == 'y':
        lines[5] = 'use-ngrok=True\n'
    elif user_input == 'n':
        lines[5] = '# use-ngrok=True\n'
    else:
        print("y or n, no inbetweens. Jeez, indecisive enough?")

    with open(conf_file_path, 'w') as file:
     file.writelines(lines)

    print("enabled! yay! wow! fun!")

    conf_file_path = '../config/conf.txt'

    with open(conf_file_path, 'r') as file:
        lines = file.readlines()

    user_input = input("Do you want to enable automatic NGROK start? [Y/N]")

    with open(conf_file_path, 'r') as file:
        lines = file.readlines()

    user_input = input("Do you want to enable automatic NGROK start? [Y/N]")

    if user_input == 'y':
        lines[6] = 'autongrok=True\n'
    elif user_input == 'n':
        lines[6] = '# autongrok=True\n'
    else:
        print("y or n, no inbetweens. Jeez, indecisive enough?")

    with open(conf_file_path, 'w') as file:
        file.writelines(lines)

def main_menu():
    while True:
        os.chdir('../scripts')
        clear_screen()
        print("SETUP PAGE -- LAUNCHER, MAIN MENU")
        print("[1] Dependency setup for Windows")
        print("[2] Dependency setup for Arch")
        print("[3] USSR for Arch")
        print("[4] USSR for Windows")
        print("[5] Install Minecraft Server")
        print("[6] Configure USSR")
        print("[X] Quit")
        print("HEADS UP! Before you can proceed, please configure the paths if you haven't already.")
        print("Don't know how to? See the guide: https://mick.gdn/wiki/ussr.html")

        choice = input("Choice: ")

        if choice == '1':
            setup_dependencies_win()
        elif choice == '2':
            setup_dependencies_arch()
        elif choice == '3':
            ussr_for_arch()
        elif choice == '4':
            ussr_for_win()
        elif choice == '5':
            mc_server()
        elif choice == '6':
            configr()
        elif choice.lower() == 'x' or 'X':
            break 
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main_menu()
