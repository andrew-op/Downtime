#!/bin/bash
# Build script for Help Desk Hero game (Linux/Mac)

echo "========================================"
echo "Building Help Desk Hero with PyInstaller"
echo "========================================"
echo

# Check if PyInstaller is installed
if ! python3 -c "import PyInstaller" 2>/dev/null; then
    echo "PyInstaller not found. Installing..."
    pip3 install pyinstaller
    echo
fi

echo "Building executable..."
pyinstaller build_game.spec --clean

if [ $? -eq 0 ]; then
    echo
    echo "========================================"
    echo "BUILD SUCCESSFUL!"
    echo "========================================"
    echo
    echo "Executable created: dist/HelpDeskHero"
    echo
    echo "You can now distribute the HelpDeskHero binary"
    echo "from the dist folder. No Python installation required!"
    echo
else
    echo
    echo "========================================"
    echo "BUILD FAILED!"
    echo "========================================"
    exit 1
fi
