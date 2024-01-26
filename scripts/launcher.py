# root/launcher.py
import os
import platform

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
    batch_script_path = '../dependencies/prerequisites.bat'
    subprocess.run([batch_script_path], shell=True)
    os.chdir('../scripts')

def setup_dependencies_arch():
    clear_screen()
    os.chdir('../dependencies')
    os.system('chmod +x install.sh')
    os.system('./install.sh')
    os.chdir('../scripts')

def ussr_for_arch():
    clear_screen()
    os.system('chmod +x start.sh')
    os.system('./start.sh')
    os.chdir('../scripts')

def ussr_for_win():
    clear_screen()
    batch_script_path = 'start.bat'
    subprocess.run([batch_script_path], shell=True)
    os.chdir('../scripts')

def mc_server():
    clear_screen()
    os.system('python ../dependencies/config.py')

def configr():
    conf_file_path = '../config/conf.txt'
    
    with open(conf_file_path, 'r') as file:
        lines = file.readlines()

    user_input = input("Do you want to enable NGROK? (Y/N): ").strip().lower()

    if user_input == 'y':
        lines[5] = '# use-ngrok=True\n'
    elif user_input == 'n':
        lines[5] = 'use-ngrok=True\n'
    else:
        print("y or n, no inbetweens. Jeez, indecisive enough?")

    with open(conf_file_path, 'w') as file:
        file.writelines(lines)

    print("enabled! yay! wow! fun!")


def main_menu():
    os.chdir('../scripts')
    clear_screen()
    print("SETUP PAGE -- LAUNCHER, MAIN MENU")
    print("[1] Dependency setup for Windows")
    print("[2] Dependency setup for Arch")
    print("[3] USSR for Arch")
    print("[4] USSR for Windows")
    print("[5] Install Minecraft")
    print("[6] Configure USSR")
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
    else:
        print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main_menu()
