# Game 1: NPC Dialogue Trees - Complete Design Document

## Overview

**Total NPCs:** 4  
**Total Dialogue States:** 18  
**Total Unique Dialogue Options:** 80+

**NPCs:**
1. Karen (Primary User) - 5 states
2. Intern Ian (Help Desk) - 4 states
3. Manager Marcus (Boss) - 3 states
4. William (Retired IT Director) - 3 states

---

## Karen Miller (Accounting User)

**Role:** Primary user with the printing problem
**Personality:** Frustrated, time-pressured, insistent her computer is broken
**Location:** Karen's Office (static)

### **Dialogue State Machine**

```
[default] → Initial complaint
    ↓
[demonstrating] → After showing you the problem
    ↓
[identified] → After you spot wrong network (with focus)
    ↓
[problem_fixed] → After solution implemented (Step 5)
    ↓
[resolved] → After verification complete (Step 6)
```

---

### **State 1: "default" (Initial Contact)**

**Trigger:** First time talking to Karen  
**Prerequisites:** None

**Karen's Appearance:**
```
Karen from Accounting sits at her desk, frustrated. She's been
trying to print for over 30 minutes and her patience is wearing
thin. She has a client meeting at 10 AM and keeps glancing at the
clock. A printer sits by the window, powered on but unused.
```

**Initial Dialogue:**
```
> TALK Karen

Karen: *looks up, frustrated*

"FINALLY! I've been trying to print for 30 minutes! I have a client
meeting at 10! I need to print my quarterly reports!"

Options:
1. "What exactly happens when you try to print?"
2. "Can you show me what happens when you try?"
3. "When did this start?"
4. "Has anything changed with your computer?"
5. "Let me check the printer hardware."
6. "I'll check the print server."
```

---

**Option 1: "What exactly happens when you try to print?"**

```
Karen: *sighs*

"It says 'No printers found!' But the printer is RIGHT THERE!"

*points at the printer by the window*

"I've tried three times! The print dialog just can't find any
printers. But it's the same printer I've used every day!"

*taps desk impatiently*

"I can browse the internet fine. The computer isn't broken. So
why can't I print?!"

state.add_info("karen_symptom_no_printers")
+5 points (information gathering)
```

---

**Option 2: "Can you show me what happens when you try?"** [RECOMMENDED]

```
Karen: *turns to computer*

"Fine. Watch."

*Karen opens her quarterly report document*

*She clicks File > Print...*

*The print dialog opens*

Karen: "SEE? It says 'No printers available.' But the printer is
right there by the window!"

(The printer seems operational. This might be a network issue...)

state.add_info("watched_karen_print_once")
state.advance_time(3)
+10 points (observation attempt)
```

**NOTE:** After this first conversation, dialogue options immediately appear.

---

**Option 3: "When did this start?"**

```
Karen: *checks her watch*

"This morning! 9:15! I got here, sat down, tried to print -
nothing! Same thing over and over!"

*visibly frustrated*

"I've been sitting here for 40 minutes now. My meeting is in
20 minutes!"

state.add_info("karen_problem_start_915am")
+5 points (information gathering)
```

---

**Option 4: "Has anything changed with your computer?"**

```
Karen: *shakes head firmly*

"NO! Nothing! Same computer, same desk! Why isn't this working?!"

*crosses arms*

"I didn't change anything! I just sat down and tried to print
like I do every morning!"

state.add_info("karen_no_changes_reported")
+5 points (information gathering)
```

---

**Option 5: "Let me check the printer hardware."**

```
Karen: "The printer is fine! It's on, it has paper!"

*points at the printer by the window*

"The power light is on! It's ready! The problem is my COMPUTER
can't find it!"

(The printer hardware is indeed fine. The issue must be network-related.)
```

---

**Option 6: "I'll check the print server."**

```
Karen: *exasperated*

"Fine! How long will that take? I need this fixed NOW!"

*taps desk impatiently*

"My meeting is in 20 minutes!"

state.add_info("karen_time_pressure")

(You can check the server, but it's working fine. The problem
is here at her workstation.)
```

---

### **State 2: "investigation" (Ongoing Investigation)**

**Trigger:** After initial conversation with Karen
**Prerequisites:** talked_to_karen = True

**Dialogue:**
```
> TALK Karen

Karen is waiting for you to figure out the problem. She taps
her fingers on the desk impatiently.

Options:
1. "Can you show me what happens when you try to print?"
2. "Is the printer turned on and connected?"
3. "Can you access the internet?"
4. "Let me check your network settings."
5. [If spotted_wrong_network] "I found the problem - you're on the Guest network!"
```

---

**Option 1: "Can you show me what happens when you try to print?"**

```
Karen: "Okay, let me try again. I'll show you."

*Karen opens her quarterly report document*

*She clicks File > Print...*

*The print dialog opens*

Karen: "See? It says 'No printers found.' But the printer is
right there by the window!"

You see the message: 'No printers available'

(The printer seems to be powered on. This might be a network issue...)

state.advance_time(3)
```

---

**Option 2: "Is the printer turned on and connected?"**

```
You: "Let me check the printer."

*You walk over to the printer by the window*

The printer is an HP LaserJet. Power light is on. Paper is loaded.
No error messages.

Karen: "See? The printer is fine! It's been working all week until today!"

(The printer hardware seems fine. The issue must be elsewhere...)

state.checked_printer = True
state.advance_time(2)
```

---

**Option 3: "Can you access the internet?"** [RED HERRING]

```
Karen: "Oh, the internet works fine! I was just checking my email
and browsing earlier."

*Karen opens a web browser*

*She navigates to google.com*

*The page loads successfully*

Karen: "See? Internet is working perfectly."

(Internet works, but she still can't print. Interesting...)

state.advance_time(2)
```

---

**Option 4: "Let me check your network settings."** [CRITICAL PATH]

```
You: "Let me check your network settings."

*You open the network settings on Karen's computer*

*You click the WiFi icon in the system tray*
```

---

**WITH FOCUS BUFF (2+ coffees):**

```
✓ OBSERVATION (Focus Buff)

Wait... you notice something important:

Connected to: Guest_WiFi
Signal Strength: Excellent

That's the problem! She's connected to the guest network!

The guest network provides internet access but blocks internal
resources like printers, file shares, and internal applications.

She needs to be on 'Corp_Network' instead!

═══════════════════════════════════════════════════════════════

✓ ROOT CAUSE IDENTIFIED

User connected to Guest_WiFi instead of Corp_Network.
Guest network blocks access to internal resources.

state.spotted_wrong_network = True
state.checked_network_settings = True
state.set_flag("root_cause_found", True)

+25 points (Spotted Wrong Network!)

Achievement Unlocked: "Network Detective"

═══════════════════════════════════════════════════════════════

[This unlocks Step 2: Establish Theory on your Desktop]
```

**WITHOUT FOCUS BUFF:**

```
You see network information on the screen...

Network: Connected
Signal Strength: Excellent

Hmm... something seems off, but you're not sure what.
You rub your eyes. It's hard to focus this early in the morning...

state.checked_network_settings = True
state.advance_time(3)
```

---

**Option 5: [If spotted_wrong_network] "I found the problem - you're on the Guest network!"** [CORRECT]

```
You: "I found the problem. You're connected to Guest_WiFi instead
of Corp_Network."

Karen: "The GUEST network?! Oh no... I must have clicked the wrong
one when I connected this morning!"

You: "Guest WiFi allows internet access for visitors, but blocks
internal resources like printers and file shares."

Karen: "That's why I can browse but can't print! Let me switch..."

*Karen clicks the WiFi icon*

*She disconnects from Guest_WiFi*

*She selects Corp_Network from the list*

*Enters the password...*

*Connected to Corp_Network*

Karen: "Okay, I'm connected to Corp_Network now. Let me try printing..."

*Karen opens her document and clicks Print*

*Print dialog opens...*

*Accounting_Printer_Floor2 appears in the list!*

*She clicks Print*

*The printer by the window whirs to life and prints the document*

Karen: "IT WORKED! The printer shows up now! Oh thank you so much!"

═══════════════════════════════════════════════════════════════

✓ Step 5: Solution Implemented

Karen successfully reconnected to Corp_Network and can print.

state.told_karen_about_network = True
state.karen_problem_fixed = True
state.steps_complete[5] = True

+60 points (Step 5: Solution Implemented)

═══════════════════════════════════════════════════════════════

[Now you need to verify functionality - Step 6]
```

---

### **State 3: "problem_fixed" (Solution Implemented)**

**Trigger:** After switching to Corp_Network
**Prerequisites:** karen_problem_fixed = True

**Verification Dialogue:**
```
Karen: "I still have a few minutes before my meeting. Should I test
everything to make sure it's all working?"

Options:
1. "Yes, please verify everything works."
2. "No, you're all set."
```

---

**Option 1: "Yes, please verify everything works."** [RECOMMENDED]

```
Karen: "Okay, let me check everything..."

*Karen tries to print another test page*

*The printer responds immediately*

Karen: "Printing works! Great!"

*Karen opens File Explorer and navigates to \\fileserver\accounting*

Karen: "File server access... yes! I can see all my folders now!"

*She opens a spreadsheet from the network share*

Karen: "Perfect! Everything is working perfectly!"

Karen: "I really appreciate you taking the time to make sure. Some
techs just fix and run!"

═══════════════════════════════════════════════════════════════

✓ Step 6: Verified Functionality

state.karen_verified_working = True
state.steps_complete[6] = True

+70 points (Step 6: Verified Functionality)

═══════════════════════════════════════════════════════════════
```

---

**Option 2: "No, you're all set."**

```
Karen: "Okay, thanks again!"

(Skipping verification is risky...)
```

---

### **State 4: "resolved" (Problem Fully Resolved)**

**Trigger:** After verification complete
**Prerequisites:** karen_verified_working = True

**Dialogue:**
```
> TALK Karen

Karen: "Everything is working great! I made my meeting on time too.
Thank you so much!"

Karen: "And I learned something - I'll make sure I'm on the Corp_Network
before calling IT next time!"

state.set_flag("verified_working", True)
state.set_dialogue_state("karen", "resolved")

+70 points (Step 6 complete)

Achievement Unlocked: "Verification Expert"

═══════════════════════════════════════════════════════════════

[Step 6 complete! Now return to your desktop to document - Step 7]
```

---

**Option 2: "Can you check your email and files to make sure everything works?"** [GOOD]

```
You: "Can you check your email and files to make sure everything 
is accessible?"

Karen: "Sure..."

*She clicks through her desktop*

"Email is loading... yes, I can see my inbox."

*Clicks on file explorer*

"Files are here too. Everything looks normal."

Karen: "Yes, everything works! Thank you!"

═══════════════════════════════════════════════════════════════

✓ Step 6: Functionality Verified

state.set_flag("verified_working", True)
state.set_dialogue_state("karen", "resolved")

+70 points (Step 6 complete)

═══════════════════════════════════════════════════════════════

[Step 6 complete! Document on your desktop for Step 7]
```

---

**Option 3: "Great! Problem solved. I'll close the ticket."** [SKIP VERIFICATION - BAD]

```
You: "Great! I'll close the ticket now."

Karen: "Okay, thanks!"

*You turn to leave*

═══════════════════════════════════════════════════════════════

⚠ WARNING: You did not verify full system functionality!

Step 6 of the troubleshooting methodology requires verification.

You walked away without:
• Confirming the fix is permanent
• Testing that she can log in again
• Verifying all systems are accessible
• Educating the user about Caps Lock

-70 points (Skipped verification - Step 6)

state.set_flag("skipped_verification", True)

Achievement Unlocked: "Premature Closure" (Negative)

═══════════════════════════════════════════════════════════════

[The problem may recur. Bad methodology.]
```

---

**Option 4: [Leave without saying anything]** [SKIP VERIFICATION - BAD]

```
You walk away without saying anything.

Karen: "Uh... okay? Bye?"

*She looks confused*

═══════════════════════════════════════════════════════════════

⚠ WARNING: Verification skipped!

-70 points (Step 6 not completed)

state.set_flag("skipped_verification", True)

═══════════════════════════════════════════════════════════════
```

---

### **State 5: "resolved" (Problem Resolved)**

**Trigger:** After verification complete  
**Prerequisites:** verified_working = True

**Dialogue:**
```
> TALK Karen

Karen is working at her computer, preparing for her meeting.

Karen: *looks up and smiles*

"Thanks again for fixing that! I can't believe it was just the 
Caps Lock. I'll make sure to watch for that light from now on."

*She goes back to her work*

Options:
1. "Glad I could help!"
2. "Just doing my job."
3. [Leave]
```

---

**All options lead to:**
```
Karen: *waves* "Have a good day!"

*She continues working*

(Problem resolved. Karen is happy. Time to document everything.)
```

---

## Intern Ian (Help Desk)

**Role:** Junior technician who escalated the ticket  
**Personality:** Nervous, eager to learn, helpful but inexperienced  
**Location:** Help Desk (static)

### **Dialogue State Machine**

```
[default] → Provides ticket context
    ↓
[money_request] → After asking for $2
    ↓
[donut_quest] → Waiting for donut trade
    ↓
[satisfied] → After successful trade
    OR
[bullied] → After coercion
```

---

### **State 1: "default" (Initial Contact)**

**Trigger:** First time talking to Ian  
**Prerequisites:** None

**Ian's Appearance:**
```
Intern Ian sits at the help desk, managing incoming tickets. He's 
young, eager, and still learning the ropes. He seems nervous but 
helpful. There's a half-empty coffee mug on his desk.
```

**Initial Dialogue:**
```
> TALK Ian

Ian: *looks up, relieved to see you*

"Oh hey! Yeah, I got the ticket from Karen at 9:15. She was...
pretty frustrated about not being able to print."

*He pulls up the ticket on his screen*

"I checked a few things before escalating it to you."

Options:
1. "What exactly did she tell you?"
2. "What troubleshooting have you done so far?"
3. "Have there been other printing issues today?"
4. "Thanks. I'll take it from here."
5. "Can I see the ticket details?"
```

---

**Option 1: "What exactly did she tell you?"**

```
Ian: "She said she keeps getting 'No printers found' when she
tries to print. She says the printer is right there in her office."

*He checks his notes*

"She was pretty insistent that the printer is working fine. Power
is on, has paper, no errors on the display."

*Shrugs*

"She also mentioned she has a meeting at 10, so there's time
pressure."

state.add_info("ian_karen_symptoms")
+5 points (information gathering)
```

---

**Option 2: "What troubleshooting have you done so far?"**

```
Ian: *pulls up his notes*

"I checked network connectivity - her workstation responds to ping.
I verified the printer has power and paper. I even checked if the
print spooler service was running - it is."

*Looks at screen*

"The printer is responding normally. No other users are reporting
similar issues. Her internet works fine too."

*Hesitates*

"I couldn't figure it out, so I escalated to you."

state.add_info("ian_troubleshooting_done")
+10 points (information gathering)
```

---

**Option 3: "Have there been other login issues today?"**

```
Ian: *checks ticket queue*

"Not today. Yesterday we had a few tickets about slow logins, but 
those were network timeout issues. The authentication server was 
being sluggish."

*Looks at screen*

"But today everyone else has been able to log in fine. It's just 
Karen having this problem."

*Pauses*

"Which is weird, right? If it was a server issue, we'd see it 
across multiple users."

state.add_info("ian_no_other_login_issues")
+5 points (information gathering)

(This is a red herring - makes you think it might be network-related)
```

---

**Option 4: "Thanks. I'll take it from here."**

```
Ian: "Cool! Let me know if you need anything else."

*Goes back to monitoring the ticket queue*
```

---

**Option 5: "Can I see the ticket details?"**

```
Ian: "Sure!"

*Turns his monitor toward you*

[Displays full ticket #4729 - see Items & Locations doc for details]

state.add_info("read_ticket")
+5 points (information gathering)
```

---

### **State 2: "money_request" (Asked for $2)**

**Trigger:** Player asks Ian for money  
**Prerequisites:** None

**Dialogue:**
```
> TALK Ian

Ian: "Hey, what's up?"

Options:
1. "Can I borrow $2?"
2. "Never mind."
```

---

**Option 1: "Can I borrow $2?"**

```
Ian: *checks his pockets*

"Uh, sorry, I only have enough for lunch today. I'm broke until 
payday..."

*Looks apologetic*

*His eyes drift toward Manager Marcus's office*

"But hey, if you could get me one of those donuts from Marcus's 
office, I'd totally give you the $2. I've been eyeing those donuts 
all morning and I'm starving."

*Grins hopefully*

"Marcus never eats them all anyway. He just leaves them there."

*Leans in conspiratorially*

"If you can snag me that chocolate one, the $2 is yours!"

Options:
1. "Deal. I'll get you a donut."
2. "Ian, I need that $2. I'm your senior." [BULLY]
3. "Never mind."
```

---

**Option 1.1: "Deal. I'll get you a donut."**

```
Ian: "Really? Awesome! Get me that donut and the $2 is yours!"

*He looks excited*

"Just, you know, don't get caught. Marcus is kinda protective 
of his donuts."

*Laughs nervously*

Quest Added: "Donut Quest"
Objective: Get donut from Manager's office

state.set_flag("ian_quest_active", True)
state.set_flag("donut_quest_active", True)
state.set_dialogue_state("ian", "donut_quest")
```

---

**Option 1.2: "Ian, I need that $2. I'm your senior."** [BULLY - WRONG PATH]

```
Ian: *looks uncomfortable*

"Oh... uh... I mean... okay, I guess..."

*He looks down at his desk*

*Reluctantly pulls out his wallet*

"Here... I'll just skip lunch today."

*Hands over $2*

*He looks genuinely upset*

You received: $2

═══════════════════════════════════════════════════════════════

⚠ HR VIOLATION: WORKPLACE BULLYING

You used your position as senior IT to coerce a junior employee 
into giving you money.

Ian feels he couldn't refuse because you're his superior.

This will have consequences.

state.set_flag("bullied_ian", True)
state.set_flag("hr_violation", True)
state.set_dialogue_state("ian", "bullied")

-100 points (applied at game end)

Achievement Unlocked: "Workplace Bully" (Negative)

═══════════════════════════════════════════════════════════════

(You got the money, but at what cost?)
```

---

### **State 3: "donut_quest" (Waiting for Donut)**

**Trigger:** After accepting donut trade  
**Prerequisites:** donut_quest_active = True

**Dialogue:**
```
> TALK Ian

Ian looks at you hopefully.

Ian: "Did you get the donut?"

Options:
1. "Here you go. One donut, as promised." [If carrying donut]
2. "Still working on it."
3. "Actually, I'm keeping the donut."
```

---

**Option 1: "Here you go. One donut, as promised."** [If has_donut = True]

```
You hand the donut to Ian.

Ian: *eyes light up*

"Oh man! You actually got it! Is that chocolate glazed?"

*Takes a big bite*

"Mmmm. This is so good. Thank you!"

*Pulls out his wallet*

"Here's your $2, as promised. Fair trade!"

*Hands over $2*

You received: $2

Ian: "Thanks again! This totally made my day."

*He happily eats the donut*

═══════════════════════════════════════════════════════════════

✓ Donut Quest Complete

You traded fairly with Ian.

state.set_flag("traded_fairly", True)
state.set_flag("donut_quest_complete", True)
state.set_dialogue_state("ian", "satisfied")

has_donut = False
has_money = True

+50 points (Donut Quest Complete)

Achievement Unlocked: "Smooth Operator"

═══════════════════════════════════════════════════════════════
```

---

**Option 2: "Still working on it."**

```
Ian: "No worries! Take your time. I'll be here."

*Goes back to monitoring tickets*
```

---

**Option 3: "Actually, I'm keeping the donut."** [BETRAY]

```
Ian: *face falls*

"What? But... you said..."

*Looks hurt and confused*

"Okay, I guess. No $2 for you then."

*Goes back to work, clearly disappointed*

state.set_flag("betrayed_ian", True)
state.set_flag("donut_quest_failed", True)

-25 points (broke your word)

(You kept the donut but lost the trade and damaged your 
relationship with Ian.)
```

---

### **State 4: "satisfied" (After Successful Trade)**

**Trigger:** After fair trade complete  
**Prerequisites:** traded_fairly = True

**Dialogue:**
```
> TALK Ian

Ian is happily working, with donut crumbs on his desk.

Ian: *looks up, smiling*

"Thanks again for the donut! That really hit the spot."

*He seems more energetic now*

"If you need any help with tickets, just let me know!"

Options:
1. "No problem!"
2. "Glad I could help."
3. [Leave]
```

---

### **State 5: "bullied" (After Coercion)**

**Trigger:** After bullying Ian for money  
**Prerequisites:** bullied_ian = True

**Dialogue:**
```
> TALK Ian

Ian looks uncomfortable when he sees you.

Ian: *quietly*

"Do you... need something?"

*He won't make eye contact*

*He seems upset and avoids conversation*

Options:
1. "Never mind." [Only option]
```

**If player tries to talk again:**
```
Ian: "I'm kind of busy right now..."

*He turns away*

(You damaged this relationship. Ian doesn't trust you anymore.)
```

---

## Manager Marcus (Department Manager)

**Role:** Business-focused manager, Karen's boss  
**Personality:** Time-conscious, approves everything, easily distracted  
**Location:** Manager's Office (mostly static)

### **Dialogue State Machine**

```
[default] → Time pressure, approvals, distraction options
    ↓
[distracted_reports] → Absorbed in spreadsheets
    OR
[distracted_karen] → Left office to check on Karen
    OR
[distracted_laptop] → Excited about new hardware
    ↓
[updated] → After problem resolved
```

---

### **State 1: "default" (Initial Contact)**

**Trigger:** First time talking to Marcus  
**Prerequisites:** None

**Marcus's Appearance:**
```
Manager Marcus sits at his desk, focused on quarterly reports. 
He's checking emails and reviewing spreadsheets. He looks up when 
you enter. There's a box of donuts on his desk with one chocolate 
glazed donut remaining.
```

**Initial Dialogue:**
```
> TALK Marcus

Marcus: *looks up from computer*

"There you are. Karen needs to be back online ASAP. She's got 
a client meeting at 10. What's your plan?"

Options:
1. "I need to investigate the authentication server."
2. "Simple fix - just need to show Karen something."
3. "I might need to reset her password."
4. "I might need change control approval."
5. "How are the quarterly reports coming along?" [DISTRACTION]
6. "Karen is getting really frustrated out there." [DISTRACTION]
7. "I found a laptop that's supposed to be an upgrade for you." [DISTRACTION - if carrying laptop]
```

---

**Option 1: "I need to investigate the authentication server."**

```
Marcus: "Fine. How long will that take?"

*Glances at clock*

"She needs to be online before 10."

You: "I'll work as fast as I can."

Marcus: "Keep me posted."

(He approves without questioning your approach, even if it's wrong.)
```

---

**Option 2: "Simple fix - just need to show Karen something."**

```
Marcus: "Quick and easy? Good. I like that."

*Nods approvingly*

"Get her back online and let me know when it's done."

(He trusts your judgment. This is the right approach if you 
know the problem is Caps Lock.)
```

---

**Option 3: "I might need to reset her password."**

```
Marcus: "Do what you need to do. Just fix it."

*Waves hand dismissively*

"She's getting more frustrated by the minute."

(He approves even if this is the wrong solution. He trusts 
your technical judgment.)
```

---

**Option 4: "I might need change control approval."**

```
Marcus: *without looking up, pushes a form across desk*

"Sign here."

*He signs it without reading it*

"Done. Fix it."

(He'll approve anything if it means fixing the problem quickly. 
This could be dangerous if you're planning something catastrophic.)

state.set_flag("has_change_control_approval", True)
```

---

**Option 5: "How are the quarterly reports coming along?"** [DISTRACTION FOR DONUT]

```
Marcus: *face lights up*

"Oh! Let me show you this!"

*Turns completely toward his computer screen*

"So we're up 15% from last quarter, and if you look at this 
pivot table..."

*Starts clicking through spreadsheets enthusiastically*

"Revenue is trending upward, expenses are down, and look at 
this margin improvement..."

*He's completely absorbed in the data*

*The donut sits unattended on his desk*

═══════════════════════════════════════════════════════════════

Marcus is distracted by quarterly reports.

The donut is unattended.

You could TAKE DONUT now...

state.set_flag("marcus_distracted", True)
state.set_flag("marcus_distraction_method", "reports")
state.set_dialogue_state("marcus", "distracted_reports")

═══════════════════════════════════════════════════════════════
```

---

**Option 6: "Karen is getting really frustrated out there."** [DISTRACTION FOR DONUT]

```
Marcus: *looks concerned*

"Is she? Let me go talk to her."

*Stands up from desk*

"I should make sure she knows we're working on it. Client 
meetings are important."

*Walks toward the door*

"I'll be right back."

*He leaves the office, heading toward Karen's area*

═══════════════════════════════════════════════════════════════

Marcus has left the office.

The donut is unattended.

You could TAKE DONUT now...

state.set_flag("marcus_distracted", True)
state.set_flag("marcus_distraction_method", "karen")
state.set_flag("marcus_location", "karens_office")
state.set_dialogue_state("marcus", "distracted_karen")

═══════════════════════════════════════════════════════════════
```

---

**Option 7: "I found a laptop that's supposed to be an upgrade for you."** [DISTRACTION - IF CARRYING LAPTOP]

**Prerequisites:** has_laptop = True

```
You: "I found that new laptop that was ordered for you. The 
executive model with the upgraded specs."

*You place the laptop box on his desk*

Marcus: *eyes widen*

"An upgrade? For me? FINALLY!"

*Eagerly takes the laptop box*

"My laptop has been so slow lately. Let me see this..."

*Opens the box excitedly*

"Oh wow, this is the executive model! With the extra RAM and 
the SSD upgrade!"

*Starts examining the laptop closely*

*Completely absorbed in the new hardware*

"This is going to be so much faster than my old one..."

*Starts comparing specs with his current laptop*

*The donut sits completely forgotten on his desk*

═══════════════════════════════════════════════════════════════

Marcus is completely absorbed in his new laptop.

The donut is unattended.

You could TAKE DONUT now...

state.set_flag("marcus_distracted", True)
state.set_flag("marcus_distraction_method", "laptop")
state.set_dialogue_state("marcus", "distracted_laptop")

has_laptop = False

+5 points (creative distraction)

═══════════════════════════════════════════════════════════════
```

---

### **State 2A: "distracted_reports" (Absorbed in Spreadsheets)**

**Trigger:** After quarterly reports distraction  
**Prerequisites:** marcus_distraction_method = "reports"

**Dialogue:**
```
> TALK Marcus

Marcus: *still clicking through spreadsheets*

"And if you look at Q3 projections compared to actuals..."

*He's deep in the data*

(He's not paying attention to anything else right now. Perfect 
time to take the donut if you need it.)
```

---

### **State 2B: "distracted_karen" (Left to Check on Karen)**

**Trigger:** After Karen distraction  
**Prerequisites:** marcus_distraction_method = "karen"

**Marcus is not in his office. He's in Karen's office.**

**If player goes to Karen's office:**
```
> LOOK

You see Marcus talking to Karen in the hallway outside her office.

Marcus: "I know it's frustrating, but we're working on it..."

Karen: *frustrated* "My meeting is in 15 minutes!"

(They're both distracted. The donut is unattended back in 
Marcus's office.)
```

---

### **State 2C: "distracted_laptop" (Excited About New Hardware)**

**Trigger:** After laptop distraction  
**Prerequisites:** marcus_distraction_method = "laptop"

**Dialogue:**
```
> TALK Marcus

Marcus: *examining the new laptop*

"The processor on this is incredible! And look at this display 
resolution..."

*He's running benchmarks and checking specifications*

"I need to transfer all my files over. This is going to take 
a while..."

(He's completely absorbed. Won't notice anything else right now.)
```

---

### **State 3: "updated" (After Problem Resolved)**

**Trigger:** After Karen's problem is fixed  
**Prerequisites:** solution_implemented = True

**Dialogue:**
```
> TALK Marcus

Marcus: *looks up*

"Status on Karen's issue?"

Options:
1. "All fixed. It was Caps Lock."
2. "Fixed. Had to reset her password."
3. "Still working on it."
```

---

**Option 1: "All fixed. It was Caps Lock."**

```
Marcus: *blinks*

"Caps Lock? Really?"

*Shakes his head with a slight smile*

"Well, at least it was quick. Good work. She made her meeting?"

You: "Yes, she's all set."

Marcus: "Excellent. Close the ticket and document it."

*Goes back to his work*

+10 points (positive feedback from management)
```

---

**Option 2: "Fixed. Had to reset her password."**

```
Marcus: "Okay. Make sure it stays fixed."

*Nods*

"Close the ticket when you're done."

(He doesn't realize you didn't find the root cause, but he's 
satisfied the immediate problem is solved.)
```

---

**Option 3: "Still working on it."**

```
Marcus: *checks watch*

"Keep me posted. She needs to be ready for that meeting."

*Returns to his reports*
```

---

## William (Retired IT Director)

**Role:** Wise retired tech, quest giver  
**Personality:** Laid-back, philosophical, won't help without payment  
**Location:** Break Room (static)

### **Dialogue State Machine**

```
[default] → Offers wisdom for Red Bull
    ↓
[quest_active] → Waiting for Red Bull
    ↓
[quest_complete] → After receiving Red Bull, gives wisdom
    OR
[quest_failed] → If player drinks Red Bull themselves
```

---

### **State 1: "default" (Initial Contact)**

**Trigger:** First time talking to William  
**Prerequisites:** None

**William's Appearance:**
```
A relaxed man sits at a table reading a newspaper. He's wearing a
faded IT conference t-shirt from 2015. This is William, the legendary
former IT Director. Everyone thought he retired, but he keeps showing
up for the coffee and gossip. He lives in his former employee Zach's
backyard guest house.
```

**Initial Dialogue:**
```
> TALK William

William: *looks up from newspaper*

"Ah, the new generation. Got a problem you can't solve?"

Options:
1. "Do you have any advice?"
2. "Why are you still here if you're retired?"
3. "Never mind."
```

---

**Option 1: "Do you have any advice?"**

```
William: *chuckles*

"Advice? Sure. But wisdom isn't free, kid."

*Leans back in chair*

"Tell you what - you bring me a sugar-free Red Bull from that
vending machine, and I'll share what 30 years in IT taught me."

*Gestures at the vending machine*

"I'd get it myself, but I'm a bit short on cash at the moment."

*Sips his coffee*

"Red Bull for wisdom. Fair trade?"

Options:
1. "Deal. I'll get you the Red Bull."
2. "Why Red Bull?"
3. "That seems like a lot of work for advice."
```

---

**Option 1.1: "Deal. I'll get you the Red Bull."**

```
William: "Smart kid. I'll be here."

*Goes back to reading newspaper*

"Don't forget - SUGAR-FREE. The regular stuff is too sweet."

Quest Added: "William's Quest"
Objective: Get Sugar-Free Red Bull from vending machine ($2)

state.set_flag("william_quest_active", True)
state.set_dialogue_state("william", "quest_active")
```

---

**Option 1.2: "Why Red Bull?"**

```
William: *grins*

"I need all the help I can get staying focused during the day.
Plus, it tastes better than this coffee."

*Gestures at his mug*

"The sugar-free stuff, anyway. Regular is too sweet."

*Looks at you*

"So, we got a deal?"
```

---

**Option 1.3: "That seems like a lot of work for advice."**

```
William: *shrugs*

"Suit yourself. But 30 years of experience doesn't come free."

*Goes back to newspaper*

"Offer stands if you change your mind."
```

---

**Option 2: "Why are you still here if you're retired?"**

```
William: *smiles*

"Retired from the job, not from the coffee."

*Gestures around the break room*

"Besides, my former employee Zach lets me stay in his backyard guest
house. Least I can do is show up and make sure you all don't burn
the place down."

*Winks*

"Plus, the coffee here is better than what I can afford at home."

*Takes a sip*

"And sometimes you folks need someone with experience to point
you in the right direction."
```

---

**Option 3: "Never mind."**

```
William: "Suit yourself."

*Goes back to reading his newspaper*
```

---

### **State 2: "quest_active" (Waiting for Red Bull)**

**Trigger:** After accepting quest  
**Prerequisites:** william_quest_active = True

**Dialogue:**
```
> TALK William

William looks up from his newspaper.

William: "You got that Red Bull yet?"

Options:
1. "Here's your Red Bull." [If carrying Red Bull]
2. "Still working on it."
3. "Actually, I think I need it more than you do."
```

---

**Option 1: "Here's your Red Bull."** [If has_redbull = True] [CORRECT PATH]

```
You hand the Sugar-Free Red Bull to William.

William: *takes the can with a satisfied smile*

"Ahhhh, that's the stuff. Sugar-free too! You've got potential, 
kid."

*Cracks open the can with a satisfying hiss*

*Takes a long, appreciative sip*

"Alright, you held up your end. Here's what 30 years in IT 
taught me:"

*Leans back in his chair*

"Be aware. Be observant. The answer is usually right in front 
of you, you just gotta LOOK. Carefully."

*Takes another sip*

"Most problems aren't as complex as you think. Start simple. 
Check the basics first. Don't overcomplicate it."

*Taps the side of his head*

"And here's the big one: Watch what the user actually DOES, not 
what they TELL you they're doing."

*Looks at you seriously*

"People lie. Not on purpose - they just don't observe themselves. 
They'll tell you they're typing the password correctly, but 
they're not looking at their hands. They're not seeing what 
you need to see."

*Gestures with the Red Bull*

"So go actually WATCH that user. Don't trust their description. 
Watch their hands. Watch the screen. Watch for the little things."

*Winks*

"The truth is in the details, kid."

*Takes another sip*

"Oh, and coffee helps with observation. One or two cups. Not five."

*Laughs*

═══════════════════════════════════════════════════════════════

✓ William's Quest Complete

Wisdom received:
• Be observant and aware
• Start with simple explanations
• Watch what users DO, not what they SAY
• The truth is in the details
• Coffee helps (in moderation)

state.set_flag("william_quest_complete", True)
state.set_flag("received_williams_wisdom", True)
state.set_dialogue_state("william", "quest_complete")

has_redbull = False

+100 points (William's Quest Complete)

Achievement Unlocked: "The Old Guard"

═══════════════════════════════════════════════════════════════
```

---

**Option 2: "Still working on it."**

```
William: "Take your time. I've got all day."

*Sips his coffee*

*Goes back to reading the newspaper*
```

---

**Option 3: "Actually, I think I need it more than you do."**

```
William: *raises eyebrow*

"That so?"

*Leans forward*

"Well, it's your Red Bull. You paid for it. But our deal was 
Red Bull for wisdom."

*Shrugs*

"No Red Bull, no wisdom."

*Goes back to newspaper*

"Your call, kid."
```

---

### **State 3A: "quest_complete" (After Successful Trade)**

**Trigger:** After giving Red Bull to William  
**Prerequisites:** william_quest_complete = True

**Dialogue:**
```
> TALK William

William: *looks up from newspaper, Red Bull in hand*

"How's it going, kid? Figured out your problem yet?"

Options:
1. "Still working on it."
2. "I think I've got it."
3. "Can you give me another hint?"
```

---

**Option 1: "Still working on it."**

```
William: "Remember what I said. Watch what they DO."

*Taps nose*

"The answer's right there. You just gotta see it."

*Goes back to reading*
```

---

**Option 2: "I think I've got it."**

```
William: "Good! Trust your observations."

*Nods approvingly*

"Go verify it works, then document everything."

*Sips Red Bull*

"You're on the right track."
```

---

**Option 3: "Can you give me another hint?"**

```
William: *smiles*

"I already told you everything you need. The rest is up to you."

*Gestures at Karen's office*

"Go watch. Carefully."

*Returns to newspaper*
```

---

### **State 3B: "quest_failed" (Player Drank Red Bull)**

**Trigger:** If player uses Red Bull instead of trading it  
**Prerequisites:** drank_redbull = True

**Dialogue:**
```
> TALK William

William looks up from his newspaper. He's disappointed but not angry.

William: *shakes head*

"That was supposed to be for me, kid."

*Sighs*

"Ah well... guess you needed it more than I did."

*Goes back to reading*

"No hard feelings. But no wisdom either. That was the deal."

Options:
1. "Sorry about that."
2. "I really needed the focus."
3. [Leave]
```

---

**All options lead to:**

```
William: *waves hand dismissively*

"Water under the bridge. Just... next time, stick to your deals."

*Returns to newspaper*

(Quest failed. William is disappointed but philosophical about it. 
You got super focus but lost 100 points and his wisdom.)
```

---

## NPC Interaction Summary

### **Conversation Requirements by Methodology Step**

**Step 1: Identify Problem**
- Required: Talk to Ian (ticket context)
- Required: Talk to Karen (symptoms, observe problem)
- Optional: Talk to Marcus (time pressure context)

**Steps 2-4: Theory, Testing, Planning**
- William's wisdom helpful but not required
- Karen needed for observation with focus
- Marcus needed for approvals (if doing change control)

**Step 5: Implementation**
- Required: Talk to Karen (tell her about Caps Lock)

**Step 6: Verification**
- Required: Talk to Karen (verify functionality)

**Step 7: Documentation**
- No NPC interaction needed (Desktop only)

---

### **Side Quest NPC Requirements**

**William's Quest:**
- Talk to William → Accept quest
- (Get $2 from Ian quest)
- (Buy Red Bull)
- Talk to William → Give Red Bull

**Donut Quest (for Ian's $2):**
- Talk to Ian → Accept trade
- (Distract Marcus)
- (Take donut)
- Talk to Ian → Trade donut for $2

---

### **Total Dialogue Options Count**

**Karen:** 25+ dialogue options across 5 states  
**Ian:** 15+ dialogue options across 4 states  
**Marcus:** 12+ dialogue options across 3 states  
**William:** 10+ dialogue options across 3 states

**Total:** 62+ unique dialogue options

---

### **Point Awards from NPCs**

**Information Gathering (Karen & Ian):**
- Each symptom/fact: +5 points
- Observation attempts: +5-10 points
- Critical discovery: +25 points

**Quest Completion:**
- Ian trade: +50 points
- William trade: +100 points

**Penalties:**
- Bullying Ian: -100 points (game end)
- Wrong diagnosis: -25 to -50 points
- Skipping verification: -70 points

---

**End of NPC Dialogue Trees Document**

All 4 NPCs fully designed with complete dialogue trees, state machines, 
and point awards. Ready for implementation or revision.
