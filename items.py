"""
Item definitions for Game 1
Each item has properties and can be examined, taken, and used
"""

from utils import print_boxed, print_separator


class Item:
    """Represents an item in the game"""

    def __init__(self, id, name, description, location, takeable=True, consumable=False, readable=False):
        self.id = id
        self.name = name
        self.description = description
        self.location = location
        self.takeable = takeable
        self.consumable = consumable
        self.readable = readable
        self.taken = False

    def examine(self, game_state):
        """Examine the item in detail"""
        print(f"\n{self.name}")
        print_separator()
        print(self.description)

    def use(self, game_state):
        """Use the item (override in subclasses)"""
        print(f"\nYou can't use {self.name} right now.")

    def read(self, game_state):
        """Read the item (override in subclasses for readable items)"""
        if self.readable:
            # Default to examine for readable items
            self.examine(game_state)
        else:
            print(f"\nYou can't read {self.name}.")


class Coffee(Item):
    """Coffee item - provides caffeine boost"""

    def __init__(self, id='coffee', name='Cup of Coffee', description='A steaming cup of black coffee. The aroma is inviting.',
                 drink_message='You take a sip of the hot coffee.', location="break_room"):
        super().__init__(
            id,
            name,
            description,
            location,
            takeable=True,
            consumable=True
        )
        self.drink_message = drink_message

    def use(self, game_state):
        """Drink the coffee"""
        print_boxed("DRINKING COFFEE")
        print()
        print(self.drink_message)
        print()

        game_state.coffees_consumed += 1
        game_state.caffeine_level += 1

        if game_state.caffeine_level == 1:
            print("Ahh, that hits the spot. You feel slightly more alert.")
            game_state.add_score(5, "First coffee")
        elif game_state.caffeine_level == 2:
            print("Your mind feels sharper. You're focused and ready.")
            print("\n✓ FOCUS BUFF ACTIVATED")
            print("You'll notice more details now.")
            game_state.add_score(30, "Optimal caffeine level")
        elif game_state.caffeine_level == 3:
            print("You're feeling pretty wired, but still focused.")
            print("Your heart is beating a bit faster.")
        elif game_state.caffeine_level == 4:
            print("You're feeling uncomfortably wired.")
            print("Your hands have a slight tremor.")
        elif game_state.caffeine_level == 5:
            print("Okay, that's definitely too much coffee...")
            print("You're not feeling great. Maybe that's enough.")
            print("\n⚠ WARNING: You're very overcaffeinated.")
        elif game_state.caffeine_level >= 6:
            # DEATH
            self.handle_caffeine_overdose(game_state)
            return

        game_state.advance_time(2)

    def handle_caffeine_overdose(self, game_state):
        """Handle death from too much caffeine"""
        print()
        print_separator()
        print("💀 CARDIAC EVENT 💀")
        print_separator()
        print()
        print("Your heart is racing uncontrollably.")
        print("The room is spinning.")
        print("Everything goes dark...")
        print()
        print("─────────────────────────────────────")
        print("GAME OVER: Caffeine Overdose")
        print("─────────────────────────────────────")
        print()
        print(f"Final Score: 0")
        print(f"Coffees Consumed: {game_state.caffeine_level}")
        print(f"Play Time: {game_state.get_real_play_time()}")
        print()
        print("Achievement Unlocked: 'Heart Attack Speedrun'")
        print()
        print("You have been permanently banned from the IT department.")
        print("Marcus is updating the employee handbook with a new section:")
        print("'Maximum 2 Coffees Per Incident'")
        print()
        print("Maybe moderation is important after all...")
        print()
        import sys
        sys.exit(0)


class RedBull(Item):
    """Red Bull - maximum caffeine boost"""
    
    def __init__(self, location="break_room"):
        super().__init__(
            'redbull',
            'Sugar-Free Red Bull',
            'A cold can of Sugar-Free Red Bull. William\'s favorite.',
            location,
            takeable=True,
            consumable=True
        )
        
    def examine(self, game_state):
        """Examine Red Bull"""
        print_boxed("SUGAR-FREE RED BULL")
        print()
        print("A cold can of Sugar-Free Red Bull.")
        print("There's a sticky note attached:")
        print()
        print("  'William's - Do NOT touch!'")
        print()
        
        if not game_state.william_quest_started:
            print("Maybe William would appreciate getting this back?")
            
    def use(self, game_state):
        """Drink the Red Bull"""
        print_boxed("DRINKING RED BULL")
        print()
        
        if game_state.william_quest_started and not game_state.william_quest_complete:
            print("Wait... you were supposed to give this to William!")
            print("He's going to be disappointed...")
            print()
            
        print("You crack open the can and chug it.")
        print("MAXIMUM CAFFEINE ACHIEVED.")
        print()
        print("✓✓ ULTRA FOCUS ACTIVATED")
        print("Your perception is heightened dramatically.")
        print("You'll spot even the tiniest details.")
        print()
        print("(But your hands are shaking from all the caffeine...)")

        game_state.redbull_consumed = True
        game_state.caffeine_level += 2  # Red Bull counts as 2 coffees
        game_state.has_redbull = False

        # Check for death from overcaffeination (6+ coffees total)
        if game_state.caffeine_level >= 6:
            Coffee.handle_caffeine_overdose(self, game_state)
            return

        if not game_state.william_quest_complete:
            # Consumed without giving to William
            game_state.add_score(-25, "Consumed William's Red Bull")
        else:
            game_state.add_score(30, "Ultra Focus")
            
        game_state.advance_time(2)


class Laptop(Item):
    """New laptop"""

    def __init__(self, location="it_office"):
        super().__init__(
            'laptop',
            'New Laptop',
            'A brand new laptop, still in its box.',
            location,
            takeable=True,
            consumable=False
        )

    def examine(self, game_state):
        """Examine the laptop"""
        print_boxed("NEW LAPTOP")
        print()
        print("A brand new Dell laptop, still sealed in its box.")
        print()
        print("Looks like a recent delivery. Someone's getting an upgrade.")


class Donut(Item):
    """Donut from Manager's office"""

    def __init__(self, location="manager_office"):
        super().__init__(
            'donut',
            'Chocolate Donut',
            'A delicious-looking chocolate donut with sprinkles.',
            location,
            takeable=True,
            consumable=True
        )

    def examine(self, game_state):
        """Examine the donut"""
        print_boxed("CHOCOLATE DONUT")
        print()
        print("A beautiful chocolate donut with rainbow sprinkles.")
        print("It looks incredibly tempting.")
        print()

        if not game_state.check_flag('marcus_has_laptop'):
            print("Marcus is sitting right there at his desk.")
            print("You can't just take his donut while he's watching!")
        else:
            print("Marcus is busy setting up his new laptop.")
            print("He's completely distracted...")
            print()
            print("There's a note: 'Marcus's donut - For after the")
            print("             morning meeting'")
            print()
            print("Taking this would be... questionable.")
        
    def use(self, game_state):
        """Eat the donut"""
        print_boxed("EATING DONUT")
        print()
        print("You devour the donut in three bites.")
        print("It's delicious. Absolutely worth it.")
        print()
        
        if not game_state.check_flag('donut_heist_complete'):
            print("Achievement Unlocked: 'The Donut Heist'")
            game_state.set_flag('donut_heist_complete', True)
            game_state.add_score(50, "Donut Heist complete")
        else:
            game_state.add_score(5, "Tasty donut")
            
        print()
        print("(Hopefully Marcus doesn't notice...)")
        
        game_state.advance_time(2)


class Methodology(Item):
    """CompTIA Methodology reference sheet"""

    def __init__(self, location="it_office"):
        super().__init__(
            'methodology',
            'CompTIA Methodology Sheet',
            'A laminated reference card showing the 7-step troubleshooting process.',
            location,
            takeable=True,
            consumable=False,
            readable=True
        )

    def examine(self, game_state):
        """Examine methodology sheet"""
        print_boxed("COMPTIA TROUBLESHOOTING METHODOLOGY")
        print()
        print("The 7-Step Process:")
        print()
        print("1. Identify the Problem")
        print("   - Gather information")
        print("   - Question users")
        print("   - Identify symptoms")
        print()
        print("2. Establish a Theory of Probable Cause")
        print("   - Question the obvious")
        print("   - Consider multiple approaches")
        print()
        print("3. Test the Theory")
        print("   - Test to determine cause")
        print("   - If confirmed, move forward")
        print("   - If not confirmed, establish new theory")
        print()
        print("4. Establish a Plan of Action")
        print("   - Consider corporate policies")
        print("   - Plan rollback strategy")
        print()
        print("5. Implement the Solution")
        print("   - Apply fix")
        print("   - Escalate if needed")
        print()
        print("6. Verify Full System Functionality")
        print("   - Verify fix resolves issue")
        print("   - Ensure user can work normally")
        print()
        print("7. Document Findings")
        print("   - Document problem")
        print("   - Document solution")
        print("   - Document lessons learned")

        if not game_state.check_flag('read_methodology'):
            game_state.set_flag('read_methodology', True)
            game_state.add_score(10, "Read methodology")

    def read(self, game_state):
        """Read methodology sheet - same as examine"""
        self.examine(game_state)


class Sticky(Item):
    """Sticky note with password hint"""

    def __init__(self, location="karen_office"):
        super().__init__(
            'sticky_note',
            'Sticky Note',
            'A yellow sticky note with handwriting.',
            location,
            takeable=True,
            consumable=False,
            readable=True
        )

    def examine(self, game_state):
        """Examine sticky note"""
        print_boxed("STICKY NOTE")
        print()
        print("A yellow sticky note with Karen's handwriting:")
        print()
        print("  Password: Accounting2024!")
        print()
        print("At least she didn't write her username too...")

        if not game_state.check_flag('found_password_sticky'):
            game_state.set_flag('found_password_sticky', True)
            game_state.add_score(5, "Found password note")

    def read(self, game_state):
        """Read sticky note - same as examine"""
        self.examine(game_state)


def init_items():
    """Initialize all game items"""
    items = {}

    # Coffee sources around the office (5 total)
    items['coffee_it_office'] = Coffee(
        id='coffee_it_office',
        name='Fresh Cup of Coffee',
        description='A fresh, steaming cup of coffee from your desk. Still hot.',
        drink_message='You drink the fresh, hot coffee. Smooth and perfectly brewed.',
        location='it_office'
    )

    items['coffee_help_desk'] = Coffee(
        id='coffee_help_desk',
        name="Ian's Coffee",
        description="Ian's cup of coffee from the Help Desk. Smells decent.",
        drink_message="You drink Ian's coffee. Not bad - he knows how to make a decent cup.",
        location='help_desk'
    )

    items['coffee_break_room'] = Coffee(
        id='coffee_break_room',
        name='Fresh Pot Coffee',
        description='Coffee from the fresh pot in the break room. Quality brew.',
        drink_message='You pour yourself coffee from the fresh pot. Rich and aromatic.',
        location='break_room'
    )

    items['coffee_mystery'] = Coffee(
        id='coffee_mystery',
        name='Mystery Coffee',
        description="An old cup of coffee from the break room table. Age unknown. Probably shouldn't drink this.",
        drink_message="You drink the mystery coffee. It's... lukewarm at best. And tastes vaguely like despair. Why did you do this?",
        location='break_room'
    )

    items['coffee_server_room'] = Coffee(
        id='coffee_server_room',
        name='Ancient Server Room Coffee',
        description='A crusty, ancient coffee mug from the server room. This might qualify as a biological hazard.',
        drink_message='You drink the ancient server room coffee. It tastes like regret and old semiconductors. This was a terrible decision.',
        location='server_room'
    )

    # Red Bull - NOT initialized here, obtained through vending machine
    # items['redbull'] = RedBull('break_room')

    # Laptop for Marcus
    items['laptop'] = Laptop('it_office')

    # Donut
    items['donut'] = Donut('manager_office')

    # Methodology sheet
    items['methodology'] = Methodology('it_office')

    # Sticky note
    items['sticky_note'] = Sticky('karen_office')

    # Add more items as needed

    return items
