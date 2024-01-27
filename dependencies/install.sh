#!/bin/bash

cd ../config

if [ -e lock.pa ]; then
    echo Already satisfied
    echo Exiting in 3s..
    sleep 3
    python ../launcher.py
    exit 0
fi

sudo pacman -Sy jdk-openjdk
sudo pacman -S python python-pip
sudo pacman -S python-requests
sudo pacman -S python-flask
sudo pacman -S git

cd ..
git clone https://aur.archlinux.org/ngrok.git
cd ngrok
makepkg -si

cd ..
git clone https://aur.archlinux.org/mcrcon.git
cd mcrcon
makepkg -si

cd ../config

touch lock.pa