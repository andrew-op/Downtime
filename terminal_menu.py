#!/usr/bin/env python3
"""
Terminal-based main menu for Help Desk Hero
Interactive menu with arrow key navigation
"""

import os
import sys

# Platform-specific imports for key detection
if os.name == 'nt':  # Windows
    import msvcrt
else:  # Unix/Linux/Mac
    import tty
    import termios


def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_title():
    """Print the game title banner"""
    print()
    print("="*70)
    print("                     HELP DESK HERO")
    print("              Game 1: Karen's Printing Problem")
    print("="*70)
    print()


def get_key_windows():
    """Get a keypress on Windows"""
    key = msvcrt.getch()

    # Handle special keys (arrows, etc.)
    if key in [b'\x00', b'\xe0']:
        key = msvcrt.getch()
        if key == b'H':  # Up arrow
            return 'up'
        elif key == b'P':  # Down arrow
            return 'down'
    elif key == b'\r':  # Enter
        return 'enter'
    elif key == b'\x1b':  # Escape
        return 'esc'

    return None


def get_key_unix():
    """Get a keypress on Unix/Linux/Mac"""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)

        # Handle escape sequences (arrow keys)
        if ch == '\x1b':
            ch2 = sys.stdin.read(1)
            if ch2 == '[':
                ch3 = sys.stdin.read(1)
                if ch3 == 'A':  # Up arrow
                    return 'up'
                elif ch3 == 'B':  # Down arrow
                    return 'down'
            return 'esc'
        elif ch == '\r' or ch == '\n':  # Enter
            return 'enter'

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    return None


def get_key():
    """Platform-independent key detection"""
    if os.name == 'nt':
        return get_key_windows()
    else:
        return get_key_unix()


def show_how_to_play():
    """Display how to play instructions"""
    clear_screen()
    print_title()

    print("                      HOW TO PLAY")
    print()
    print("-"*70)
    print()
    print("OBJECTIVE:")
    print("  Solve Karen's printing problem using the CompTIA troubleshooting")
    print("  methodology.")
    print()
    print("BASIC COMMANDS:")
    print("  Movement:")
    print("    • go [direction] or just [direction] - Move around")
    print("    • north, south, east, west (or n, s, e, w)")
    print()
    print("  Interaction:")
    print("    • talk [person]     - Talk to NPCs")
    print("    • take [item]       - Pick up items")
    print("    • give [item] to [person] - Give items to NPCs")
    print("    • use [item]        - Use items from inventory")
    print("    • read [item]       - Read notes and documents")
    print("    • examine [thing]   - Look at something closely")
    print("    • look              - Look around current location")
    print()
    print("  Information:")
    print("    • inventory / i     - Check your inventory")
    print("    • status            - See score and progress")
    print("    • help / ?          - Show in-game help")
    print()
    print("  Special:")
    print("    • computer          - Use your desktop (IT Office only)")
    print()
    print("TIPS:")
    print("  • Follow the CompTIA methodology: Identify, Establish Theory, Test,")
    print("    Plan, Implement, Verify, Document")
    print("  • Talk to everyone and explore all locations")
    print()
    print("-"*70)
    print()
    print("              Press any key to return to menu...")

    get_key()


def show_menu():
    """Display interactive menu with arrow key navigation"""
    options = ['Play Game', 'How to Play', 'Exit']
    selected = 0  # Currently selected option

    while True:
        clear_screen()
        print_title()

        print("                        MAIN MENU")
        print()
        print("              Use ↑↓ Arrow Keys to Navigate")
        print("                  Press ENTER to Select")
        print()

        # Display options with selection indicator
        for i, option in enumerate(options):
            if i == selected:
                # Highlighted option
                print(f"                    >>> {option} <<<")
            else:
                # Normal option
                print(f"                        {option}")

        print()
        print("-"*70)

        # Get user input
        key = get_key()

        if key == 'up':
            selected = (selected - 1) % len(options)
        elif key == 'down':
            selected = (selected + 1) % len(options)
        elif key == 'enter':
            # User selected an option
            if selected == 0:  # Play Game
                clear_screen()
                return 'play'
            elif selected == 1:  # How to Play
                show_how_to_play()
                # Return to menu after viewing instructions
            elif selected == 2:  # Exit
                clear_screen()
                print("\nThanks for considering Help Desk Hero!")
                print("See you next time!\n")
                return 'exit'
        elif key == 'esc':
            # Allow ESC to exit
            clear_screen()
            print("\nThanks for considering Help Desk Hero!")
            print("See you next time!\n")
            return 'exit'


def main():
    """Main entry point for terminal menu"""
    choice = show_menu()

    if choice == 'play':
        # Import and run the game
        try:
            from game1_main import main as game_main
            game_main()
        except ImportError:
            print("\nError: Could not find game1_main.py")
            print("Make sure the game files are in the same directory.\n")
            sys.exit(1)
    elif choice == 'exit':
        sys.exit(0)


if __name__ == "__main__":
    main()
