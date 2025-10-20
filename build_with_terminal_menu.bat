@echo off
REM Build Downtime with Terminal Menu
echo Building Downtime with Terminal Menu...
echo.

pyinstaller --clean build_with_terminal_menu.spec

echo.
echo Build complete! Check the dist folder for Downtime.exe
echo.
pause
