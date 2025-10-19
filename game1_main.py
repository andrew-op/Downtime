#!/usr/bin/env python3
"""
Game 1: Karen's Login Problem - Help Desk Training Game
A text-based adventure teaching CompTIA troubleshooting methodology
"""

import sys
from game_state import GameState
from locations import Location, init_locations
from items import Item, init_items
from npcs import NPC, init_npcs
from desktop import DesktopMenu
from utils import clear_screen, print_boxed, print_separator


class Game:
    """Main game controller"""
    
    def __init__(self):
        self.state = GameState()
        self.locations = init_locations()
        self.items = init_items()
        self.npcs = init_npcs()
        self.desktop = DesktopMenu(self.state)
        self.running = True
        
    def start(self):
        """Start the game"""
        clear_screen()
        self.show_intro()
        self.game_loop()
        
    def show_intro(self):
        """Display game introduction"""
        print_boxed("HELP DESK HERO: GAME 1")
        print("\n" + "="*70)
        print("           KAREN'S LOGIN PROBLEM")
        print("           A Help Desk Training Adventure")
        print("="*70 + "\n")
        
        print("Monday, 9:45 AM\n")
        print("Your first day as an IT Support Technician.")
        print("You've been assigned to solve a user login issue.")
        print("Use the CompTIA troubleshooting methodology to succeed.\n")

        input("Press Enter to begin...")
        clear_screen()

        # Opening scene
        print_boxed("YOUR OFFICE - 9:45 AM")
        print()
        print("You sit at your new desk in the IT Support office.")
        print("Your computer displays a fresh ticket in the queue.\n")

        print("Manager Marcus walks over with a coffee mug.\n")

        print('Marcus: "Morning! Welcome to the team. I see Ian from Help Desk"')
        print('        "escalated a ticket to you. User login issue."\n')

        print('        "Should be straightforward, but the user has a client"')
        print('        "meeting at 10 AM, so time is tight."\n')

        print('        "Let me know if you need anything. Good luck!"\n')

        print("*Marcus walks away*\n")
        
        input("Press Enter to continue...")
        self.state.current_location = "it_office"
        
    def game_loop(self):
        """Main game loop"""
        # Show initial location
        self.show_status()
        self.show_location()

        while self.running:
            command = input("\n> ").strip().lower()
            self.process_command(command)

            # Check win condition
            if self.state.check_win_condition():
                self.handle_win()
                break

            # Check time-based events
            self.check_time_events()
            
    def show_status(self):
        """Display current status bar"""
        time_str = self.state.get_time_string()
        score = self.state.score
        step = self.state.current_step
        caffeine = self.state.get_caffeine_level_name()
        
        print("="*70)
        print(f"Time: {time_str} | Score: {score} | Step: {step}/7 | Caffeine: {caffeine}")
        print("="*70)
        
    def show_location(self):
        """Display current location description"""
        loc = self.locations[self.state.current_location]
        print(f"\n{loc.name}")
        print("-" * len(loc.name))

        # Get items present in this location (not taken)
        items_here = [item.id for item in self.items.values()
                     if item.location == self.state.current_location and not item.taken]

        # Use dynamic description that includes items
        print(loc.get_full_description(items_here))

        # Show NPCs in location
        npcs_here = [npc for npc in self.npcs.values()
                     if npc.location == self.state.current_location]
        if npcs_here:
            print(f"\nYou see: {', '.join(npc.name for npc in npcs_here)}")
            
    def process_command(self, command):
        """Process user command"""
        if not command:
            return
            
        parts = command.split()
        verb = parts[0]
        args = parts[1:] if len(parts) > 1 else []
        
        # Movement commands
        if verb in ['go', 'move', 'walk']:
            if args:
                self.move(args[0])
            else:
                print("Go where?")
        elif verb in ['n', 'north', 's', 'south', 'e', 'east', 'w', 'west']:
            self.move(verb[0])
        elif verb in self.locations[self.state.current_location].exits.keys():
            self.move(verb)
            
        # Interaction commands
        elif verb in ['talk', 'speak']:
            if args:
                self.talk_to(' '.join(args))
            else:
                print("Talk to whom?")
        elif verb in ['take', 'get', 'grab']:
            if args:
                self.take_item(' '.join(args))
            else:
                print("Take what?")
        elif verb in ['use', 'drink', 'consume']:
            if args:
                self.use_item(' '.join(args))
            else:
                print("Use what?")
        elif verb in ['examine', 'look', 'inspect', 'x']:
            if args:
                self.examine(' '.join(args))
            else:
                print()
                self.show_location()
        elif verb == 'inventory' or verb == 'i':
            self.show_inventory()
            
        # Special commands
        elif verb == 'computer' and self.state.current_location == 'it_office':
            self.desktop.show(self.state)
        elif verb == 'help' or verb == '?':
            self.show_help()
        elif verb in ['quit', 'exit', 'q']:
            self.quit_game()
        else:
            print(f"I don't understand '{command}'.")
            print("Type 'help' for available commands.")
            
    def move(self, direction):
        """Move to a new location"""
        loc = self.locations[self.state.current_location]
        
        if direction in loc.exits:
            new_location = loc.exits[direction]
            
            # Check if movement is allowed
            if new_location == 'break_room' and self.state.william_blocking_break_room:
                print("\nWilliam is blocking the doorway to the break room.")
                print("He's looking at you expectantly...")
                return

            self.state.current_location = new_location
            self.state.advance_time(2)  # Moving takes 2 minutes
            print()
            self.show_location()
        else:
            print(f"You can't go that way.")
            
    def talk_to(self, npc_name):
        """Talk to an NPC"""
        # Find NPC in current location
        npc = None
        for n in self.npcs.values():
            if n.location == self.state.current_location:
                if npc_name.lower() in n.name.lower():
                    npc = n
                    break
                    
        if npc:
            print()
            npc.talk(self.state, self.items)
        else:
            print(f"I don't see {npc_name} here.")
            
    def take_item(self, item_name):
        """Take an item"""
        # Find item in current location
        item = None
        for i in self.items.values():
            if i.location == self.state.current_location and not i.taken:
                if item_name.lower() in i.name.lower():
                    item = i
                    break
                    
        if item:
            if item.takeable:
                item.taken = True
                item.location = "inventory"
                self.state.inventory.append(item.id)
                print(f"\nYou take the {item.name}.")

                # Special handling
                if item.id == 'redbull':
                    self.state.has_redbull = True
            else:
                print(f"\nYou can't take that.")
        else:
            print(f"I don't see {item_name} here.")
            
    def use_item(self, item_name):
        """Use an item from inventory"""
        # Find item in inventory
        item = None
        for item_id in self.state.inventory:
            i = self.items[item_id]
            if item_name.lower() in i.name.lower():
                item = i
                break
                
        if item:
            print()
            item.use(self.state)

            # Remove from inventory if consumable
            if item.consumable:
                self.state.inventory.remove(item.id)
        else:
            print(f"You don't have {item_name}.")
            
    def examine(self, target):
        """Examine something in detail"""
        # Check items in location
        for item in self.items.values():
            if item.location == self.state.current_location and not item.taken:
                if target.lower() in item.name.lower():
                    print()
                    item.examine(self.state)
                    return

        # Check NPCs
        for npc in self.npcs.values():
            if npc.location == self.state.current_location:
                if target.lower() in npc.name.lower():
                    print(f"\n{npc.description}")
                    return

        # Check inventory
        for item_id in self.state.inventory:
            item = self.items[item_id]
            if target.lower() in item.name.lower():
                print()
                item.examine(self.state)
                return

        print(f"I don't see {target} here.")
        
    def show_inventory(self):
        """Show player inventory"""
        print()
        print_boxed("INVENTORY")

        if not self.state.inventory:
            print("\nYour pockets are empty.")
        else:
            print()
            for item_id in self.state.inventory:
                item = self.items[item_id]
                print(f"- {item.name}")

        print(f"\nCaffeine Level: {self.state.get_caffeine_level_name()}")
        print(f"Focus Buff: {self.state.get_focus_description()}")
        
    def show_help(self):
        """Show help text"""
        print()
        print_boxed("HELP - AVAILABLE COMMANDS")
        print()
        print("MOVEMENT:")
        print("  go [direction]     - Move in a direction")
        print("  [direction]        - Shortcut (e.g., 'north', 'n')")
        print()
        print("INTERACTION:")
        print("  talk [person]      - Talk to someone")
        print("  take [item]        - Pick up an item")
        print("  use [item]         - Use an item from inventory")
        print("  examine [thing]    - Look at something closely")
        print("  look               - Look around current location")
        print()
        print("INVENTORY:")
        print("  inventory / i      - Show what you're carrying")
        print()
        print("SPECIAL:")
        print("  computer           - Use desktop computer (IT Office only)")
        print("  help / ?           - Show this help")
        print("  quit / q           - Quit game")
        
    def quit_game(self):
        """Quit the game"""
        print("\nAre you sure you want to quit? (yes/no)")
        response = input("> ").strip().lower()

        if response in ['yes', 'y']:
            print("\nThanks for playing!")
            self.running = False
        else:
            print("\nReturning to game...")
            
    def check_time_events(self):
        """Check for time-based events"""
        # Check if time limit exceeded
        if self.state.minutes >= 60:  # 10:00 AM deadline
            self.handle_time_limit_exceeded()
            
    def handle_time_limit_exceeded(self):
        """Handle exceeding time limit"""
        print()
        print_boxed("TIME'S UP!")
        print()
        print("It's now 10:00 AM.\n")
        print("Karen's client meeting has started.")
        print("She still can't log in.\n")
        print("Karen storms out of the building to find another computer.")
        print("The client meeting is a disaster.\n")
        print("Manager Marcus is not happy.\n")
        
        print_separator()
        print("GAME OVER: Time Limit Exceeded")
        print_separator()
        print(f"\nFinal Score: {self.state.score}")
        print("\nYou failed to solve the problem in time.")
        print("Karen missed her meeting deadline.")
        print()
        
        self.running = False
        
    def handle_win(self):
        """Handle winning the game"""
        print()

        # Calculate final score
        final_score = self.state.calculate_final_score()
        rank = self.state.get_rank()

        print_boxed("CONGRATULATIONS!")
        print()
        print("You successfully solved Karen's login problem!\n")

        print("Karen was able to log in and make her 10:00 AM meeting.")
        print("Manager Marcus is impressed with your methodology.")
        print("Your documentation is thorough and professional.\n")
        
        print_separator()
        print("FINAL SCORE REPORT")
        print_separator()
        print(f"\nCore Methodology: {self.state.methodology_score}/400 points")
        print(f"Bonus Points: {self.state.bonus_score}/600 points")
        print(f"\nFINAL SCORE: {final_score}/1000")
        print(f"\nRANK: {rank}")
        print_separator()
        
        print(f"\nTime: {self.state.get_time_string()}")
        print(f"Steps Completed: {self.state.current_step}/7")
        
        if self.state.check_flag('william_quest_complete'):
            print("\n✓ William's Quest Complete")
        if self.state.check_flag('donut_heist_complete'):
            print("✓ Donut Heist Complete")
            
        print()
        
        self.running = False


def main():
    """Main entry point"""
    game = Game()
    game.start()
    
    print("\nThanks for playing Help Desk Hero: Game 1!")
    print("You've learned the CompTIA troubleshooting methodology.\n")


if __name__ == "__main__":
    main()
