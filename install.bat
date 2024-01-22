@echo off
title run 2

echo please make sure this window is in administrator
echo additionally, ensure the 'bitsadmin' utility is operational.
echo.
echo press any key to continue after you've confirmed the following.
echo.
pause >nul

REM ty stackoverflow uwu :3

echo Checking for permissions
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"

echo Permission check result: %errorlevel%

REM --> If error flag set, we do not have admin.
if '%errorlevel%' NEQ '0' (
echo Requesting administrative privileges...
goto UACPrompt
) else ( goto gotAdmin )

:UACPrompt
echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
echo UAC.ShellExecute "%~s0", "", "", "runas", 1 >> "%temp%\getadmin.vbs"

echo Running created temporary "%temp%\getadmin.vbs"
timeout /T 5
"%temp%\getadmin.vbs"
exit /B

:gotAdmin
if exist "%temp%\getadmin.vbs" ( del "%temp%\getadmin.vbs" )
pushd "%CD%"
CD /D "%~dp0"

:run

set "pythonInstallerUrl=https://www.python.org/ftp/python/3.9.10/python-3.9.10-amd64.exe"
set "pythonInstallerPath=%TEMP%\python-3.9.10-amd64.exe"

bitsadmin /transfer "PythonInstaller" %pythonInstallerUrl% %pythonInstallerPath%

start /wait "" %pythonInstallerPath% /quiet InstallAllUsers=1 PrependPath=1

python -m pip install flask
python -m pip install mcrcon
python -m pip install requests

del %pythonInstallerPath%

