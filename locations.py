"""
Location definitions for Game 1
Each location has a name, description, and connections to other locations
"""


class Location:
    """Represents a location in the game"""

    def __init__(self, id, name, description, exits=None, item_descriptions=None):
        self.id = id
        self.name = name
        self.description = description
        self.exits = exits or {}
        self.item_descriptions = item_descriptions or {}

    def add_exit(self, direction, destination):
        """Add an exit to another location"""
        self.exits[direction] = destination

    def get_full_description(self, items_present):
        """Get description with items naturally integrated"""
        desc = self.description

        # Add item-specific descriptions for items that are present
        for item_id in items_present:
            if item_id in self.item_descriptions:
                desc += " " + self.item_descriptions[item_id]

        return desc


def init_locations():
    """Initialize all game locations"""
    locations = {}
    
    # IT Office
    locations['it_office'] = Location(
        'it_office',
        'IT SUPPORT OFFICE',
        "Your new office space. A desk with a computer, a phone, and a stack of " \
        "documentation. The walls are covered with network diagrams and old CompTIA " \
        "certification posters. There's a coffee maker in the corner (currently empty).",
        item_descriptions={
            'methodology': "A laminated CompTIA Methodology Sheet is pinned to the cubicle wall."
        }
    )
    
    # Hallway
    locations['hallway'] = Location(
        'hallway',
        'MAIN HALLWAY',
        "A long corridor connecting various offices. Fluorescent lights hum overhead. " \
        "You can see the Help Desk to the south, Accounting to the east, the Break Room " \
        "to the west, and your IT Office to the north."
    )
    
    # Help Desk
    locations['help_desk'] = Location(
        'help_desk',
        'HELP DESK',
        "The Help Desk area with several workstations. Ian sits at his desk, phone " \
        "headset on, looking relieved to see you. Tickets scroll across multiple monitors. " \
        "There's a persistent ringing of phones in the background."
    )
    
    # Accounting
    locations['accounting'] = Location(
        'accounting',
        'ACCOUNTING DEPARTMENT',
        "A quiet office space filled with cubicles. Financial spreadsheets glow on " \
        "various monitors. You can hear the gentle clicking of keyboards and occasional " \
        "frustrated sighs."
    )
    
    # Karen's Office
    locations['karen_office'] = Location(
        'karen_office',
        "KAREN'S OFFICE",
        "A small office with filing cabinets, a desk covered in papers, and a computer " \
        "displaying a login screen. Karen sits at her desk, looking stressed. A clock " \
        "on the wall reminds everyone of approaching deadlines.",
        item_descriptions={
            'sticky_note': "A yellow sticky note is attached to the edge of her monitor."
        }
    )
    
    # Break Room
    locations['break_room'] = Location(
        'break_room',
        'BREAK ROOM',
        "A small kitchen area with a refrigerator, microwave, and coffee maker. Several " \
        "tables with mismatched chairs are scattered around. A vending machine hums in " \
        "the corner.",
        item_descriptions={
            'coffee': "The coffee maker is full and fresh, the aroma filling the room.",
            'redbull': "In the fridge, you can see a Sugar-Free Red Bull with a sticky note on it."
        }
    )
    
    # Server Room
    locations['server_room'] = Location(
        'server_room',
        'SERVER ROOM',
        "A cold, climate-controlled room filled with racks of humming servers. Blinking " \
        "LEDs cast an eerie glow. The authentication server is here, along with the file " \
        "servers and network equipment. A wall-mounted monitor displays system stats."
    )
    
    # Manager's Office
    locations['manager_office'] = Location(
        'manager_office',
        "MARCUS'S OFFICE",
        "Manager Marcus's office. Neat and organized, with motivational posters about " \
        "IT excellence and customer service. His desk has a computer, several project " \
        "folders, and a photo of his family.",
        item_descriptions={
            'donut': "On the desk sits a tempting chocolate donut with rainbow sprinkles and a note."
        }
    )
    
    # Connect locations
    # IT Office
    locations['it_office'].exits = {
        'south': 'hallway',
        's': 'hallway',
        'hallway': 'hallway'
    }
    
    # Hallway
    locations['hallway'].exits = {
        'north': 'it_office',
        'n': 'it_office',
        'south': 'help_desk',
        's': 'help_desk',
        'east': 'accounting',
        'e': 'accounting',
        'west': 'break_room',
        'w': 'break_room',
        'it': 'it_office',
        'help': 'help_desk',
        'accounting': 'accounting',
        'break': 'break_room'
    }
    
    # Help Desk
    locations['help_desk'].exits = {
        'north': 'hallway',
        'n': 'hallway',
        'hallway': 'hallway'
    }
    
    # Accounting
    locations['accounting'].exits = {
        'west': 'hallway',
        'w': 'hallway',
        'karen': 'karen_office',
        'hallway': 'hallway'
    }
    
    # Karen's Office
    locations['karen_office'].exits = {
        'accounting': 'accounting',
        'out': 'accounting'
    }
    
    # Break Room
    locations['break_room'].exits = {
        'east': 'hallway',
        'e': 'hallway',
        'hallway': 'hallway'
    }
    
    # Server Room (accessed from hallway in later implementations)
    locations['server_room'].exits = {
        'out': 'hallway',
        'hallway': 'hallway'
    }
    
    # Manager Office
    locations['manager_office'].exits = {
        'out': 'hallway',
        'hallway': 'hallway'
    }
    
    return locations
