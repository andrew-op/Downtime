# Game 1: Desktop Computer Menu System - Complete Design Document

## Overview

**Purpose:** Progress logger and methodology validator  
**Location:** IT Office (player's desk)  
**Access:** USE computer command

**Core Principle:**  
The desktop never offers choices - it confirms what you discovered in the world.

---

## Design Philosophy

### **The Desktop is NOT:**
- A hint system
- A multiple-choice quiz
- A way to skip investigation
- A source of new information

### **The Desktop IS:**
- A progress tracker
- A methodology validator
- An official record keeper
- A documentation generator

### **Key Rules:**

1. **Desktop locks/unlocks based on world progress**
   - You must gather info in the world first
   - Desktop only unlocks when you've earned it

2. **Desktop commits findings to official record**
   - What you log becomes permanent
   - No guessing allowed

3. **Desktop never offers choices**
   - It confirms what you discovered
   - No branching paths in methodology options

4. **Desktop tracks everything for final documentation**
   - Every step recorded
   - Every action timestamped
   - Final report auto-generated

---

## Main Menu Structure

### **Base Template**

```
╔═══════════════════════════════════════════════╗
║           IT SUPPORT DESKTOP                  ║
╚═══════════════════════════════════════════════╝

TICKET #4729 - Karen Miller - Login Failure
Status: [STATUS]
Current Step: [X]/7 ([Step Name])

AVAILABLE ACTIONS:
─────────────────────────────────────────────────
1. View Ticket Details
2. Check Authentication Logs
3. Run Diagnostics
4. View Methodology Checklist

METHODOLOGY ACTIONS:
─────────────────────────────────────────────────
5. [STATE] Log Problem Identification
6. [STATE] Log Theory
7. [STATE] Log Test Results
8. [STATE] Log Implementation Plan
9. [STATE] Close Ticket & Document

─────────────────────────────────────────────────
0. Log Off

Enter option: _
```

---

## Menu State Evolution

### **Option States Legend**

```
[LOCKED] - Not yet available
         - Shows hint why it's locked
         - Gray text

★ [READY] - Unlocked and ready
          - Bright/highlighted
          - Player can select

✓ [DONE] - Already completed
         - Checkmark indicates completion
         - Still selectable (shows what was logged)
```

---

## Progressive Menu Evolution

### **Phase 1: Game Start**

```
╔═══════════════════════════════════════════════╗
║           IT SUPPORT DESKTOP                  ║
╚═══════════════════════════════════════════════╝

TICKET #4729 - Karen Miller - Login Failure
Status: ASSIGNED
Current Step: 0/7 (Not Started)

AVAILABLE ACTIONS:
─────────────────────────────────────────────────
1. View Ticket Details
2. Check Authentication Logs
3. Run Diagnostics
4. View Methodology Checklist

METHODOLOGY ACTIONS:
─────────────────────────────────────────────────
5. [LOCKED] Log Problem Identification
   └─ Gather information first
6. [LOCKED] Log Theory
   └─ Complete Step 1 first
7. [LOCKED] Log Test Results
   └─ Complete Step 2 first
8. [LOCKED] Log Implementation Plan
   └─ Complete Step 3 first
9. [LOCKED] Close Ticket & Document
   └─ Complete Steps 1-6 first

─────────────────────────────────────────────────
0. Log Off

Enter option: _
```

---

### **Phase 2: After Gathering Info (Step 1 Ready)**

**Unlock Trigger:**  
```python
if (talked_to_ian and 
    talked_to_karen and 
    watched_karen_demonstrate and 
    checked_logs_or_workstation):
    unlock_step_1()
```

```
╔═══════════════════════════════════════════════╗
║           IT SUPPORT DESKTOP                  ║
╚═══════════════════════════════════════════════╝

TICKET #4729 - Karen Miller - Login Failure
Status: INVESTIGATING
Current Step: 0/7 (Ready for Step 1)

AVAILABLE ACTIONS:
─────────────────────────────────────────────────
1. View Ticket Details
2. Check Authentication Logs
3. Run Diagnostics
4. View Methodology Checklist

METHODOLOGY ACTIONS:
─────────────────────────────────────────────────
★ 5. [READY] Log Problem Identification
6. [LOCKED] Log Theory
   └─ Complete Step 1 first
7. [LOCKED] Log Test Results
   └─ Complete Step 2 first
8. [LOCKED] Log Implementation Plan
   └─ Complete Step 3 first
9. [LOCKED] Close Ticket & Document
   └─ Complete Steps 1-6 first

─────────────────────────────────────────────────
0. Log Off

Enter option: _
```

---

### **Phase 3: After Step 1 Complete**

```
╔═══════════════════════════════════════════════╗
║           IT SUPPORT DESKTOP                  ║
╚═══════════════════════════════════════════════╝

TICKET #4729 - Karen Miller - Login Failure
Status: INVESTIGATING
Current Step: 1/7 (Problem Identified)

AVAILABLE ACTIONS:
─────────────────────────────────────────────────
1. View Ticket Details
2. Check Authentication Logs
3. Run Diagnostics
4. View Methodology Checklist

METHODOLOGY ACTIONS:
─────────────────────────────────────────────────
✓ 5. [DONE] Log Problem Identification
6. [LOCKED] Log Theory
   └─ Find root cause in the world first
7. [LOCKED] Log Test Results
   └─ Complete Step 2 first
8. [LOCKED] Log Implementation Plan
   └─ Complete Step 3 first
9. [LOCKED] Close Ticket & Document
   └─ Complete Steps 1-6 first

─────────────────────────────────────────────────
0. Log Off

Enter option: _
```

---

### **Phase 4: After Finding Root Cause (Step 2 Ready)**

**Unlock Trigger:**  
```python
if (step_1_complete and 
    spotted_caps_lock):
    unlock_step_2()
```

```
╔═══════════════════════════════════════════════╗
║           IT SUPPORT DESKTOP                  ║
╚═══════════════════════════════════════════════╝

TICKET #4729 - Karen Miller - Login Failure
Status: ROOT CAUSE FOUND
Current Step: 1/7 (Ready for Step 2)

AVAILABLE ACTIONS:
─────────────────────────────────────────────────
1. View Ticket Details
2. Check Authentication Logs
3. Run Diagnostics
4. View Methodology Checklist

METHODOLOGY ACTIONS:
─────────────────────────────────────────────────
✓ 5. [DONE] Log Problem Identification
★ 6. [READY] Log Theory
7. [LOCKED] Log Test Results
   └─ Complete Step 2 first
8. [LOCKED] Log Implementation Plan
   └─ Complete Step 3 first
9. [LOCKED] Close Ticket & Document
   └─ Complete Steps 1-6 first

─────────────────────────────────────────────────
0. Log Off

Enter option: _
```

---

### **Phase 5: All Steps 1-4 Complete**

```
╔═══════════════════════════════════════════════╗
║           IT SUPPORT DESKTOP                  ║
╚═══════════════════════════════════════════════╝

TICKET #4729 - Karen Miller - Login Failure
Status: READY FOR IMPLEMENTATION
Current Step: 4/7 (Plan Created)

AVAILABLE ACTIONS:
─────────────────────────────────────────────────
1. View Ticket Details
2. Check Authentication Logs
3. Run Diagnostics
4. View Methodology Checklist

METHODOLOGY ACTIONS:
─────────────────────────────────────────────────
✓ 5. [DONE] Log Problem Identification
✓ 6. [DONE] Log Theory
✓ 7. [DONE] Log Test Results
✓ 8. [DONE] Log Implementation Plan
9. [LOCKED] Close Ticket & Document
   └─ Implement and verify solution first

─────────────────────────────────────────────────
0. Log Off

Go implement the solution in the world!

Enter option: _
```

---

### **Phase 6: After Implementation & Verification**

```
╔═══════════════════════════════════════════════╗
║           IT SUPPORT DESKTOP                  ║
╚═══════════════════════════════════════════════╝

TICKET #4729 - Karen Miller - Login Failure
Status: READY TO CLOSE
Current Step: 6/7 (Verified Working)

AVAILABLE ACTIONS:
─────────────────────────────────────────────────
1. View Ticket Details
2. Check Authentication Logs
3. Run Diagnostics
4. View Methodology Checklist

METHODOLOGY ACTIONS:
─────────────────────────────────────────────────
✓ 5. [DONE] Log Problem Identification
✓ 6. [DONE] Log Theory
✓ 7. [DONE] Log Test Results
✓ 8. [DONE] Log Implementation Plan
★ 9. [READY] Close Ticket & Document

─────────────────────────────────────────────────
0. Log Off

Enter option: _
```

---

## Information Actions (Always Available)

### **Option 1: View Ticket Details**

```
> 1

╔═══════════════════════════════════════════════╗
║              TICKET DETAILS                   ║
╚═══════════════════════════════════════════════╝

TICKET #4729 - LOGIN FAILURE

Reported by: Karen Miller (Accounting)
Workstation: WS-ACC-07
Time Reported: 9:15 AM
Priority: MEDIUM
Escalated by: Ian (Help Desk)

DESCRIPTION:
User reports "Invalid Password" error when attempting to log in.
User insists password is correct and has not changed it recently.
Issue began this morning upon arrival at work.

TROUBLESHOOTING COMPLETED BY HELP DESK:
- Network connectivity verified (ping successful)
- Workstation responds to remote management
- No similar reports from other users
- User has client meeting at 10:00 AM

STATUS: Escalated to IT Support

NOTES: 
User becoming increasingly frustrated. Urgent resolution needed.

─────────────────────────────────────────────────
Press any key to return to main menu...
```

---

### **Option 2: Check Authentication Logs**

**Display changes based on focus buff state**

#### **Without Focus Buff (0-1 coffee)**

```
> 2

╔═══════════════════════════════════════════════╗
║         AUTHENTICATION LOGS - WS-ACC-07       ║
╚═══════════════════════════════════════════════╝

Multiple AUTH_FAILED entries for user 'karen'

09:15:03 - AUTH_FAILED - User: karen - Invalid credentials
09:18:47 - AUTH_FAILED - User: karen - Invalid credentials
09:22:15 - AUTH_FAILED - User: KAREN - Invalid credentials
09:27:33 - AUTH_FAILED - User: KAREN - Invalid credentials
09:31:12 - AUTH_FAILED - User: KAREN - Invalid credentials

All attempts from workstation WS-ACC-07
Network connectivity verified
Domain controller responding normally

─────────────────────────────────────────────────

The logs show repeated authentication failures, but no obvious 
pattern is visible.

(You might notice more details with better focus.)

─────────────────────────────────────────────────
Press any key to return to main menu...
```

---

#### **With Focus Buff (2+ coffees)**

```
> 2

╔═══════════════════════════════════════════════╗
║    AUTHENTICATION LOGS - WS-ACC-07 [ENHANCED] ║
╚═══════════════════════════════════════════════╝

Your focused mind processes the authentication logs carefully.

09:15:03 - AUTH_FAILED - User: karen - Invalid credentials
09:18:47 - AUTH_FAILED - User: karen - Invalid credentials
─────────────────────────────────────────────────
Pattern change detected at 09:22:15 →
─────────────────────────────────────────────────
09:22:15 - AUTH_FAILED - User: KAREN - Invalid credentials
09:27:33 - AUTH_FAILED - User: KAREN - Invalid credentials
09:31:12 - AUTH_FAILED - User: KAREN - Invalid credentials

═══════════════════════════════════════════════

✓ PATTERN IDENTIFIED

The username changed from lowercase 'karen' to uppercase 'KAREN' 
at 09:22:15.

This suggests Caps Lock was enabled between 09:18 and 09:22.

Windows authentication is case-sensitive for passwords but not 
usernames. However, the case change indicates Caps Lock may be 
affecting password entry.

Probability: High likelihood of user error related to Caps Lock.

state.add_info("noticed_case_change_in_logs")
+10 points (enhanced observation)

═══════════════════════════════════════════════
Press any key to return to main menu...
```

---

#### **With Super Focus (Red Bull)**

```
> 2

╔═══════════════════════════════════════════════╗
║ AUTHENTICATION LOGS - WS-ACC-07 [ULTRA MODE]  ║
╚═══════════════════════════════════════════════╝

Your hyper-focused mind analyzes the data with exceptional clarity.

09:15:03 - AUTH_FAILED - User: karen - Invalid credentials
          ↓ Lowercase username (Caps Lock OFF)
          ↓ 3 minutes 44 seconds
09:18:47 - AUTH_FAILED - User: karen - Invalid credentials
          ↓ Lowercase username (Caps Lock OFF)
          ↓ 3 minutes 28 seconds - CHANGE OCCURS HERE
09:22:15 - AUTH_FAILED - User: KAREN - Invalid credentials
          → UPPERCASE username (Caps Lock ON)
          ↓ 5 minutes 18 seconds
09:27:33 - AUTH_FAILED - User: KAREN - Invalid credentials
          → UPPERCASE username (Caps Lock ON)
          ↓ 3 minutes 39 seconds
09:31:12 - AUTH_FAILED - User: KAREN - Invalid credentials
          → UPPERCASE username (Caps Lock ON)

═══════════════════════════════════════════════

✓✓ ULTRA ANALYSIS COMPLETE

Clear pattern indicates Caps Lock was enabled between 09:18:47 
and 09:22:15 (approximately 09:20).

Analysis:
• User attempted login twice with Caps Lock OFF (failed)
• User accidentally enabled Caps Lock around 09:20
• All subsequent attempts have Caps Lock ON (all failed)
• Caps Lock affects password case, causing authentication failure

Confidence Level: 95%
Recommended Action: Verify Caps Lock state at workstation

state.add_info("ultra_log_analysis_complete")
+15 points (ultra enhanced observation)

═══════════════════════════════════════════════
Press any key to return to main menu...
```

---

### **Option 3: Run Diagnostics**

```
> 3

╔═══════════════════════════════════════════════╗
║         RUNNING SYSTEM DIAGNOSTICS            ║
╚═══════════════════════════════════════════════╝

Checking workstation WS-ACC-07...

[████████████████████] 100%

WORKSTATION STATUS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Network Connection:      ✓ ACTIVE
Domain Join:             ✓ CONNECTED
Authentication Server:   ✓ REACHABLE
Local Hardware:          ✓ OPERATIONAL
System Services:         ✓ RUNNING
Event Logs:              ✓ NO ERRORS

AUTHENTICATION SERVER STATUS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Active Directory:        ✓ OPERATIONAL
Kerberos:                ✓ OPERATIONAL
LDAP:                    ✓ OPERATIONAL
User Accounts:           500 active
Failed Logins (1 hour):  6 (all user 'karen')

═══════════════════════════════════════════════

DIAGNOSTIC SUMMARY:

All systems are operational. No infrastructure issues detected.

The problem appears to be user-specific or related to the login 
attempt itself, not the network or server infrastructure.

Time spent: 10 minutes

(This diagnostic didn't provide useful information for solving 
the problem, but at least you've confirmed the infrastructure 
is working correctly.)

─────────────────────────────────────────────────
Press any key to return to main menu...
```

---

### **Option 4: View Methodology Checklist**

**Display changes as steps are completed**

#### **Early Game (No Steps Complete)**

```
> 4

╔═══════════════════════════════════════════════╗
║         TROUBLESHOOTING METHODOLOGY           ║
╚═══════════════════════════════════════════════╝

CompTIA Troubleshooting Process:

Step 1: Identify the Problem
□ Gather information
□ Question users
□ Identify symptoms
□ Duplicate problem (if possible)

Step 2: Establish a Theory of Probable Cause
□ Question the obvious
□ Consider multiple approaches
□ Start with simple explanations

Step 3: Test the Theory
□ Test theory to determine cause
□ If theory confirmed, move to next step
□ If theory not confirmed, establish new theory

Step 4: Establish a Plan of Action
□ Consider corporate policies
□ Consider change control
□ Plan rollback strategy

Step 5: Implement the Solution
□ Apply fix
□ Escalate if needed

Step 6: Verify Full System Functionality
□ Verify fix resolves issue
□ Ensure user can perform normal tasks
□ Implement preventive measures

Step 7: Document Findings
□ Document problem description
□ Document solution
□ Document lessons learned

─────────────────────────────────────────────────

Current Progress: 0/7 steps complete
Current Score: [score]

─────────────────────────────────────────────────
Press any key to return to main menu...
```

---

#### **Mid-Game (Some Steps Complete)**

```
> 4

╔═══════════════════════════════════════════════╗
║         TROUBLESHOOTING METHODOLOGY           ║
╚═══════════════════════════════════════════════╝

CompTIA Troubleshooting Process:

✓ Step 1: Identify the Problem (50 pts)
  ✓ Gathered information from user and help desk
  ✓ Observed user attempting login
  ✓ Identified symptoms: "Invalid Password" error

✓ Step 2: Establish a Theory (50 pts)
  ✓ Root cause identified: Caps Lock enabled
  ✓ Theory: Password typed in wrong case

✓ Step 3: Test the Theory (60 pts)
  ✓ Observed Caps Lock indicator light active
  ✓ Verified with authentication logs
  ✓ Theory confirmed

✓ Step 4: Establish a Plan of Action (40 pts)
  ✓ Plan: Inform user about Caps Lock
  ✓ Simple fix, no change control needed
  ✓ Low risk, immediate implementation

□ Step 5: Implement the Solution
  → Go to user's workstation
  → Inform user about Caps Lock issue
  → Have user disable Caps Lock and retry

□ Step 6: Verify Full System Functionality
  → Ensure user can log in successfully
  → Verify applications load correctly
  → Confirm no other issues

□ Step 7: Document Findings
  → Return to desktop to document

─────────────────────────────────────────────────

Current Progress: 4/7 steps complete
Current Score: [score]

Next Action: Go implement the solution

─────────────────────────────────────────────────
Press any key to return to main menu...
```

---

## Methodology Actions (Progressive Unlocking)

### **Option 5: Log Problem Identification (Step 1)**

**Unlock Requirements:**
```python
def check_step_1_unlock():
    required = [
        talked_to_ian,          # Got ticket context
        talked_to_karen,        # Heard user symptoms
        watched_karen_type,     # Observed problem
        checked_workstation_or_logs  # Technical verification
    ]
    return all(required)
```

**When Locked:**
```
> 5

[LOCKED] Log Problem Identification

You haven't gathered enough information yet.

Required before logging Step 1:
□ Talk to help desk about ticket
□ Talk to affected user
□ Observe the problem firsthand
□ Check system logs or workstation

Complete these tasks in the world first.

─────────────────────────────────────────────────
Press any key to return to main menu...
```

---

**When Ready:**
```
> 5

╔═══════════════════════════════════════════════╗
║        STEP 1: IDENTIFY THE PROBLEM           ║
╚═══════════════════════════════════════════════╝

Compiling gathered information...

INFORMATION SOURCES CONSULTED:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ Help Desk (Ian) - Ticket escalation
✓ User (Karen Miller) - Direct symptoms
✓ Workstation observation - Problem reproduction
✓ Authentication logs - Technical data

USER SYMPTOMS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• "Invalid Password" error on login
• User insists password is correct
• Issue started this morning (9:15 AM)
• No recent password changes
• Time pressure: Client meeting at 10:00 AM

TECHNICAL FINDINGS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• Network connectivity: Verified
• Workstation hardware: Operational
• Authentication server: Responding normally
• Other users: No similar reports
• Pattern: Multiple failed login attempts

PROBLEM IDENTIFIED:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
User Karen Miller (Accounting) unable to log into workstation 
WS-ACC-07. Receiving "Invalid Password" error despite entering 
what she believes to be the correct password. Issue isolated to 
this user only. Infrastructure verified operational.

═══════════════════════════════════════════════

✓ Step 1 Complete: Problem Identified

+50 points

Timestamp: [current time]
Time spent on Step 1: [X] minutes

Step 2 will unlock when you discover the root cause.

═══════════════════════════════════════════════

state.set_flag("step_1_complete", True)
state.increment_step()

─────────────────────────────────────────────────
Press any key to return to main menu...
```

---

### **Option 6: Log Theory (Step 2)**

**Unlock Requirements:**
```python
def check_step_2_unlock():
    required = [
        step_1_complete,
        spotted_caps_lock  # Must find actual root cause
    ]
    return all(required)
```

**When Locked (Before Step 1):**
```
> 6

[LOCKED] Log Theory

Complete Step 1 first.

You need to identify the problem before establishing a theory.

─────────────────────────────────────────────────
Press any key to return to main menu...
```

---

**When Locked (After Step 1, Before Finding Caps Lock):**
```
> 6

[LOCKED] Log Theory

Find the root cause in the world first.

You've identified the symptoms, but you haven't discovered 
what's actually causing the login failures.

Go investigate further. Watch the user carefully.
(Coffee might help you spot subtle details.)

─────────────────────────────────────────────────
Press any key to return to main menu...
```

---

**When Ready (After Spotting Caps Lock):**
```
> 6

╔═══════════════════════════════════════════════╗
║       STEP 2: ESTABLISH THEORY                ║
╚═══════════════════════════════════════════════╝

Based on your investigation, the following theory has been 
established:

ROOT CAUSE IDENTIFIED:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Caps Lock key is enabled on user's keyboard

THEORY:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
When the user types her password, the Caps Lock key is active, 
causing the password to be entered with incorrect capitalization.

Windows authentication is case-sensitive for passwords. With 
Caps Lock enabled, the user's password is being typed in the 
wrong case, resulting in authentication failure.

SUPPORTING EVIDENCE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• Caps Lock indicator light observed active on keyboard
• User unaware of Caps Lock state
• Authentication logs show username case change pattern
• Consistent "Invalid Password" errors

PROBABILITY:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
High (95%+)

This is a simple, obvious cause that explains all symptoms.

═══════════════════════════════════════════════

✓ Step 2 Complete: Theory Established

+50 points

Timestamp: [current time]

Next: Test this theory before implementing a solution.

═══════════════════════════════════════════════

state.set_flag("step_2_complete", True)
state.increment_step()

─────────────────────────────────────────────────
Press any key to return to main menu...
```

---

### **Option 7: Log Test Results (Step 3)**

**Unlock Requirements:**
```python
def check_step_3_unlock():
    required = [
        step_2_complete,
        # Auto-unlocks immediately after Step 2
        # Testing happens mentally/observationally
    ]
    return all(required)
```

**When Ready:**
```
> 7

╔═══════════════════════════════════════════════╗
║        STEP 3: TEST THE THEORY                ║
╚═══════════════════════════════════════════════╝

Testing theory: Caps Lock causing password case mismatch

TESTS PERFORMED:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Test 1: Visual Inspection
✓ Observed Caps Lock indicator light is illuminated
✓ User unaware of indicator light
Result: SUPPORTS THEORY

Test 2: Authentication Log Analysis
✓ Username case changes from lowercase to uppercase at 09:22
✓ Pattern consistent with Caps Lock activation
✓ All subsequent attempts show uppercase pattern
Result: SUPPORTS THEORY

Test 3: User Observation
✓ Watched user type password
✓ User does not look at keyboard while typing
✓ User does not notice Caps Lock light
✓ User believes she is typing correctly
Result: SUPPORTS THEORY

THEORY CONFIRMATION:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ THEORY CONFIRMED

All tests support the hypothesis that Caps Lock is enabled and 
causing the password to be typed in the wrong case.

No alternative theories needed.

CONFIDENCE LEVEL: Very High (95%+)

═══════════════════════════════════════════════

✓ Step 3 Complete: Theory Tested and Confirmed

+60 points
[+10 bonus if multiple test methods used]

Timestamp: [current time]

Next: Create an implementation plan.

═══════════════════════════════════════════════

state.set_flag("step_3_complete", True)
state.increment_step()

─────────────────────────────────────────────────
Press any key to return to main menu...
```

---

### **Option 8: Log Implementation Plan (Step 4)**

**Unlock Requirements:**
```python
def check_step_4_unlock():
    required = [
        step_3_complete
    ]
    return all(required)
```

**When Ready:**
```
> 8

╔═══════════════════════════════════════════════╗
║      STEP 4: ESTABLISH PLAN OF ACTION         ║
╚═══════════════════════════════════════════════╝

Generating implementation plan based on confirmed theory...

PROBLEM:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Caps Lock enabled, causing password case mismatch

SOLUTION:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Inform user of Caps Lock state and have them disable it

IMPLEMENTATION STEPS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Go to user's workstation (Karen's Office)
2. Inform user that Caps Lock is enabled
3. Show user the Caps Lock indicator light
4. Have user press Caps Lock key to disable it
5. Have user retry login with Caps Lock off
6. Verify successful authentication

CHANGE CONTROL ASSESSMENT:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Change Control Required: NO
Reason: User education only, no system changes

RISK ASSESSMENT:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Risk Level: MINIMAL
- No system modifications required
- No configuration changes needed
- User action only
- Immediately reversible

ROLLBACK PLAN:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Not applicable (no changes to roll back)
If solution doesn't work: Reassess theory

ESTIMATED TIME:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2-3 minutes

APPROVAL STATUS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Approved - no management sign-off needed for user education

═══════════════════════════════════════════════

✓ Step 4 Complete: Implementation Plan Created

+40 points

Timestamp: [current time]

Next: Go implement this solution in the world.
(Go to Karen's office and talk to her)

═══════════════════════════════════════════════

state.set_flag("step_4_complete", True)
state.increment_step()

─────────────────────────────────────────────────
Press any key to return to main menu...
```

---

### **Option 9: Close Ticket & Document (Step 7)**

**Unlock Requirements:**
```python
def check_step_7_unlock():
    required = [
        step_4_complete,
        solution_implemented,  # Step 5 (happens in world)
        verified_working       # Step 6 (happens in world)
    ]
    return all(required)
```

**When Locked (Before Implementation):**
```
> 9

[LOCKED] Close Ticket & Document

Implement and verify the solution first.

You need to:
□ Implement solution (Step 5) - Go to Karen's office
□ Verify functionality (Step 6) - Ask Karen to test
□ Then return here to document

Steps 5 and 6 happen in the world, not at your desktop.

─────────────────────────────────────────────────
Press any key to return to main menu...
```

---

**When Locked (After Implementation, Before Verification):**
```
> 9

[LOCKED] Close Ticket & Document

Verify full system functionality first.

You've implemented the solution, but you haven't verified that 
everything works correctly.

Step 6 requires verification:
□ User can log in successfully
□ All applications accessible
□ User understands the issue

Go back to Karen's office and verify functionality.

─────────────────────────────────────────────────
Press any key to return to main menu...
```

---

**When Ready (After Full Verification):**
```
> 9

╔═══════════════════════════════════════════════╗
║     STEP 7: DOCUMENT FINDINGS & CLOSE         ║
╚═══════════════════════════════════════════════╝

Generating comprehensive documentation...

Please wait...

[████████████████████] 100%

═══════════════════════════════════════════════

TICKET #4729 - FINAL DOCUMENTATION

PROBLEM DESCRIPTION:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
User Karen Miller (Accounting) unable to authenticate to 
workstation WS-ACC-07. Receiving "Invalid Password" error 
despite entering correct password. Issue began 9:15 AM on 
[current date]. User has urgent client meeting at 10:00 AM.

ROOT CAUSE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Caps Lock key was enabled on keyboard, causing password to be 
entered with incorrect capitalization. Windows authentication 
is case-sensitive for passwords, resulting in authentication 
failure.

SOLUTION IMPLEMENTED:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Identified Caps Lock indicator light was illuminated
2. Informed user of Caps Lock state
3. User pressed Caps Lock key to disable it
4. User successfully authenticated after disabling Caps Lock
5. Verified full system functionality
6. Educated user about Caps Lock indicator light

VERIFICATION COMPLETED:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ User can log in successfully
✓ User locked and re-authenticated successfully
✓ Email accessible
✓ File shares accessible
✓ Applications loading normally
✓ User understands how to identify Caps Lock state

PREVENTIVE MEASURES:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• User educated about Caps Lock indicator light
• User instructed to check keyboard indicators before 
  contacting support for login issues

LESSONS LEARNED:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• Simple user errors can appear as complex system issues
• Direct observation is critical for diagnosis
• User education prevents recurring issues
• Focus and attention to detail reveals obvious solutions

TIME TO RESOLUTION:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[X] minutes (from 9:15 AM to [current time])

User made their 10:00 AM meeting: [YES/NO]

METHODOLOGY COMPLIANCE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ Step 1: Problem identified (50 pts)
✓ Step 2: Theory established (50 pts)
✓ Step 3: Theory tested (60 pts)
✓ Step 4: Plan created (40 pts)
✓ Step 5: Solution implemented (60 pts)
✓ Step 6: Functionality verified (70 pts)
✓ Step 7: Findings documented (70 pts)

Total Methodology Points: 400/400

═══════════════════════════════════════════════

✓ Step 7 Complete: Documentation Finalized

+70 points

═══════════════════════════════════════════════

TICKET #4729 STATUS: CLOSED - RESOLVED

Closing ticket...

Documentation saved to knowledge base.
User notification sent.
Metrics updated.

═══════════════════════════════════════════════

state.set_flag("step_7_complete", True)
state.set_flag("ticket_closed", True)
state.increment_step()

─────────────────────────────────────────────────
Press any key to continue to final score...
```

---

## Special Cases and Edge Cases

### **Skipped Verification Warning**

**If player implements solution but skips verification:**

```
> 9

[LOCKED] Close Ticket & Document

⚠ WARNING: Verification Not Completed

You implemented the solution but did not verify full system 
functionality with the user.

Step 6 of the methodology requires:
✗ User confirmation that issue is resolved
✗ Testing that user can perform normal functions
✗ Verification of preventive measures

Without verification, you cannot guarantee:
• The fix is permanent
• The user understands the solution
• Related issues don't exist

This is a critical methodology violation.

Options:
1. Go back and verify properly (recommended)
2. Close ticket without verification (-70 points)

Enter choice: _
```

---

**If player chooses to close without verification:**

```
> 2

Closing ticket without proper verification...

⚠ METHODOLOGY VIOLATION

-70 points (Skipped Step 6: Verification)

state.set_flag("skipped_verification", True)

Documentation will reflect this omission.

[Proceeds to Step 7 documentation with warning notes]
```

---

### **Attempting to Close Prematurely**

```
> 9

[LOCKED] Close Ticket & Document

You cannot close a ticket that hasn't been resolved.

Current status:
✓ Step 1: Complete
✓ Step 2: Complete
✓ Step 3: Complete
✓ Step 4: Complete
✗ Step 5: NOT COMPLETE - Solution not implemented
✗ Step 6: NOT COMPLETE - Not verified

Go implement the solution first.

─────────────────────────────────────────────────
Press any key to return to main menu...
```

---

## Final Score Screen

**Accessed after closing ticket (Option 9 complete):**

```
╔═══════════════════════════════════════════════════════════════╗
║                    FINAL SCORE REPORT                         ║
╚═══════════════════════════════════════════════════════════════╝

TICKET #4729 - Karen Miller - Login Failure
Status: CLOSED - RESOLVED
Time to Resolution: [X] minutes

METHODOLOGY PERFORMANCE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Step 1: Identify Problem        ✓   50 points
Step 2: Establish Theory         ✓   50 points
Step 3: Test Theory              ✓   60 points
Step 4: Create Plan              ✓   40 points
Step 5: Implement Solution       ✓   60 points
Step 6: Verify Functionality     ✓   70 points
Step 7: Document Findings        ✓   70 points
                                    ─────────
Core Methodology Total:             400 points

BONUS POINTS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Side Quests:
  William's Quest                ✓  100 points
  Donut Quest                    ✓   50 points
  Methodology Note Found         ✓   25 points
  Auth Log Analysis              ✓   25 points
                                    ─────────
Side Quests Subtotal:              200 points

Information Gathering:
  All NPCs Consulted             ✓   50 points
  All Diagnostic Sources         ✓   50 points
  All Relevant Items             ✓   50 points
                                    ─────────
Information Gathering Subtotal:    150 points

Methodology Excellence:
  Correct Theory First Try       ✓   50 points
  Multiple Testing Methods       ✓   50 points
  Thorough Investigation         ✓   50 points
                                    ─────────
Methodology Excellence Subtotal:   150 points

Coffee System:
  Optimal Caffeine (2 coffees)   ✓   30 points
  Maintained Focus               ✓   20 points
                                    ─────────
Coffee System Subtotal:             50 points

Efficiency:
  Zero Mistakes                  ✓   20 points
  Systematic Approach            ✓   30 points
                                    ─────────
Efficiency Subtotal:                50 points

TOTAL BONUS POINTS:                600 points

PENALTIES:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[None]                               0 points

═══════════════════════════════════════════════════════════════

FINAL SCORE: 1000 / 1000

RANK: MASTER TROUBLESHOOTER

═══════════════════════════════════════════════════════════════

PERFORMANCE SUMMARY:

You solved Karen's login problem using perfect troubleshooting 
methodology. Your systematic approach, attention to detail, and 
thorough verification demonstrate exceptional technical skills.

Karen made her meeting on time.
Manager Marcus is extremely impressed.
Your documentation is exemplary.

Achievements Unlocked: [List]

═══════════════════════════════════════════════════════════════

[CONTINUE TO ENDING] [PLAY AGAIN] [QUIT]
```

---

## Implementation Notes

### **Menu State Tracking**

```python
class DesktopMenu:
    def __init__(self):
        self.current_step = 0
        self.steps_complete = {
            1: False,  # Identify
            2: False,  # Theory
            3: False,  # Test
            4: False,  # Plan
            5: False,  # Implement (world)
            6: False,  # Verify (world)
            7: False   # Document
        }
        
    def check_step_unlock(self, step):
        """Check if a methodology step can be unlocked"""
        if step == 1:
            return self.check_step_1_requirements()
        elif step == 2:
            return (self.steps_complete[1] and 
                    game_state.spotted_caps_lock)
        elif step == 3:
            return self.steps_complete[2]
        elif step == 4:
            return self.steps_complete[3]
        elif step == 7:
            return (self.steps_complete[4] and 
                    self.steps_complete[5] and
                    self.steps_complete[6])
        return False
    
    def get_option_state(self, option):
        """Return LOCKED, READY, or DONE for menu option"""
        if option == 5:  # Step 1
            if self.steps_complete[1]:
                return "DONE"
            elif self.check_step_unlock(1):
                return "READY"
            else:
                return "LOCKED"
        # ... etc for other options
```

---

### **Auto-Completion Flags**

```python
# Steps 5 and 6 auto-complete when actions happen in world

# Step 5: Implementation
if game_state.told_karen_about_caps_lock and karen_logged_in:
    desktop.steps_complete[5] = True
    desktop.current_step = max(desktop.current_step, 5)
    award_points(60, "Step 5: Solution Implemented")

# Step 6: Verification
if game_state.karen_verified_functionality:
    desktop.steps_complete[6] = True
    desktop.current_step = max(desktop.current_step, 6)
    award_points(70, "Step 6: Functionality Verified")
```

---

## Summary

**Total Menu Options:** 10 (0-9)  
**Always Available:** 4 (Options 1-4)  
**Progressive Unlock:** 5 (Options 5-9)  
**Exit Option:** 1 (Option 0)

**Menu States:** 6 distinct phases from start to completion

**Core Design Principles:**
1. Desktop confirms discoveries, never makes them
2. All methodology steps must be earned through world actions
3. No guessing or multiple choice
4. Complete audit trail of all actions
5. Automatic documentation generation

---

**End of Desktop Computer Menu System Document**

Complete menu system designed with all states, unlocks, and content.
Ready for implementation or revision.
