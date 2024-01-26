:: starter.bat

@echo off

timeout /t 1 /nobreak
start /b ngrok tcp --region ap 25565
timeout /t 1 /nobreak
start /b ngrok tcp --region us 25565
timeout /t 1 /nobreak
start /b ngrok tcp --region au 25565
timeout /t 1 /nobreak
start /b ngrok tcp --region eu 25565
timeout /t 1 /nobreak
start /b ngrok tcp --region in 25565

timeout /t 15 /nobreak

cd ../../ngrok/ngrok.exe