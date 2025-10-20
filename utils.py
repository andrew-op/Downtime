"""
Utility functions for game display and formatting
"""

import os
import sys
import time


def clear_screen():
    """Clear the terminal screen"""
    os.system('clear' if os.name != 'nt' else 'cls')


def print_boxed(text):
    """Print text in a box"""
    width = len(text) + 4
    print("+" + "=" * width + "+")
    print("|  " + text + "  |")
    print("+" + "=" * width + "+")


def print_separator(char="-", length=70):
    """Print a separator line"""
    print(char * length)


def slow_print(text, delay=0.03):
    """Print text with slight delay for dramatic effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Newline at end


def format_dialogue(speaker, text, width=70):
    """Format dialogue text"""
    lines = []
    words = text.split()
    current_line = f"{speaker}: "
    
    for word in words:
        if len(current_line) + len(word) + 1 <= width:
            current_line += word + " "
        else:
            lines.append(current_line.rstrip())
            current_line = " " * (len(speaker) + 2) + word + " "
            
    if current_line.strip():
        lines.append(current_line.rstrip())
        
    return "\n".join(lines)


def wrap_text(text, width=70, indent=0):
    """Wrap text to specified width"""
    words = text.split()
    lines = []
    current_line = " " * indent
    
    for word in words:
        if len(current_line) + len(word) + 1 <= width:
            current_line += word + " "
        else:
            lines.append(current_line.rstrip())
            current_line = " " * indent + word + " "
            
    if current_line.strip():
        lines.append(current_line.rstrip())
        
    return "\n".join(lines)


def get_confirmation(prompt="Are you sure? (yes/no): "):
    """Get yes/no confirmation from user"""
    while True:
        response = input(prompt).strip().lower()
        if response in ['yes', 'y']:
            return True
        elif response in ['no', 'n']:
            return False
        else:
            print("Please answer 'yes' or 'no'.")


def display_choices(choices, prompt="Choose an option: "):
    """Display numbered choices and get selection"""
    print()
    for i, choice in enumerate(choices, 1):
        print(f"{i}. {choice}")
    print()
    
    while True:
        try:
            selection = int(input(prompt).strip())
            if 1 <= selection <= len(choices):
                return selection
            else:
                print(f"Please enter a number between 1 and {len(choices)}")
        except ValueError:
            print("Please enter a valid number")
