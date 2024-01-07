# Universal Server Start Remote (USSR)
* USSR is intentional, I wanted to make a funny abbreviation.
* I am not serious, the comments are trash
* Good luck LOL

# Archlinux Installation
This guide assumes you have basic Archlinux & overall Linux experience. Please RTFM if you encounter any issues.

Step 1 **Installing python & pip**
pacman -Sy python
sudo pacman -S python-pip

Step 2 **Let's get Flask installed**

cd ~/arch-2.0
git clone https://aur.archlinux.org/python-flask-git.git
cd python-flask-git
makepkg -si

> TIP: I recommend you extract the /arch folder in your home directory (~/)

Step 3 **Installing MCRCON**

cd /src/arch/script
git clone https://aur.archlinux.org/mcrcon.git
cd mcrcon
makepkg -si

Step 4 **Running the file**

cd /src/arch
sudo python ussr(-ssl).py

> TIP: ussr-ssl.py must be edited in order to fully support HTTPS with your certificate.
> TIP: on default, ussr-ssl.py runs on port 443
> TIP: run ussr.py to make a basic port 80 webserver
