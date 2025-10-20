#!/usr/bin/env python3
"""
Graphical Launcher for Help Desk Hero
Opens a GUI window with a menu before launching the game
"""

import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import os


class HelpDeskHeroLauncher:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Help Desk Hero")
        self.root.geometry("600x500")
        self.root.resizable(False, False)

        # Set background color
        self.root.configure(bg='#2c3e50')

        # Center window on screen
        self.center_window()

        self.create_widgets()

    def center_window(self):
        """Center the window on screen"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def create_widgets(self):
        """Create all GUI widgets"""
        # Title Frame
        title_frame = tk.Frame(self.root, bg='#34495e', padx=20, pady=20)
        title_frame.pack(fill='x', pady=(0, 20))

        # Title
        title_label = tk.Label(
            title_frame,
            text="HELP DESK HERO",
            font=('Consolas', 28, 'bold'),
            fg='#ecf0f1',
            bg='#34495e'
        )
        title_label.pack()

        subtitle_label = tk.Label(
            title_frame,
            text="Game 1: Karen's Printing Problem",
            font=('Consolas', 14),
            fg='#95a5a6',
            bg='#34495e'
        )
        subtitle_label.pack(pady=(5, 0))

        # Main content frame
        content_frame = tk.Frame(self.root, bg='#2c3e50', padx=40, pady=20)
        content_frame.pack(expand=True, fill='both')

        # Description
        desc_text = (
            "A text-based adventure teaching the CompTIA\n"
            "troubleshooting methodology through an interactive\n"
            "help desk scenario.\n\n"
            "Use observation, investigation, and proper methodology\n"
            "to solve Karen's printing problem before her\n"
            "10 AM client meeting!"
        )
        desc_label = tk.Label(
            content_frame,
            text=desc_text,
            font=('Arial', 11),
            fg='#bdc3c7',
            bg='#2c3e50',
            justify='center'
        )
        desc_label.pack(pady=(0, 30))

        # Buttons
        button_frame = tk.Frame(content_frame, bg='#2c3e50')
        button_frame.pack()

        # Play button
        play_btn = tk.Button(
            button_frame,
            text="▶  PLAY GAME",
            font=('Consolas', 14, 'bold'),
            bg='#27ae60',
            fg='white',
            activebackground='#229954',
            activeforeground='white',
            width=20,
            height=2,
            cursor='hand2',
            command=self.launch_game
        )
        play_btn.pack(pady=10)

        # How to Play button
        howto_btn = tk.Button(
            button_frame,
            text="📖  HOW TO PLAY",
            font=('Consolas', 12),
            bg='#3498db',
            fg='white',
            activebackground='#2980b9',
            activeforeground='white',
            width=20,
            height=2,
            cursor='hand2',
            command=self.show_instructions
        )
        howto_btn.pack(pady=10)

        # Credits button
        credits_btn = tk.Button(
            button_frame,
            text="ℹ  ABOUT",
            font=('Consolas', 12),
            bg='#95a5a6',
            fg='white',
            activebackground='#7f8c8d',
            activeforeground='white',
            width=20,
            height=2,
            cursor='hand2',
            command=self.show_about
        )
        credits_btn.pack(pady=10)

        # Exit button
        exit_btn = tk.Button(
            button_frame,
            text="✖  EXIT",
            font=('Consolas', 12),
            bg='#e74c3c',
            fg='white',
            activebackground='#c0392b',
            activeforeground='white',
            width=20,
            height=2,
            cursor='hand2',
            command=self.exit_launcher
        )
        exit_btn.pack(pady=10)

        # Footer
        footer_label = tk.Label(
            self.root,
            text="© 2024 - Educational Game",
            font=('Arial', 9),
            fg='#7f8c8d',
            bg='#2c3e50'
        )
        footer_label.pack(side='bottom', pady=10)

    def launch_game(self):
        """Launch the main game"""
        self.root.destroy()

        # Import and run the game
        try:
            from game1_main import main
            main()
        except Exception as e:
            print(f"Error launching game: {e}")
            sys.exit(1)

    def show_instructions(self):
        """Show how to play instructions"""
        instructions = (
            "HOW TO PLAY\n\n"
            "COMMANDS:\n"
            "• Movement: north, south, east, west (or n, s, e, w)\n"
            "• Interaction: talk [person], take [item], use [item]\n"
            "• Investigation: examine [thing], look\n"
            "• Menu: inventory (or i), status, computer\n\n"
            "OBJECTIVE:\n"
            "Follow the CompTIA 7-step troubleshooting methodology\n"
            "to solve Karen's problem before 10 AM.\n\n"
            "TIPS:\n"
            "• Talk to everyone - they have valuable information\n"
            "• Use your desktop computer to track progress\n"
            "• Observe what users DO, not just what they SAY\n"
            "• Complete side quests for bonus points"
        )

        messagebox.showinfo("How to Play", instructions)

    def show_about(self):
        """Show about/credits"""
        about = (
            "HELP DESK HERO: GAME 1\n\n"
            "An educational text adventure teaching\n"
            "IT troubleshooting methodology.\n\n"
            "Based on CompTIA A+ troubleshooting principles.\n\n"
            "Featuring:\n"
            "• 7-step methodology tracking\n"
            "• Multiple NPCs with dialogue trees\n"
            "• Coffee/focus system\n"
            "• Side quests and achievements\n"
            "• Realistic IT scenarios\n\n"
            "Learn by doing - experience real help desk scenarios\n"
            "in a fun, interactive environment!"
        )

        messagebox.showinfo("About Help Desk Hero", about)

    def exit_launcher(self):
        """Exit the launcher"""
        self.root.destroy()
        sys.exit(0)

    def run(self):
        """Run the launcher"""
        self.root.mainloop()


def main():
    """Entry point for launcher"""
    launcher = HelpDeskHeroLauncher()
    launcher.run()


if __name__ == '__main__':
    main()
