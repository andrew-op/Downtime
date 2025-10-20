#!/bin/bash

# Downtime - Game 1 Launcher
# Quick start script for the game

echo "╔════════════════════════════════════════════════════╗"
echo "║     DOWNTIME: GAME 1                               ║"
echo "║     Karen's Login Problem                          ║"
echo "╚════════════════════════════════════════════════════╝"
echo ""
echo "Starting game..."
echo ""

# Check if Python 3 is available
if command -v python3 &> /dev/null; then
    python3 game1_main.py
elif command -v python &> /dev/null; then
    python game1_main.py
else
    echo "Error: Python 3 is required to play this game."
    echo "Please install Python 3.6 or higher."
    exit 1
fi
