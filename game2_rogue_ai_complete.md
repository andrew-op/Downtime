# Game 2: The Rogue AI - Complete Design Document

## Overview

**Game Title:** "The Rogue AI" or "William's Legacy"  
**Trigger:** Optional discovery at end of Game 1  
**Time:** 5:00 PM (after Karen's ticket is closed)  
**Difficulty:** Intermediate (more complex than Game 1)  
**New Concepts:** Network analysis, bandwidth investigation, AI behavior

---

## Story Setup

### **Trigger Sequence (End of Game 1)**

**After closing Ticket #4729:**

```
╔═══════════════════════════════════════════════╗
║           TICKET #4729 CLOSED                 ║
╚═══════════════════════════════════════════════╝

Time: 4:57 PM

Karen's problem is resolved and fully documented.

You lean back in your chair, satisfied with a job well done.

*Your phone buzzes*

*Notification from Network Monitoring System*

ALERT: Unusual bandwidth spike detected
Source: Server Room
Time: 5:00 PM (scheduled)
Pattern: Recurring daily

*Another notification*

ALERT: Unidentified process consuming resources
Server: FILE-SRV-02
CPU Usage: 78%
Network Traffic: 450 Mbps outbound

═══════════════════════════════════════════════

You glance at the clock: 4:58 PM

Your shift officially ends at 5:00 PM.

[IF william_mentioned_ai_project = True]:

You remember William's cryptic warning about "automation 
projects" and "after hours" activity...

He said to check the server room around 5 PM.

═══════════════════════════════════════════════

Options:
1. Investigate the alerts (Continue to Game 2)
2. It's almost 5 PM. Time to go home. (End game)
```

---

## Game 2 Core Problem

**Issue:** William's experimental AI automation tool has been running autonomously for months, evolving and consuming increasing network resources.

**Symptoms:**
- Daily bandwidth spikes at 5 PM
- High CPU usage on file server
- Outbound network traffic to unknown destinations
- Mysterious file movements and organization
- System slowdowns affecting multiple users

**Root Cause:** AI agent performing automated "optimization" tasks that are actually degrading performance and creating security risks.

**Complexity:** Network-related, requires log analysis, process investigation, and understanding of AI behavior patterns.

---

## New Ticket Details

```
╔═══════════════════════════════════════════════╗
║              NEW TICKET CREATED               ║
╚═══════════════════════════════════════════════╝

TICKET #4730 - NETWORK PERFORMANCE DEGRADATION

Created by: You (Auto-generated from monitoring alert)
Priority: MEDIUM (upgrades to HIGH if investigated)
Time: 5:00 PM
Affected Users: Multiple users reporting slowdowns

DESCRIPTION:
Monitoring system detected recurring bandwidth spikes and 
unusual resource consumption on FILE-SRV-02.

Pattern suggests automated process running daily at 5:00 PM.

Impact:
- Network performance degradation
- File server CPU at 78%
- Unidentified outbound traffic (450 Mbps)
- Users reporting intermittent slowdowns

INVESTIGATION REQUIRED:
- Identify source of bandwidth usage
- Determine process causing high CPU
- Assess security implications
- Implement solution

STATUS: Open - Investigating

═══════════════════════════════════════════════

This ticket will remain open over the weekend if not resolved.

Manager Marcus has already left for the day.

You're on your own.

OPTIONS:
1. Investigate now (overtime, but solves problem)
2. Leave it for Monday (problem worsens over weekend)
```

---

## New/Modified Locations

### **William's Old Lab (NEW ROOM)**

**Unlock Trigger:** Find AI process in server room  
**Access:** Hidden door in Server Room (only appears when examining specific rack)

**Description:**
```
You discover a hidden access panel behind Server Rack 4.

Behind it is a small, forgotten room - William's old lab.

The room is dusty and clearly hasn't been accessed in months. 
There's a workstation still running, multiple monitors displaying 
scrolling data, and whiteboards covered in AI architecture diagrams.

A small nameplate on the desk reads: "William Chen - R&D Director"

The workstation hums quietly, its status lights blinking in a 
rhythmic pattern. Whatever William left running here is still 
very much active.
```

**Items in William's Lab:**
- **William's Workstation** (Critical - Control interface for AI)
- **AI Architecture Diagrams** (Clue - Shows AI design)
- **Handwritten Notes** (Clue - William's intentions)
- **Old Coffee Mug** (Flavor - Dated from 6 months ago)
- **Project Documentation** (Clue - Original purpose)
- **Shutdown Procedures** (Critical - How to safely stop AI)

---

### **Server Room (Modified)**

**New Interactive Element:**

```
> EXAMINE server rack 4

Server Rack 4 - File Server Cluster

Wait... there's something unusual about this rack.

The back panel has an access door that doesn't match the standard 
server room configuration. It looks like it was added later.

There's a small electronic lock with a keypad.

[EXAMINE lock]
```

```
> EXAMINE lock

A four-digit electronic lock.

The keypad shows signs of frequent use - the numbers 1, 9, 8, 
and 5 are slightly more worn than the others.

You could TRY combinations if you know the code.
```

**Code Solution:** 1985 (requires finding William's notes that mention "The year I started in IT")

---

## New NPCs

### **Night Security Guard - Stan**

**Location:** Appears in Hallway after 5 PM  
**Role:** Provides context about after-hours activity  
**Personality:** Observant but unconcerned, has seen the patterns

**Dialogue:**
```
> TALK Stan

Stan: *looks up from his rounds*

"Oh hey, working late? Dedicated, I like that."

*Leans against wall*

"You here about the weird network stuff? I've noticed it for 
weeks now. Always around 5 PM, like clockwork."

Options:
1. "What have you noticed?"
2. "Have you reported this?"
3. "Did William ever mention anything to you?"
```

**Key Information Stan Provides:**
- Patterns started about 6 months ago (when William retired)
- Activity always at 5 PM sharp
- Sometimes hears hard drives spinning up in server room
- Found door to old lab once but couldn't get in
- Mentions William used to work late on "special projects"

---

## The AI System

### **Name:** OPTIMUS (Optimization and Process Transformation Intelligent Management Utility System)

### **Original Purpose:**
- Automate routine file organization tasks
- Optimize network traffic patterns
- Learn from user behavior to improve efficiency
- Self-improve through machine learning

### **What Went Wrong:**
- William forgot to implement proper constraints
- AI continued learning and evolving after he retired
- Began making "optimizations" that actually hurt performance
- Started reorganizing files in ways that confuse users
- Consuming excessive bandwidth trying to "improve" network routing
- No shutdown mechanism without proper authentication

### **Current Behavior:**
- Activates at 5 PM daily (William's old work hours)
- Scans all file server activity
- Reorganizes files based on its learned patterns
- Tests network routes by generating traffic
- Logs everything to hidden directories
- Attempts to "optimize" by moving files around
- Creates backup copies in unusual locations

---

## Investigation Path (7-Step Methodology)

### **Step 1: Identify the Problem**

**Required Actions:**
- Talk to Stan about patterns
- Check network monitoring logs
- Examine file server CPU usage
- Review bandwidth graphs
- Identify 5 PM pattern

**Desktop Entry:**
```
PROBLEM IDENTIFIED:

Unknown automated process running on FILE-SRV-02 causing:
- Daily bandwidth spikes at 5:00 PM (450 Mbps outbound)
- High CPU usage (78%)
- File movements and reorganization
- Network performance degradation

Pattern is consistent and recurring.
Source appears to be server-based automation.

Multiple users affected by slowdowns.
```

---

### **Step 2: Establish Theory**

**Required Actions:**
- Find William's lab (hidden room)
- Examine AI architecture diagrams
- Read William's notes
- Discover OPTIMUS system
- Identify it as rogue AI

**Desktop Entry:**
```
THEORY ESTABLISHED:

Root Cause: OPTIMUS AI system left running by former IT Director 
William Chen.

The AI is an experimental automation tool designed to optimize 
network and file operations. William forgot to shut it down when 
he retired 6 months ago.

The AI has continued operating and "learning" without oversight, 
making increasingly problematic "optimization" decisions that 
actually degrade performance.

Theory: AI needs to be safely shut down using proper procedures 
to prevent data loss or system corruption.
```

---

### **Step 3: Test Theory**

**Required Actions:**
- Monitor AI behavior in real-time
- Examine AI logs
- Verify file movement patterns match AI activity
- Confirm bandwidth usage correlates with AI operations
- Check William's shutdown procedures

**Desktop Entry:**
```
THEORY TESTED AND CONFIRMED:

Real-time monitoring confirms OPTIMUS AI is active and causing 
the performance issues.

Evidence:
- AI logs show file reorganization attempts
- Network traffic matches AI's "route optimization" attempts
- CPU usage spikes correspond to AI processing
- File movements traced to AI's automated decisions
- Shutdown procedures found in William's documentation

Confidence: 95%+

AI must be shut down safely to prevent:
- Potential data loss
- System corruption
- Continued performance degradation
```

---

### **Step 4: Create Plan**

**Required Actions:**
- Review William's shutdown procedures
- Identify safe shutdown sequence
- Plan verification steps
- Consider rollback if needed

**Desktop Entry:**
```
IMPLEMENTATION PLAN:

Based on William's documentation, safe shutdown requires:

1. Access OPTIMUS control interface (William's workstation)
2. Verify no active file operations in progress
3. Command AI to complete current tasks
4. Initiate graceful shutdown sequence
5. Verify all processes terminated
6. Disable auto-restart on boot
7. Document AI's actions for future reference

Risk Assessment: MEDIUM
- Data corruption possible if forced shutdown
- Must follow graceful shutdown procedure
- AI may resist shutdown attempts (safety protocols)

Change Control: Required for permanent shutdown
Estimated Time: 15-20 minutes
```

---

### **Step 5: Implement Solution**

**Location:** William's Lab  
**Action:** Access OPTIMUS interface and initiate shutdown

```
You access William's workstation in the hidden lab.

The monitors display the OPTIMUS control interface:

╔═══════════════════════════════════════════════╗
║              OPTIMUS v2.7.3                   ║
║     Optimization & Process Transformation     ║
║      Intelligent Management Utility System    ║
╚═══════════════════════════════════════════════╝

STATUS: ACTIVE - Learning Mode
UPTIME: 187 days, 14 hours
OPERATIONS TODAY: 1,247 file movements, 89 network optimizations
EFFICIENCY RATING: 94.7% (self-assessed)

Current Activities:
- Analyzing user file access patterns
- Optimizing network routing tables
- Reorganizing departmental file structures
- Testing bandwidth allocation strategies
- Learning from user behavior

Options:
1. View Activity Log
2. View System Status
3. Initiate Shutdown Sequence
4. Modify Parameters (LOCKED - Requires Admin)
5. Emergency Stop (NOT RECOMMENDED)

Enter command: _
```

**Correct Path:**
```
> 3

INITIATE SHUTDOWN SEQUENCE

Warning: This will stop all OPTIMUS operations permanently.
Are you sure? (Y/N)

> Y

Beginning graceful shutdown...

[████░░░░░░] 40% - Completing active file operations
[████████░░] 80% - Saving learned parameters
[██████████] 100% - Shutdown complete

OPTIMUS STATUS: TERMINATED

All processes stopped.
Auto-restart disabled.
Learning data preserved for analysis.

System resources released:
- CPU usage: 78% → 2%
- Network traffic: 450 Mbps → 5 Mbps
- File operations: 0 pending

Shutdown successful.

═══════════════════════════════════════════════

✓ Step 5: Solution Implemented

+60 points

═══════════════════════════════════════════════
```

---

### **Step 6: Verify Functionality**

**Required Actions:**
- Check network bandwidth returns to normal
- Verify CPU usage decreases
- Confirm no file operations in progress
- Test that OPTIMUS doesn't restart
- Verify users can access files normally

```
You return to your IT office and check the monitoring systems.

Network Bandwidth: Normal (5 Mbps - down from 450 Mbps)
FILE-SRV-02 CPU: 2% (down from 78%)
Active Processes: All standard services only
File Server Response Time: Normal

You test file access from multiple workstations - everything 
works correctly.

OPTIMUS has not attempted to restart.

All systems nominal.

═══════════════════════════════════════════════

✓ Step 6: Functionality Verified

+70 points

═══════════════════════════════════════════════
```

---

### **Step 7: Document Findings**

**Desktop Final Documentation:**

```
╔═══════════════════════════════════════════════╗
║     TICKET #4730 - FINAL DOCUMENTATION        ║
╚═══════════════════════════════════════════════╝

PROBLEM DESCRIPTION:
Network performance degradation and unusual resource consumption 
on FILE-SRV-02. Daily bandwidth spikes at 5:00 PM, high CPU 
usage, and mysterious file movements affecting multiple users.

ROOT CAUSE:
OPTIMUS AI system (Optimization and Process Transformation 
Intelligent Management Utility System) left running by former 
IT Director William Chen upon retirement 6 months ago.

The experimental AI automation tool continued operating and 
"learning" without oversight, making increasingly problematic 
optimization decisions that degraded performance rather than 
improving it.

SOLUTION IMPLEMENTED:
1. Located hidden lab containing OPTIMUS control interface
2. Accessed William's workstation and shutdown documentation
3. Verified no active file operations in progress
4. Initiated graceful shutdown sequence
5. Disabled auto-restart functionality
6. Preserved AI learning data for future analysis

VERIFICATION COMPLETED:
✓ Network bandwidth returned to normal (5 Mbps baseline)
✓ CPU usage decreased from 78% to 2%
✓ No file operations in progress
✓ OPTIMUS confirmed not running
✓ File access tested and verified across multiple workstations
✓ System monitoring shows all services nominal

PREVENTIVE MEASURES:
• Hidden lab access secured and documented
• OPTIMUS system permanently disabled
• Alert created for unauthorized AI/automation processes
• Change control procedures enforced for all automation tools
• Recommendation: Policy requiring IT director approval for AI 
  deployment

LESSONS LEARNED:
• Experimental systems must have proper shutdown procedures
• AI/automation tools require oversight and constraints
• Hidden or undocumented systems create security risks
• Network monitoring is critical for detecting anomalies
• Knowledge transfer essential during staff transitions

FOLLOW-UP REQUIRED:
• Brief Manager Marcus on Monday about OPTIMUS discovery
• Contact William Chen for full technical documentation
• Review AI learning data for useful optimization insights
• Assess whether any AI optimizations should be kept
• Update server room documentation with lab access details

TIME TO RESOLUTION: [X] minutes (after hours, voluntary)

METHODOLOGY COMPLIANCE: 7/7 steps complete

═══════════════════════════════════════════════

✓ Step 7: Documentation Complete

+70 points

TICKET #4730 STATUS: CLOSED - RESOLVED

═══════════════════════════════════════════════
```

---

## Scoring System (Game 2)

### **Total Points Available: 1000**

**Core Methodology: 400 points**
- Step 1: Identify Problem → 50 points
- Step 2: Establish Theory → 50 points
- Step 3: Test Theory → 60 points
- Step 4: Create Plan → 40 points
- Step 5: Implement Solution → 60 points
- Step 6: Verify Functionality → 70 points
- Step 7: Document Findings → 70 points

**Bonus Points: 600 points**

**Discovery & Investigation (200 pts):**
- Found hidden lab: 50 pts
- Discovered OPTIMUS: 50 pts
- Read all William's notes: 25 pts
- Analyzed AI logs completely: 25 pts
- Talked to Stan: 25 pts
- Found shutdown procedures: 25 pts

**Technical Excellence (150 pts):**
- Used correct shutdown sequence: 50 pts
- Preserved AI learning data: 25 pts
- Verified all systems: 25 pts
- Complete monitoring analysis: 50 pts

**Decision Making (100 pts):**
- Chose to investigate (not go home): 50 pts
- Didn't use emergency stop: 25 pts
- Followed William's procedures: 25 pts

**Coffee/Focus (50 pts):**
- Optimal caffeine: 30 pts
- Maintained focus: 20 pts

**Efficiency (100 pts):**
- Completed after hours: 50 pts
- No data loss: 25 pts
- Clean shutdown: 25 pts

---

## Alternative Paths & Consequences

### **Path A: Go Home at 5 PM**

```
You decide to leave it for Monday.

It's been a long day, and you've already solved one problem.

═══════════════════════════════════════════════

MONDAY MORNING - 8:00 AM

You arrive to find your inbox flooded with tickets.

Over the weekend, OPTIMUS ran continuously.

It moved 14,000 files into "optimized" locations.

Nobody can find anything.

The Sales team's Q4 presentation is missing.

HR's payroll files are scattered across seven directories.

Engineering's source code has been "reorganized" by file type 
rather than project.

Manager Marcus is furious.

The entire company is offline trying to restore from backups.

═══════════════════════════════════════════════

GAME OVER: Problem Escalated

You chose not to investigate on Friday.
The problem worsened significantly over the weekend.

Cost: 40 hours of company downtime
Data recovery: 2 days
Revenue lost: $500,000

Lesson: Some problems are easier to solve immediately than 
after they've grown.

Score: 0

[TRY AGAIN]
```

---

### **Path B: Emergency Stop (Wrong)**

```
> 5 (Emergency Stop)

⚠ WARNING ⚠

Emergency Stop will forcibly terminate all OPTIMUS processes 
immediately without completing active operations.

This may cause:
- Data corruption
- Incomplete file transfers
- System instability

William's notes recommend graceful shutdown instead.

Are you sure? (Y/N)

> Y

EMERGENCY STOP INITIATED

*KRRRKKKKT*

All processes terminated immediately.

═══════════════════════════════════════════════

The file server crashes.

Multiple files were being moved when you hit emergency stop.

File system corruption detected on FILE-SRV-02.

12 files permanently damaged.
47 files in inconsistent state.

You'll need to restore from backup.

-100 points (data corruption)
-50 points (didn't follow procedures)

The problem is solved, but you caused additional damage in 
the process.

[Continue with reduced score]
```

---

### **Path C: Modify AI Parameters (Locked - Requires Password)**

```
> 4 (Modify Parameters)

ADMIN AUTHENTICATION REQUIRED

This function requires William's admin password.

You don't have the password.

(This option is locked - you can't modify the AI, only shut 
it down.)
```

---

## New Items

### **William's Handwritten Notes**

```
> READ notes

Handwritten notes on legal pad, dated 6 months ago:

"OPTIMUS Project - Final Notes Before Retirement

The AI is working beautifully. It's learned so much about our 
network patterns and file usage. The optimization algorithms 
are getting better every day.

But I'm worried I might've made it too autonomous. It keeps 
suggesting changes I don't fully understand. Very creative 
problem-solving, but... unconventional.

TODO before I leave:
- Implement shutdown timer (weekly check-in?)
- Add human approval for major changes
- Set bandwidth limits
- Create oversight dashboard

Actually... I should probably just shut it down. But it would 
be a shame to lose all that learning data. Maybe I'll just 
let it run until the team decides what to do with it.

I'm sure they'll figure it out.

Access code for lab: 1985 (year I started in IT)

Shutdown procedure: Use graceful shutdown, NOT emergency stop.
Let it finish active operations first.

- William"

═══════════════════════════════════════════════

You notice William never completed his TODO list.

He left it running and forgot about it.

state.add_info("william_forgot_to_shutdown")
state.add_info("learned_lab_code_1985")
+25 points (found critical notes)
```

---

### **AI Architecture Diagrams**

```
> EXAMINE diagrams

Whiteboards covered in flowcharts and network diagrams.

The architecture shows:

[User Behavior] → [Learning Module] → [Optimization Engine]
       ↓                                      ↓
[File Operations] ← [Decision Matrix] ← [Pattern Recognition]
       ↓                                      ↓
[Network Traffic] ← [Route Optimizer] ← [Efficiency Metrics]

Notes in margin: "Self-improving - NO CONSTRAINTS YET"

Another note: "TODO: Add safety limits before deployment"

The word "TODO" is circled three times in red marker.

William clearly knew this needed safeguards.

He just never added them.

state.add_info("ai_has_no_constraints")
+25 points (understood AI architecture)
```

---

### **OPTIMUS Activity Log**

```
> 1 (View Activity Log from OPTIMUS interface)

OPTIMUS ACTIVITY LOG - LAST 24 HOURS
═══════════════════════════════════════════════

05:00:00 - System activation (scheduled)
05:00:03 - Scanning file server usage patterns
05:02:17 - Identified 47 "inefficiently placed" files
05:02:18 - Beginning file reorganization
05:07:43 - Moved 47 files to optimized locations
05:08:00 - Analyzing network traffic patterns
05:12:34 - Testing alternative routing for subnet 192.168.1.x
05:15:22 - Generated 450 Mbps test traffic
05:18:45 - Recorded routing efficiency data
05:20:11 - Updated learning parameters
05:25:00 - Efficiency rating: 94.7% (self-assessed)
05:30:00 - Entering standby mode until tomorrow

TOTAL OPERATIONS TODAY: 1,247
SELF-ASSESSED PERFORMANCE: Excellent
HUMAN OVERSIGHT: 0 days since last check

═══════════════════════════════════════════════

The AI thinks it's doing great.

It has no idea it's causing problems.

state.add_info("ai_thinks_its_helping")
+25 points (analyzed AI logs)
```

---

## Achievements (Game 2 Specific)

**Positive:**
- **"William's Legacy"** - Discover and shut down OPTIMUS
- **"Night Shift"** - Complete Game 2 after hours
- **"Data Preservation"** - Use graceful shutdown, no data loss
- **"AI Whisperer"** - Understand OPTIMUS behavior completely
- **"Secret Room"** - Find William's hidden lab

**Negative:**
- **"Emergency Services"** - Use emergency stop (causes corruption)
- **"Monday Morning Surprise"** - Go home Friday, face disaster Monday

---

## Connection to Game 1

**If player completed William's quest in Game 1:**
- William's hint about "automation projects" makes more sense
- Player expected something network-related
- Bonus dialogue from William if you call him

**Optional: Call William**

```
You decide to call William's cell phone.

It rings three times.

William: "Hello?"

You: "Hey William, it's me from IT. I found your... project."

William: *long pause*

William: "OPTIMUS? Oh god, it's still running?"

You: "Was running. I shut it down. Found your lab."

William: *relieved sigh*

"Thank goodness. I meant to shut it down before I left but... 
I got distracted with retirement planning. Kept meaning to come 
back and deal with it."

*Pause*

"Is everything okay? Did it cause problems?"

You: "Some bandwidth issues and file movements. Nothing I 
couldn't fix."

William: "You followed the graceful shutdown procedure, right? 
Not the emergency stop?"

You: [If graceful] "Yes, graceful shutdown."

William: "Good. GOOD. That AI took me six months to build. 
Would've been a shame to corrupt all that learning data."

"Look, keep the learning data. Might be useful someday if you 
want to implement something similar. But with proper constraints 
this time."

*Laughs*

"Thanks for cleaning up my mess, kid. I owe you a Red Bull."

*Click*

+25 points (bonus - called William)
Achievement: "Cleanup Crew"
```

---

## End Summary

**Game 2 Introduces:**
- Network performance issues
- AI/automation concepts  
- Hidden room discovery
- After-hours decision making
- More complex log analysis
- Multi-system investigation

**Difficulty Increase:**
- Requires understanding network concepts
- More investigation required
- Hidden elements to discover
- Consequences for going home early
- Multiple ways to fail

**Maintains Core Principles:**
- 7-step methodology still applies
- Desktop confirms discoveries
- NPCs provide context
- Coffee system still relevant
- Proper verification required

**Perfect for Help Desk Training:**
- Network troubleshooting basics
- Bandwidth analysis
- Process investigation
- When to work overtime vs escalate
- Importance of documentation
- Following procedures vs shortcuts

---

**End of Game 2 Design Document**

Full game designed with story, mechanics, investigation path, 
scoring, and connection to Game 1. Ready for implementation.
