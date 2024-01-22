@echo off

start /b ngrok tcp --region ap 25565
start /b ngrok tcp --region us 25565
start /b ngrok tcp --region au 25565
start /b ngrok tcp --region eu 25565
start /b ngrok tcp --region in 25565

timeout /t 15 /nobreak

cd /d C:\path\to\ngrok
rem replace this with the path of your ngrok.exe
rem example path: D:\Ngrok\bin\ngrok.exe

python ngroksenpai.py