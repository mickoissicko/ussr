# !launcher.py

import os
import webbrowser
import subprocess
import platform

def clear_screen():
    system = platform.system().lower()

    if 'windows' in system:
        os.system('cls')
    else:
        print("Average Hello Kitty OS user:")
        print("Ok, but serious... not Linux, Darwin, or Windows?! Wuh da heellll.?!")

def setup_dependencies_arch():
    clear_screen()
    choice = input("\nDo you have the dependencies set up already? [y/n] ")
    if choice.lower() == 'n':
        os.chdir('archlinux/')
        os.system('chmod +x install.sh')
        os.system('./install.sh')
        os.chdir('..')

def setup_dependencies_win():
    clear_screen()
    choice = input("\nDo you have the dependencies set up already? [y/n] ")
    if choice.lower() == 'n':
        os.chdir('windows/')
        os.system('setup/')
        batch_script_path = 'windows/setup/prerequisites.bat'
        subprocess.run([batch_script_path], shell=True)

        os.chdir('..')

def ussr_for_arch():
    clear_screen()
    os.system('python archlinux/setup/arch.py')

def ussr_for_win():
    clear_screen()
    os.system('python windows/setup/win.py')

def mc_server():
    clear_screen()
    os.system('python prerequisites/config.py')

def main_menu():
    clear_screen()
    print("SETUP PAGE -- LAUNCHER, MAIN MENU")
    print("[1] Dependency setup for Windows")
    print("[2] Dependency setup for Arch")
    print("[3] USSR for Arch")
    print("[4] USSR for Windows")
    print("[5] Install Minecraft")
    print("HEADS UP! Before you can proceed, please configure the paths if you haven't already.")
    print("Don't know how to? See the guide: https://mick.gdn/wiki/ussr.html")
    print("Choice: ")

if __name__ == "__main__":
    while True:
        main_menu()
        choice = input()

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
        else:
            print("Invalid choice. Please choose again.")
