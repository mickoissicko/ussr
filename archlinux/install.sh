#!/bin/bash

sudo pacman -Sy python python-pip
sudo pacman -S python-requests
sudo pacman -S git

cd tmp/
git clone https://aur.archlinux.org/python-flask-git.git
cd python-flask-git
makepkg -si

git clone https://aur.archlinux.org/ngrok.git
cd ngrok
makepkg -si

cd server-arch/script/
git clone https://aur.archlinux.org/mcrcon.git
cd mcrcon
makepkg -si