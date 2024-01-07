# Universal Server Start Remote (USSR)
* USSR is intentional, I wanted to make a funny abbreviation.
* I am not serious, the comments are trash
* Good luck LOL

# Archlinux Installation
This guide assumes you have basic Archlinux & overall Linux experience. Please fix the issue yourself if you encounter any.

Step 1 **Installing python & pip**

`pacman -Sy python`

`sudo pacman -S python-pip`

Step 2 **Let's get Flask installed**

`cd ~/2.0`

`git clone https://aur.archlinux.org/python-flask-git.git`

`cd python-flask-git`

`makepkg -si`

> TIP: I recommend you extract the /arch folder in your home directory (~/)

Step 3 **Installing MCRCON**

`cd ~/2.0/script`

`git clone https://aur.archlinux.org/mcrcon.git`

`cd mcrcon`

`makepkg -si`

Step 4 **Running the application**

`cd ~/2.0`

`sudo python ussr(-ssl).py`

> TIP: ussr-ssl.py must be edited in order to fully support HTTPS with your certificate.
> TIP: on default, ussr-ssl.py runs on port 443
> TIP: run ussr.py to make a basic port 80 webserver

Step 5 **Installing Packetriot to expose your Flask app to your friends**

`cd ~/2.0`

`git clone https://aur.archlinux.org/pktriot.git`

`cd pktriot`

`makepkg -si`

*(ussr-ssl.py)* `pktriot http 443` 

*(ussr.py)* `pktriot http 80 `

It will ask you for an Email & Password. Head over to [Packetriot](https://packetriot.com/) and make an account, once done, proceed.

**EXAMPLE:**

Email: mickey@coolkids.club

Password: asirrationalaspi

This will log you in, it may say 'permission denied'. To fix this, run:

`sudo pktriot http 443` for ussr-ssl.py
`sudo pktriot http 80` for ussr.py

# Windows installation

Step 1 **Python**

Download [Python 3.9.10](https://www.python.org/downloads/)

Run the installer, disable PATH limit, and add Python to PATH, it should be in the installer options; if it is not, refer to this [tutorial](https://www.youtube.com/watch?v=Y2q_b4ugPWk)

Step 2 **Dependencies**

Run these commands in an elevated command prompt window:

`pip install flask`

`pip install mcrcon`

Step 3 **Using the requirements.bat file**

Instead of using Pip, you can run the requirements.bat file provided.

Step 4 **Running the application**

Just double click ussr-ssl.py or ussr.py, whichever you want to use.

Step 5 **Installing Packetriot**

Head over to [Packetriot](https://packetriot.com/) and make an account, once done, proceed.

Now that you have an account, go to the [downloads](https://packetriot.com/downloads) page, and scroll down until you find the download for your Window's system's architecture. (32 bit or 64 bit.)

To see the architecture, watch this [tutorial](https://www.youtube.com/watch?v=gHeiQTn0_JU)

After you have downloaded the file, create a new folder in the 2.0 directory, and extract the pktriot.exe there. Open command prompt in an elevated window, and type:

`pktriot.exe http 443`

for ussr-ssl.py

`pktriot.exe http 80`

for ussr.py

It will ask you for a login, so type in the credentials of the account you created eariler -- and that's it!
