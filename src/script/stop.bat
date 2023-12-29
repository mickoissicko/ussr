@echo off
title Stopping -- v0.0.8a
cd advanced
"stop_server.py"
timeout /t 10
taskkill /f /im "WindowsTerminal.exe"
taskkill /f /im "cmd.exe"
exit