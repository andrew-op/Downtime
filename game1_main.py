#!/usr/bin/env python3
"""
Game 1: Karen's Login Problem - Downtime
A text-based adventure teaching CompTIA troubleshooting methodology
"""

import sys
import random
from game_state import GameState
from locations import Location, init_locations
from items import Item, init_items
from npcs import NPC, init_npcs
from desktop import DesktopMenu
from utils import clear_screen, print_boxed, print_separator, format_dialogue


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
        print_boxed("DOWNTIME: GAME 1")
        print("\n" + "="*70)
        print("           KAREN'S PRINTING PROBLEM")
        print("           A Help Desk Training Adventure")
        print("="*70 + "\n")
        
        print("Monday, 9:45 AM\n")
        print("Your first day as an IT Support Technician.")
        print("You've been assigned to solve a user printing issue.")
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
        print('        "escalated a ticket to you. Printing problem."')
        print('        "Should be straightforward, but the user has an important"')
        print('        "client meeting coming up."')
        print('        "Let me know if you need anything. Good luck!"')

        print("*Marcus walks away*\n")
        
        input("Press Enter to continue...")
        self.state.current_location = "it_office"
        
    def game_loop(self):
        """Main game loop"""
        # Show initial location
        self.show_location()

        while self.running:
            command = input("\n> ").strip().lower()
            self.process_command(command)

            # Check win condition
            if self.state.check_win_condition():
                self.handle_win()
                break
            
    def show_status(self):
        """Display current game status"""
        score = self.state.score
        steps_done = sum(1 for completed in self.state.steps_complete.values() if completed)

        print()
        print_boxed("GAME STATUS")
        print()
        print(f"Score: {score}")
        print(f"Steps Completed: {steps_done}/7")

        # Only show caffeine info if player has consumed at least one coffee
        if self.state.coffees_consumed > 0 or self.state.redbull_consumed:
            print(f"Caffeine Level: {self.state.get_caffeine_level_name()}")
            print(f"Focus Status: {self.state.get_focus_description()}")
        
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
        elif verb in ['give']:
            if len(args) >= 2:
                # Command format: give [item] [to] [person] or give [item] [person]
                if 'to' in args:
                    to_index = args.index('to')
                    item_name = ' '.join(args[:to_index])
                    person_name = ' '.join(args[to_index+1:])
                else:
                    # Assume last word is person, rest is item
                    item_name = ' '.join(args[:-1])
                    person_name = args[-1]
                self.give_item(item_name, person_name)
            else:
                print("Give what to whom? (Usage: give [item] to [person])")
        elif verb in ['use', 'drink', 'consume']:
            if args:
                self.use_item(' '.join(args))
            else:
                print("Use what?")
        elif verb in ['pour', 'spill', 'dump']:
            if args:
                self.handle_pour_command(' '.join(args))
            else:
                print("Pour what?")
        elif verb in ['read']:
            if args:
                self.read_item(' '.join(args))
            else:
                print("Read what?")
        elif verb in ['examine', 'look', 'inspect', 'x']:
            if args:
                self.examine(' '.join(args))
            else:
                print()
                self.show_location()
        elif verb == 'inventory' or verb == 'i':
            self.show_inventory()
        elif verb == 'status':
            self.show_status()

        # Special commands
        elif verb == 'computer' and self.state.current_location == 'it_office':
            self.desktop.show(self.state)
        elif verb == 'help' or verb == '?':
            self.show_help()
        elif verb in ['quit', 'exit', 'q']:
            self.quit_game()
        else:
            self.show_confused_response(command)
            
    def move(self, direction):
        """Move to a new location"""
        loc = self.locations[self.state.current_location]

        if direction in loc.exits:
            new_location = loc.exits[direction]

            # Check for special exit (outside door)
            if new_location == 'outside_exit':
                self.handle_outside_exit()
                return

            self.state.current_location = new_location
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
            # Special handling for donut - requires Marcus to have laptop
            if item.id == 'donut' and not self.state.check_flag('marcus_has_laptop'):
                print("\nMarcus is sitting right at his desk, watching you.")
                print("You can't just take his donut while he's staring at you!")
                print()
                print("(Maybe if he was distracted with something...)")
                return

            if item.takeable:
                item.taken = True
                item.location = "inventory"
                self.state.inventory.append(item.id)
                print(f"\nYou take the {item.name}.")

                # Special handling
                if item.id == 'redbull':
                    self.state.has_redbull = True
                elif item.id == 'donut':
                    print("Marcus is completely absorbed in setting up his new laptop.")
                    print("He didn't even notice!")
            else:
                print(f"\nYou can't take that.")
        else:
            # Check if it's a location object (non-takable scenery)
            loc = self.locations[self.state.current_location]
            obj = loc.get_object(item_name)
            if obj and 'take' in obj:
                print(f"\n{obj['take']}")
            else:
                print(f"I don't see {item_name} here.")

    def give_item(self, item_name, npc_name):
        """Give an item to an NPC"""
        # Check if item is in inventory
        item = None
        for item_id in self.state.inventory:
            i = self.items[item_id]
            if item_name.lower() in i.name.lower():
                item = i
                break

        if not item:
            print(f"\nYou don't have {item_name} in your inventory.")
            return

        # Find NPC in current location
        npc = None
        for n in self.npcs.values():
            if n.location == self.state.current_location:
                if npc_name.lower() in n.name.lower():
                    npc = n
                    break

        if not npc:
            print(f"\nI don't see {npc_name} here.")
            return

        # Redirect laptop giving to dialogue option
        if item.id == 'laptop' and npc.id == 'marcus':
            print("\nYou should talk to Marcus if you want to give him the laptop.")
            print("(Hint: Use 'talk marcus' to start a conversation)")
        # Redirect Red Bull giving to dialogue option
        elif item.id == 'redbull' and npc.id == 'william':
            print("\nYou should talk to William if you want to give him the Red Bull.")
            print("(Hint: Use 'talk william' to start a conversation)")
        else:
            # Default response for other items/NPCs
            print(f"\n{npc.name} doesn't seem interested in {item.name}.")

    def use_item(self, item_name):
        """Use an item from inventory or interact with location objects"""
        # First check inventory items
        item = None
        for item_id in self.state.inventory:
            i = self.items[item_id]
            if item_name.lower() in i.name.lower():
                item = i
                break

        if item:
            # Special case: Using coffee in server room
            if 'coffee' in item.id.lower() and self.state.current_location == 'server_room':
                self.pour_coffee_on_servers(item)
                return

            print()
            item.use(self.state)

            # Remove from inventory if consumable
            if item.consumable:
                self.state.inventory.remove(item.id)
            return

        # Check if it's a useable location object
        loc = self.locations[self.state.current_location]
        obj = loc.get_object(item_name)
        if obj and 'use' in obj:
            # Special handling for vending machine
            if obj['use'] == 'vending_machine_interaction':
                self.use_vending_machine()
            else:
                print(f"\n{obj['use']}")
            return

        print(f"You don't have {item_name}.")

    def read_item(self, item_name):
        """Read an item"""
        # Check items in location
        for item in self.items.values():
            if item.location == self.state.current_location and not item.taken:
                if item_name.lower() in item.name.lower():
                    print()
                    item.read(self.state)
                    return

        # Check inventory
        for item_id in self.state.inventory:
            item = self.items[item_id]
            if item_name.lower() in item.name.lower():
                print()
                item.read(self.state)
                return

        # Check location objects for readable scenery
        loc = self.locations[self.state.current_location]
        obj = loc.get_object(item_name)
        if obj and 'read' in obj:
            print(f"\n{obj['read']}")
            return

        print(f"I don't see {item_name} here.")

    def use_vending_machine(self):
        """Handle vending machine interaction"""
        from items import RedBull

        print()
        print("You approach the vending machine.")
        print()

        # Check if player already has Red Bull
        if self.state.has_redbull:
            print("You already got the Red Bull from this machine.")
            return

        # Check if player has money
        if self.state.money < 2:
            print("The Sugar-Free Red Bull in slot D4 costs $2.00.")
            print()
            print(f"You only have ${self.state.money}.")
            print()
            print("(You need to find $2 to buy the Red Bull.)")

            # Set flag that player now knows they need money
            if not self.state.knows_needs_money:
                self.state.knows_needs_money = True

            return

        # Player has enough money
        print("The Sugar-Free Red Bull in slot D4 costs $2.00.")
        print(f"You have ${self.state.money}.")
        print()
        print("Purchase Red Bull? (yes/no)")
        response = input("> ").strip().lower()

        if response in ['yes', 'y']:
            print()
            print("*You insert $2 into the machine*")
            print("*Mechanical whirring*")
            print("*THUNK*")
            print()
            print("You retrieve the cold Sugar-Free Red Bull from the slot.")

            # Give player the Red Bull
            redbull = RedBull('inventory')
            self.items['redbull'] = redbull
            redbull.taken = True
            self.state.inventory.append('redbull')
            self.state.has_redbull = True
            self.state.money -= 2

            print()
            print("Red Bull acquired!")
        else:
            print()
            print("You decide not to buy anything right now.")

    def handle_outside_exit(self):
        """Handle player attempting to leave through the outside exit"""
        print()
        print_boxed("⚠️  LEAVING THE BUILDING  ⚠️")
        print()
        print("You stand at the exit door.")
        print("Through the glass, you can see the parking lot.")
        print("Your car is right there.")
        print()
        print("You could just... leave. Walk away from all of this.")
        print("The ticket, the pressure, the technology...")
        print()
        print("Walk out and never come back? (yes/no)")
        print()

        response = input("> ").strip().lower()

        if response in ['yes', 'y']:
            clear_screen()
            print()
            print_boxed("🚪 WALKING AWAY 🚪")
            print()
            print("You push open the door.")
            print("Fresh air hits your face.")
            print("You don't look back.")
            print()
            input("Press Enter...")
            print()
            print("You walk to your car, get in, and drive.")
            print("You don't stop at home.")
            print("You just... keep driving.")
            print()
            input("Press Enter...")
            clear_screen()
            print()
            print_separator()
            print("SIX MONTHS LATER...")
            print_separator()
            print()
            print("You're standing in a field on a small farm in Vermont.")
            print("The sun is warm. There's no wifi here.")
            print("Your phone hasn't had a signal in months.")
            print()
            print("You have twelve goats now. You know all their names.")
            print("Beatrice is your favorite. She headbutted you yesterday.")
            print()
            print("Sometimes you think about that ticket you abandoned.")
            print("Karen probably never got her printing problem fixed.")
            print("You feel... surprisingly okay with that.")
            print()
            input("Press Enter...")
            print()
            print("There are no computers here.")
            print("No tickets. No escalations. No methodology checklists.")
            print("Just goats, and cheese-making, and the quiet.")
            print()
            print("Your former manager Marcus tried calling.")
            print("You threw your phone in a pond.")
            print()
            print("The goats don't judge you for your career choices.")
            print("They just want hay and occasional head scratches.")
            print()
            input("Press Enter for final results...")
            clear_screen()
            print()
            print_separator()
            print("🐐 ALTERNATE ENDING: PASTORAL ESCAPE 🐐")
            print_separator()
            print()
            print("Final Score: 0 (but are we really counting?)")
            print(f"Play Time: {self.state.get_real_play_time()}")
            print(f"Goats Acquired: 12")
            print(f"IT Career: Abandoned")
            print(f"Happiness Level: Surprisingly High")
            print()
            print("═" * 60)
            print("ACHIEVEMENT UNLOCKED:")
            print("═" * 60)
            print("🏆 'Escape Velocity' - Ran away from IT forever")
            print("═" * 60)
            print()
            print("You technically got fired for job abandonment.")
            print("But you make excellent goat cheese now.")
            print("And honestly? That's a win in its own way.")
            print()
            print("Sometimes the best troubleshooting methodology is:")
            print("Step 1: Leave")
            print("Step 2: Get goats")
            print("Step 3: Never look back")
            print()
            print_separator()
            print("Thanks for playing Downtime!")
            print("(You took the name literally)")
            print_separator()
            print()

            # Exit the game
            import sys
            sys.exit(0)
        else:
            print()
            print("You hesitate, then step back from the door.")
            print()
            print("Not today. You have a ticket to close.")
            print("...probably.")

    def handle_pour_command(self, item_name):
        """Handle the pour command"""
        # Check if player has coffee in inventory
        coffee_item = None
        for item_id in self.state.inventory:
            item = self.items[item_id]
            if 'coffee' in item.id.lower() and item_name.lower() in item.name.lower():
                coffee_item = item
                break

        # If no specific coffee found, check for any coffee-like command
        if not coffee_item:
            for item_id in self.state.inventory:
                item = self.items[item_id]
                if 'coffee' in item.id.lower():
                    coffee_item = item
                    break

        if coffee_item and self.state.current_location == 'server_room':
            # Special handling for server room
            self.pour_coffee_on_servers(coffee_item)
        elif coffee_item:
            print()
            print("You pour the coffee onto the floor.")
            print("What a waste of perfectly good coffee.")
            print()
            print("Now you just have a mess and no coffee.")
            # Remove coffee from inventory
            if coffee_item.id in self.state.inventory:
                self.state.inventory.remove(coffee_item.id)
        else:
            print()
            print("You don't have any coffee to pour.")

    def pour_coffee_on_servers(self, coffee_item):
        """Handle the catastrophic decision to pour coffee on server racks"""
        print()
        print_boxed("⚠️  CRITICAL ERROR IMMINENT  ⚠️")
        print()
        print("You stand in front of the humming server racks,")
        print("holding your cup of coffee.")
        print()
        print("A terrible idea crosses your mind...")
        print()
        print("Pour coffee on the servers? This will end VERY badly.")
        print()
        print("Are you sure? (yes/no)")
        print()

        response = input("> ").strip().lower()

        if response in ['yes', 'y']:
            # Remove coffee from inventory before the chaos
            if coffee_item.id in self.state.inventory:
                self.state.inventory.remove(coffee_item.id)

            clear_screen()
            print()
            print_boxed("💀 CATASTROPHIC FAILURE 💀")
            print()
            print("You slowly tilt your cup of coffee toward the server rack...")
            print()
            input("Press Enter to continue your descent into chaos...")
            print()
            print("The hot liquid splashes across the authentication server.")
            print()
            print("⚡ *CRACK* *POP* *SIZZLE* ⚡")
            print()
            print("Blue sparks erupt from the rack!")
            print("Smoke starts billowing from the servers!")
            print()
            input("Press Enter...")
            print()
            print("🔥 The fire alarm begins wailing! 🔥")
            print()
            print("Emergency systems kick in:")
            print("- Sprinkler system: ACTIVATED")
            print("- Fire suppression: ACTIVATED")
            print("- All servers: SHUTDOWN")
            print("- Your career: TERMINATED")
            print()
            input("Press Enter...")
            print()
            print("The entire company network goes dark.")
            print("Every computer in the building loses connection.")
            print("Karen's printing problem is now EVERYONE'S problem.")
            print()
            print("You hear running footsteps in the hallway...")
            print()
            input("Press Enter...")
            clear_screen()
            print()
            print_separator()
            print("MARCUS ARRIVES")
            print_separator()
            print()
            print('Marcus: "WHAT HAVE YOU DONE?!"')
            print()
            print('Marcus: "That was our ENTIRE infrastructure!"')
            print('        "The authentication server! The file servers!"')
            print('        "DO YOU HAVE ANY IDEA HOW MUCH DATA WE JUST LOST?!"')
            print()
            input("Press Enter...")
            print()
            print('Marcus: "This is your FIRST DAY!"')
            print('        "You were supposed to fix a PRINTER!"')
            print('        "Not DESTROY THE ENTIRE COMPANY!"')
            print()
            print("Security escorts you out of the building.")
            print("Your badge access is revoked before you reach the parking lot.")
            print()
            input("Press Enter for final results...")
            clear_screen()
            print()
            print_separator()
            print("🔥 GAME OVER: SERVER ROOM DISASTER 🔥")
            print_separator()
            print()
            print("Final Score: -9999 (New record!)")
            print(f"Time Employed: {self.state.get_time_string()}")
            print(f"Play Time: {self.state.get_real_play_time()}")
            print(f"Servers Destroyed: ALL OF THEM")
            print(f"Cost of Damage: $847,000")
            print(f"Lives Ruined: 1 (yours)")
            print()
            print("═" * 60)
            print("ACHIEVEMENT UNLOCKED:")
            print("═" * 60)
            print("🏆 'Wrong Kind of Downtime' - Took down the entire network")
            print("═" * 60)
            print()
            print("The company adds a new rule to the employee handbook:")
            print('"NO LIQUIDS WITHIN 10 FEET OF SERVER RACKS"')
            print()
            print("Karen never gets her printing problem fixed.")
            print("But honestly, that's the least of anyone's problems now.")
            print()
            print("You are permanently banned from working in IT.")
            print("Also from this office building.")
            print("And probably this city.")
            print()
            print("Legend says on quiet nights, you can still hear")
            print("the faint sound of Marcus screaming...")
            print()
            print_separator()
            print("Thanks for playing Downtime!")
            print("(In the most literal sense possible)")
            print_separator()
            print()

            # Exit the game
            import sys
            sys.exit(0)
        else:
            print()
            print("You pause and reconsider.")
            print()
            print("That would have been... really, REALLY bad.")
            print("You decide to keep your coffee and your job.")
            print()
            print("Crisis averted. Your career lives to see another day.")

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

        # Check location objects (non-takable scenery)
        loc = self.locations[self.state.current_location]
        obj = loc.get_object(target)
        if obj and 'examine' in obj:
            print(f"\n{obj['examine']}")

            # Special handling for vending machine - set flag that player knows they need money
            if target.lower() in ['vending machine', 'vending', 'machine'] and self.state.current_location == 'break_room':
                if not self.state.knows_needs_money and self.state.money < 2:
                    print()
                    print("(You need $2 to buy the Red Bull.)")
                    self.state.knows_needs_money = True

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

        # Only show caffeine info if player has consumed at least one coffee
        if self.state.coffees_consumed > 0 or self.state.redbull_consumed:
            print(f"\nCaffeine Level: {self.state.get_caffeine_level_name()}")
            print(f"Focus Buff: {self.state.get_focus_description()}")

    def show_confused_response(self, command):
        """Show a humorous response to unrecognized commands"""
        responses = [
            f"'{command}'? That's not in my job description.",
            f"Error 404: Command '{command}' not found. Have you tried turning it off and on again?",
            f"I'm a help desk tech, not a '{command}' interpreter.",
            f"'{command}' is not a valid command. Did you mean to file a ticket about that?",
            f"Hmm, '{command}' doesn't compute. Maybe it needs more coffee?",
            f"'{command}'? I'll escalate that to someone who understands it.",
            f"Syntax error: '{command}' is not recognized as a valid help desk action.",
            f"'{command}'? That sounds like a job for Level 3 support.",
            f"I tried '{command}', but my computer just stared back at me.",
            f"'{command}' is beyond my scope of practice. Also, it's not a real command.",
            f"Permission denied. Just kidding - '{command}' isn't a thing.",
            f"'{command}'? Let me check the knowledge base... Nope, nothing.",
            f"You can't '{command}' here. Or anywhere, really.",
            f"'{command}' failed successfully.",
            f"I don't speak '{command}'. Try English commands instead."
        ]
        print(random.choice(responses))

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
        print("  give [item] to [person] - Give an item to someone")
        print("  use [item]         - Use an item from inventory")
        print("  read [item]        - Read readable items like notes")
        print("  examine [thing]    - Look at something closely")
        print("  look               - Look around current location")
        print()
        print("INVENTORY:")
        print("  inventory / i      - Show what you're carrying")
        print("  status             - Show score and progress")
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
            import sys
            sys.exit(0)
        else:
            print("\nReturning to game...")

    def handle_win(self):
        """Handle winning the game"""
        print()

        # Calculate final score
        final_score = self.state.calculate_final_score()
        rank = self.state.get_rank()

        print_boxed("CONGRATULATIONS!")
        print()
        print("You successfully solved Karen's printing problem!\n")

        print("Karen was able to print her reports for her client meeting.")
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
        print(f"Play Time: {self.state.get_real_play_time()}")
        print(f"Steps Completed: {self.state.current_step}/7")
        
        if self.state.check_flag('william_quest_complete'):
            print("\n✓ William's Quest Complete")
        if self.state.check_flag('donut_heist_complete'):
            print("✓ Donut Heist Complete")

        print()

        # Check for HR complaint ending
        if self.state.check_flag('bullied_ian'):
            input("Press Enter to continue...")
            clear_screen()
            print()
            print_separator()
            print("ONE WEEK LATER...")
            print_separator()
            print()
            print("You're called into Marcus's office.")
            print()
            input("Press Enter...")
            print()
            print(format_dialogue("Marcus",
                "We need to talk. I received a complaint from Ian."))
            print()
            print(format_dialogue("Marcus",
                "He says you demanded money from him. Bullied him, actually."))
            print()
            print(format_dialogue("Marcus",
                "That's not how we treat our colleagues here. I don't care if "
                "you're technically his superior on the org chart."))
            print()
            print(format_dialogue("Marcus",
                "HR has reviewed the incident and... well, you solved the ticket, "
                "so that's in your favor. But this is a FORMAL WARNING."))
            print()
            print(format_dialogue("Marcus",
                "One more incident like this and you're out. Understood?"))
            print()
            print("You nod silently.")
            print()
            print_separator()
            print("⚠ ALTERNATE ENDING: FORMAL WARNING ⚠")
            print_separator()
            print()
            print("You kept your job... barely.")
            print("But you've earned a reputation as a bully.")
            print("Ian avoids eye contact with you now.")
            print()
            print("Technical skills aren't everything in IT.")
            print("People skills matter too.")
            print()
            print_separator()
            print("Achievement Unlocked:")
            print("🏆 'Technically Competent, Morally Questionable'")
            print_separator()
            print()
        else:
            print_separator()
            print("Thanks for playing Downtime: Game 1!")
            print("You've learned the CompTIA troubleshooting methodology.")
            print_separator()
            print()

        # Exit the game
        import sys
        sys.exit(0)


def main():
    """Main entry point"""
    game = Game()
    game.start()


if __name__ == "__main__":
    main()
