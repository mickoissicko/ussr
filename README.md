# Universal Server Start Remote (USSR)
* USSR is intentional, I wanted to make a funny abbreviation.
* I am not serious, the comments are trash
* Good luck LOL

# Setting up the Minecraft Server
> NOTE: This tutorial is for a Fabric server. If you want to use something like PaperMC, Glowstone, or Airplane, figure it out -- it isn't rocket science.
## For Arch

Step 1 **Accquire the file**

`$ mkdir server`

`$ cd ~/server`

`$ wget https://meta.fabricmc.net/v2/versions/loader/1.19.4/0.15.3/1.0.0/server/jar`

`$ mv fabric-server-mc.1.19.4-loader.0.15.3-launcher.1.0.0.jar fabric.jar`

Step 2 **Install java**

`$ sudo pacman -S jdk-openjdk`

Step 3 **Initialise and configure**

`$ cd ~/server`

`$ sudo nano eula.txt`

Add the following text:

eula=true

`$ sudo java -jar -Xms256M -Xmx5G fabric.jar`

`$ stop`

`$ sudo nano server.properties`

In the server.properties file, change the rcon port to 25575, the rcon password to root_admin, and the address to 0.0.0.0, localhost, or 127.0.0.1.

## For Windows

Step 1 **Downloading Java**

Download [Liberica JDK](https://download.bell-sw.com/java/21.0.1+12/bellsoft-jdk21.0.1+12-windows-amd64.msi)

Step 2 **Initalise and start**

Make a folder somewhere safe, and name it `server`.

Download the [Fabric server software](https://meta.fabricmc.net/v2/versions/loader/1.19.4/0.15.3/1.0.0/server/jar) in the folder

Change the name of this file to fabric.jar

Create a text document (.txt) named eula.txt and in the contents of the document, type eula=true.

Open an elevated command prompt window in the server folder

`$ java -jar -Xms256M -Xmx5G fabric.jar`

`$ stop`

Step 3 **RCON settings**

After this, open `server.properties` with whatever text-editor, and change:

RCON port to 25575
RCON password to root_admin
RCON address localhost

# Setting up the USSR for your PC

## Archlinux installation
This guide assumes you have basic Archlinux & overall Linux experience. Please fix the issue yourself if you encounter any.

Step 4a **Let's install Python & dependencies**

`$ sudo pacman -S python`

`$ cd ussr-xyz`

> ussr-***xyz*** is the version, e.g. you are using version 2.2, that would be: ussr-2.2

`$ cd archlinux`

`$ chmod +x install.sh`

`$ ./install.sh`

Step 4b **Running the USSR**

`$ cd server-arch`

`$ sudo python ussr(-ssl).py`

> ussr-ssl.py is optional, use the SSL version if you want HTTPS instead of HTTP. It doesn't matter if you will use Pktriot, though.

Step 5 **Installing Packetriot to expose the Flask app to your friends (friends..?)**

`$ cd ~/path/to/ussr/directory`

`$ git clone https://aur.archlinux.org/pktriot.git`

`$ cd pktriot`

`$ makepkg -si`

*(ussr-ssl.py)* `$ pktriot http 443` 

*(ussr.py)* `$ pktriot http 80 `

It will ask you for an Email & Password. Head over to [Packetriot](https://packetriot.com/) and make an account, once done, proceed.

**EXAMPLE:**

Email: mickey@koolkids.klan

Password: asirrationalaspi

This will log you in, it may say 'permission denied'. To fix this, run:

`$ sudo pktriot http 443` for ussr-ssl.py
`$ sudo pktriot http 80` for ussr.py

## Windows installation
Step 1 **Python**

Download [Python 3.9.10](https://www.python.org/downloads/)

Run the installer, disable PATH limit, and add Python to PATH, it should be in the installer options; if it is not, refer to this [tutorial](https://www.youtube.com/watch?v=Y2q_b4ugPWk)

Step 2 **Dependencies**
Open an elevated command prompt window in the ussr directory.

`$ cd ussr-xyz`

> no need for this if you are already in the directory

> not explaining what 'xyz' is, scroll up

`$ cd windows`

`$ "install.bat"`

Step 5 **Installing Packetriot**

Head over to [Packetriot](https://packetriot.com/) and make an account, once done, proceed.

Now that you have an account, go to the [downloads](https://packetriot.com/downloads) page, and scroll down until you find the download for your Window's system's architecture. (32 bit or 64 bit.)

To see the architecture, watch this [tutorial](https://www.youtube.com/watch?v=gHeiQTn0_JU)

After you have downloaded the file, create a new folder in the 2.0 directory, and extract the pktriot.exe there. Open command prompt in an elevated window, and type:

`$ pktriot.exe http 443`

for ussr-ssl.py

`$ pktriot.exe http 80`

for ussr.py

It will ask you for a login, so type in the credentials of the account you created eariler -- and that's it!

# Port-forwarding your Minecraft server
We will be using ngrok because it is better.

# Installation for Archlinux
Step 1 **Installing ngrok**

Step 1a **Install snap**

`$ cd ~/`

`$ git clone https://aur.archlinux.org/snapd.git`

`$ cd snapd`

`$ makepkg -si`

Step 1b **Install ngrok**

`$ sudo snap install ngrok`

Step 2 **Making an account and logging in**

Make an account on the [ngrok](https://dashboard.ngrok.com/signup) website.

After you have made the account, navigate to the [setup](https://dashboard.ngrok.com/get-started/setup/linux) page

`$ ngrok config add-authtoken THE-AUTHTOKEN-GIVEN`

Change 'the-authtoken-given' to the one given on the website.

Step 3 **Starting Ngrok**
You do not need to start ngrok manually, `ussr(-ssl).py` does it automatically for you, unless you have ngrok.functionality=False.

Step 4 **Running the tool**
Copy the webhook URL

![](https://i.ibb.co/0Qb8d4q/Untitled.png)

Navigate to Line 26, and edit this:

`discord_webhook_url = "ur_webhook_noob"`

with the actual webhook URI.

![](https://i.ibb.co/wyTZ0nH/2.png)

After you have added the URL, run the following command in the directory where `ngroksenpai.py` is located.

`$ sudo python ngroksenpai.py`

Enter your password and it should send the links in Discord!

# Installation for Windows
Step 1. **Installing Ngrok**

Install [ngrok](ngrok.com). You can choose the [64-bit version](https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-windows-amd64.zip) or the [32-bit version](https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-windows-386.zip). 

Step 2 **Making an account and logging in**

Make an account on the [ngrok](https://dashboard.ngrok.com/signup) website.

After you have made the account, navigate to the [setup](https://dashboard.ngrok.com/get-started/setup/linux) page

Open a command prompt window in the folder where you downloaded ngrok, and type

`$ ngrok.exe config add-authtoken THE-AUTHTOKEN-GIVEN`

Step 3 **Starting the service**

You do not need to start ngrok manually, `ussr(-ssl).py` does it automatically for you, unless you have ngrok.functionality=False.

Step 4 **Running the tool**
Copy the webhook URL

![](https://i.ibb.co/0Qb8d4q/Untitled.png)

Navigate to Line 26, and edit this:

`discord_webhook_url = "ur_webhook_noob"`

with the actual webhook URI.

![](https://i.ibb.co/wyTZ0nH/2.png)


