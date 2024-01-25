# !launcher.py

import os

def setup_dependencies():
    choice = input("Do you have the dependencies set up already? [y/n] ")
    if choice.lower() == 'n':
        os.chdir('archlinux/')
        os.system('chmod +x install.sh')
        os.system('./install.sh')
        os.chdir('..')

def ussr_for_arch():
    os.system('python setup/arch.py')

def ussr_for_win():
    os.system('python setup/win.py')

def main_menu():
    print("[1] Dependency setup")
    print("[2] USSR for Arch")
    print("[3] USSR for Windows")
    print("\nChoice: ")

if __name__ == "__main__":
    while True:
        main_menu()
        choice = input()

        if choice == '1':
            setup_dependencies()
        elif choice == '2':
            ussr_for_arch()
        elif choice == '3':
            ussr_for_win()
        else:
            print("Invalid choice. Please choose again.")
