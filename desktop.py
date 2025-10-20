"""
Desktop Computer Menu System
Provides ticket details, logs, diagnostics, and methodology tracking
"""

from utils import print_boxed, print_separator, clear_screen, display_choices


class DesktopMenu:
    """Desktop computer interface"""
    
    def __init__(self, game_state):
        self.game_state = game_state
        
    def show(self, game_state):
        """Show desktop menu"""
        while True:
            print()
            self.show_header(game_state)
            choice = self.show_main_menu(game_state)

            if choice == 0:
                print("\nLogging out of desktop...")
                break
            elif choice == 1:
                self.view_ticket_details(game_state)
            elif choice == 2:
                self.check_auth_logs(game_state)
            elif choice == 3:
                self.run_diagnostics(game_state)
            elif choice == 4:
                self.view_methodology(game_state)
            elif choice == 5:
                self.log_step_1(game_state)
            elif choice == 6:
                self.log_step_2(game_state)
            elif choice == 7:
                self.log_step_3(game_state)
            elif choice == 8:
                self.log_step_4(game_state)
            elif choice == 9:
                self.log_step_7(game_state)
                
    def show_header(self, game_state):
        """Show desktop header"""
        print_boxed("IT SUPPORT DESKTOP")
        print()
        print("TICKET #4729 - Karen Miller - Printing Issue")
        print(f"Status: {self.get_status(game_state)}")
        print(f"Current Step: {game_state.current_step}/7")
        print()
        
    def get_status(self, game_state):
        """Get current ticket status"""
        if game_state.steps_complete[7]:
            return "CLOSED - RESOLVED"
        elif game_state.karen_problem_fixed:
            return "READY TO CLOSE"
        elif game_state.steps_complete[4]:
            return "READY FOR IMPLEMENTATION"
        elif game_state.spotted_wrong_network:
            return "ROOT CAUSE FOUND"
        elif game_state.steps_complete[1]:
            return "INVESTIGATING"
        else:
            return "ASSIGNED"
            
    def show_main_menu(self, game_state):
        """Show main menu options"""
        print("AVAILABLE ACTIONS:")
        print_separator()
        print("1. View Ticket Details")
        print("2. Check Network Connection Logs")
        print("3. Run Diagnostics")
        print("4. View Methodology Checklist")
        print()
        print("METHODOLOGY ACTIONS:")
        print_separator()
        
        # Step 1
        self.print_step_option(5, "Log Problem Identification", 
                              game_state.steps_complete[1],
                              game_state.check_step_1_unlock())
                              
        # Step 2
        self.print_step_option(6, "Log Theory",
                              game_state.steps_complete[2],
                              game_state.check_step_2_unlock())
                              
        # Step 3
        self.print_step_option(7, "Log Test Results",
                              game_state.steps_complete[3],
                              game_state.check_step_3_unlock())
                              
        # Step 4
        self.print_step_option(8, "Log Implementation Plan",
                              game_state.steps_complete[4],
                              game_state.check_step_4_unlock())
                              
        # Step 7
        self.print_step_option(9, "Close Ticket & Document",
                              game_state.steps_complete[7],
                              game_state.check_step_7_unlock())
                              
        print_separator()
        print("0. Log Off")
        print()
        
        try:
            choice = int(input("Enter option: ").strip())
            return choice
        except ValueError:
            return -1
            
    def print_step_option(self, num, name, completed, unlocked):
        """Print a methodology step option"""
        if completed:
            print(f"✓ {num}. [DONE] {name}")
        elif unlocked:
            print(f"★ {num}. [READY] {name}")
        else:
            print(f"{num}. [LOCKED] {name}")
            
    def view_ticket_details(self, game_state):
        """View full ticket details"""
        clear_screen()
        print_boxed("TICKET DETAILS")
        print()
        print("TICKET #4729 - PRINTING ISSUE")
        print()
        print("Reported by: Karen Miller (Accounting)")
        print("Workstation: WS-ACC-07")
        print("Time Reported: 9:15 AM")
        print("Priority: MEDIUM")
        print("Escalated by: Ian (Help Desk)")
        print()
        print("DESCRIPTION:")
        print("User unable to print to network printer (Accounting_Printer_Floor2).")
        print("Print dialog displays 'No printers found' message.")
        print("User needs to print quarterly reports for client meeting.")
        print()
        print("TROUBLESHOOTING COMPLETED BY HELP DESK:")
        print("- Network connectivity verified (ping successful)")
        print("- Printer power and hardware checked (operational)")
        print("- Print spooler service verified (running)")
        print("- No similar reports from other users")
        print("- User has client meeting at 10:00 AM")
        print()
        print("STATUS: Escalated to IT Support")
        print()
        print("NOTES:")
        print("User becoming increasingly frustrated. Urgent resolution needed.")


        game_state.advance_time(2)
        
    def check_auth_logs(self, game_state):
        """Check network connection logs"""
        clear_screen()
        print_boxed("NETWORK CONNECTION LOGS - WS-ACC-07")
        print()

        if game_state.has_focus_buff() or game_state.redbull_consumed:
            # Enhanced view with focus
            print("Your focused mind processes the logs carefully...")
            print()
            print("09:05:12 - CONNECTED - SSID: Corp_Network - IP: 10.1.2.45")
            print("09:14:33 - DISCONNECTED - SSID: Corp_Network")
            print_separator("-", 60)
            print("Connection change detected at 09:14:55 →")
            print_separator("-", 60)
            print("09:14:55 - CONNECTED - SSID: Guest_WiFi - IP: 192.168.100.23")
            print("09:15:01 - DHCP_LEASE - Gateway: 192.168.100.1")
            print("09:15:03 - DNS_REQUEST - google.com - SUCCESS")
            print("09:15:45 - SMB_CONNECTION_FAILED - \\\\fileserver\\accounting")
            print("09:16:22 - PRINTER_DISCOVERY_FAILED - No network printers found")
            print()
            print("✓ PATTERN IDENTIFIED")
            print()
            print("The workstation switched from 'Corp_Network' to 'Guest_WiFi'")
            print("at 09:14:55.")
            print()
            print("Guest network allows internet but blocks internal resources!")
            print()

            if not game_state.check_flag('noticed_network_change'):
                game_state.set_flag('noticed_network_change', True)
                game_state.add_score(10, "Noticed network change in logs")
        else:
            # Normal view - pattern not obvious
            print("Network connection events for WS-ACC-07:")
            print()
            print("09:05:12 - CONNECTED - SSID: Corp_Network")
            print("09:14:33 - DISCONNECTED - SSID: Corp_Network")
            print("09:14:55 - CONNECTED - SSID: Guest_WiFi")
            print("09:15:45 - SMB_CONNECTION_FAILED - \\\\fileserver\\accounting")
            print("09:16:22 - PRINTER_DISCOVERY_FAILED - No network printers found")
            print()
            print("Workstation has network connectivity")
            print("Internet access confirmed")
            print("Some internal resource access failures")
            print()
            print("The logs show some failed connections, but no obvious")
            print("pattern is visible.")
            print()
            print("(You might notice more details with better focus.)")

        if not game_state.checked_logs:
            game_state.checked_logs = True
            game_state.add_score(5, "Checked network logs")


        game_state.advance_time(3)
        
    def run_diagnostics(self, game_state):
        """Run network diagnostics (time-waster)"""
        clear_screen()
        print_boxed("RUNNING SYSTEM DIAGNOSTICS")
        print()
        print("Checking workstation WS-ACC-07...")
        print()
        print("[████████████████████] 100%")
        print()
        print("WORKSTATION STATUS:")
        print_separator()
        print("Network Connection:      ✓ ACTIVE")
        print("Internet Access:         ✓ WORKING")
        print("Printer Hardware:        ✓ OPERATIONAL")
        print("Local Hardware:          ✓ OPERATIONAL")
        print()
        print("DIAGNOSTIC SUMMARY:")
        print()
        print("All systems are operational. No infrastructure issues detected.")
        print()
        print("The problem appears to be user-specific or related to network")
        print("configuration, not hardware or basic connectivity.")
        print()
        print("Time spent: 10 minutes")
        print()
        print("(This diagnostic didn't provide useful information for solving")
        print("the problem, but at least you've confirmed infrastructure is OK.)")


        game_state.advance_time(10)
        
    def view_methodology(self, game_state):
        """View methodology checklist"""
        clear_screen()
        print_boxed("TROUBLESHOOTING METHODOLOGY")
        print()
        print("CompTIA Troubleshooting Process:")
        print()
        
        self.print_step_status(1, "Identify the Problem", game_state)
        self.print_step_status(2, "Establish a Theory", game_state)
        self.print_step_status(3, "Test the Theory", game_state)
        self.print_step_status(4, "Establish a Plan", game_state)
        self.print_step_status(5, "Implement Solution", game_state)
        self.print_step_status(6, "Verify Functionality", game_state)
        self.print_step_status(7, "Document Findings", game_state)
        
        print()
        print(f"Current Progress: {game_state.current_step}/7 steps complete")
        print(f"Current Score: {game_state.score}")
        
        
        
    def print_step_status(self, num, name, game_state):
        """Print status of a methodology step"""
        if game_state.steps_complete[num]:
            print(f"✓ Step {num}: {name}")
        else:
            print(f"□ Step {num}: {name}")
            
    def log_step_1(self, game_state):
        """Log Step 1: Identify the Problem"""
        clear_screen()
        
        if game_state.steps_complete[1]:
            print_boxed("STEP 1: IDENTIFY THE PROBLEM [DONE]")
            print()
            print("You already completed this step.")
            
            return
            
        if not game_state.check_step_1_unlock():
            print_boxed("STEP 1: LOCKED")
            print()
            print("You haven't gathered enough information yet.")
            print()
            print("Required before logging Step 1:")
            print(f"{'✓' if game_state.talked_to_ian else '□'} Talk to help desk about ticket")
            print(f"{'✓' if game_state.talked_to_karen else '□'} Talk to affected user")
            print(f"{'✓' if game_state.checked_network_settings else '□'} Investigate the problem")
            print()
            print("Complete these tasks in the world first.")

            return

        # Log Step 1
        print_boxed("STEP 1: IDENTIFY THE PROBLEM")
        print()
        print("INFORMATION SOURCES CONSULTED:")
        print_separator()
        print("✓ Help Desk (Ian) - Ticket escalation")
        print("✓ User (Karen Miller) - Direct symptoms")
        print("✓ Workstation investigation - Network settings checked")
        print()
        print("PROBLEM IDENTIFIED:")
        print_separator()
        print("User Karen Miller (Accounting) unable to print to network printer")
        print("from workstation WS-ACC-07. Print dialog shows 'No printers found'")
        print("despite printer being operational. Issue started this morning.")
        print()
        
        game_state.complete_step(1, 50)
        
        print_separator()
        print("✓ Step 1 Complete: Problem Identified")
        print("+50 points")
        print_separator()
        print()
        print("Step 2 will unlock when you discover the root cause.")
        
        
        game_state.advance_time(5)
        
    def log_step_2(self, game_state):
        """Log Step 2: Establish Theory"""
        clear_screen()
        
        if game_state.steps_complete[2]:
            print_boxed("STEP 2: ESTABLISH THEORY [DONE]")
            print()
            print("You already completed this step.")
            
            return
            
        if not game_state.check_step_2_unlock():
            print_boxed("STEP 2: LOCKED")
            print()
            if not game_state.steps_complete[1]:
                print("Complete Step 1 first.")
            else:
                print("Find the root cause in the world first.")
                print()
                print("You've identified the symptoms, but you haven't discovered")
                print("what's actually causing the printing problem.")
                print()
                print("Go investigate further. Check network settings carefully.")
                print("(Coffee might help you spot subtle details.)")

            return

        # Log Step 2
        print_boxed("STEP 2: ESTABLISH THEORY")
        print()
        print("ROOT CAUSE IDENTIFIED:")
        print_separator()
        print("User connected to Guest_WiFi instead of Corp_Network")
        print()
        print("THEORY:")
        print_separator()
        print("The Guest WiFi network provides internet access for visitors")
        print("but blocks access to internal corporate resources for security.")
        print()
        print("Network printers, file shares, and internal applications are")
        print("only accessible from the Corp_Network. User must have accidentally")
        print("connected to Guest_WiFi this morning instead of Corp_Network.")
        print()
        
        game_state.complete_step(2, 50)
        
        print_separator()
        print("✓ Step 2 Complete: Theory Established")
        print("+50 points")
        print_separator()
        
        
        game_state.advance_time(3)
        
    def log_step_3(self, game_state):
        """Log Step 3: Test Theory"""
        clear_screen()
        
        if game_state.steps_complete[3]:
            print_boxed("STEP 3: TEST THEORY [DONE]")
            print()
            print("You already completed this step.")
            
            return
            
        if not game_state.check_step_3_unlock():
            print_boxed("STEP 3: LOCKED")
            print()
            print("Complete Step 2 first.")
            
            return
            
        # Log Step 3
        print_boxed("STEP 3: TEST THEORY")
        print()
        print("THEORY: Wrong network (Guest_WiFi vs Corp_Network)")
        print()
        print("TESTS PERFORMED:")
        print_separator()
        print("✓ Checked WiFi settings - connected to Guest_WiFi")
        print("✓ Verified internet access works (public sites load)")
        print("✓ Confirmed printer discovery fails on Guest_WiFi")
        print("✓ Network logs show switch from Corp to Guest at 9:14 AM")
        print()
        print("THEORY CONFIRMATION:")
        print_separator()
        print("✓ THEORY CONFIRMED")
        print()
        print("All tests support the hypothesis that Guest_WiFi network")
        print("blocks internal resources while allowing internet access.")
        print()
        
        game_state.complete_step(3, 60)
        
        print_separator()
        print("✓ Step 3 Complete: Theory Tested and Confirmed")
        print("+60 points")
        print_separator()
        
        
        game_state.advance_time(3)
        
    def log_step_4(self, game_state):
        """Log Step 4: Create Plan"""
        clear_screen()
        
        if game_state.steps_complete[4]:
            print_boxed("STEP 4: PLAN OF ACTION [DONE]")
            print()
            print("You already completed this step.")
            
            return
            
        if not game_state.check_step_4_unlock():
            print_boxed("STEP 4: LOCKED")
            print()
            print("Complete Step 3 first.")
            
            return
            
        # Log Step 4
        print_boxed("STEP 4: ESTABLISH PLAN OF ACTION")
        print()
        print("SOLUTION:")
        print_separator()
        print("Disconnect from Guest_WiFi and reconnect to Corp_Network")
        print()
        print("IMPLEMENTATION STEPS:")
        print("1. Go to user's office")
        print("2. Inform user they're on the wrong network (Guest_WiFi)")
        print("3. Show user the WiFi settings")
        print("4. Have user disconnect from Guest_WiFi")
        print("5. Have user connect to Corp_Network")
        print("6. Verify printer discovery and file share access works")
        print()
        print("RISK ASSESSMENT: MINIMAL")
        print("CHANGE CONTROL: Not required (network configuration only)")
        print()
        
        game_state.complete_step(4, 40)
        
        print_separator()
        print("✓ Step 4 Complete: Implementation Plan Created")
        print("+40 points")
        print_separator()
        print()
        print("Next: Go implement this solution in the world.")
        print("(Go to Karen's office and talk to her)")
        
        
        game_state.advance_time(3)
        
    def log_step_7(self, game_state):
        """Log Step 7: Document & Close"""
        clear_screen()
        
        if game_state.steps_complete[7]:
            print_boxed("STEP 7: DOCUMENTATION [DONE]")
            print()
            print("Ticket already closed.")
            
            return
            
        if not game_state.check_step_7_unlock():
            print_boxed("STEP 7: LOCKED")
            print()
            print("Implement and verify the solution first.")
            print()
            print("You need to:")
            print(f"{'✓' if game_state.steps_complete[4] else '□'} Create plan (Step 4)")
            print(f"{'✓' if game_state.told_karen_about_network and game_state.karen_problem_fixed else '□'} Implement solution (Step 5)")
            print(f"{'✓' if game_state.karen_verified_working else '□'} Verify functionality (Step 6)")
            print()
            print("Steps 5 and 6 happen in the world, not at your desktop.")
            
            return
            
        # Complete Step 7
        clear_screen()
        print_boxed("STEP 7: DOCUMENT FINDINGS & CLOSE")
        print()
        print("Generating comprehensive documentation...")
        print()
        
        
        clear_screen()
        print_boxed("TICKET #4729 - FINAL DOCUMENTATION")
        print()
        print("PROBLEM DESCRIPTION:")
        print_separator()
        print("User Karen Miller (Accounting) unable to print to network printer")
        print("from workstation WS-ACC-07. Print dialog shows 'No printers found'.")
        print("User needs to print quarterly reports. Issue began 9:15 AM.")
        print()
        print("ROOT CAUSE:")
        print_separator()
        print("Workstation connected to Guest_WiFi instead of Corp_Network.")
        print("Guest network provides internet but blocks internal resources.")
        print()
        print("SOLUTION IMPLEMENTED:")
        print_separator()
        print("1. Identified workstation on Guest_WiFi network")
        print("2. Informed user of incorrect network connection")
        print("3. User disconnected from Guest_WiFi")
        print("4. User connected to Corp_Network")
        print("5. Printer discovery successful, printing functional")
        print("6. Verified file share access restored")
        print()
        print("VERIFICATION:")
        print_separator()
        if game_state.karen_verified_working:
            print("✓ Network printing functional")
            print("✓ File shares accessible")
            print("✓ Internal applications accessible")
            print("✓ User made 10:00 AM meeting")
        else:
            print("⚠ Verification skipped")
        print()
        
        game_state.complete_step(7, 70)
        
        print_separator()
        print("✓ Step 7 Complete: Documentation Finalized")
        print("+70 points")
        print_separator()
        print()
        print("TICKET #4729 STATUS: CLOSED - RESOLVED")
        print()
        
        input("Press Enter to view final score...")
        game_state.advance_time(5)
