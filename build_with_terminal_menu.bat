@echo off
REM Build Help Desk Hero with Terminal Menu
echo Building Help Desk Hero with Terminal Menu...
echo.

pyinstaller --clean build_with_terminal_menu.spec

echo.
echo Build complete! Check the dist folder for HelpDeskHero.exe
echo.
pause
