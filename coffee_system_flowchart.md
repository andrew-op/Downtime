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
    │    • Hallway note invisible
    │
    ▼
DRINK COFFEE #1
    │
    ├──> 1 Coffee (Insufficient)
    │    • Slight alertness
    │    • No focus buff yet
    │    • No bonuses
    │    Message: "You feel slightly more alert."
    │
    ▼
DRINK COFFEE #2
    │
    ├──> 2 Coffees (✓ OPTIMAL - FOCUS UNLOCKED)
    │    • ✓ Enhanced observation
    │    • ✓ Can spot Caps Lock clearly
    │    • ✓ Enhanced auth logs
    │    • ✓ Hallway note visible
    │    • +30 points
    │    • Achievement: "Properly Caffeinated"
    │    Message: "Focus ability unlocked!"
    │
    ▼
DRINK COFFEE #3
    │
    ├──> 3 Coffees (Over-caffeinated)
    │    • Focus remains active
    │    • Hands slightly shaky (flavor text)
    │    • Minor anxious thoughts
    │    • No point penalties
    │    Message: "Your heart is beating faster."
    │
    ▼
DRINK COFFEE #4
    │
    ├──> 4 Coffees (Very Jittery)
    │    • Focus still active
    │    • Strong impulse to act
    │    • Overthinking flavor text
    │    • No point penalties
    │    Message: "You're feeling uncomfortably wired."
    │
    ▼
DRINK COFFEE #5
    │
    ├──> 5 Coffees (⚠ VAGUE WARNING)
    │    • Focus still active
    │    • Physical discomfort
    │    • ⚠ Subtle warning (not explicit about death)
    │    • No point penalties
    │    Message: "You're not feeling great. Maybe that's enough."
    │
    ▼
DRINK COFFEE #6
    │
    └──> 6 Coffees (💀 INSTANT DEATH)
         • Cardiac event
         • Humorous game over
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
    │    • Immediately grants Focus
    │    • Grants Super Focus bonus
    │    • +15 points (super focus)
    │    • William's Quest FAILS (-100 pts)
    │    • Net loss: -85 points
    │    
    └──> If already at 4+ coffees:
         Risk of reaching 6 total = DEATH
```

---

## Coffee Sources Map

```
┌─────────────────────────────────────────────────────────────────┐
│                      AVAILABLE COFFEE                           │
└─────────────────────────────────────────────────────────────────┘

1. IT Office
   └─> Fresh Coffee (Best choice, optimal)
       Quality: ★★★★★
       Risk: None

2. Help Desk  
   └─> Ian's Coffee (Offered during conversation)
       Quality: ★★★★☆
       Risk: None

3. Break Room
   └─> Fresh Pot (Backup source)
       Quality: ★★★★★
       Risk: None

4. Break Room
   └─> Mystery Coffee (Old, unknown age)
       Quality: ★☆☆☆☆
       Risk: Questionable
       Flavor: "This tastes... interesting."

5. Server Room
   └─> Ancient Coffee (Very old, crusty mug)
       Quality: ☆☆☆☆☆
       Risk: High disgust factor
       Flavor: "This might be a biological hazard."

6. Break Room Vending Machine
   └─> Red Bull (Costs $2, counts as 2 coffees)
       Quality: ★★★★☆
       Effect: Super Focus OR trade to William
```

---

## Focus Buff Effects

```
╔═══════════════════════════════════════════════════════════════╗
║                    WITHOUT FOCUS (0-1 coffee)                 ║
╚═══════════════════════════════════════════════════════════════╝

Authentication Logs:
├─> Basic view only
├─> Pattern not obvious
└─> No highlighting

Karen Observation:
├─> Can't spot Caps Lock
├─> Details blur together
└─> Miss critical evidence

Hallway Trash:
├─> Note invisible
└─> Just see generic trash

Result: Cannot efficiently complete game


╔═══════════════════════════════════════════════════════════════╗
║              WITH FOCUS (2-5 coffees) ✓ REQUIRED              ║
╚═══════════════════════════════════════════════════════════════╝

Authentication Logs:
├─> Enhanced view
├─> Pattern highlighted
├─> Case change obvious
└─> +10 points bonus

Karen Observation:
├─> ✓ Spot Caps Lock clearly
├─> See LED indicator
├─> Notice finger slip
└─> +25 points bonus

Hallway Trash:
├─> Note becomes visible
├─> Can take methodology reminder
└─> +25 points bonus

Result: Efficient problem solving


╔═══════════════════════════════════════════════════════════════╗
║            WITH SUPER FOCUS (Red Bull) ✓✓ ENHANCED            ║
╚═══════════════════════════════════════════════════════════════╝

Authentication Logs:
├─> Ultra enhanced view
├─> Timestamp analysis
├─> Probability assessment
└─> +15 points bonus (instead of +10)

Karen Observation:
├─> ✓✓ Instant recognition
├─> Frame-by-frame mental replay
└─> Same +25 points bonus

Hallway Trash:
├─> Same as regular focus
└─> Same +25 points bonus

Trade-off:
└─> Lose William's quest (-100 pts)
    Total net: -85 points (bad trade)
```

---

## Coffee Count & Death Risk

```
Risk Level by Coffee Count:

┌────────┬──────────┬─────────┬──────────────────────────┐
│ Count  │  Focus   │  Risk   │       Status             │
├────────┼──────────┼─────────┼──────────────────────────┤
│   0    │    ✗     │  Safe   │ Base state               │
│   1    │    ✗     │  Safe   │ Insufficient             │
│   2    │    ✓     │  Safe   │ ✓ OPTIMAL                │
│   3    │    ✓     │  Safe   │ Over-caffeinated         │
│   4    │    ✓     │  Safe   │ Very jittery             │
│   5    │    ✓     │ Warning │ ⚠ Vague discomfort       │
│   6    │    💀    │  DEATH  │ 💀 Cardiac event         │
└────────┴──────────┴─────────┴──────────────────────────┘

Note: Red Bull adds +2 to count instantly
```

---

## Detailed Message Flow

### Coffee #1 Message
```
You drink the coffee. 

It's warm and pleasant. You feel slightly more alert.

(No special effects yet.)

coffee_count = 1
```

### Coffee #2 Message (FOCUS UNLOCKED)
```
You drink the coffee. 

Warmth spreads through you. Your mind sharpens considerably.
Colors seem slightly brighter. Details stand out more clearly.

Focus ability unlocked!

+30 points
has_focus_buff = True
coffee_count = 2

Achievement Unlocked: "Properly Caffeinated"
```

### Coffee #3 Message
```
That might have been one coffee too many.
Your heart is beating a little faster.
Your hands feel slightly jittery.

(You still have your focus, but you're feeling wired.)

coffee_count = 3
```

### Coffee #4 Message
```
You're definitely feeling jittery now.
Your leg won't stop bouncing.
Every little thing seems like it could be critical.

(Focus remains, but you're uncomfortably caffeinated.)

coffee_count = 4
```

### Coffee #5 Message (VAGUE WARNING)
```
Your heart is racing now.
You're sweating despite the air conditioning.
This might not have been a good idea.

You don't feel great. Maybe that's enough coffee for today?

(A small voice in your head suggests stopping.)

coffee_count = 5

⚠ Warning given, but not explicit about death
```

### Coffee #6 Message (DEATH)
```
You drink another cup of coffee.

This was a mistake.

For a moment, nothing happens.

Then your heart starts racing. Really racing.

*THUMP* *THUMP* *THUMP* *THUMP* *THUMP*

The room spins. Your vision blurs at the edges.
You feel dizzy. Very dizzy.

Your chest tightens.

Everything goes dark.

═══════════════════════════════════════════════

You wake up in the break room.

William is standing over you with a phone.
Paramedics are on their way.

William: "Six cups of coffee in twenty minutes? What were you 
thinking, kid? Your body can't handle that."

═══════════════════════════════════════════════

╔═══════════════════════════════════════════════╗
║         GAME OVER: CAFFEINE OVERDOSE          ║
║                                               ║
║ You drank 6 cups of coffee in 20 minutes.    ║
║ Your cardiovascular system objected.          ║
║                                               ║
║ Karen still can't log in.                     ║
║ But hey, the paramedics are really nice!      ║
║                                               ║
║ You survive, but you're banned from IT.       ║
║ HR assigns you to manage the company's        ║
║ new "Employee Wellness Initiative."           ║
║                                               ║
║ The irony is not lost on anyone.              ║
║                                               ║
║ Achievement Unlocked: "Heart Attack Speedrun" ║
╚═══════════════════════════════════════════════╝

Final Score: 0
Rank: Cardiac Patient
Status: Banned from IT Department

[GAME OVER]
[Press any key to restart]
```

---

## Red Bull Flow

### Red Bull Consumption
```
You crack open the sugar-free Red Bull.

*gulp* *gulp* *gulp*

Whoa.

Your pupils dilate. Colors seem brighter. Sounds sharper.
Everything is in ULTRA FOCUS now.

This is like drinking two coffees at once.

But...

William is watching from across the break room.

William: *shakes head* "That was supposed to be for me, kid. 
Ah well... guess you needed it more." *sighs* 
*goes back to newspaper*

[William's quest failed - no wisdom bonus for you]

+15 points (super focus bonus)
coffee_count += 2

Achievement Unlocked: "Red Bull Gives You Focus"
Achievement Failed: "The Old Guard"

Current coffee count: [previous + 2]
```

### Red Bull Trade (Correct Path)
```
You give the Red Bull to William.

William: *takes the Red Bull* "Ahhhh, that's the stuff. 
Sugar-free too! You've got potential, kid."

*cracks open the can*

"Alright, here's what 30 years taught me: Be aware. 
Be observant. The answer is usually right in front of you, 
you just gotta LOOK. Carefully."

*takes a long sip*

"Most problems aren't as complex as you think. Start simple."

"Now go actually WATCH that user. Don't trust what they tell you. 
Watch what they DO."

+100 points
william_quest_complete = True

Achievement Unlocked: "The Old Guard"
```

---

## Decision Tree: To Drink or Not to Drink

```
                    Player Enters Room with Coffee
                              │
                              ▼
                    ┌──────────────────┐
                    │   TAKE coffee?   │
                    └──────────────────┘
                         │         │
                    YES  │         │  NO
                         ▼         ▼
                    Add to      Continue
                    inventory   playing
                         │
                         ▼
                    ┌──────────────────┐
                    │   USE coffee?    │
                    └──────────────────┘
                         │
                         ▼
                 Check coffee_count
                         │
        ┌────────────────┼────────────────┐
        │                │                │
     Count=0-1        Count=2-5        Count=6
        │                │                │
        ▼                ▼                ▼
    Increase        Focus active    INSTANT DEATH
    counter         Still works     Game Over
        │           No penalties    Achievement
        │                │
        │                ▼
        └──────> Continue playing
```

---

## Optimal Strategy

```
╔═══════════════════════════════════════════════════════════════╗
║                    OPTIMAL COFFEE PATH                        ║
╚═══════════════════════════════════════════════════════════════╝

Step 1: Start in IT Office
        └─> TAKE coffee (fresh)
        └─> USE coffee (count = 1)

Step 2: Progress through game without focus
        └─> Gather initial information
        └─> Talk to NPCs
        └─> Read ticket

Step 3: Return to IT Office (or find second coffee)
        └─> TAKE coffee (any source)
        └─> USE coffee (count = 2)
        └─> ✓ FOCUS UNLOCKED (+30 points)

Step 4: Use focus for critical observations
        └─> Watch Karen type (spot Caps Lock)
        └─> Check auth logs (see pattern)
        └─> Find hallway note

Step 5: Complete game with focus active
        └─> Solve problem efficiently
        └─> DO NOT drink more coffee
        └─> Maximum points achieved

TOTAL COFFEE: 2 (Optimal)
POINTS GAINED: +30 (Coffee System) + bonuses from focus discoveries
```

---

## Suboptimal Strategies

### Strategy A: Zero Coffee (Impossible)
```
✗ Cannot spot Caps Lock without focus
✗ Cannot see enhanced auth logs
✗ Cannot find hallway note
✗ Will struggle to complete efficiently

Result: Likely to fail or get low score
```

### Strategy B: Drink Red Bull (Trade-off)
```
✓ Grants focus immediately
✓ Grants super focus (+15 pts)
✗ Loses William's quest (-100 pts)
✗ Net loss: -85 points

Result: Can complete game, but worse score
```

### Strategy C: Over-caffeinate (4-5 coffees)
```
✓ Focus remains active
✓ No point penalties
✗ Uncomfortable flavor text
✗ Risk of accidentally drinking 6th

Result: Same as 2 coffees, but risky
```

### Strategy D: Death Speedrun (6 coffees)
```
✗ Instant game over
✗ Score: 0
✓ Humorous ending
✓ Achievement unlocked

Result: Funny, but must restart
```

---

## Implementation Pseudocode

```python
class CoffeeSystem:
    def __init__(self):
        self.coffee_count = 0
        self.has_focus = False
        self.has_super_focus = False
        self.focus_unlocked_event_shown = False
        
    def drink_coffee(self):
        """Handle drinking regular coffee"""
        self.coffee_count += 1
        
        if self.coffee_count == 1:
            return self._message_coffee_1()
        elif self.coffee_count == 2:
            self.has_focus = True
            self.focus_unlocked_event_shown = True
            return self._message_coffee_2_focus_unlock()
        elif self.coffee_count == 3:
            return self._message_coffee_3()
        elif self.coffee_count == 4:
            return self._message_coffee_4()
        elif self.coffee_count == 5:
            return self._message_coffee_5_warning()
        elif self.coffee_count >= 6:
            return self._trigger_death()
    
    def drink_redbull(self):
        """Handle drinking Red Bull (counts as 2 coffees)"""
        previous_count = self.coffee_count
        self.coffee_count += 2
        self.has_focus = True
        self.has_super_focus = True
        
        # Check if this pushed us to 6+
        if self.coffee_count >= 6:
            return self._trigger_death()
        
        return self._message_redbull()
    
    def get_log_view_level(self):
        """Determine which log view to show"""
        if self.has_super_focus:
            return "ultra_enhanced"
        elif self.has_focus:
            return "enhanced"
        else:
            return "normal"
    
    def can_spot_caps_lock(self):
        """Check if player has focus to spot Caps Lock"""
        return self.has_focus or self.has_super_focus
    
    def is_hallway_note_visible(self):
        """Check if hallway note is visible"""
        return self.has_focus or self.has_super_focus
    
    def _trigger_death(self):
        """Trigger cardiac event game over"""
        game.set_game_over(
            reason="caffeine_overdose",
            score=0,
            achievement="Heart Attack Speedrun"
        )
        return "death_sequence"
    
    def _message_coffee_1(self):
        return """You drink the coffee. 

It's warm and pleasant. You feel slightly more alert.

(No special effects yet.)"""
    
    def _message_coffee_2_focus_unlock(self):
        game.award_points(30, "Coffee System - Optimal")
        game.unlock_achievement("Properly Caffeinated")
        
        return """You drink the coffee. 

Warmth spreads through you. Your mind sharpens considerably.
Colors seem slightly brighter. Details stand out more clearly.

Focus ability unlocked!

+30 points
Achievement Unlocked: "Properly Caffeinated" """
    
    def _message_coffee_3(self):
        return """That might have been one coffee too many.
Your heart is beating a little faster.
Your hands feel slightly jittery.

(You still have your focus, but you're feeling wired.)"""
    
    def _message_coffee_4(self):
        return """You're definitely feeling jittery now.
Your leg won't stop bouncing.
Every little thing seems like it could be critical.

(Focus remains, but you're uncomfortably caffeinated.)"""
    
    def _message_coffee_5_warning(self):
        return """Your heart is racing now.
You're sweating despite the air conditioning.
This might not have been a good idea.

You don't feel great. Maybe that's enough coffee for today?

(A small voice in your head suggests stopping.)"""
    
    def _message_redbull(self):
        game.award_points(15, "Super Focus")
        game.unlock_achievement("Red Bull Gives You Focus")
        game.fail_achievement("The Old Guard")
        game.fail_quest("william_quest")
        
        return """You crack open the sugar-free Red Bull.

*gulp* *gulp* *gulp*

Whoa.

Your pupils dilate. Colors seem brighter. Sounds sharper.
Everything is in ULTRA FOCUS now.

This is like drinking two coffees at once.

But...

William is watching from across the break room.

William: *shakes head* "That was supposed to be for me, kid. 
Ah well... guess you needed it more." *sighs* 

[William's quest failed - no wisdom bonus for you]

+15 points (super focus bonus)
Achievement Unlocked: "Red Bull Gives You Focus"
Achievement Failed: "The Old Guard" """
```

---

## Warning System Comparison

### Coffee #5 (Vague Warning) ⚠
```
"Your heart is racing now.
You're sweating despite the air conditioning.
This might not have been a good idea.

You don't feel great. Maybe that's enough coffee for today?"
```

**Characteristics:**
- Mentions physical discomfort
- Suggests stopping ("maybe that's enough")
- Does NOT mention death or cardiac issues
- Does NOT explicitly warn "one more will kill you"
- Vague enough that curious players might test it

### Coffee #6 (Death) 💀
```
"You drink another cup of coffee.

This was a mistake."

[Then cardiac event sequence]
```

**Player Experience:**
- Players at 5 can still explore safely
- Vague warning allows discovery
- Death is surprising but humorous
- Replayability remains high

---

## Achievement Summary

```
╔═══════════════════════════════════════════════════════════════╗
║                    COFFEE ACHIEVEMENTS                        ║
╚═══════════════════════════════════════════════════════════════╝

✓ "Properly Caffeinated" (+30 pts)
  └─> Reach optimal focus (2 coffees)
  └─> Required for efficient completion

✓ "Red Bull Gives You Focus" (+15 pts)
  └─> Drink Red Bull for super focus
  └─> Trade-off: Lose William's quest

✗ "The Old Guard" (Quest Failed)
  └─> Happens if you drink Red Bull
  └─> Should have traded it to William

☠ "Heart Attack Speedrun" (0 pts)
  └─> Die from 6 coffees
  └─> Humorous game over

◎ "Coffee Addict" (0 pts) [Hidden]
  └─> Drink from all 5 coffee sources
  └─> Flavor text only, no point value
```

---

## Visual Summary

```
                    COFFEE SYSTEM SUMMARY
                    
┌──────────────────────────────────────────────────────────┐
│                                                          │
│  REQUIRED: 2 coffees (Focus Buff)                        │
│  OPTIMAL:  2 coffees (+30 points)                       │
│  WARNING:  5 coffees (vague physical discomfort)        │
│  DEATH:    6 coffees (instant game over)                │
│                                                          │
│  RED BULL: Counts as 2 coffees, super focus             │
│            Trade to William = +100 pts (better choice)   │
│            Drink yourself = +15 pts (worse choice)       │
│                                                          │
│  NO PENALTIES: Over-caffeination has no point loss       │
│  NO HINTS: NPCs never mention coffee system             │
│  DISCOVERY: Player learns through experimentation       │
│                                                          │
└──────────────────────────────────────────────────────────┘

                         THE END
```

---

**Last Updated:** [Current Date]  
**System Status:** Finalized  
**Max Coffee Count:** 6 (was 5)  
**Warning Level:** Coffee 5 (vague, not explicit)  
**Death Trigger:** Coffee 6  
**Optimal Play:** 2 coffees exactly
