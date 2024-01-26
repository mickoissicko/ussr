:: scripts/start.bat

@echo off

cd ../config

if exist lock.pa (
    cd ../bin_win
    python ussr-ssl.py
) else (
    echo Please install dependencies first.
    echo Exiting in 3 seconds
    timeout /t /nobreak 3
)