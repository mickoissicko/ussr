REM setup/start.bat

@echo off

:: Set the download URL and file name
set downloadURL=https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-windows-amd64.zip
set fileName=ngrok-v3-stable-windows-amd64.zip

set extractDir=ngrok

curl -o %fileName% %downloadURL%

tar -xf %fileName% -C %extractDir%


del %fileName%

echo Download and extraction complete.
