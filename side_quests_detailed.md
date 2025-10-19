# Game 1 Side Quests - Complete Design Document

## Overview

**Two Primary Side Quests:**
1. William's Quest (Red Bull Trade) - +100 points
2. Donut Heist (Multiple Methods) - +50 points

**Total Side Quest Points:** 150 points (out of 200 available in category)

**Both required for perfect score (1000 points)**

---

## Quest Integration Map

```
┌─────────────────────────────────────────────────────────────────┐
│                    SIDE QUEST FLOW                              │
└─────────────────────────────────────────────────────────────────┘

START
  │
  ▼
Talk to William (Break Room)
  │
  ├─> William wants Red Bull
  │   └─> Quest: Get Red Bull from vending machine ($2)
  │
  ▼
Need $2 for Red Bull
  │
  ├─> Option A: Ask Ian for $2 (Help Desk)
  │   └─> Ian says no, but hints at trade
  │       └─> Quest: Get donut for Ian
  │
  ├─> Option B: Bully Ian for $2 [WRONG PATH]
  │   └─> Get $2 immediately
  │   └─> HR Violation flag set
  │   └─> -100 points at game end
  │
  └─> Option C: Already have $2 somehow
      └─> Skip to vending machine
  │
  ▼
Get Donut from Manager's Office
  │
  ├─> METHOD 1: Distract with Quarterly Reports
  │   └─> Mike talks about spreadsheets
  │   └─> Take donut while distracted
  │
  ├─> METHOD 2: Distract with Karen Complaint
  │   └─> Mike leaves office to check on Karen
  │   └─> Take donut while he's gone
  │
  ├─> METHOD 3: Distract with New Laptop [NEW]
  │   └─> Get laptop from IT Office
  │   └─> Give to Mike ("upgrade")
  │   └─> Mike absorbed in new laptop
  │   └─> Take donut while distracted
  │
  └─> WRONG: Try to take without distraction
      └─> Mike catches you
      └─> Cannot take donut
  │
  ▼
Return to Ian (Help Desk)
  │
  └─> Trade donut for $2
      └─> +50 points (Donut Quest Complete)
      └─> Achievement: "Smooth Operator"
  │
  ▼
Use Vending Machine (Break Room)
  │
  └─> Buy Red Bull ($2)
  │
  ▼
DECISION POINT: Red Bull Usage
  │
  ├─> PATH A: Trade to William [CORRECT]
  │   └─> +100 points
  │   └─> Get troubleshooting wisdom
  │   └─> Achievement: "The Old Guard"
  │   └─> TOTAL: +150 points
  │
  └─> PATH B: Drink Red Bull yourself [WRONG]
      └─> +15 points (super focus)
      └─> William's Quest FAILS
      └─> Lose -100 point opportunity
      └─> NET LOSS: -85 points
      └─> Achievement: "Red Bull Gives You Wings"

END
```

---

## William's Quest - Detailed Flow

### **Quest Giver: William (Break Room)**

**Location:** Break Room  
**Availability:** From game start  
**Requirement:** None (always available)

---

### **Stage 1: Initial Contact**

**Player enters Break Room:**

```
You enter the company break room. Fluorescent lights hum overhead. 
There's a coffee maker on the counter with a fresh pot. A vending 
machine hums in the corner.

An older man sits at a table reading a newspaper. He's wearing a 
faded IT conference t-shirt from 2015. This is William, the legendary 
former IT Director. Everyone thought he retired, but he keeps showing 
up for the coffee and gossip.
```

**Player Action:**
```
> TALK William
```

**William's Response (State: default):**

```
William: *looks up from newspaper* 

"Ah, the new generation. Got a problem you can't solve?"

Options:
1. "Do you have any advice?"
2. "Why are you still here if you're retired?"
3. "Never mind."
```

---

**Selecting Option 1: "Do you have any advice?"**

```
William: *chuckles* 

"Advice? Sure. But wisdom isn't free, kid. Tell you what - you bring 
me a sugar-free Red Bull from that vending machine, and I'll share 
what 30 years taught me."

*gestures at vending machine*

"I'd get it myself, but I'm comfortable here. And broke until my 
pension check comes in."

Quest Added: "The Old Guard"
Objective: Get Red Bull for William

william_quest_active = True
```

**Selecting Option 2: "Why are you still here if you're retired?"**

```
William: *smiles*

"Retired from the job, not from the coffee. Besides, Munia lets me 
stay in her guest house for free. Least I can do is show up and make 
sure you kids don't burn the place down."

*takes a sip of coffee*

"Plus, the coffee here is better than what I can afford at home."
```

**Selecting Option 3: "Never mind."**

```
William: "Suit yourself, kid."

*goes back to reading newspaper*
```

---

### **Stage 2: Quest Active - Need $2**

**Player examines vending machine:**

```
> EXAMINE vending machine

A typical office vending machine. Soda, energy drinks, chips, candy.

You spot a Sugar-Free Red Bull in slot D4.
Price: $2.00

You don't have any money.

(You need $2 to purchase the Red Bull.)
```

**Player tries to use vending machine without money:**

```
> USE vending machine

You need $2 to buy anything from this machine.

(Where can you get $2?)
```

---

### **Stage 3: Getting Money - Ian Route**

**Player goes to Help Desk:**

```
> TALK Ian

Ian: "Hey! Need something?"

Options:
1. "Can I borrow $2?"
2. "Just checking in."
```

**Selecting Option 1: "Can I borrow $2?"**

```
Ian: *checks pockets*

"Uh, sorry, I only have enough for lunch today. I'm broke until 
payday..."

*looks apologetic*

"But hey, if you could get me one of those donuts from Mike's office, 
I'd totally give you the $2. I've been eyeing those donuts all morning 
and I'm starving."

*grins hopefully*

"Mike never eats them all anyway. He just leaves them there."

Options:
1. "Deal. I'll get you a donut."
2. "Ian, I need that $2. I'm your senior." [BULLY]
3. "Never mind."
```

---

**Option 1: "Deal. I'll get you a donut."**

```
Ian: "Really? Awesome! Get me a donut and the $2 is yours!"

Quest Added: "Donut Quest"
Objective: Get donut from Manager's office

ian_quest_active = True
donut_quest_active = True
```

**Option 2: "Ian, I need that $2. I'm your senior." [BULLY]**

```
Ian: *looks uncomfortable*

"Oh... uh... I mean... okay, I guess..."

*reluctantly pulls out $2 from wallet*

"Here... I'll just skip lunch today."

*looks down at desk, clearly upset*

You received: $2

bullied_ian = True
hr_violation = True

⚠ WARNING: Ian looks upset. This may have consequences.

(You got the money, but at what cost?)
```

**Consequences of Bullying Ian:**
- Get $2 immediately (skip donut quest)
- Can proceed to buy Red Bull
- BUT: -100 points applied at game end
- HR violation ending triggered
- Even with perfect methodology, career damaged

---

### **Stage 4: Donut Heist - Getting into Manager's Office**

**Player goes to Manager's Office:**

```
> LOOK

Manager Mike's office. Nicer than yours, with a window and everything. 
His desk is organized chaos - reports, budgets, and a box of donuts. 
Mike sits at his computer, checking emails.

There's one chocolate glazed donut left in the box.

Mike is currently: [PRESENT / DISTRACTED]
```

**Attempting to take donut while Mike is present:**

```
> TAKE donut

Mike: "Hey! That's MY donut! Get your own!"

*Mike watches his donuts closely*

You can't take it while he's watching.

(You need to distract him somehow.)
```

---

### **Donut Heist - METHOD 1: Quarterly Reports Distraction**

**Player talks to Mike:**

```
> TALK Mike

Mike: "There you are. Karen needs to be back online ASAP. She's got 
a client meeting at 10. What's your plan?"

Options:
1. "I need to investigate the authentication server."
2. "Simple fix - just need to show Karen something."
3. "How are the quarterly reports coming along?" [DISTRACTION]
4. "Karen is getting really frustrated out there." [DISTRACTION]
5. "I found a laptop in IT that needs upgrading." [DISTRACTION - NEW]
```

**Selecting Option 3: "How are the quarterly reports coming along?"**

```
Mike: *lights up* 

"Oh! Let me show you this!"

*turns completely toward his computer screen*

"So we're up 15% from last quarter, and if you look at this pivot 
table..."

*starts clicking through spreadsheets enthusiastically*

*He's completely absorbed in the data*

mike_distracted = True
mike_distraction_method = "reports"

─────────────────────────────────────────────────
Mike is distracted. The donut is unattended.
You could TAKE DONUT now...
─────────────────────────────────────────────────
```

**Taking the donut while distracted:**

```
> TAKE donut

You quickly pocket the chocolate donut while Mike is absorbed in 
his spreadsheets.

*Mike continues talking about Q3 projections*

Donut acquired!

(That was surprisingly easy.)

has_donut = True
+10 points (successful heist)
```

---

### **Donut Heist - METHOD 2: Karen Complaint Distraction**

**Selecting Option 4: "Karen is getting really frustrated out there."**

```
Mike: *looks concerned*

"Is she? Let me go talk to her."

*stands up from desk*

"I should make sure she knows we're working on it."

*walks out of office toward Karen's area*

mike_distracted = True
mike_distraction_method = "karen"
mike_location = "Karen's Office"

─────────────────────────────────────────────────
Mike has left the office. The donut is unattended.
You could TAKE DONUT now...
─────────────────────────────────────────────────
```

**Taking the donut:**

```
> TAKE donut

You quickly grab the chocolate donut from Mike's desk.

*You hear Mike's voice down the hall talking to Karen*

Donut acquired!

(Mike will be back soon, but you got what you came for.)

has_donut = True
+10 points (successful heist)
```

---

### **Donut Heist - METHOD 3: New Laptop Distraction [NEW]**

**Getting the Laptop:**

**Player in IT Office:**

```
> LOOK

You're in your cramped IT office. Cables snake across the floor like 
digital spaghetti. Your desk is covered in sticky notes with various 
passwords and server IPs.

On a shelf, you spot a brand new laptop still in its box - one of 
the executive models that just came in. It's supposed to go to the 
sales team, but it's been sitting here for a week.

Items visible:
- Desktop Computer
- Fresh Coffee
- New Laptop (in box)
```

**Taking the laptop:**

```
> TAKE laptop

You pick up the new laptop box. It's surprisingly light.

The sales team won't miss it for a few more hours.

(This could be useful for... something.)

has_laptop = True
```

**Going to Manager's Office with laptop:**

```
> TALK Mike

Mike: "There you are. Karen needs to be back online ASAP. What's 
your plan?"

Options:
1. "I need to investigate the authentication server."
2. "Simple fix - just need to show Karen something."
3. "How are the quarterly reports coming along?" [DISTRACTION]
4. "Karen is getting really frustrated out there." [DISTRACTION]
5. "I found a laptop that's supposed to be an upgrade for you." [DISTRACTION - NEW]
```

**Selecting Option 5: "I found a laptop that's supposed to be an upgrade for you."** [Only appears if has_laptop = True]

```
Mike: *eyes widen*

"An upgrade? For me? Finally!"

*takes the laptop box eagerly*

"My laptop has been so slow lately. Let me see this..."

*opens box and starts examining the new laptop*

"Oh wow, this is the executive model! With the extra RAM and 
everything!"

*completely absorbed in the new hardware*

*starts comparing specs with his old laptop*

mike_distracted = True
mike_distraction_method = "laptop"
has_laptop = False

─────────────────────────────────────────────────
Mike is completely absorbed in his new laptop.
The donut is unattended.
You could TAKE DONUT now...
─────────────────────────────────────────────────
```

**Taking the donut:**

```
> TAKE donut

You smoothly take the chocolate donut while Mike is lost in 
laptop specs and setup screens.

*Mike is installing updates*

Donut acquired!

(The sales team might be upset about that laptop later, but 
Mike's happy now. And you got your donut.)

has_donut = True
+10 points (successful heist)
+5 points (creative solution bonus)

Achievement Unlocked: "Tech Bribery"
```

---

### **Stage 5: Trading with Ian**

**Returning to Ian with donut:**

```
> TALK Ian

Ian: *eyes light up when he sees the donut*

"Oh man! You actually got one! Is that chocolate glazed?"

Options:
1. "Here you go. One donut, as promised."
2. "Actually, I'm keeping this."
3. "Give me the $2 first."
```

**Option 1: "Here you go. One donut, as promised."**

```
Ian: "Yes! Thank you so much!"

*happily takes the donut*

*pulls out $2 from wallet*

"Here's your $2, as promised. Fair trade!"

*takes a big bite of donut*

"Mmmm. Worth it."

You received: $2
has_donut = False
has_money = True
traded_fairly = True

+50 points (Donut Quest Complete)
Achievement Unlocked: "Smooth Operator"

Quest Complete: "Donut Quest"
```

**Option 2: "Actually, I'm keeping this."**

```
Ian: "What? But... you said..."

*looks disappointed*

"Okay, I guess. No $2 for you then."

(You kept the donut but lost the trade opportunity.)

donut_quest_failed = True
```

**Option 3: "Give me the $2 first."**

```
Ian: "Sure, makes sense."

*hands over $2*

"Here you go."

*waits for donut*

Options:
1. [Give donut] "Here's your donut."
2. [Keep donut] "Actually, I'm keeping this."
```

---

### **Stage 6: Buying Red Bull**

**At Break Room Vending Machine:**

```
> USE vending machine

You have $2.

The Sugar-Free Red Bull costs $2.

Purchase Red Bull? (Y/N)
```

**Selecting Yes:**

```
*insert coins*
*mechanical whirring*
*thunk*

You retrieve the Sugar-Free Red Bull from the machine.

Red Bull acquired!

has_redbull = True
has_money = False
```

---

### **Stage 7: CRITICAL DECISION - Red Bull Usage**

**Player can now:**
1. Trade Red Bull to William (correct path)
2. Drink Red Bull themselves (wrong path)

---

### **PATH A: Trading to William (CORRECT)**

**Talking to William with Red Bull:**

```
> TALK William

William: *looks up from newspaper*

"Ah, you're back. Did you get my Red Bull?"

Options:
1. "Here's your Red Bull." [if has_redbull]
2. "Still working on it."
3. "Actually, I might need this myself."
```

**Option 1: "Here's your Red Bull."**

```
You hand the Red Bull to William.

William: *takes the can with a satisfied smile*

"Ahhhh, that's the stuff. Sugar-free too! You've got potential, kid."

*cracks open the can with a satisfying hiss*

*takes a long, appreciative sip*

"Alright, you held up your end. Here's what 30 years in IT taught me:"

*leans back in chair*

"Be aware. Be observant. The answer is usually right in front of you, 
you just gotta LOOK. Carefully."

*takes another sip*

"Most problems aren't as complex as you think. Start simple. 
Check the basics. Watch what the user actually DOES, not what 
they TELL you they're doing."

*winks*

"And hey, coffee helps with that. One or two cups. Not five."

*taps nose knowingly*

"Now go actually WATCH that user. Don't trust their description. 
Watch their hands. Watch the screen. The truth is in the details."

+100 points (William's Quest Complete)
Achievement Unlocked: "The Old Guard"

Quest Complete: "William's Quest"

william_quest_complete = True
received_williams_wisdom = True
```

**William's Dialogue After Quest:**

```
> TALK William

William: *reading newspaper*

"Go on, kid. Put that wisdom to use. I'll be here if you need 
to bounce ideas around."

*sips his Red Bull contentedly*
```

---

### **PATH B: Drinking Red Bull Yourself (WRONG)**

**Player uses Red Bull on themselves:**

```
> USE redbull

You crack open the sugar-free Red Bull.

*gulp* *gulp* *gulp*

Whoa.

Your pupils dilate. Colors seem brighter. Sounds sharper.
Everything is in ULTRA FOCUS now.

This is like drinking two coffees at once.

But...

You look across the break room.

William is watching you from his table.

William: *shakes head slowly*

"That was supposed to be for me, kid."

*sighs*

"Ah well... guess you needed it more than I did."

*goes back to reading his newspaper*

*he doesn't look angry, just... disappointed*

─────────────────────────────────────────────────

You gained Super Focus!
+15 points (super focus bonus)

But...

William's Quest FAILED
Lost opportunity: -100 points
NET RESULT: -85 points

coffee_count += 2
has_super_focus = True
william_quest_failed = True

Achievement Unlocked: "Red Bull Gives You Wings"
Achievement Failed: "The Old Guard"

─────────────────────────────────────────────────

(Maybe you should have traded it to William instead...)
```

---

## Side Quest Scoring Summary

### **Perfect Path (Both Quests Complete):**

```
Donut Heist:
- Distraction Method: +10 points
- Laptop Distraction Bonus: +5 points (optional)
- Trade with Ian: +50 points
- Achievement: "Smooth Operator"

William's Quest:
- Trade Red Bull: +100 points  
- Achievement: "The Old Guard"

TOTAL: +150 to +155 points
```

---

### **Partial Completion:**

**Scenario 1: Complete Donut, Fail William**
- Drink Red Bull yourself: +15 points
- Lost William opportunity: 0 points
- Total: +15 points (vs +150 optimal)
- Net loss: -135 points

**Scenario 2: Bully Ian, Complete William**
- Skip donut quest: 0 points
- Get $2 by bullying: 0 points
- Buy Red Bull: 0 points
- Trade to William: +100 points
- HR Violation penalty: -100 points (at game end)
- Total: 0 points (cancelled out)

**Scenario 3: Fail Both**
- No donut quest: 0 points
- Bully Ian: HR violation
- Drink Red Bull: +15 points
- Total: +15 points, career damaged

---

## Quest Items Tracking

**Items Involved:**

1. **New Laptop** (IT Office)
   - Optional item for Manager distraction
   - Gives bonus points (+5)
   - Creates "Tech Bribery" achievement

2. **Donut** (Manager's Office)
   - Requires distraction to obtain
   - Tradeable to Ian
   - Worth +50 points via trade

3. **$2** (From Ian or bullying)
   - Required for vending machine
   - Obtained via fair trade or coercion

4. **Red Bull** (Vending Machine)
   - Costs $2
   - Can be traded OR consumed
   - Trading = +100 pts, Drinking = +15 pts

---

## Achievement List

**Positive Achievements:**

- **"Smooth Operator"** (+50 pts) - Complete donut trade fairly
- **"The Old Guard"** (+100 pts) - Trade Red Bull to William
- **"Tech Bribery"** (+5 pts) - Use laptop to distract Manager

**Neutral/Alternative:**

- **"Red Bull Gives You Wings"** (+15 pts) - Drink Red Bull yourself

**Negative/Warning:**

- **"Workplace Bully"** (-100 pts) - Bully Ian for money
- **"Short-Sighted"** (0 pts) - Fail William's quest after completing donut

---

## Hidden Notes for Future Development

**Rogue AI Quest (Post-5pm Discovery):**

*Brief notes for later expansion:*

- Triggers after closing Karen's ticket
- Time check: 5:00 PM
- William's dialogue hints: "I might've left a few things running..."
- Discovery location: Server Room (unusual processes)
- Unlocks: New room (William's Old Lab? AI Testing Area?)
- Creates: New ticket in Desktop system
- Rewards: +200-300 bonus points
- Achievement: "William's Legacy" or "AI Whisperer"
- Full 7-step methodology practice
- Network-related issue (bandwidth, DNS, port activity)
- Optional: Player can choose to go home or investigate

*Design this fully after core systems complete.*

---

## Quest Dependencies Map

```
╔═══════════════════════════════════════════════════════════════╗
║                    QUEST DEPENDENCY TREE                      ║
╚═══════════════════════════════════════════════════════════════╝

William's Quest (Primary)
    │
    ├─> Requires: Red Bull
    │     │
    │     └─> Requires: $2
    │           │
    │           ├─> Path A: Ian Trade (Recommended)
    │           │     │
    │           │     └─> Requires: Donut
    │           │           │
    │           │           └─> Requires: Manager Distraction
    │           │                 │
    │           │                 ├─> Method 1: Quarterly Reports
    │           │                 ├─> Method 2: Karen Complaint  
    │           │                 └─> Method 3: New Laptop
    │           │
    │           └─> Path B: Bully Ian (Not Recommended)
    │                 │
    │                 └─> Immediate $2, but -100 pts at end
    │
    └─> Decision: Trade or Drink?
          │
          ├─> Trade: +100 pts (Correct)
          └─> Drink: +15 pts, lose quest (Wrong)
```

---

## Implementation Flags

```python
# Quest Tracking
william_quest_active = False
william_quest_complete = False
ian_quest_active = False
donut_quest_active = False
donut_quest_complete = False

# Item Tracking
has_laptop = False
has_donut = False
has_money = False
has_redbull = False

# Manager State
mike_distracted = False
mike_distraction_method = None  # "reports", "karen", "laptop"

# Trade Behavior
traded_fairly = False
bullied_ian = False
hr_violation = False

# William's Wisdom
received_williams_wisdom = False

# Quest Outcome
william_quest_failed = False
```

---

## Dialogue State Transitions

**William States:**
1. `default` → Offers quest
2. `quest_active` → Waiting for Red Bull
3. `quest_complete` → Thanks you, gives wisdom
4. `quest_failed` → Disappointed, no wisdom

**Ian States:**
1. `default` → Provides ticket info
2. `money_request` → After you ask for $2
3. `donut_quest` → Waiting for donut
4. `satisfied` → After successful trade
5. `bullied` → After coercion (upset)

**Manager Mike States:**
1. `default` → Working at desk
2. `distracted_reports` → Absorbed in spreadsheets
3. `distracted_karen` → Left office
4. `distracted_laptop` → Excited about new hardware

---

**End of Side Quests Design Document**

Ready to move to the next system, or would you like any revisions to the side quests?
