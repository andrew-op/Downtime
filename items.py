"""
Item definitions for Game 1
Each item has properties and can be examined, taken, and used
"""

from utils import print_boxed, print_separator


class Item:
    """Represents an item in the game"""
    
    def __init__(self, id, name, description, location, takeable=True, consumable=False):
        self.id = id
        self.name = name
        self.description = description
        self.location = location
        self.takeable = takeable
        self.consumable = consumable
        self.taken = False
        
    def examine(self, game_state):
        """Examine the item in detail"""
        print(f"\n{self.name}")
        print_separator()
        print(self.description)
        
    def use(self, game_state):
        """Use the item (override in subclasses)"""
        print(f"\nYou can't use {self.name} right now.")


class Coffee(Item):
    """Coffee item - provides caffeine boost"""
    
    def __init__(self, location="break_room"):
        super().__init__(
            'coffee',
            'Cup of Coffee',
            'A steaming cup of black coffee. The aroma is inviting.',
            location,
            takeable=True,
            consumable=True
        )
        
    def use(self, game_state):
        """Drink the coffee"""
        print_boxed("DRINKING COFFEE")
        print()
        print("You take a sip of the hot coffee.")
        print()
        
        game_state.coffees_consumed += 1
        game_state.caffeine_level += 1
        
        if game_state.caffeine_level == 1:
            print("Ahh, that hits the spot. You feel more alert.")
            game_state.add_score(5, "First coffee")
        elif game_state.caffeine_level == 2:
            print("Your mind feels sharper. You're focused and ready.")
            print("\n✓ FOCUS BUFF ACTIVATED")
            print("You'll notice more details now.")
            game_state.add_score(10, "Optimal caffeine level")
        elif game_state.caffeine_level == 3:
            print("You're feeling pretty wired, but still in control.")
        elif game_state.caffeine_level == 4:
            print("Okay, that might have been too much coffee...")
            print("Your hands are starting to shake a bit.")
            print("\n⚠ OVERCAFFEINATED")
            print("You lose focus from too much caffeine.")
            game_state.add_score(-10, "Too much coffee")
        else:
            print("You're way too caffeinated. Your heart is racing.")
            print("This is definitely not helping anymore.")
            game_state.add_score(-5, "Excessive coffee")
            
        game_state.advance_time(2)


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
        game_state.caffeine_level = 5
        game_state.has_redbull = False
        
        if not game_state.william_quest_complete:
            # Consumed without giving to William
            game_state.add_score(-25, "Consumed William's Red Bull")
        else:
            game_state.add_score(30, "Ultra Focus")
            
        game_state.advance_time(2)


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
            consumable=False
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


class Sticky(Item):
    """Sticky note with password hint"""
    
    def __init__(self, location="karen_office"):
        super().__init__(
            'sticky_note',
            'Sticky Note',
            'A yellow sticky note with handwriting.',
            location,
            takeable=True,
            consumable=False
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


def init_items():
    """Initialize all game items"""
    items = {}
    
    # Create coffee (multiple can be taken from break room)
    items['coffee'] = Coffee('break_room')
    
    # Red Bull
    items['redbull'] = RedBull('break_room')
    
    # Donut
    items['donut'] = Donut('manager_office')
    
    # Methodology sheet
    items['methodology'] = Methodology('it_office')
    
    # Sticky note
    items['sticky_note'] = Sticky('karen_office')
    
    # Add more items as needed
    
    return items
