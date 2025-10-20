# Building Downtime with PyInstaller

This guide explains how to package the game into a standalone executable that can run without Python installed.

## Prerequisites

- Python 3.6 or higher installed
- PyInstaller (will be auto-installed by build scripts)

## Quick Build

### Windows

Simply double-click `build.bat` or run:

```cmd
build.bat
```

The executable will be created at: `dist\Downtime.exe`

### Linux/Mac

Make the script executable and run it:

```bash
chmod +x build.sh
./build.sh
```

The executable will be created at: `dist/Downtime`

## Manual Build

If you prefer to build manually:

### 1. Install PyInstaller

```bash
pip install pyinstaller
```

### 2. Build the Executable

**Option A: Using the spec file (recommended)**

```bash
pyinstaller build_game.spec --clean
```

**Option B: Quick one-liner**

```bash
pyinstaller --onefile --name Downtime game1_main.py
```

### 3. Find Your Executable

The executable will be in the `dist/` folder:
- **Windows**: `dist\Downtime.exe`
- **Linux/Mac**: `dist/Downtime`

## Distribution

You can distribute just the executable file from the `dist/` folder. No Python installation or additional files are needed!

### What Gets Packaged

The PyInstaller build automatically includes:
- `game1_main.py` (entry point)
- `game_state.py`
- `locations.py`
- `items.py`
- `npcs.py`
- `desktop.py`
- `utils.py`
- All Python standard library dependencies

### What's NOT Included

Documentation files (*.md) are NOT packaged into the executable. They're for development reference only.

## Customization

### Adding an Icon

1. Create or obtain an `.ico` file (Windows) or `.icns` file (Mac)
2. Edit `build_game.spec` and change the `icon=None` line to:
   ```python
   icon='your_icon.ico'  # Windows
   icon='your_icon.icns'  # Mac
   ```

### Changing the Executable Name

Edit `build_game.spec` and change the `name='Downtime'` line to your preferred name.

### One-File vs One-Folder

The current spec creates a **single executable file** (`--onefile`). This is easiest for distribution.

If you prefer a folder with dependencies separated (faster startup), change the spec to use:
```python
exe = EXE(
    pyz,
    a.scripts,
    # Remove these two lines:
    # a.binaries,
    # a.zipfiles,
    # a.datas,
    ...
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='HelpDeskHero',
)
```

## Troubleshooting

### "PyInstaller not found"

Install it manually:
```bash
pip install pyinstaller
```

### Antivirus Flags the Executable

This is common with PyInstaller executables. You can:
1. Add an exception in your antivirus
2. Submit the executable to your antivirus vendor as a false positive
3. Sign the executable with a code signing certificate (advanced)

### Console Window Appears

The game is a console/terminal application, so this is expected. The `console=True` setting in the spec file enables this.

### Import Errors

If you get import errors, check that all `.py` files are in the same directory as `game1_main.py`.

## File Sizes

Expect the executable to be **15-25 MB** on Windows due to the bundled Python interpreter. This is normal for PyInstaller executables.

## Testing

After building:

1. Navigate to the `dist/` folder
2. Run the executable
3. Verify the game starts and runs correctly
4. Test on a clean machine (without Python) to confirm it's truly standalone

## Clean Build

To rebuild from scratch:

```bash
# Delete build artifacts
rmdir /s build dist  # Windows
rm -rf build dist    # Linux/Mac

# Rebuild
pyinstaller build_game.spec --clean
```

## Cross-Platform Notes

- **Windows exe**: Only runs on Windows
- **Linux binary**: Only runs on Linux (may need same glibc version)
- **Mac binary**: Only runs on macOS

To distribute to multiple platforms, you must build on each platform separately. PyInstaller does not support cross-compilation.
