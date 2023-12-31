@echo off
title Stopping -- v0.0.8a
echo hello world
G:
cd G:\USSR\script\advanced
python "stop_server.py"
timeout /t 5
taskkill /f /im "playit-0.9.3-signed.exe"
taskkill /f /im "cmd.exe"
timeout /t 2
exit