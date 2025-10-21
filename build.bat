@echo off
REM Build script for Downtime using PyInstaller
REM Creates a standalone executable with the terminal menu launcher

echo ========================================================
echo      DOWNTIME - Build Script
echo ========================================================
echo.

REM Check if PyInstaller is installed
where pyinstaller >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo [X] PyInstaller is not installed!
    echo.
    echo To install PyInstaller, run:
    echo   pip install pyinstaller
    echo.
    pause
    exit /b 1
)

echo [OK] PyInstaller found
echo.

REM Clean previous build artifacts
echo Cleaning previous build artifacts...
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist __pycache__ rmdir /s /q __pycache__
del /q *.pyc 2>nul
echo [OK] Cleanup complete
echo.

REM Build the game
echo Building Downtime with Terminal Menu...
echo.
pyinstaller --clean build_with_terminal_menu.spec

REM Check if build was successful
if %ERRORLEVEL% EQU 0 (
    echo.
    echo ========================================================
    echo      BUILD SUCCESSFUL!
    echo ========================================================
    echo.
    echo Executable created at: dist\Downtime.exe
    echo.
    echo To run the game:
    echo   dist\Downtime.exe
    echo.
    echo To distribute, share the entire 'dist' folder or just Downtime.exe
    echo.
) else (
    echo.
    echo ========================================================
    echo      BUILD FAILED
    echo ========================================================
    echo.
    echo Check the error messages above for details.
    echo.
)

pause
