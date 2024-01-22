#!/bin/bash

sudo pacman -Sy python python-pip
sudo pacman -S python-requests

cd server/
git clone https://aur.archlinux.org/python-flask-git.git
cd python-flask-git
makepkg -si

cd script/
git clone https://aur.archlinux.org/mcrcon.git
cd mcrcon
makepkg -si

cd ..
sudo python ussr-ssl.py