@echo off

set "currentDir=%cd%"

cd ../config

if exist lock.pa.txt (
    cd ..
    cd scripts
    py launcher.py
) else (
    echo.
)

cd C:/ProgramData/
rd /s /q chocolatey *
del /q chocolatey

echo Installing Chocolatey...
@powershell -NoProfile -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"

echo Installing curl...
choco install curl -y

echo Installing tar...
choco install tar -y

echo Installation complete.

cd "%currentDir%"

cd ..
mkdir ngrok
cd ngrok

echo Downloading ngrok...
curl -O https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-windows-amd64.zip

echo Extracting ngrok...
tar -xf ngrok-v3-stable-windows-amd64.zip

echo Download and extraction complete.

cd ..

choco install python39 -y
py -m pip install mcrcon
py -m pip install flask
py -m pip install requests

cd "%currentDir%"
cd ..
cd config
echo. > lock.pa

cd ..
cd scripts
python launcher.py

cd "%currentDir%"
cd ..
cd config
echo. > lock.pa

cd "%currentDir%"
cd ..
cd scripts

py launcher.py

cd ..
cd config
echo. > lock.pa