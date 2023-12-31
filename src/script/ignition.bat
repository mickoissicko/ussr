@echo off
title mc-server
cd G:\.mc\Minecraft Server
java -Xms2G -Xmx6G -jar fabric-server-mc.1.19.4-loader.0.14.19-launcher.0.11.2.jar nogui
pause >nul