# Downtime: Game 1 - Karen's Printing Problem

A text-based adventure game teaching the CompTIA troubleshooting methodology through an interactive help desk scenario.

## Story

It's your first day as an IT Support Technician. You've been assigned a seemingly simple ticket: a user can't print. But as with all good IT mysteries, the solution lies in the details. 

Use the CompTIA 7-step troubleshooting methodology to solve the problem before Karen's 10 AM client meeting!

## Features

- **7-Step Troubleshooting Methodology**: Learn and apply the industry-standard CompTIA process
- **Coffee & Focus System**: Caffeine affects your ability to spot subtle details
- **Side Quests**: Complete William's quest for bonus wisdom and points
- **Multiple NPCs**: Talk to Ian (Help Desk), Karen (the user), Marcus (your manager), and William (retired IT director)
- **Desktop Computer**: Track your progress and document findings
- **Multiple Endings**: Your choices and efficiency determine your final rank
- **Scoring System**: Earn up to 1000 points through methodology, investigation, and efficiency

## Installation

### Requirements
- Python 3.6 or higher
- No external dependencies required (uses only Python standard library)

### Setup
1. Ensure all game files are in the same directory:
   - `game1_main.py` - Main game file
   - `game_state.py` - Game state management
   - `locations.py` - Room/location definitions
   - `items.py` - Item system (coffee, donuts, etc.)
   - `npcs.py` - NPC dialogue trees
   - `desktop.py` - Desktop computer menu system
   - `utils.py` - Utility functions

2. Make the main file executable (Linux/Mac):
   ```bash
   chmod +x game1_main.py
   ```

## How to Play

### Starting the Game

**Linux/Mac:**
```bash
./game1_main.py
```

**or**

```bash
python3 game1_main.py
```

**Windows:**
```cmd
python game1_main.py
```

### Basic Commands

**Movement:**
- `go [direction]` - Move in a direction (north, south, east, west)
- `[direction]` - Shortcut (e.g., just type 'north' or 'n')

**Interaction:**
- `talk [person]` - Talk to an NPC (e.g., 'talk karen', 'talk william')
- `take [item]` - Pick up an item
- `use [item]` - Use an item from your inventory
- `examine [thing]` - Look at something closely
- `look` - Look around your current location

**Inventory:**
- `inventory` or `i` - Show what you're carrying

**Special:**
- `computer` - Use desktop computer (IT Office only)
- `help` or `?` - Show help
- `quit` or `q` - Quit game

### Tips for Success

1. **Talk to everyone** - NPCs provide crucial information
2. **Drink coffee strategically** - 2 coffees = optimal focus for spotting details
3. **Watch the user** - Observe what they DO, not what they SAY
4. **Use the desktop** - Track your progress through the methodology
5. **Manage your time** - You have until 10:00 AM (60 minutes)
6. **Complete side quests** - They provide valuable bonuses and wisdom

### The 7-Step Methodology

This game teaches the CompTIA troubleshooting process:

1. **Identify the Problem** - Gather information and understand symptoms
2. **Establish a Theory** - Determine the probable cause
3. **Test the Theory** - Verify your hypothesis
4. **Establish a Plan** - Create an implementation strategy
5. **Implement the Solution** - Apply the fix
6. **Verify Functionality** - Ensure everything works
7. **Document Findings** - Record the problem and solution

## Locations

- **IT Office** - Your workspace with a computer
- **Hallway** - Central corridor connecting all areas
- **Help Desk** - Where Ian works
- **Accounting** - Department where Karen works
- **Karen's Office** - The user's workspace
- **Break Room** - Coffee and... William
- **Manager's Office** - Marcus's office

## NPCs

- **Ian (Help Desk)** - Escalated the ticket to you, can provide context
- **Karen (Accounting)** - The user with the printing problem
- **Marcus (Manager)** - Your boss, tracks your progress
- **William (Retired IT Director)** - Offers wisdom in exchange for a favor

## Items

- **Coffee** - Increases focus (+10 observation bonus at 2-3 cups)
- **Red Bull** - Maximum focus, but part of William's quest
- **Methodology Sheet** - Reference for the 7-step process
- **Donut** - Marcus's donut (optional heist)

## Scoring

- **Core Methodology**: 400 points (7 steps × varying points)
- **Bonus Points**: Up to 600 points
  - Side quests (William, Donut)
  - Information gathering
  - Methodology excellence
  - Coffee optimization
  - Efficiency bonuses

**Ranks:**
- 950+: Master Troubleshooter
- 850+: Expert Technician
- 750+: Skilled Professional
- 650+: Competent Support
- 500+: Adequate Performance
- Below: Needs Improvement

## The Problem (No Spoilers!)

Karen can't print. Her computer says "No printers found." The printer hardware is fine. The network seems fine. She can access the internet. So what's the problem?

Use your observation skills, talk to people, and follow the methodology to find out!

(Hint: Coffee helps you notice details...)

## Educational Value

This game teaches:
- CompTIA A+ troubleshooting methodology
- User interaction skills
- Problem investigation techniques
- Documentation practices
- Time management under pressure
- The importance of observation
- Why watching users is better than listening to descriptions

## Credits

Designed as an interactive training tool for help desk technicians and IT support professionals.

## License

Educational use permitted. Created for IT training purposes.

---

**Have fun troubleshooting!** 

Remember: The truth is in the details. 😊
