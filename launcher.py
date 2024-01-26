# !launcher.py

import os
import webbrowser
import subprocess

def setup_dependencies_arch():
    choice = input("\nDo you have the dependencies set up already? [y/n] ")
    if choice.lower() == 'n':
        os.chdir('archlinux/')
        os.system('chmod +x install.sh')
        os.system('./install.sh')
        os.chdir('..')

def setup_dependencies_win():
    choice = input("\nDo you have the dependencies set up already? [y/n] ")
    if choice.lower() == 'n':
        os.chdir('windows/')
        os.system('setup/')
        batch_script_path = 'windows/setup/prerequisites.bat'
        subprocess.run([batch_script_path], shell=True)

        os.chdir('..')

def ussr_for_arch():
    os.system('python archlinux/setup/arch.py')

def ussr_for_win():
    os.system('python windows/setup/win.py')

def mc_server():
    os.system('python prerequisites/config.py')

def main_menu():
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
