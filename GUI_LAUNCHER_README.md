# GUI Launcher for Help Desk Hero

A graphical main menu launcher has been added to give your game a professional look before the text adventure begins.

## What It Looks Like

The GUI launcher features:
- **Clean, modern design** with IT-themed colors (dark blue/gray)
- **Large "PLAY GAME" button** to start the adventure
- **"HOW TO PLAY" button** with command reference and tips
- **"ABOUT" button** with game information
- **"EXIT" button** to close without playing

## Files Added

1. **[launcher.py](launcher.py)** - The GUI launcher code (using tkinter)
2. **[build_game_with_gui.spec](build_game_with_gui.spec)** - PyInstaller spec for GUI version
3. **[build_with_gui.bat](build_with_gui.bat)** - Build script for GUI version (Windows)

## Testing the GUI Launcher

### Method 1: Run Directly (Development)

```bash
python launcher.py
```

The GUI will open, and clicking "PLAY GAME" will launch your text game in the same console window.

### Method 2: Build Executable

```bash
build_with_gui.bat
```

This creates `dist\HelpDeskHero.exe` with the GUI launcher included.

## Two Build Options

You now have **two ways** to build your game:

### Option A: Console-Only (Original)
```bash
build.bat
```
- Uses: `build_game.spec`
- Entry: `game1_main.py`
- Result: Direct to text game
- Use for: Players who prefer classic text adventures

### Option B: With GUI Launcher (New)
```bash
build_with_gui.bat
```
- Uses: `build_game_with_gui.spec`
- Entry: `launcher.py` → `game1_main.py`
- Result: GUI menu first, then text game
- Use for: Professional presentation, Steam/itch.io releases

## Customization

### Changing Colors

Edit `launcher.py` and modify these hex colors:

```python
self.root.configure(bg='#2c3e50')  # Main background (dark blue-gray)

# Button colors:
bg='#27ae60'  # Play button (green)
bg='#3498db'  # How to Play (blue)
bg='#95a5a6'  # About (gray)
bg='#e74c3c'  # Exit (red)
```

### Changing Text

Edit these sections in `launcher.py`:

```python
title_label = tk.Label(
    title_frame,
    text="HELP DESK HERO",  # Change main title
    ...
)

subtitle_label = tk.Label(
    title_frame,
    text="Game 1: Karen's Printing Problem",  # Change subtitle
    ...
)

desc_text = (
    "Your description here..."  # Change description
)
```

### Adding a Background Image

Add to `create_widgets()` method in `launcher.py`:

```python
from PIL import Image, ImageTk  # Install: pip install pillow

# Load image
bg_image = Image.open("background.png")
bg_photo = ImageTk.PhotoImage(bg_image)

# Create canvas
canvas = tk.Canvas(self.root, width=600, height=500)
canvas.pack(fill='both', expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor='nw')
canvas.image = bg_photo  # Keep reference
```

**Note:** Adding PIL/Pillow adds dependencies to PyInstaller build.

### Window Size

Change dimensions in `__init__()`:

```python
self.root.geometry("600x500")  # Change to "800x600" etc.
```

## How It Works

1. **Launcher starts** → Shows GUI window with menu
2. **User clicks "PLAY GAME"** → GUI closes
3. **Text game launches** → Uses same console window
4. **Game runs normally** → All text-based as usual
5. **Game ends** → Returns to command prompt

## Why Use the GUI Launcher?

### Benefits:
✅ **Professional first impression** - Looks polished
✅ **Easy instructions** - "How to Play" button for new players
✅ **About screen** - Share credits and game info
✅ **Cleaner distribution** - People expect GUI apps on Windows
✅ **No code changes** - Text game works exactly the same

### When NOT to use it:
❌ You want pure retro terminal aesthetic
❌ Target audience prefers command-line tools
❌ Building for terminal-only environments

## Dependencies

The GUI launcher uses **tkinter**, which is:
- ✅ Included with Python (no pip install needed)
- ✅ Automatically bundled by PyInstaller
- ✅ No extra file size (minimal)
- ✅ Works on Windows, Mac, and Linux

**No additional dependencies required!**

## Comparison

| Feature | Console-Only | With GUI Launcher |
|---------|--------------|-------------------|
| Entry point | game1_main.py | launcher.py |
| First screen | Text in console | Graphical menu |
| File size | ~20 MB | ~21 MB |
| Dependencies | None | None (tkinter built-in) |
| Professional | ✓ | ✓✓✓ |
| Retro feel | ✓✓✓ | ✓ |

## Troubleshooting

### GUI doesn't appear
- Check if tkinter is installed: `python -m tkinter`
- On Linux: `sudo apt-get install python3-tk`

### Game doesn't launch after clicking Play
- Check that `game1_main.py` is in the same directory
- Check console for error messages

### GUI appears but is blank
- Update tkinter: Reinstall Python with tkinter support
- Windows: tkinter included by default

### Want to test without building
```bash
python launcher.py
```

## Future Enhancements

Ideas for expanding the GUI launcher:

1. **Difficulty Selection** - Add easy/normal/hard modes
2. **Save Game Loading** - List available saves
3. **Settings Menu** - Font size, colors, etc.
4. **Statistics** - Show previous game scores
5. **Update Checker** - Check for new versions online
6. **Custom Themes** - Let players choose color schemes

## Recommendation

For **public distribution** (Steam, itch.io, sharing with friends):
→ Use **build_with_gui.bat** for professional presentation

For **personal use** or **retro enthusiasts**:
→ Use **build.bat** for pure text adventure experience

Both versions play the exact same game - only the entry experience differs!
