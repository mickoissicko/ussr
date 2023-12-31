@echo off
title install Python requirements
color c
echo Make sure Python is added to PATH
echo Make sure PATH limit is disabled
echo Make sure you are running Python 3.9.10 for best performance
echo.
echo Verify that you meet all of the above and press any key to continue
pause >nul
color 0f
pip install -r requirements.txt
color 0a
echo Success
pause