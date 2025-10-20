# Coffee & Focus Buff System - Visual Flowchart

## System Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                    COFFEE SYSTEM FLOW                           │
│                                                                 │
│  Player can drink from 5 coffee sources + 1 Red Bull           │
│  Maximum: 6 coffees = DEATH                                    │
│  Optimal: 2 coffees = Focus Buff Unlocked                      │
└─────────────────────────────────────────────────────────────────┘
```

---

## Coffee Level Progression

```
START: 0 Coffees
    │
    ├──> Base State (No Focus)
    │    • Standard observation
    │    • Will miss subtle details
    │    • No special bonuses
    │    • Cannot spot Caps Lock easily
    │
    ▼
DRINK COFFEE #1
    │
    ├──> 1 Coffee (Insufficient)
    │    • Slight alertness
    │    • No focus buff yet
    │    • +5 points
    │    Message: "Ahh, that hits the spot. You feel slightly more alert."
    │
    ▼
DRINK COFFEE #2
    │
    ├──> 2 Coffees (✓ OPTIMAL - FOCUS UNLOCKED)
    │    • ✓ Enhanced observation
    │    • ✓ Can spot Caps Lock clearly
    │    • ✓ Enhanced perception
    │    • +30 points
    │    Message: "Your mind feels sharper. You're focused and ready."
    │             "✓ FOCUS BUFF ACTIVATED"
    │             "You'll notice more details now."
    │
    ▼
DRINK COFFEE #3
    │
    ├──> 3 Coffees (Wired but focused)
    │    • Focus remains active ✓
    │    • Heart beating faster
    │    • No point penalties
    │    Message: "You're feeling pretty wired, but still focused."
    │             "Your heart is beating a bit faster."
    │
    ▼
DRINK COFFEE #4
    │
    ├──> 4 Coffees (Jittery)
    │    • Focus still active ✓
    │    • Hands trembling
    │    • No point penalties
    │    Message: "You're feeling uncomfortably wired."
    │             "Your hands have a slight tremor."
    │
    ▼
DRINK COFFEE #5
    │
    ├──> 5 Coffees (⚠ WARNING)
    │    • Focus still active ✓
    │    • Physical discomfort warning
    │    • No point penalties
    │    Message: "Okay, that's definitely too much coffee..."
    │             "You're not feeling great. Maybe that's enough."
    │             "⚠ WARNING: You're very overcaffeinated."
    │
    ▼
DRINK COFFEE #6
    │
    └──> 6 Coffees (💀 INSTANT DEATH)
         • Cardiac event
         • Game immediately exits
         • Score: 0
         • Achievement: "Heart Attack Speedrun"
         • Status: Banned from IT
```

---

## Red Bull Alternative Path

```
START: Any coffee count
    │
    ▼
DRINK RED BULL
    │
    ├──> Coffee Count +2
    │    • Grants Focus immediately
    │    • Grants Ultra Focus
    │    • William's Quest FAILS
    │    • -25 points (consumed William's Red Bull)
    │    • +30 points if quest already complete
    │
    └──> If already at 4+ coffees:
         4 coffees + Red Bull = 6 total = INSTANT DEATH 💀
         5 coffees + Red Bull = 7 total = INSTANT DEATH 💀
```

---

## Coffee Sources Map

```
┌─────────────────────────────────────────────────────────────────┐
│                      AVAILABLE COFFEE                           │
└─────────────────────────────────────────────────────────────────┘

1. IT Office (coffee_it_office)
   └─> Fresh Coffee on your desk
       Location: "There's a fresh cup of coffee on your desk, still steaming."
       Quality: ★★★★★
       Risk: None

2. Help Desk (coffee_help_desk)
   └─> Ian's Coffee
       Location: "Ian has a cup of coffee on his desk."
       Quality: ★★★★☆
       Risk: None

3. Break Room (coffee_break_room)
   └─> Fresh Pot from coffee maker
       Location: "The coffee maker has a fresh pot brewing, the aroma filling the room."
       Quality: ★★★★★
       Risk: None

4. Break Room (coffee_mystery)
   └─> Mystery Coffee (Old, unknown age)
       Location: "There's an old cup of coffee on one of the tables. It's... unclear how old it is."
       Quality: ★☆☆☆☆
       Risk: Questionable flavor

5. Server Room (coffee_server_room)
   └─> Ancient Coffee (Very old, crusty mug)
       Location: "There's an ancient, crusty coffee mug on top of a server rack. It might be a biological hazard."
       Quality: ☆☆☆☆☆
       Risk: High disgust factor

6. Break Room Vending Machine (NOT an item, requires interaction)
   └─> Red Bull (Costs $2, counts as +2 coffees)
       Command: "use vending machine"
       Quality: ★★★★☆
       Effect: Ultra Focus OR trade to William (+100 pts)
```

---

## Focus Buff Effects

```
╔═══════════════════════════════════════════════════════════════╗
║                    WITHOUT FOCUS (0-1 coffee)                 ║
╚═══════════════════════════════════════════════════════════════╝

Karen Observation:
├─> Can't spot Caps Lock easily
├─> Details blur together
└─> Miss critical evidence

Result: Difficult to complete game efficiently


╔═══════════════════════════════════════════════════════════════╗
║              WITH FOCUS (2-5 coffees) ✓ REQUIRED              ║
╚═══════════════════════════════════════════════════════════════╝

Karen Observation:
├─> ✓ Spot Caps Lock clearly (watch_karen_type)
├─> See LED indicator
└─> +25 points bonus

Result: Efficient problem solving


╔═══════════════════════════════════════════════════════════════╗
║            WITH ULTRA FOCUS (Red Bull) ✓✓ ENHANCED            ║
╚═══════════════════════════════════════════════════════════════╝

Karen Observation:
├─> ✓✓ Enhanced perception
└─> Same +25 points bonus

Trade-off:
└─> Lose William's quest (-100 pts vs drinking = -25 pts)
    Net loss compared to trading
```

---

## Coffee Count & Death Risk

```
Risk Level by Coffee Count:

┌────────┬──────────┬─────────┬──────────────────────────┐
│ Count  │  Focus   │  Risk   │       Status             │
├────────┼──────────┼─────────┼──────────────────────────┤
│   0    │    ✗     │  Safe   │ Base state               │
│   1    │    ✗     │  Safe   │ Slightly alert (+5 pts)  │
│   2    │    ✓     │  Safe   │ ✓ OPTIMAL (+30 pts)      │
│   3    │    ✓     │  Safe   │ Wired but focused        │
│   4    │    ✓     │  Safe   │ Jittery                  │
│   5    │    ✓     │ Warning │ ⚠ Very overcaffeinated   │
│   6+   │    💀    │  DEATH  │ 💀 Cardiac event         │
└────────┴──────────┴─────────┴──────────────────────────┘

Note: Red Bull adds +2 to count instantly
      4+ coffees then Red Bull = DEATH
```

---

## Detailed Message Flow

### Coffee #1 Message
```
DRINKING COFFEE
───────────────

You take a sip of the hot coffee.

Ahh, that hits the spot. You feel slightly more alert.

+5 points (First coffee)

caffeine_level = 1
```

### Coffee #2 Message (FOCUS UNLOCKED)
```
DRINKING COFFEE
───────────────

You take a sip of the hot coffee.

Your mind feels sharper. You're focused and ready.

✓ FOCUS BUFF ACTIVATED
You'll notice more details now.

+30 points (Optimal caffeine level)

has_focus_buff = True
caffeine_level = 2
```

### Coffee #3 Message
```
DRINKING COFFEE
───────────────

You take a sip of the hot coffee.

You're feeling pretty wired, but still focused.
Your heart is beating a bit faster.

caffeine_level = 3
```

### Coffee #4 Message
```
DRINKING COFFEE
───────────────

You take a sip of the hot coffee.

You're feeling uncomfortably wired.
Your hands have a slight tremor.

caffeine_level = 4
```

### Coffee #5 Message (WARNING)
```
DRINKING COFFEE
───────────────

You take a sip of the hot coffee.

Okay, that's definitely too much coffee...
You're not feeling great. Maybe that's enough.

⚠ WARNING: You're very overcaffeinated.

caffeine_level = 5
```

### Coffee #6 Message (DEATH)
```
DRINKING COFFEE
───────────────

You take a sip of the hot coffee.

(Death handler executes immediately)

───────────────
💀 CARDIAC EVENT 💀
───────────────

Your heart is racing uncontrollably.
The room is spinning.
Everything goes dark...

─────────────────────────────────────
GAME OVER: Caffeine Overdose
─────────────────────────────────────

Final Score: 0
Coffees Consumed: 6

Achievement Unlocked: 'Heart Attack Speedrun'

You have been permanently banned from the IT department.
Marcus is updating the employee handbook with a new section:
'Maximum 2 Coffees Per Incident'

Maybe moderation is important after all...

[Game exits immediately with sys.exit(0)]
```

---

## Red Bull Flow

### Red Bull Consumption (If William's Quest Active)
```
DRINKING RED BULL
─────────────────

Wait... you were supposed to give this to William!
He's going to be disappointed...

You crack open the can and chug it.
MAXIMUM CAFFEINE ACHIEVED.

✓✓ ULTRA FOCUS ACTIVATED
Your perception is heightened dramatically.
You'll spot even the tiniest details.

(But your hands are shaking from all the caffeine...)

-25 points (Consumed William's Red Bull)

redbull_consumed = True
caffeine_level += 2

IF caffeine_level >= 6:
    → INSTANT DEATH (same as coffee #6)
```

### Red Bull Trade (Correct Path)
```
> talk william
> give william red bull

William: "Ah! You found it! Thank you!"

*William cracks open the Red Bull*
*Takes a long, satisfied sip*

William: "Alright, as promised. Here's what 30 years in IT taught me:"

"Be OBSERVANT. The answer is usually right in front of you.
You just have to actually LOOK. Carefully."

"Most problems aren't as complex as you think. Start simple.
Check the basics first."

"And here's the big one: Watch what the user actually DOES,
not what they TELL you they're doing."

"People don't lie on purpose - they just don't observe themselves.
They'll say they're typing correctly, but they're not watching
their hands."

"So go WATCH that user. Don't trust their description. Watch their
hands. Watch the screen. Watch for the little things."

*Winks*

"The truth is in the details, kid."

───────────────
✓ William's Quest Complete!
───────────────

Wisdom Received:
  • Be observant and aware
  • Start with simple explanations
  • Watch what users DO, not what they SAY
  • The truth is in the details

+100 points (William's Quest Complete)

Achievement Unlocked: 'The Old Guard'
```

---

## Optimal Strategy

```
╔═══════════════════════════════════════════════════════════════╗
║                    OPTIMAL COFFEE PATH                        ║
╚═══════════════════════════════════════════════════════════════╝

Step 1: Start in IT Office
        └─> TAKE coffee (fresh on desk)
        └─> USE coffee (caffeine_level = 1, +5 pts)

Step 2: Get second coffee (any source)
        └─> TAKE coffee (break room, help desk, etc.)
        └─> USE coffee (caffeine_level = 2, +30 pts)
        └─> ✓ FOCUS UNLOCKED

Step 3: Use focus for critical observations
        └─> Watch Karen type (spot Caps Lock, +25 pts)
        └─> Solve the problem

Step 4: Get Red Bull for William (optional but recommended)
        └─> Complete donut quest to get $2
        └─> Buy Red Bull from vending machine
        └─> Give to William (+100 pts)

Step 5: DO NOT drink more coffee
        └─> Stay at caffeine_level = 2
        └─> Avoid death risk

TOTAL COFFEE: 2 (Optimal)
POINTS GAINED:
  - First coffee: +5
  - Second coffee (focus): +30
  - William's quest: +100
  - Caps Lock discovery: +25
  = +160 points minimum from coffee system
```

---

## Suboptimal Strategies

### Strategy A: Zero-One Coffee (Very Difficult)
```
✗ No focus buff
✗ Cannot easily spot Caps Lock
✗ Harder to complete efficiently

Result: Possible but challenging
```

### Strategy B: Drink Red Bull (Poor Choice)
```
✓ Grants focus immediately
✓ Grants ultra focus
✗ Loses William's quest (-100 pts opportunity)
✗ Net: -25 points

Result: Can complete game, but much worse score
```

### Strategy C: Over-caffeinate (3-5 coffees)
```
✓ Focus remains active
✓ No point penalties
✗ Uncomfortable flavor text
✗ Risk of accidentally drinking 6th = death

Result: Same as 2 coffees functionally, but risky
```

### Strategy D: Death Speedrun (6+ coffees)
```
✗ Instant game over
✗ Score: 0
✗ Must restart
✓ Humorous ending
✓ Achievement unlocked

Result: Game over, must restart
```

### Strategy E: Red Bull Death Trap (4-5 coffees + Red Bull)
```
Example: 5 coffees + Red Bull = 7 caffeine = INSTANT DEATH

✗ Immediately triggers death handler
✗ Score: 0
✗ Game exits

Result: Worst possible outcome
```

---

## Implementation Reference

### Game State Tracking
```python
# game_state.py
self.caffeine_level = 0  # 0-6+ (death at 6)
self.coffees_consumed = 0  # Track number of coffee items used
self.has_redbull = False  # Has Red Bull in inventory
self.redbull_consumed = False  # Drank the Red Bull
self.money = 0  # For vending machine ($2 required)
```

### Caffeine Level Descriptions
```python
def get_caffeine_level_name(self):
    if self.caffeine_level >= 6:
        return "CRITICAL - DANGEROUS"
    elif self.caffeine_level == 5:
        return "Very Overcaffeinated"
    elif self.redbull_consumed:
        return "Ultra Caffeinated (Red Bull)"
    elif self.caffeine_level >= 4:
        return "Jittery"
    elif self.caffeine_level >= 2:
        return "Focused (Optimal)"
    elif self.caffeine_level == 1:
        return "Awake"
    else:
        return "None"
```

### Focus Buff Check
```python
def has_focus_buff(self):
    """Check if player has beneficial focus buff"""
    return self.caffeine_level >= 2 or self.redbull_consumed
```

### Coffee Items Initialization
```python
# items.py - init_items()
items['coffee_it_office'] = Coffee('it_office')
items['coffee_help_desk'] = Coffee('help_desk')
items['coffee_break_room'] = Coffee('break_room')
items['coffee_mystery'] = Coffee('break_room')
items['coffee_server_room'] = Coffee('server_room')
# Red Bull created dynamically from vending machine
```

---

## Vending Machine Interaction

```
Player in Break Room:
> examine vending machine

"A humming vending machine stocked with snacks and drinks.
Chips, candy bars, and energy drinks are visible behind
the glass. You can see a Sugar-Free Red Bull in slot D4
($2.00). It takes bills and coins."

> use vending machine

You approach the vending machine.

The Sugar-Free Red Bull in slot D4 costs $2.00.
You only have $0.

(You need to find $2 to buy the Red Bull.)

[After getting $2 from donut quest]

> use vending machine

You approach the vending machine.

The Sugar-Free Red Bull in slot D4 costs $2.00.
You have $2.

Purchase Red Bull? (yes/no)
> yes

*You insert $2 into the machine*
*Mechanical whirring*
*THUNK*

You retrieve the cold Sugar-Free Red Bull from the slot.

Red Bull acquired!

[Red Bull now in inventory]
money = 0
has_redbull = True
```

---

## Achievement Summary

```
╔═══════════════════════════════════════════════════════════════╗
║                    COFFEE ACHIEVEMENTS                        ║
╚═══════════════════════════════════════════════════════════════╝

✓ "The Old Guard" (+100 pts)
  └─> Trade Red Bull to William
  └─> Get 30 years of IT wisdom

☠ "Heart Attack Speedrun" (0 pts)
  └─> Die from 6+ coffees
  └─> Humorous game over
  └─> Game immediately exits
```

---

## Visual Summary

```
                    COFFEE SYSTEM SUMMARY

┌──────────────────────────────────────────────────────────┐
│                                                          │
│  REQUIRED: 2 coffees (Focus Buff)                        │
│  OPTIMAL:  2 coffees (+30 points)                       │
│  WARNING:  5 coffees (physical discomfort warning)      │
│  DEATH:    6+ coffees (instant game over, sys.exit)     │
│                                                          │
│  RED BULL: Counts as +2 coffees, ultra focus             │
│            Trade to William = +100 pts (BEST choice)     │
│            Drink yourself = -25 pts (BAD choice)         │
│                                                          │
│  NO PENALTIES: Levels 3-5 have no point loss             │
│  DEATH IS INSTANT: Game exits immediately at 6+          │
│  DISCOVERY: Player learns through experimentation       │
│                                                          │
└──────────────────────────────────────────────────────────┘

                         THE END
```

---

**Last Updated:** 2025-01-19
**System Status:** Implemented and Verified
**Total Coffee Sources:** 5 individual coffees
**Red Bull:** +2 caffeine, obtained from vending machine
**Death Trigger:** caffeine_level >= 6
**Optimal Play:** 2 coffees for focus, trade Red Bull to William
**Maximum Safe Caffeine:** 5 (warning given)
