"""
Location definitions for Game 1
Each location has a name, description, and connections to other locations
"""


class Location:
    """Represents a location in the game"""

    def __init__(self, id, name, description, exits=None, item_descriptions=None, objects=None):
        self.id = id
        self.name = name
        self.description = description
        self.exits = exits or {}
        self.item_descriptions = item_descriptions or {}
        self.objects = objects or {}  # Dictionary of examinable/interactable objects

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

    def get_object(self, object_name):
        """Get an object by name (case-insensitive partial match)"""
        object_name_lower = object_name.lower()
        for obj_key, obj_data in self.objects.items():
            # Check if any of the object's keywords match
            if object_name_lower in obj_key.lower():
                return obj_data
            # Also check aliases if they exist
            if 'aliases' in obj_data:
                for alias in obj_data['aliases']:
                    if object_name_lower in alias.lower():
                        return obj_data
        return None


def init_locations():
    """Initialize all game locations"""
    locations = {}
    
    # IT Office
    locations['it_office'] = Location(
        'it_office',
        'IT SUPPORT OFFICE',
        "Your new office space. A desk with a computer, a phone, and a stack of " \
        "documentation. The walls are covered with network diagrams and old CompTIA " \
        "certification posters. A reinforced door on the east wall leads to the server room.",
        item_descriptions={
            'methodology': "A laminated CompTIA Methodology Sheet is pinned to the cubicle wall.",
            'coffee_it_office': "There's a fresh cup of coffee on your desk, still steaming.",
            'laptop': "A sealed laptop box sits on the corner of your desk - looks like a recent delivery."
        },
        objects={
            'desk': {
                'examine': "A standard IT department desk. It has some scratches and coffee stains, " \
                          "showing years of use. Your computer sits on top.",
                'take': "The desk is bolted to the floor. Plus, where would you even put it?",
                'aliases': ['table']
            },
            'phone': {
                'examine': "A standard office phone with multiple lines. The message light isn't blinking.",
                'take': "You need to leave the phone here in case someone calls.",
                'aliases': ['telephone']
            },
            'documentation': {
                'examine': "Stacks of technical manuals, network diagrams, and reference guides. " \
                          "Most look like they haven't been touched in months.",
                'take': "There's too much to carry, and most of it looks outdated anyway.",
                'read': "You flip through some of the manuals. They're mostly outdated guides for " \
                        "Windows XP and Server 2003. Not very useful for your current problem.",
                'aliases': ['manuals', 'papers', 'guides', 'stack']
            },
            'network diagrams': {
                'examine': "Large posters showing the office network topology. Looks like a standard " \
                          "setup with switches, routers, and a server room.",
                'take': "They're pinned to the wall and you don't need them right now.",
                'aliases': ['diagrams', 'poster', 'posters', 'wall']
            },
            'coffee maker': {
                'examine': "An old coffee maker in the corner. It's empty and could use a cleaning.",
                'take': "The coffee maker stays here. You'd need to go to the break room for coffee.",
                'aliases': ['coffeemaker', 'maker']
            }
        }
    )
    
    # Hallway
    locations['hallway'] = Location(
        'hallway',
        'MAIN HALLWAY',
        "A long corridor connecting various offices. Fluorescent lights hum overhead. " \
        "You can see the Help Desk to the south, Accounting to the east, the Break Room " \
        "to the west, and your IT Office to the north.",
        objects={
            'lights': {
                'examine': "Standard fluorescent office lights. They hum with that familiar annoying buzz.",
                'take': "The lights are mounted in the ceiling. You'd need a ladder and a reason.",
                'aliases': ['fluorescent lights', 'light', 'ceiling']
            },
            'corridor': {
                'examine': "A typical office hallway with plain walls and industrial carpet.",
                'take': "You can't take a hallway.",
                'aliases': ['hallway', 'walls', 'carpet']
            }
        }
    )
    
    # Help Desk
    locations['help_desk'] = Location(
        'help_desk',
        'HELP DESK',
        "The Help Desk area with several workstations. Ian sits at his desk, phone " \
        "headset on, looking relieved to see you. Tickets scroll across multiple monitors. " \
        "There's a persistent ringing of phones in the background. Marcus's office is to the west.",
        item_descriptions={
            'coffee_help_desk': "Ian has a cup of coffee on his desk."
        },
        objects={
            'workstations': {
                'examine': "Several cubicles with computers, phones, and headsets. Most are occupied " \
                          "by Help Desk staff fielding calls.",
                'take': "The workstations are occupied and belong to the Help Desk team.",
                'aliases': ['workstation', 'cubicles', 'cubicle', 'desks']
            },
            'monitors': {
                'examine': "Multiple monitors display a ticket queue system. You can see various " \
                          "support tickets scrolling by - password resets, printer issues, the usual.",
                'take': "The monitors are mounted to the desks and actively in use.",
                'aliases': ['monitor', 'screens', 'screen']
            },
            'phones': {
                'examine': "Help Desk phones ring constantly. The sound of people troubleshooting " \
                          "computer issues fills the air.",
                'take': "The phones need to stay at the Help Desk.",
                'aliases': ['phone']
            }
        }
    )
    
    # Accounting
    locations['accounting'] = Location(
        'accounting',
        'ACCOUNTING DEPARTMENT',
        "A quiet office space filled with cubicles. Financial spreadsheets glow on " \
        "various monitors. You can hear the gentle clicking of keyboards and occasional " \
        "frustrated sighs. A reception desk sits near the entrance. Karen's office is to the north. " \
        "There's an exit door to the south leading outside.",
        objects={
            'cubicles': {
                'examine': "Rows of accounting cubicles. Most are occupied by people working intently " \
                          "on spreadsheets. Karen's office is in the back.",
                'take': "The cubicles are part of the office furniture and occupied.",
                'aliases': ['cubicle']
            },
            'spreadsheets': {
                'examine': "You can see various financial spreadsheets on the monitors - budgets, " \
                          "expense reports, and profit/loss statements.",
                'take': "Those are on other people's computers. You'd need to talk to them first.",
                'aliases': ['spreadsheet', 'monitors', 'monitor', 'screens']
            },
            'keyboards': {
                'examine': "The sound of typing fills the air. Accountants at work.",
                'take': "Those keyboards belong to the accounting staff.",
                'aliases': ['keyboard']
            },
            'reception desk': {
                'examine': "A simple wooden desk with a phone, some filing trays, and a small plant. " \
                          "Nobody's sitting here at the moment. There's a sign-in sheet for visitors.",
                'take': "The desk is part of the office furniture.",
                'aliases': ['desk', 'reception']
            },
            'exit door': {
                'examine': "A glass door leading outside to the parking lot. You can see daylight and " \
                          "freedom beyond it. The door is unlocked.",
                'take': "You can't take a door.",
                'aliases': ['door', 'exit', 'outside door']
            }
        }
    )
    
    # Karen's Office
    locations['karen_office'] = Location(
        'karen_office',
        "KAREN'S OFFICE",
        "A small office with filing cabinets, a desk covered in papers, and a computer. " \
        "Karen sits at her desk, looking frustrated. A network printer sits by the window. " \
        "A clock on the wall reminds everyone of approaching deadlines.",
        item_descriptions={
            'sticky_note': "A yellow sticky note is attached to the edge of her monitor."
        },
        objects={
            'filing cabinets': {
                'examine': "Tall metal filing cabinets labeled with fiscal years and account categories.",
                'take': "Those filing cabinets are way too heavy and full of important documents.",
                'aliases': ['filing cabinet', 'cabinets', 'cabinet', 'files']
            },
            'desk': {
                'examine': "Karen's desk is covered with papers, printouts, and sticky notes. " \
                          "Her computer sits in the center with a document open on screen.",
                'take': "You can't take Karen's desk.",
                'aliases': ['table']
            },
            'papers': {
                'examine': "Various financial documents, reports, and printouts scattered across the desk. " \
                          "Looks like she's working on quarterly reports and trying to print them.",
                'take': "Those are Karen's work documents. You shouldn't take them.",
                'aliases': ['documents', 'printouts', 'reports']
            },
            'clock': {
                'examine': "A wall clock showing the time ticking away. Karen keeps glancing at it nervously.",
                'take': "The clock is mounted on the wall and you have no reason to take it.",
                'aliases': ['wall clock']
            },
            'printer': {
                'examine': "An HP LaserJet network printer sitting by the window. Power light is on, paper loaded. " \
                          "It looks ready to print, but Karen's computer can't find it.",
                'take': "The printer is way too large and heavy to carry around.",
                'aliases': ['network printer', 'hp', 'laserjet']
            },
            'computer': {
                'examine': "Karen's desktop computer. The screen shows a document open, but the print " \
                          "dialog says 'No printers found.'",
                'take': "You can't take Karen's computer.",
                'aliases': ['screen', 'monitor', 'pc']
            }
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
            'coffee_break_room': "The coffee maker has a fresh pot brewing, the aroma filling the room.",
            'coffee_mystery': "There's an old cup of coffee on one of the tables. It's... unclear how old it is."
        },
        objects={
            'refrigerator': {
                'examine': "A standard office refrigerator. Inside you can see various lunches, " \
                          "drinks, and condiments. Someone's lunch is labeled 'DO NOT TOUCH'.",
                'take': "The refrigerator is plugged in and full of people's food. You can't take it.",
                'aliases': ['fridge', 'icebox']
            },
            'microwave': {
                'examine': "A well-used microwave with some dubious stains inside. There's a sign " \
                          "that says 'Please cover your food'.",
                'take': "The microwave is mounted above the counter and plugged in.",
                'aliases': []
            },
            'tables': {
                'examine': "Several break room tables with mismatched chairs. Some have old magazines " \
                          "and yesterday's newspaper.",
                'take': "The tables are break room furniture. Leave them here.",
                'aliases': ['table', 'chairs', 'chair', 'furniture']
            },
            'vending machine': {
                'examine': "A humming vending machine stocked with snacks and drinks. Chips, candy bars, " \
                          "and energy drinks are visible behind the glass. You can see a Sugar-Free Red Bull " \
                          "in slot D4 ($2.00). It takes bills and coins.",
                'take': "The vending machine is bolted to the floor and extremely heavy.",
                'use': "vending_machine_interaction",  # Special flag for custom interaction
                'aliases': ['vending', 'machine']
            },
            'magazines': {
                'examine': "Old copies of People magazine and Tech Weekly from several months ago.",
                'take': "They're outdated and dog-eared. Not worth taking.",
                'read': "You flip through the magazines. Celebrity gossip from three months ago and " \
                        "tech articles about products that have already been discontinued. Riveting stuff.",
                'aliases': ['magazine', 'newspaper', 'papers']
            }
        }
    )
    
    # Server Room
    locations['server_room'] = Location(
        'server_room',
        'SERVER ROOM',
        "A cold, climate-controlled room filled with racks of humming servers. Blinking " \
        "LEDs cast an eerie glow. The authentication server is here, along with the file " \
        "servers and network equipment. A wall-mounted monitor displays system stats.",
        item_descriptions={
            'coffee_server_room': "There's an ancient, crusty coffee mug on top of a server rack. " \
                                 "It might be a biological hazard."
        },
        objects={
            'servers': {
                'examine': "Rows of rack-mounted servers. You can identify the authentication server, " \
                          "file servers, and database servers by their labels. All show green status lights.",
                'take': "The servers are mounted in racks and critical to company operations. Don't touch.",
                'aliases': ['server', 'racks', 'rack', 'authentication server', 'file servers']
            },
            'LEDs': {
                'examine': "Countless blinking status lights - mostly green with a few amber warnings. " \
                          "The pattern is almost hypnotic.",
                'take': "The LEDs are part of the server equipment.",
                'aliases': ['lights', 'status lights']
            },
            'network equipment': {
                'examine': "Switches, routers, and patch panels with countless cables running between them. " \
                          "Everything appears to be functioning normally.",
                'take': "The network equipment is vital infrastructure. Leave it alone.",
                'aliases': ['switches', 'routers', 'cables', 'equipment']
            },
            'monitor': {
                'examine': "A wall-mounted display showing system statistics, CPU usage, memory, and " \
                          "network traffic. Everything looks normal.",
                'take': "The monitor is mounted to the wall and displaying important system info.",
                'aliases': ['display', 'screen', 'system stats']
            }
        }
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
        },
        objects={
            'posters': {
                'examine': "Motivational posters with slogans like 'Excellence in IT' and " \
                          "'Customer Satisfaction is Our Priority'. Typical manager decor.",
                'take': "The posters are Marcus's office decorations. Leave them on the wall.",
                'read': "You read the motivational slogans: 'Excellence in IT', 'Customer Satisfaction " \
                        "is Our Priority', 'Teamwork Makes the Dream Work'. Standard corporate inspiration.",
                'aliases': ['poster', 'motivational posters']
            },
            'desk': {
                'examine': "A clean, organized desk with a computer, some project folders, and " \
                          "a family photo. Much neater than most IT desks.",
                'take': "That's Marcus's desk. You can't take it.",
                'aliases': ['table']
            },
            'computer': {
                'examine': "Marcus's workstation is locked. You can see some project management " \
                          "software in the background.",
                'take': "That's Marcus's computer. You shouldn't touch it.",
                'aliases': ['workstation', 'pc']
            },
            'folders': {
                'examine': "Project folders labeled with various IT initiatives - 'Network Upgrade Q3', " \
                          "'Security Audit', 'Help Desk Optimization'.",
                'take': "Those are Marcus's project files. You shouldn't take them.",
                'aliases': ['project folders', 'folder', 'files']
            },
            'photo': {
                'examine': "A framed photo of Marcus with his wife and two kids at what looks like " \
                          "a beach vacation. They all look happy.",
                'take': "That's Marcus's personal family photo. Leave it on his desk.",
                'aliases': ['family photo', 'picture', 'frame']
            }
        }
    )
    
    # Connect locations
    # IT Office
    locations['it_office'].exits = {
        'south': 'hallway',
        's': 'hallway',
        'east': 'server_room',
        'e': 'server_room',
        'hallway': 'hallway',
        'server': 'server_room',
        'servers': 'server_room'
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
        'west': 'manager_office',
        'w': 'manager_office',
        'hallway': 'hallway',
        'manager': 'manager_office',
        'marcus': 'manager_office'
    }
    
    # Accounting
    locations['accounting'].exits = {
        'west': 'hallway',
        'w': 'hallway',
        'north': 'karen_office',
        'n': 'karen_office',
        'south': 'outside_exit',  # Special exit that triggers ending
        's': 'outside_exit',
        'karen': 'karen_office',
        'office': 'karen_office',
        'hallway': 'hallway',
        'exit': 'outside_exit',
        'outside': 'outside_exit'
    }
    
    # Karen's Office
    locations['karen_office'].exits = {
        'south': 'accounting',
        's': 'accounting',
        'accounting': 'accounting',
        'out': 'accounting'
    }
    
    # Break Room
    locations['break_room'].exits = {
        'east': 'hallway',
        'e': 'hallway',
        'hallway': 'hallway'
    }
    
    # Server Room
    locations['server_room'].exits = {
        'west': 'it_office',
        'w': 'it_office',
        'out': 'it_office',
        'it': 'it_office',
        'office': 'it_office'
    }
    
    # Manager Office
    locations['manager_office'].exits = {
        'east': 'help_desk',
        'e': 'help_desk',
        'out': 'help_desk',
        'help': 'help_desk'
    }
    
    return locations
