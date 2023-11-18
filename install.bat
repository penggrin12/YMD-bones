@echo off
python -m venv venv
%~dp0/venv/Scripts/pip.exe install -r requirements.txt
copy .env.example .env
echo.
echo Now fill up the .env file (Press any key when done)
echo.
pause
echo.
echo Done. Now run launch.bat