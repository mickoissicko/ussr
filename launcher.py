# !launcher.py

import os
import webbrowser

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
        bsc = 'windows/setup/prerequisites.bat'
        subprocess.run([batch_script_path], shell=True)
        os.chdir('..')

def ussr_for_arch():
    
    paths = input("Did you configure the paths? [y/n]")
    if paths == "y":
        pass
    elif paths == "n":
        print("Read the guide!")
        webbrowser.open("https://mick.gdn/wiki/ussr.html")
    else:
        print("Read the guide!")
        webbrowser.open("https://mick.gdn/wiki/ussr.html")

    os.system('python archlinux/setup/arch.py')

def ussr_for_win():

    paths = input("Did you configure the paths? [y/n]")
    if paths == "y":
        pass
    elif paths == "n":
        print("Read the guide!")
        webbrowser.open("https://mick.gdn/wiki/ussr.html")
    else:
        print("Read the guide!")
        webbrowser.open("https://mick.gdn/wiki/ussr.html")

    os.system('python windows/setup/win.py')

def main_menu():
    print("[1] Dependency setup for Windows")
    print("[2] Dependency setup for Arch")
    print("[3] USSR for Arch")
    print("[4] USSR for Windows")
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
        else:
            print("Invalid choice. Please choose again.")