:: launcher.bat

@echo off

cd dependencies/
"prerequisites.bat"

cd ../scripts
python launcher.py
