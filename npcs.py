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
        
        if not game_state.talked_to_ian:
            # First conversation
            print(format_dialogue("Ian", 
                "Hey! You must be the new IT support. Thank god you're here."))
            print()
            print(format_dialogue("Ian",
                "I've been working on this login issue for Karen in Accounting "
                "for the last 20 minutes and I'm getting nowhere."))
            print()
            print(format_dialogue("Ian",
                "She keeps getting 'Invalid Password' errors. I verified her "
                "network connection, pinged her workstation - everything looks "
                "fine from a network perspective."))
            print()
            print(format_dialogue("Ian",
                "But she INSISTS her password is correct, and honestly, I believe "
                "her. She's been working here for 10 years and knows her password."))
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
            
        else:
            # Subsequent conversations
            choices = [
                "What exactly did you try?",
                "Tell me more about the user.",
                "Thanks, I'll handle it."
            ]
            
            choice = display_choices(choices)
            print()
            
            if choice == 1:
                print(format_dialogue("Ian",
                    "I checked network connectivity with ping - got responses. "
                    "I verified the workstation shows up in Active Directory. "
                    "I checked the authentication logs and saw multiple failed "
                    "login attempts."))
                print()
                print(format_dialogue("Ian",
                    "That's about where I ran out of ideas. The network is fine, "
                    "the server is responding, but she can't log in."))
                    
            elif choice == 2:
                print(format_dialogue("Ian",
                    "Karen Miller. Accounting department. Been here forever. "
                    "She's usually pretty calm, but she's stressed today because "
                    "of that client meeting."))
                print()
                print(format_dialogue("Ian",
                    "She's not super tech-savvy, but she's not clueless either. "
                    "She knows her way around the basics."))
                    
            else:
                print(format_dialogue("Ian",
                    "Thanks! Let me know if you need anything."))


class Karen(NPC):
    """Karen - Accounting User with login problem"""
    
    def __init__(self):
        super().__init__(
            'karen',
            'Karen (Accounting)',
            'A stressed-looking woman in her 40s, sitting at her desk looking at a login screen.',
            'karen_office'
        )
        
    def talk(self, game_state, items):
        """Karen's dialogue tree"""
        print_boxed("TALKING TO KAREN")
        print()
        
        # Check if problem is solved
        if game_state.karen_logged_in:
            self.dialogue_solved(game_state)
            return
            
        if not game_state.talked_to_karen:
            # First conversation
            print(format_dialogue("Karen",
                "Oh, thank goodness. Are you from IT? Please tell me you can "
                "fix this. I have a client meeting in... " +
                ("less than 15 minutes!" if game_state.minutes >= 45 else "soon!")))
            print()
            print(format_dialogue("Karen",
                "I've been trying to log in all morning and I keep getting "
                "'Invalid Password' errors. But I KNOW my password is correct!"))
            print()
            print(format_dialogue("Karen",
                "I haven't changed it. I use the same password every day. "
                "There's no reason this shouldn't work!"))

            game_state.talked_to_karen = True
            game_state.add_score(10, "Talked to Karen")
            game_state.advance_time(3)

            # Show dialogue options immediately after first conversation
            print()
            self.dialogue_investigation(game_state)

        else:
            # Subsequent conversations
            if game_state.told_karen_about_caps_lock:
                self.dialogue_post_solution(game_state)
            else:
                self.dialogue_investigation(game_state)
                
    def dialogue_investigation(self, game_state):
        """Investigation phase dialogue"""
        choices = [
            "Can you show me what happens when you try to log in?",
            "What's your password? (Just kidding)",
            "Have you tried turning it off and on again?",
            "Let me look at your keyboard."
        ]
        
        # Add Caps Lock option if spotted
        if game_state.spotted_caps_lock and not game_state.told_karen_about_caps_lock:
            choices.append("I think I found the problem - your Caps Lock is on!")
        
        choice = display_choices(choices)
        print()
        
        if choice == 1:
            # Watch Karen type - CRITICAL
            self.watch_karen_type(game_state)
            
        elif choice == 2:
            print(format_dialogue("Karen",
                "*glares at you*"))
            print()
            print(format_dialogue("Karen",
                "Very funny. My password is written on a sticky note in my drawer "
                "if you MUST know, but I'm not telling you the drawer code."))
            print()
            print("(She looks unamused)")
            
        elif choice == 3:
            print(format_dialogue("Karen",
                "I rebooted twice already! The computer is fine, it's the PASSWORD "
                "that won't work!"))
            game_state.add_score(-5, "Cliché IT response")
            
        elif choice == 4:
            self.examine_keyboard(game_state)
            
        elif choice == 5 and game_state.spotted_caps_lock:
            # Tell her about Caps Lock
            game_state.told_karen_about_caps_lock = True
            self.dialogue_post_solution(game_state)
            
    def watch_karen_type(self, game_state):
        """Watch Karen attempt login - spot Caps Lock"""
        print(format_dialogue("Karen",
            "Okay, watch. I'll type it exactly like I always do."))
        print()
        print("*Karen types her username: karen*")
        print()
        
        # Caps Lock check
        if game_state.has_focus_buff() and not game_state.spotted_caps_lock:
            print("Wait... you notice something.")
            print()
            print("✓ OBSERVATION (Focus Buff)")
            print()
            print("There's a small light on her keyboard - the Caps Lock indicator.")
            print("It's ON.")
            print()
            print("*Karen starts typing her password*")
            print()
            print("You can't see what she's typing, but with Caps Lock on...")
            print("Every letter would be the wrong case!")
            print()
            print("*Login fails: 'Invalid Password'*")
            print()
            print(format_dialogue("Karen",
                "SEE?! I'm typing it exactly right and it won't work!"))
            
            game_state.spotted_caps_lock = True
            game_state.add_score(25, "Spotted Caps Lock!")
            
        elif not game_state.spotted_caps_lock:
            print("*Karen types her password (you can't see it)*")
            print()
            print("*Login fails: 'Invalid Password'*")
            print()
            print(format_dialogue("Karen",
                "See? Same thing every time!"))
            print()
            print("You're not sure what the problem is yet.")
            print("Maybe more coffee would help you focus...")
            
        else:
            # Already spotted it
            print("You watch Karen type.")
            print("The Caps Lock light is still on.")
            print("That's definitely the problem.")
            
        game_state.watched_karen_type = True
        game_state.advance_time(3)
        
    def examine_keyboard(self, game_state):
        """Examine the keyboard directly"""
        print("You lean over to look at Karen's keyboard.")
        print()
        
        if game_state.has_focus_buff() and not game_state.spotted_caps_lock:
            print("✓ OBSERVATION (Focus Buff)")
            print()
            print("The Caps Lock indicator light is ON!")
            print()
            print("That's it! The Caps Lock key is active, which means")
            print("every letter she types is the wrong case!")
            
            game_state.spotted_caps_lock = True
            game_state.add_score(25, "Spotted Caps Lock!")
            
        elif not game_state.spotted_caps_lock:
            print("It's a standard keyboard. Nothing seems obviously wrong.")
            print()
            print("Maybe you need to be more focused to spot subtle issues...")
            
        else:
            print("The Caps Lock light is on. That's the problem.")
            
        game_state.advance_time(2)
        
    def dialogue_post_solution(self, game_state):
        """After telling Karen about Caps Lock"""
        print(format_dialogue("Karen",
            "Oh my god. CAPS LOCK?! I can't believe... I've been sitting here "
            "for 30 minutes and it was CAPS LOCK?!"))
        print()
        
        if not game_state.karen_logged_in:
            print(format_dialogue("Karen",
                "Let me try again..."))
            print()
            print("*Karen presses Caps Lock to turn it off*")
            print()
            print("*She types her password*")
            print()
            print("*Login succeeds!*")
            print()
            print(format_dialogue("Karen",
                "IT WORKED! Oh thank you, thank you! I can't believe it was "
                "something so simple!"))
            
            game_state.karen_logged_in = True
            game_state.steps_complete[5] = True  # Implementation
            game_state.add_score(60, "Step 5: Solution Implemented")
            game_state.advance_time(2)
            
            # Now offer verification
            print()
            print(format_dialogue("Karen",
                "I still have a few minutes before my meeting. Should I test "
                "everything to make sure it's all working?"))
            print()
            
            choices = ["Yes, please verify everything works", "No, you're all set"]
            choice = display_choices(choices)
            print()
            
            if choice == 1:
                self.verify_functionality(game_state)
            else:
                print(format_dialogue("Karen",
                    "Okay, thanks again!"))
                print()
                print("(Skipping verification is risky...)")
                
        else:
            print(format_dialogue("Karen",
                "Everything is working now. Thank you so much!"))
            
    def verify_functionality(self, game_state):
        """Verify system functionality (Step 6)"""
        print(format_dialogue("Karen",
            "Okay, let me check everything..."))
        print()
        print("*Karen opens her email*")
        print()
        print(format_dialogue("Karen",
            "Email is working... loading... yes, all my messages are here."))
        print()
        print("*Karen accesses the file server*")
        print()
        print(format_dialogue("Karen",
            "File server... I can see all my folders. Opening a spreadsheet..."))
        print()
        print("*Spreadsheet loads successfully*")
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
                "And I learned something - I'll check that Caps Lock light "
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
        
        if game_state.karen_logged_in:
            print(format_dialogue("Marcus",
                "I heard you solved Karen's problem! Great work! Make sure you "
                "document everything in the ticket system."))
        else:
            print(format_dialogue("Marcus",
                "How's it going with Karen's ticket? Need any help?"))
            print()
            
            choices = ["I'm working on it", "Can you give me more time?"]
            choice = display_choices(choices)
            print()
            
            if choice == 1:
                print(format_dialogue("Marcus",
                    "Good. Keep me posted. Remember the methodology!"))
            else:
                print(format_dialogue("Marcus",
                    "The meeting is at 10 AM. Do your best, but keep me informed."))


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
        
        if game_state.william_quest_complete:
            # Quest complete
            print(format_dialogue("William",
                "How's that ticket going? Remember - watch what the user DOES, "
                "not what they SAY."))

        elif game_state.william_quest_started:
            # Quest in progress
            if game_state.has_redbull:
                # Has Red Bull - can complete quest
                self.complete_quest(game_state)
            else:
                print(format_dialogue("William",
                    "Find that Red Bull yet?"))
                    
        else:
            # Start quest
            self.start_quest(game_state)
            
    def start_quest(self, game_state):
        """Start William's quest"""
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
        
        choices = ["Sure, what do you need?", "Sorry, I'm busy with a ticket."]
        choice = display_choices(choices)
        print()
        
        if choice == 1:
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
            
        else:
            print(format_dialogue("William",
                "No problem. Come back when you have time."))
            
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
