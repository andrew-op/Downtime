@echo off
REM Build script for Help Desk Hero game

echo ========================================
echo Building Help Desk Hero with PyInstaller
echo ========================================
echo.

REM Check if PyInstaller is installed
python -c "import PyInstaller" 2>nul
if errorlevel 1 (
    echo PyInstaller not found. Installing...
    pip install pyinstaller
    echo.
)

echo Building executable...
pyinstaller build_game.spec --clean

if errorlevel 1 (
    echo.
    echo ========================================
    echo BUILD FAILED!
    echo ========================================
    pause
    exit /b 1
)

echo.
echo ========================================
echo BUILD SUCCESSFUL!
echo ========================================
echo.
echo Executable created: dist\HelpDeskHero.exe
echo.
echo You can now distribute the HelpDeskHero.exe file
echo from the dist folder. No Python installation required!
echo.
pause
