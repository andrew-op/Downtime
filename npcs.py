"""
NPC definitions with dialogue trees for Game 1
"""

from utils import print_boxed, print_separator, format_dialogue, display_choices


class NPC:
    """Base NPC class"""
    
    def __init__(self, id, name, description, location):
        self.id = id
        self.name = name
        self.description = description
        self.location = location
        self.dialogue_state = "initial"
        
    def talk(self, game_state, items):
        """Talk to the NPC - override in subclasses"""
        print(f"{self.name}: Hello!")


class Ian(NPC):
    """Ian - Help Desk Technician"""
    
    def __init__(self):
        super().__init__(
            'ian',
            'Ian (Help Desk)',
            'A harried-looking help desk tech with a phone headset.',
            'help_desk'
        )
        
    def talk(self, game_state, items):
        """Ian's dialogue tree"""
        print_boxed("TALKING TO IAN")
        print()

        # First time talking
        if not game_state.talked_to_ian:
            # First conversation
            print(format_dialogue("Ian",
                "Hey! You must be the new IT support. Thank god you're here."))
            print()
            print(format_dialogue("Ian",
                "I've been working on this printing issue for Karen in Accounting "
                "for the last 20 minutes and I'm getting nowhere."))
            print()
            print(format_dialogue("Ian",
                "She can't print to the network printer. I verified the printer "
                "is powered on, has paper, no jams... The hardware is fine."))
            print()
            print(format_dialogue("Ian",
                "I even pinged her workstation - network connection looks good. "
                "She can access the internet just fine."))
            print()
            print(format_dialogue("Ian",
                "But her computer says 'No printers found' when she tries to print. "
                "I can't figure it out."))
            print()
            print(format_dialogue("Ian",
                "I escalated it to you because, well... it's weird. And she has a "
                "client meeting at 10 AM, so there's time pressure."))
            print()
            print(format_dialogue("Ian",
                "Her office is in Accounting. East from the hallway. Good luck!"))

            game_state.talked_to_ian = True
            game_state.add_score(10, "Talked to Ian")
            game_state.advance_time(5)
            print()

        # Conversation loop
        while True:
            choices = [
                "What exactly did you try?",
                "Tell me more about the user.",
                "Leave conversation"
            ]

            choice = display_choices(choices)
            print()

            if choice == 3:  # Leave
                break
            elif choice == 1:
                print(format_dialogue("Ian",
                    "I checked network connectivity with ping - got responses. "
                    "I verified the printer has power and paper. "
                    "I even checked if the print spooler service was running - it is."))
                print()
                print(format_dialogue("Ian",
                    "That's about where I ran out of ideas. The network seems fine, "
                    "the printer is fine, but she can't print."))
                print()
            elif choice == 2:
                print(format_dialogue("Ian",
                    "Karen Miller. Accounting department. Been here forever. "
                    "She's usually pretty calm, but she's stressed today because "
                    "of that client meeting."))
                print()
                print(format_dialogue("Ian",
                    "She's not super tech-savvy, but she's not clueless either. "
                    "She knows her way around the basics."))
                print()


class Karen(NPC):
    """Karen - Accounting User with network/printing problem"""

    def __init__(self):
        super().__init__(
            'karen',
            'Karen (Accounting)',
            'A stressed-looking woman in her 40s, sitting at her desk with a frustrated expression.',
            'karen_office'
        )
        
    def talk(self, game_state, items):
        """Karen's dialogue tree"""
        print_boxed("TALKING TO KAREN")
        print()

        # Check if problem is solved
        if game_state.karen_problem_fixed:
            self.dialogue_solved(game_state)
            return

        # First time talking
        if not game_state.talked_to_karen:
            # First conversation
            print(format_dialogue("Karen",
                "Oh, thank goodness. Are you from IT? Please tell me you can "
                "fix this. I have a client meeting in... " +
                ("less than 15 minutes!" if game_state.minutes >= 45 else "soon!")))
            print()
            print(format_dialogue("Karen",
                "I can't print! I've been trying to print my quarterly report "
                "for the meeting, but my computer won't send it to the printer!"))
            print()
            print(format_dialogue("Karen",
                "I've tried three times already! The print dialog just says "
                "'No printers found.' But the printer is right there!"))

            game_state.talked_to_karen = True
            game_state.add_score(10, "Talked to Karen")
            game_state.advance_time(3)
            print()

        # Conversation loop
        while True:
            if game_state.told_karen_about_network:
                if not self.dialogue_post_solution(game_state):
                    break
            else:
                if not self.dialogue_investigation(game_state):
                    break
                
    def dialogue_investigation(self, game_state):
        """Investigation phase dialogue - returns False if player leaves"""
        choices = [
            "Can you show me what happens when you try to print?",
            "Is the printer turned on and connected?",
            "Can you access the internet?",
            "Let me check your network settings."
        ]

        # Add network solution option if spotted
        if game_state.spotted_wrong_network and not game_state.told_karen_about_network:
            choices.append("I found the problem - you're on the Guest network!")

        # Always add leave option
        choices.append("Leave conversation")

        choice = display_choices(choices)
        print()

        # Check if player is leaving (always last option)
        if choice == len(choices):
            return False

        if choice == 1:
            # Watch Karen attempt to print
            self.watch_karen_print(game_state)

        elif choice == 2:
            # Check printer physically
            self.check_printer(game_state)

        elif choice == 3:
            # Check internet (red herring!)
            self.check_internet(game_state)

        elif choice == 4:
            # Check network settings - CRITICAL
            self.check_network_settings(game_state)

        elif choice == 5 and game_state.spotted_wrong_network:
            # Tell her about network issue
            game_state.told_karen_about_network = True
            self.dialogue_post_solution(game_state)

        return True  # Continue conversation
            
    def watch_karen_print(self, game_state):
        """Watch Karen attempt to print"""
        print(format_dialogue("Karen",
            "Okay, let me try again. I'll show you."))
        print()
        print("*Karen opens her quarterly report document*")
        print()
        print("*She clicks File > Print...*")
        print()
        print("*The print dialog opens*")
        print()
        print(format_dialogue("Karen",
            "See? It says 'No printers found.' But the printer is right there "
            "by the window!"))
        print()
        print("You see the message: 'No printers available'")
        print()
        print("(The printer seems to be powered on. This might be a network issue...)")

        game_state.advance_time(3)
        
    def check_printer(self, game_state):
        """Check if printer is physically working"""
        print("You walk over to the printer by the window.")
        print()
        print("The printer is a network-capable HP LaserJet.")
        print("Power light is on. Paper is loaded. No error messages.")
        print()
        print(format_dialogue("Karen",
            "See? The printer is fine! It's been working all week until today!"))
        print()
        print("(The printer hardware seems fine. The issue must be elsewhere...)")

        game_state.checked_printer = True
        game_state.advance_time(2)

    def check_internet(self, game_state):
        """Check internet connectivity (red herring)"""
        print(format_dialogue("Karen",
            "Oh, the internet works fine! I was just checking my email "
            "and browsing earlier."))
        print()
        print("*Karen opens a web browser*")
        print()
        print("*She navigates to google.com*")
        print()
        print("*The page loads successfully*")
        print()
        print(format_dialogue("Karen",
            "See? Internet is working perfectly."))
        print()
        print("(Internet works, but she still can't print. Interesting...)")

        game_state.advance_time(2)

    def check_network_settings(self, game_state):
        """Check network settings - CRITICAL PATH"""
        print("You open the network settings on Karen's computer.")
        print()
        print("*Clicking the WiFi icon in the system tray*")
        print()

        # Network check with focus buff requirement
        if game_state.has_focus_buff() and not game_state.spotted_wrong_network:
            print("✓ OBSERVATION (Focus Buff)")
            print()
            print("Wait... you notice something important:")
            print()
            print("Connected to: Guest_WiFi")
            print("Signal Strength: Excellent")
            print()
            print("That's the problem! She's connected to the guest network!")
            print()
            print("The guest network provides internet access but blocks internal")
            print("resources like printers, file shares, and internal applications.")
            print()
            print("She needs to be on 'Corp_Network' instead!")

            game_state.spotted_wrong_network = True
            game_state.add_score(25, "Spotted Wrong Network!")

        elif not game_state.spotted_wrong_network:
            print("You see network information on the screen...")
            print()
            print("Network: Connected")
            print("Signal Strength: Excellent")
            print()
            print("Hmm... something seems off, but you're not sure what.")
            print("You rub your eyes. It's hard to focus this early in the morning...")

        else:
            # Already spotted it
            print("You check the network settings again.")
            print()
            print("Connected to: Guest_WiFi")
            print()
            print("That's definitely the problem. She's on the wrong network.")

        game_state.checked_network_settings = True
        game_state.advance_time(3)
        
    def dialogue_post_solution(self, game_state):
        """After telling Karen about the network issue - returns False if player leaves"""
        if not game_state.karen_problem_fixed:
            print(format_dialogue("Karen",
                "The GUEST network?! Oh no... I must have clicked the wrong one "
                "when I connected this morning!"))
            print()
            print(format_dialogue("Karen",
                "Let me disconnect and connect to the right network..."))
            print()
            print("*Karen clicks the WiFi icon*")
            print()
            print("*She disconnects from Guest_WiFi*")
            print()
            print("*She selects Corp_Network from the list*")
            print()
            print("*Enters the password...*")
            print()
            print("*Connected to Corp_Network*")
            print()
            print(format_dialogue("Karen",
                "Okay, I'm connected to Corp_Network now. Let me try printing..."))
            print()
            print("*Karen opens her document and clicks Print*")
            print()
            print("*Print dialog opens...*")
            print()
            print("*Accounting_Printer_Floor2 appears in the list!*")
            print()
            print("*She clicks Print*")
            print()
            print("*The printer by the window whirs to life and prints the document*")
            print()
            print(format_dialogue("Karen",
                "IT WORKED! The printer shows up now! Oh thank you so much!"))

            game_state.karen_problem_fixed = True
            game_state.steps_complete[5] = True  # Implementation
            game_state.add_score(60, "Step 5: Solution Implemented")
            game_state.advance_time(3)

            # Now offer verification
            print()
            print(format_dialogue("Karen",
                "I still have a few minutes before my meeting. Should I test "
                "the file shares and other systems to make sure everything works?"))
            print()

            choices = ["Yes, please verify everything works", "No, you're all set", "Leave conversation"]
            choice = display_choices(choices)
            print()

            if choice == 3:  # Leave
                return False
            elif choice == 1:
                self.verify_functionality(game_state)
            else:
                print(format_dialogue("Karen",
                    "Okay, thanks again!"))

            return True

        else:
            print(format_dialogue("Karen",
                "Everything is working now. Thank you so much!"))
            print()

            choices = ["Leave conversation"]
            choice = display_choices(choices)
            return False  # Only option is to leave
            
    def verify_functionality(self, game_state):
        """Verify system functionality (Step 6)"""
        print(format_dialogue("Karen",
            "Okay, let me check everything..."))
        print()
        print("*Karen tries to print another test page*")
        print()
        print("*The printer responds immediately*")
        print()
        print(format_dialogue("Karen",
            "Printing works! Great!"))
        print()
        print("*Karen opens File Explorer and navigates to \\\\fileserver\\accounting*")
        print()
        print(format_dialogue("Karen",
            "File server access... yes! I can see all my folders now!"))
        print()
        print("*She opens a spreadsheet from the network share*")
        print()
        print(format_dialogue("Karen",
            "Perfect! Everything is working perfectly!"))
        print()
        print(format_dialogue("Karen",
            "I really appreciate you taking the time to make sure. Some techs "
            "just fix and run!"))

        game_state.karen_verified_working = True
        game_state.steps_complete[6] = True  # Verification
        game_state.add_score(70, "Step 6: Verified Functionality")
        game_state.advance_time(5)
        
    def dialogue_solved(self, game_state):
        """After everything is resolved"""
        print(format_dialogue("Karen",
            "Everything is working great! I made my meeting on time too. "
            "Thank you so much!"))
        print()

        if game_state.karen_verified_working:
            print(format_dialogue("Karen",
                "And I learned something - I'll make sure I'm on the Corp_Network "
                "before calling IT next time!"))
        else:
            print(format_dialogue("Karen",
                "I should probably verify everything is working before my "
                "meeting though..."))


class Marcus(NPC):
    """Marcus - IT Manager"""
    
    def __init__(self):
        super().__init__(
            'marcus',
            'Marcus (Manager)',
            'Your manager. Professional, supportive, and slightly stressed.',
            'manager_office'
        )
        
    def talk(self, game_state, items):
        """Marcus's dialogue"""
        print_boxed("TALKING TO MARCUS")
        print()

        # Conversation loop
        while True:
            if game_state.karen_problem_fixed:
                print(format_dialogue("Marcus",
                    "I heard you solved Karen's problem! Great work! Make sure you "
                    "document everything in the ticket system."))
                print()
                choices = ["Leave conversation"]
                choice = display_choices(choices)
                break
            else:
                print(format_dialogue("Marcus",
                    "How's it going with Karen's ticket? Need any help?"))
                print()

                choices = ["I'm working on it", "Can you give me more time?", "Leave conversation"]
                choice = display_choices(choices)
                print()

                if choice == 3:  # Leave
                    break
                elif choice == 1:
                    print(format_dialogue("Marcus",
                        "Good. Keep me posted. Remember the methodology!"))
                    print()
                else:
                    print(format_dialogue("Marcus",
                        "The meeting is at 10 AM. Do your best, but keep me informed."))
                    print()


class William(NPC):
    """William - Retired IT Director"""
    
    def __init__(self):
        super().__init__(
            'william',
            'William (Retired IT Director)',
            'A relaxed-looking man reading a newspaper.',
            'break_room'
        )
        
    def talk(self, game_state, items):
        """William's dialogue tree - quest giver"""
        print_boxed("TALKING TO WILLIAM")
        print()

        # Conversation loop
        while True:
            if game_state.william_quest_complete:
                # Quest complete
                print(format_dialogue("William",
                    "How's that ticket going? Remember - watch what the user DOES, "
                    "not what they SAY."))
                print()
                choices = ["Leave conversation"]
                choice = display_choices(choices)
                break

            elif game_state.william_quest_started:
                # Quest in progress
                if game_state.has_redbull:
                    # Has Red Bull - can complete quest
                    self.complete_quest(game_state)
                    # After completing quest, continue loop
                    continue
                else:
                    print(format_dialogue("William",
                        "Find that Red Bull yet?"))
                    print()
                    choices = ["Leave conversation"]
                    choice = display_choices(choices)
                    break

            else:
                # Start quest
                if not self.start_quest(game_state):
                    break
                # After starting quest, continue loop
                continue
            
    def start_quest(self, game_state):
        """Start William's quest - returns False if player leaves"""
        print(format_dialogue("William",
            "Ah, the new IT support! Welcome to the team."))
        print()
        print(format_dialogue("William",
            "I'm William. Retired IT director. Just enjoying my coffee and "
            "reading the paper."))
        print()
        print(format_dialogue("William",
            "Say... I don't suppose you could help me out?"))
        print()

        choices = ["Sure, what do you need?", "Sorry, I'm busy with a ticket.", "Leave conversation"]
        choice = display_choices(choices)
        print()

        if choice == 3:  # Leave
            return False
        elif choice == 1:
            print(format_dialogue("William",
                "There's a Sugar-Free Red Bull in the vending machine down the hall. "
                "I'd get it myself, but I'm a bit short on cash at the moment."))
            print()
            print(format_dialogue("William",
                "Bring me that Red Bull, and I'll share some wisdom from "
                "30 years in IT. Deal?"))

            game_state.william_quest_started = True
            game_state.set_flag('william_quest_started', True)
            print()
            print("Quest Started: William's Wisdom")
            print("Find the Sugar-Free Red Bull and bring it to William")
            print()
            return True
        else:
            print(format_dialogue("William",
                "No problem. Come back when you have time."))
            print()
            return False
            
    def complete_quest(self, game_state):
        """Complete William's quest"""
        print(format_dialogue("William",
            "Ah! You found it! Thank you!"))
        print()
        print("*William cracks open the Red Bull*")
        print()
        print("*Takes a long, satisfied sip*")
        print()
        print(format_dialogue("William",
            "Alright, as promised. Here's what 30 years in IT taught me:"))
        print()
        print(format_dialogue("William",
            "Be OBSERVANT. The answer is usually right in front of you. "
            "You just have to actually LOOK. Carefully."))
        print()
        print(format_dialogue("William",
            "Most problems aren't as complex as you think. Start simple. "
            "Check the basics first."))
        print()
        print(format_dialogue("William",
            "And here's the big one: Watch what the user actually DOES, "
            "not what they TELL you they're doing."))
        print()
        print(format_dialogue("William",
            "People don't lie on purpose - they just don't observe themselves. "
            "They'll say they're typing correctly, but they're not watching "
            "their hands."))
        print()
        print(format_dialogue("William",
            "So go WATCH that user. Don't trust their description. Watch their "
            "hands. Watch the screen. Watch for the little things."))
        print()
        print("*Winks*")
        print()
        print(format_dialogue("William",
            "The truth is in the details, kid."))
        
        print()
        print_separator()
        print("✓ William's Quest Complete!")
        print()
        print("Wisdom Received:")
        print("  • Be observant and aware")
        print("  • Start with simple explanations")
        print("  • Watch what users DO, not what they SAY")
        print("  • The truth is in the details")
        print_separator()
        
        game_state.william_quest_complete = True
        game_state.has_redbull = False
        game_state.add_score(100, "William's Quest Complete")
        
        print()
        print("Achievement Unlocked: 'The Old Guard'")


def init_npcs():
    """Initialize all NPCs"""
    npcs = {}
    
    npcs['ian'] = Ian()
    npcs['karen'] = Karen()
    npcs['marcus'] = Marcus()
    npcs['william'] = William()
    
    return npcs
