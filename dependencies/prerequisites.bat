@echo off

cd ../config

if exist lock.pa (
    echo Lock file detected. Going back to scripts directory and running start.bat.
    cd ../scripts
    call start.bat
    echo Exiting main batch script.
    exit /b
) else (
    echo.
)

where choco >nul 2>nul
if %errorlevel% neq 0 (
    echo Installing Chocolatey...
    @powershell -NoProfile -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
) else (
    echo Chocolatey is already installed.
)

echo Installing curl...
choco install curl -y

echo Installing tar...
choco install tar -y

echo Installation complete.

mkdir ../ngrok
cd ngrok
set downloadURL=https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-windows-amd64.zip
set fileName=ngrok-v3-stable-windows-amd64.zip

set extractDir=ngrok

curl -o %fileName% %downloadURL%

tar -xf %fileName% -C %extractDir%

del %fileName%

echo Download and extraction complete.

cd ..
cd config
echo. > lock.pa
echo Lock file created.