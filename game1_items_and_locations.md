# Game 1: Items & Locations - Complete Design Document

## Map Overview

```
        [Manager's Office]
                |
         [IT Office]--------[Break Room]
                |
           [Hallway]
           /        \
   [Help Desk]    [Karen's Office]
        |
  [Server Room]
```

**Total Rooms:** 7  
**Navigation:** N, S, E, W only  
**Starting Location:** IT Office

---

## Room-by-Room Design

---

## 1. IT Office (Starting Room)

### **Description**

```
You're in your cramped IT office. Cables snake across the floor like 
digital spaghetti. Your desk is covered in sticky notes with various 
passwords and server IPs. A coffee-stained keyboard sits next to your 
monitor.

A fresh cup of coffee steams invitingly on your desk. On the shelf, 
you spot a brand new laptop still in its box - one of the executive 
models that came in last week.

The hallway is to the south. The break room is to the east. 
Manager Mike's office is to the north.
```

### **Exits**
- North → Manager's Office
- South → Hallway
- East → Break Room
- West → [Wall] "There's a wall there."

### **Items**

#### **Desktop Computer** (Not Takeable)
```
> EXAMINE computer

Your workstation. A standard corporate desktop with dual monitors.
This is where you access the ticketing system, check logs, and 
run diagnostics.

You can USE the computer to access your IT support desktop.
```

```
> USE computer

[Launches Desktop Computer Menu System]
[See Desktop Computer System document for full menu]
```

#### **Fresh Coffee** (Takeable)
```
> EXAMINE coffee

A fresh cup of coffee, still steaming. It smells good - someone 
must have just made it. Probably you, but you don't remember.

You can TAKE this.
```

```
> TAKE coffee

You pick up the coffee mug.

Coffee added to inventory.
```

```
> USE coffee

[See Coffee System for full message based on coffee_count]

You drink the coffee.

[Message varies by coffee count - see coffee_system_flowchart.md]
```

#### **New Laptop (in box)** (Takeable)
```
> EXAMINE laptop

A brand new laptop still sealed in its box. This is one of the 
executive models - Core i7, 32GB RAM, the works. 

It's supposed to go to the sales team eventually, but it's been 
sitting here for a week. Nobody seems to be in a hurry for it.

You could probably TAKE this if you needed it for something.
```

```
> TAKE laptop

You pick up the laptop box. It's surprisingly light.

The sales team won't miss it for a few more hours.

(This could be useful for... something.)

Laptop added to inventory.
has_laptop = True
```

#### **Sticky Notes** (Not Takeable, Examinable)
```
> EXAMINE notes

Dozens of sticky notes plastered around your monitors. Passwords, 
server IPs, reminders about server maintenance windows, a note 
that says "UPDATE DOCUMENTATION" that's been there for six months.

The usual IT chaos.
```

#### **Keyboard** (Not Takeable, Examinable)
```
> EXAMINE keyboard

Your keyboard. Standard corporate issue. Some keys are worn smooth 
from years of use. There's a coffee stain on the spacebar.

It's seen better days, but it works.
```

---

## 2. Hallway

### **Description**

```
A typical fluorescent-lit corporate hallway. The lights hum overhead 
with that distinctive office building drone. There's a water cooler 
in the corner and a trash can nearby. Generic corporate art hangs 
on the walls - probably something about "synergy" or "teamwork."

The IT office is to the north. The help desk is to the south. 
Karen's office is to the east.
```

### **Exits**
- North → IT Office
- South → Help Desk
- East → Karen's Office
- West → [Wall] "That's just wall."

### **Items**

#### **Water Cooler** (Not Takeable, Useable)
```
> EXAMINE water cooler

A standard office water cooler. The bottle is half empty. Or half 
full, if you're an optimist.

Some paper cups are stacked next to it.
```

```
> USE water cooler

You fill a paper cup with water and drink it.

*glug glug glug*

Refreshing, but it doesn't do anything special.

(Unlike coffee, water doesn't give you focus. Sorry.)
```

#### **Trash Can** (Not Takeable, Examinable)

**WITHOUT Focus Buff:**
```
> EXAMINE trash

A standard office trash can. Contains crumpled papers and empty 
coffee cups.

Nothing interesting.
```

**WITH Focus Buff (2+ coffees):**
```
> EXAMINE trash

A standard office trash can. Contains crumpled papers and empty 
coffee cups.

Wait...

Your sharp eyes notice something among the debris. There's a 
crumpled note with handwriting on it. It looks like someone threw 
away a reminder.

You can TAKE the note.

note_visible = True
```

#### **Crumpled Note** (Takeable - Only visible with Focus)
```
> TAKE note

You fish the crumpled note out of the trash and unfold it.

Crumpled note added to inventory.
has_methodology_note = True
+25 points (found hidden reminder)
```

```
> READ note

The note reads:

"Troubleshooting Reminder:
1. Identify the problem (talk to users!)
2. Establish a theory
3. Test the theory
4. Make a plan
5. Implement it
6. VERIFY it works!! (Don't skip this!)
7. Document everything

- Past Me"

Someone wrote this as a reminder and threw it away.

Looks like good advice though.
```

#### **Corporate Art** (Not Takeable, Examinable)
```
> EXAMINE art

A framed motivational poster. It shows a mountain climber and says:

"SYNERGY: Together we achieve more."

Inspiring. Or something.
```

---

## 3. Help Desk

### **Description**

```
The help desk area. A small desk with a computer and a phone that 
never stops ringing. Intern Ian sits here, looking slightly 
overwhelmed by the stack of tickets on his desk. There's a half-empty 
coffee mug next to his keyboard with a faded "World's Okayest Intern" 
logo.

A whiteboard on the wall shows a list of open tickets. Yours is at 
the top.

The hallway is to the north. The server room is to the south.
```

### **Exits**
- North → Hallway
- South → Server Room
- East → [Wall] "Can't go that way."
- West → [Wall] "There's a wall there."

### **Items**

#### **Intern Ian** (NPC)
```
> EXAMINE Ian

Intern Ian sits at the help desk, managing incoming tickets. He's 
young, eager, and still learning the ropes. He seems nervous but 
helpful.

You can TALK to Ian.
```

```
> TALK Ian

[See NPC Dialogue Trees document for full conversation options]
```

#### **Ian's Computer** (Not Takeable, Examinable/Useable)
```
> EXAMINE computer

Ian's help desk computer. The screen shows the ticketing system with 
several open tickets. Ticket #4729 is highlighted at the top of the 
queue - Karen's login issue.

You can USE the computer to view ticket details.
```

```
> USE computer

You lean over to look at Ian's screen.

Ian: "Oh, you want to see Karen's ticket? Here..."

*clicks on ticket #4729*

TICKET #4729 - LOGIN FAILURE

Reported by: Karen Miller (Accounting)
Workstation: WS-ACC-07
Time: 9:15 AM
Priority: MEDIUM
Escalated by: Ian (Help Desk)

DESCRIPTION:
User reports "Invalid Password" error when attempting to log in.
User insists password is correct and has not changed it recently.
Issue began this morning upon arrival at work.

TROUBLESHOOTING COMPLETED:
- Network connectivity verified (ping successful)
- Workstation responds to remote management
- No similar reports from other users
- User has client meeting at 10:00 AM

STATUS: Escalated to IT Support

NOTES: User becoming increasingly frustrated. Urgent resolution needed.

state.add_info("read_ticket")
```

#### **Ian's Coffee** (Takeable - Offered during conversation)
```
> EXAMINE coffee

Ian's coffee mug sits on his desk. It says "World's Okayest Intern" 
in faded letters. The coffee inside looks fresh.

Ian might offer this to you if you talk to him.
```

**Note:** Ian's coffee only becomes takeable if he offers it during 
conversation. You can't just take it without asking.

#### **Monitor Display** (Not Takeable, Examinable)
```
> EXAMINE monitor

Ian's second monitor shows the help desk ticket queue in real-time:

OPEN TICKETS - PRIORITY SORTED:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#4729 - K.Miller - Login Issue - URGENT ⚠
#4730 - Sales - Slow VPN - Low 
#4731 - HR - Printer Jam - Low
#4732 - Engineering - Software Install - Medium

Your assigned ticket is at the top of the urgent queue.
```

#### **Phone** (Not Takeable, Useable)
```
> EXAMINE phone

A standard office desk phone. It has a blinking message light.

Probably more people calling about Karen's issue.
```

```
> USE phone

You pick up the phone and listen to voicemail.

*beep*

"Ian, this is Karen from Accounting. I STILL can't log in! 
Is anyone working on this?!"

*beep*

You hang up.

(Yeah, you're working on it.)
```

---

## 4. Karen's Office

### **Description**

```
Karen's office in the accounting department. Her desk has a computer, 
a stack of folders, and a framed photo of her cat wearing a tiny 
accountant visor. Karen sits at her desk, arms crossed, looking 
frustrated at her login screen.

A small plant on her windowsill looks like it needs water.

The hallway is to the west.
```

### **Exits**
- West → Hallway
- North/South/East → [Wall] "You can't go that way."

### **Items**

#### **Karen** (NPC)
```
> EXAMINE Karen

Karen from Accounting sits at her desk, clearly frustrated. She's 
been trying to log in for over 30 minutes and her patience is wearing 
thin. She has a client meeting at 10 AM and keeps glancing at the 
clock.

You can TALK to Karen.
```

```
> TALK Karen

[See NPC Dialogue Trees document for full conversation options]
```

#### **Karen's Workstation** (Not Takeable, Examinable/Useable)

**WITHOUT Focus Buff:**
```
> EXAMINE workstation

A standard corporate desktop computer. The login screen is displayed, 
showing "Invalid Password" in red text.

Everything looks normal from here. You'd need to watch Karen type 
to see what's happening.
```

**WITH Focus Buff:**
```
> EXAMINE workstation

A standard corporate desktop computer. The login screen shows 
"Invalid Password" in red.

Your focused observation notices the keyboard has a Caps Lock 
indicator light. You should watch Karen type to see if that's 
relevant.
```

```
> USE workstation

You sit down at Karen's workstation.

Karen: "What are you doing?"

You: "Just checking something..."

*You try to log in with test credentials*

Login successful.

The workstation itself works fine. The issue is definitely related 
to Karen's login attempt, not the hardware.
```

#### **Keyboard** (Not Takeable, Examinable - CRITICAL ITEM)

**WITHOUT Focus Buff:**
```
> EXAMINE keyboard

A standard corporate keyboard. It has a numeric keypad and function 
keys. Looks normal.

Nothing obviously wrong with it.
```

**WITH Focus Buff AND after watching Karen type:**
```
> EXAMINE keyboard

A standard corporate keyboard. 

Your focused observation notices a small green LED indicator light 
illuminated above the Caps Lock key.

The Caps Lock is currently ON.

Interesting. You saw Karen typing her password, and this light was on...

state.add_info("spotted_caps_lock")
+25 points (critical discovery)

[This is key evidence - player must connect this to the login failures]
```

#### **Cat Photo** (Not Takeable, Examinable)
```
> EXAMINE photo

A framed photo of an orange tabby cat wearing a tiny green visor 
like an old-timey accountant. The cat looks deeply unimpressed with 
this outfit.

The frame has an engraved nameplate: "Mr. Whiskers, CPA"

(Karen really loves her cat.)
```

#### **Plant** (Not Takeable, Examinable)
```
> EXAMINE plant

A small succulent in a ceramic pot on the windowsill. It looks a 
bit droopy and could use some water.

Not your problem right now though.
```

#### **Login Screen** (Not Takeable, Examinable)
```
> EXAMINE screen

The Windows login screen displays:

Username: karen
Password: [hidden]

Below the password field in red text:
"The username or password is incorrect."

The cursor blinks in the password field, waiting for another attempt.
```

---

## 5. Server Room

### **Description**

```
The server room. It's always too cold in here - at least 10 degrees 
colder than the rest of the office. Rows of rack-mounted servers 
blink and hum with activity. The authentication server sits in the 
corner, its status lights all green.

There's a dusty old coffee mug on a shelf that looks like it's been 
here for weeks. Maybe months. The network diagram on the wall is 
dated from 2019.

The help desk is to the north.
```

### **Exits**
- North → Help Desk
- South/East/West → [Wall] "Can't go that way."

### **Items**

#### **Authentication Server** (Not Takeable, Examinable/Useable)

```
> EXAMINE authentication server

The primary authentication server. A rack-mounted server with blinking 
status lights:

- Power: GREEN
- Network: GREEN  
- CPU: GREEN
- Storage: GREEN

All indicators show the server is operating normally.

You could RESTART this server, but that seems like a drastic step 
for a single user login issue.
```

```
> USE authentication server

Are you sure you want to restart the authentication server?
This will disconnect ALL 500 users from network authentication.

Options:
1. "Yes, restart it." [CATASTROPHIC]
2. "No, that's a terrible idea."
```

**If player selects Option 1 - INSTANT GAME OVER:**
```
You've decided to restart the authentication server.

You schedule emergency maintenance.

╔═══════════════════════════════════════════════╗
║          RESTARTING AUTHENTICATION            ║
╚═══════════════════════════════════════════════╝

*Server shutting down...*
*Authentication services offline...*

Suddenly, your phone EXPLODES with calls.

"I can't log in!"
"Email is down!"
"VPN disconnected!"
"File shares are inaccessible!"

ALL 500 EMPLOYEES just lost authentication.

The CEO can't access the quarterly report for the board meeting.
Sales team can't access CRM during a major deal.
HR can't process payroll.

Manager Mike appears in the server room.
He does not look happy.

Mike: "What did you do?"

You: "I... I restarted the authentication server... to fix Karen's 
login..."

Mike: "For ONE user? WITHOUT testing? WITHOUT change control?"

*long silence*

Mike: "Security will escort you out. Clean out your desk."

╔═══════════════════════════════════════════════╗
║         GAME OVER: TERMINATED                 ║
║                                               ║
║ You took down authentication for 500 users    ║
║ to fix a Caps Lock issue for one person.      ║
║                                               ║
║ The company lost $47,000 in productivity.     ║
║ Three major deals fell through.               ║
║ The CEO's board presentation was delayed.     ║
║                                               ║
║ Your IT career is over.                       ║
║                                               ║
║ You are now troubleshooting carrier pigeons   ║
║ for a medieval reenactment society.           ║
║                                               ║
║ Achievement: "Chaos Agent"                    ║
╚═══════════════════════════════════════════════╝

Final Score: 0
Rank: Fired
Status: Escorted Out by Security
```

**If player selects Option 2:**
```
You: "No, that's a terrible idea."

Good call. Restarting the authentication server for a single user 
login issue would be catastrophic.

Better to investigate the actual problem first.
```

#### **Server Console** (Not Takeable, Useable)
```
> EXAMINE console

A terminal connected to the server rack. You can use this to run 
diagnostics or check logs.

You can USE this console.
```

```
> USE console

You log into the server console.

Running standard diagnostics...

[████████████████████] 100%

AUTHENTICATION SERVER STATUS:
- Active Directory: OPERATIONAL
- Kerberos: OPERATIONAL  
- LDAP: OPERATIONAL
- User accounts: 500 active
- Failed login attempts (last hour): 6
  - User 'karen': 6 attempts (all failed)
- No other anomalies detected

The server is working perfectly. This appears to be a user-specific 
issue, not a server problem.

(Time spent: 10 minutes. This didn't help, but at least you didn't 
break anything.)
```

#### **Network Diagram** (Not Takeable, Readable)
```
> EXAMINE diagram

A network diagram taped to the wall. It's dated "Last Updated: 
March 2019" - over two years old.

It shows the overall network topology, server locations, and 
connection paths.
```

```
> READ diagram

The diagram shows:

CORPORATE NETWORK TOPOLOGY
Last Updated: March 2019

[Internet] 
    ↓
[Firewall]
    ↓
[Core Switch]
    ↓
├─ [Server VLAN] → Auth Server, File Server, Email Server
├─ [Workstation VLAN] → User computers
└─ [Management VLAN] → IT equipment

Authentication flow:
Workstation → Core Switch → Auth Server → Domain Controller

Everything shows as properly connected. The infrastructure is fine.

(This confirms it's not a network issue. The problem must be with 
Karen's specific login attempt.)
```

#### **Ancient Coffee** (Takeable)
```
> EXAMINE coffee

An old coffee mug sitting on a shelf. The coffee inside looks... 
questionable. There's a thin film on top and it's definitely not 
steaming anymore.

This has been here for at least a week. Maybe two.

You... could TAKE this? But should you?
```

```
> TAKE coffee

Against your better judgment, you pick up the ancient coffee mug.

Ancient coffee added to inventory.

(Why did you do this?)
```

```
> USE coffee

You drink the ancient coffee.

*gulp*

Oh.

Oh no.

That was a mistake.

This tastes like regret and poor life choices. It's cold, bitter, 
and has an unsettling texture.

Your face contorts in disgust.

-10 points (terrible decision)
coffee_count += 1

Achievement Unlocked: "Dumpster Diver"

(You immediately regret this choice. But hey, it's technically 
coffee, so it counts toward your caffeine intake.)
```

#### **Server Racks** (Not Takeable, Examinable)
```
> EXAMINE racks

Rows of rack-mounted servers, switches, and storage arrays. LEDs 
blink in seemingly random patterns. Cables are neatly organized with 
color-coded tags.

Everything is humming along normally. The distinctive white noise 
of enterprise IT infrastructure.

Peaceful, in a way.
```

#### **Air Conditioning Vent** (Not Takeable, Examinable)
```
> EXAMINE vent

A large air conditioning vent in the ceiling. Cold air pours out 
constantly, keeping the server room at a crisp 62°F.

You can see your breath in here.

(Why do server rooms have to be so cold?)
```

---

## 6. Manager's Office

### **Description**

```
Manager Marcus's office. Nicer than yours, with a window and everything. 
His desk is organized chaos - spreadsheets, budget reports, and a box 
of donuts from this morning's management meeting.

Marcus sits at his computer, checking emails and looking at quarterly 
numbers. There's one chocolate glazed donut left in the box.

The IT office is to the south.
```

### **Exits**
- South → IT Office
- North/East/West → [Wall] "That's a wall."

### **Items**

#### **Manager Marcus** (NPC)
```
> EXAMINE Marcus

Manager Marcus sits at his desk, focused on his computer screen. He's 
reviewing quarterly reports and checking emails. He looks up when 
you enter.

You can TALK to Marcus.
```

```
> TALK Marcus

[See NPC Dialogue Trees document for full conversation options]
```

#### **Box of Donuts** (Not Takeable, Examinable)
```
> EXAMINE donuts

A white box from the local bakery. It originally contained a dozen 
donuts from this morning's management meeting.

There's one chocolate glazed donut left.

It looks delicious.
```

#### **Donut (chocolate)** (Takeable - Only when Marcus is distracted)

**When Marcus is NOT distracted:**
```
> TAKE donut

Marcus: "Hey! That's MY donut! Get your own!"

*Marcus watches his donut protectively*

You can't take it while he's watching.

(You need to distract him somehow.)
```

**When Marcus IS distracted (any method):**
```
> TAKE donut

You quickly pocket the chocolate donut while Marcus is distracted.

*Marcus continues [talking about reports / being away / examining laptop]*

Donut acquired!

Donut added to inventory.
has_donut = True
+10 points (successful heist)

[+5 additional points if used laptop method]
```

#### **Manager's Computer** (Not Takeable, Examinable)
```
> EXAMINE computer

Marcus's computer displays multiple spreadsheets and email windows. 
You can see quarterly budget projections and revenue charts.

Everything looks very... manager-y.

Marcus wouldn't appreciate you snooping, so you leave it alone.
```

#### **Change Control Form** (Takeable)
```
> EXAMINE form

A stack of blank change control forms on Marcus's desk. These are 
required for any major changes to production systems.

You can TAKE one if you need to submit a change request.
```

```
> TAKE form

You take a change control form.

Change control form added to inventory.
has_change_control_form = True
```

```
> READ form

CHANGE CONTROL REQUEST FORM

Requestor: _______________
Date: _______________
System Affected: _______________
Change Description: _______________
Risk Assessment: _______________
Rollback Plan: _______________
Approval: _______________

(You could fill this out if you needed to make major system changes, 
but for Karen's issue, that seems unnecessary.)
```

#### **Phone** (Not Takeable, Useable)
```
> EXAMINE phone

Marcus's desk phone. It has speed dial buttons for various departments.

You could USE this to call people, but Marcus might not appreciate it.
```

```
> USE phone

You pick up Marcus's phone.

Marcus: "What are you doing?"

You: "Just... checking something."

Marcus: "Use your own phone."

*You put the phone down*

(That was awkward.)
```

#### **Window** (Not Takeable, Examinable)
```
> EXAMINE window

A nice window with a view of the parking lot. Marcus's office is on 
the third floor, so you can see the cars below and some trees in 
the distance.

Much better than your windowless IT office.

(Management perks.)
```

#### **Budget Reports** (Not Takeable, Examinable)
```
> EXAMINE reports

Spreadsheets and printed budget reports cover Marcus's desk. Charts 
show quarterly revenue, expenses, and projections.

You can see the IT department's budget allocation. It's... less than 
you'd hoped.

(Maybe don't look too closely at this.)
```

---

## 7. Break Room

### **Description**

```
The company break room. Fluorescent lights hum overhead. There's a 
coffee maker on the counter with a fresh pot. Next to it is another 
cup that's been sitting there... you're not sure how long. Could be 
hours. Could be days.

A vending machine hums in the corner, offering snacks and energy 
drinks. William, a retired IT director, sits at a table reading a 
newspaper and enjoying his coffee.

The IT office is to the west.
```

### **Exits**
- West → IT Office
- North/South/East → [Wall] "Can't go that way."

### **Items**

#### **William** (NPC)
```
> EXAMINE William

A relaxed man sits at a table reading a newspaper. He's wearing a
faded IT conference t-shirt from 2015. This is William, the legendary
former IT Director.

Everyone thought he retired, but he keeps showing up for the coffee
and gossip. He lives in his former employee Zach's backyard guest house.

You can TALK to William.
```

```
> TALK William

[See NPC Dialogue Trees document for full conversation options]
```

#### **Coffee Maker** (Not Takeable, Useable)
```
> EXAMINE coffee maker

A standard office coffee maker. Someone made a fresh pot recently - 
the coffee smells good and is still hot.

There are some coffee cups stacked next to it.
```

```
> USE coffee maker

You pour yourself a cup of fresh coffee from the pot.

Fresh coffee added to inventory.
```

#### **Fresh Coffee (from pot)** (Takeable via coffee maker)
```
After using coffee maker:

You now have fresh coffee.

[Same as IT Office coffee when used]
```

#### **Mystery Coffee** (Takeable)
```
> EXAMINE mystery coffee

A coffee mug sitting on the counter. The coffee inside is lukewarm 
at best. You have no idea when this was made or who made it.

It could be from this morning. It could be from yesterday.

Do you really want to drink this?
```

```
> TAKE mystery coffee

You pick up the mysterious coffee.

Mystery coffee added to inventory.

(Questionable choice.)
```

```
> USE mystery coffee

You drink the mystery coffee.

It's... not good. Lukewarm, stale, and bitter.

But it's caffeine, technically.

-10 points (poor decision)
coffee_count += 1

(You've made better choices in life.)
```

#### **Vending Machine** (Not Takeable, Useable)
```
> EXAMINE vending machine

A typical office vending machine. Various snacks and drinks are visible 
through the glass.

You spot a Sugar-Free Red Bull in slot D4.
Price: $2.00

You can USE the vending machine to purchase items.
```

```
> USE vending machine

[If has no money:]
You need $2 to use the vending machine.

[If has $2:]
You have $2.

The Sugar-Free Red Bull costs $2.00.

Purchase Red Bull? (Y/N)
```

**If Yes:**
```
You insert $2 into the machine.

*whirr* *clunk*

The Sugar-Free Red Bull drops into the collection bin.

You retrieve the Red Bull.

Sugar-Free Red Bull added to inventory.
has_redbull = True
has_money = False
```

**If No:**
```
You decide not to purchase anything right now.

(You keep your $2.)
```

#### **Sugar-Free Red Bull** (Takeable - From vending machine)
```
> EXAMINE redbull

A can of Sugar-Free Red Bull. Cold from the vending machine.

William wants this. But you could also drink it yourself...

Options:
1. GIVE to William (correct path)
2. USE it yourself (wrong path)
```

```
> USE redbull

[See Coffee System and Side Quests documents for full outcomes]

You crack open the Red Bull...
[Triggers super focus or trade quest failure]
```

```
> GIVE redbull William

[See Side Quests document for William's response]

You hand the Red Bull to William...
[Completes William's Quest, +100 points]
```

#### **Microwave** (Not Takeable, Useable)
```
> EXAMINE microwave

A standard office microwave. Someone's lunch exploded in here last 
week and it still smells faintly of burnt popcorn.

You can USE the microwave if you have food.
```

```
> USE microwave

[If no food items:]
You don't have anything to microwave.

[If have donut:]
You consider microwaving the donut.

No. That would be weird. And Ian wouldn't want a microwaved donut.

You decide against it.
```

#### **Refrigerator** (Not Takeable, Examinable)
```
> EXAMINE refrigerator

A standard office refrigerator. There's a sign taped to it:

"PLEASE LABEL YOUR FOOD
ITEMS OVER 3 DAYS OLD WILL BE THROWN OUT
- Management"

You can hear it humming quietly.

(Nothing useful in there for your current task.)
```

#### **Table** (Not Takeable, Examinable)
```
> EXAMINE table

A simple break room table where William is sitting. It's one of 
those folding tables with a laminate top.

There are some coffee rings on the surface from years of use.
```

#### **Newspaper** (Not Takeable, Examinable)
```
> EXAMINE newspaper

William's newspaper. It's today's paper - you can see the date on 
the front page.

William is reading the business section.
```

```
> TAKE newspaper

William: *looks up sharply*

"Hey now, I'm reading that."

*pulls newspaper closer*

You can't take someone's newspaper while they're reading it.

(That would be rude.)
```

---

## Item Summary by Category

### **Takeable Items (Total: 10)**

**Coffee Sources (5):**
1. Fresh Coffee (IT Office)
2. Fresh Coffee (Break Room pot)
3. Ian's Coffee (Help Desk - offered)
4. Mystery Coffee (Break Room)
5. Ancient Coffee (Server Room)

**Quest Items (4):**
6. New Laptop (IT Office)
7. Donut (Manager's Office - when distracted)
8. Sugar-Free Red Bull (Vending Machine - $2)
9. Change Control Form (Manager's Office)

**Clues/Documents (1):**
10. Crumpled Note (Hallway trash - requires focus)

### **Interactive Items (Non-Takeable: 12)**

**Computers/Tech:**
1. Desktop Computer (IT Office) - Main interface
2. Ian's Computer (Help Desk) - View tickets
3. Karen's Workstation (Karen's Office) - Can test
4. Authentication Server (Server Room) - Can restart (BAD!)
5. Server Console (Server Room) - Run diagnostics
6. Manager's Computer (Manager's Office) - Examinable only

**NPCs:**
7. Intern Ian (Help Desk)
8. Karen (Karen's Office)
9. Manager Marcus (Manager's Office)
10. William (Break Room)

**Utility Items:**
11. Coffee Maker (Break Room) - Produces coffee
12. Vending Machine (Break Room) - Requires $2

### **Critical Evidence Items (3)**

1. **Keyboard** (Karen's Office) - Shows Caps Lock light with focus
2. **Authentication Logs** (Desktop Computer) - Shows case change pattern
3. **Crumpled Note** (Hallway) - Methodology reminder

### **Flavor/Atmosphere Items (15+)**

- Sticky Notes (IT Office)
- Corporate Art (Hallway)
- Monitor Display (Help Desk)
- Cat Photo (Karen's Office)
- Plant (Karen's Office)
- Network Diagram (Server Room)
- Server Racks (Server Room)
- Window (Manager's Office)
- Budget Reports (Manager's Office)
- Microwave (Break Room)
- Refrigerator (Break Room)
- Table (Break Room)
- Newspaper (Break Room)
- Water Cooler (Hallway)
- Plus various other examinable items

---

## Navigation Quick Reference

```
Manager's Office
       ↓
   IT Office ←→ Break Room
       ↓
   Hallway ←→ Karen's Office
       ↓
   Help Desk
       ↓
  Server Room
```

**Total Connections:** 7 rooms, 8 directional connections

---

## Special Item Interactions

### **Items That Change Based on Game State**

1. **Trash Can (Hallway)**
   - Without focus: Generic trash
   - With focus: Reveals crumpled note

2. **Keyboard (Karen's Office)**
   - Without focus: Looks normal
   - With focus + observation: Shows Caps Lock light

3. **Donut (Manager's Office)**
   - Marcus present: Can't take
   - Marcus distracted: Can take

4. **Ian's Coffee (Help Desk)**
   - Default: Not takeable
   - After Ian offers: Takeable

### **Items That Trigger Events**

1. **Authentication Server** → Restart = Instant Game Over
2. **Red Bull** → Trade to William = +100 pts
3. **Red Bull** → Drink yourself = Quest failure
4. **Donut** → Trade to Ian = +50 pts
5. **Laptop** → Give to Marcus = Distraction + bonus

### **Items That Affect Coffee Count**

All coffee items increase `coffee_count` when used:
- Fresh coffees: +1 each
- Mystery coffee: +1 (with penalty)
- Ancient coffee: +1 (with penalty)
- Red Bull: +2 (super focus)

---

## Room Atmosphere Notes

**IT Office:** Cramped, chaotic, familiar  
**Hallway:** Generic corporate, transitional  
**Help Desk:** Busy, overwhelmed, urgent  
**Karen's Office:** Frustrated user, time pressure  
**Server Room:** Cold, humming, technical  
**Manager's Office:** Nice, windowed, authority  
**Break Room:** Relaxed, social, coffee central

---

**End of Items & Locations Document**

All 7 rooms designed with full descriptions, items, and interactions.
Ready for implementation or revision.
