@echo off
title Running -- v0.0.8a
:: CDs to script directory
cd G:\USSR\script
:: starts server
start ignition.bat
:: if you proxies, add them to proxy directory (e.g. play-it.gg, NGROK)
cd proxy
start start1.bat
