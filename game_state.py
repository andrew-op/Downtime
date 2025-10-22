"""
Game State Management
Tracks all game variables, flags, and progress
"""

import time


class GameState:
    """Manages all game state variables"""
    
    def __init__(self):
        # Time tracking (in-game)
        self.start_time = 945  # 9:45 AM in minutes from midnight
        self.minutes = 0  # Minutes elapsed since start

        # Real-world play time tracking
        self.real_start_time = time.time()  # Unix timestamp when game started
        
        # Location
        self.current_location = "it_office"
        
        # Inventory
        self.inventory = []
        
        # Score tracking
        self.score = 0
        self.methodology_score = 0
        self.bonus_score = 0
        
        # Methodology progress
        self.current_step = 0
        self.steps_complete = {
            1: False,  # Identify
            2: False,  # Theory
            3: False,  # Test
            4: False,  # Plan
            5: False,  # Implement
            6: False,  # Verify
            7: False   # Document
        }
        
        # Coffee/Caffeine system
        self.caffeine_level = 0  # 0-5 scale
        self.coffees_consumed = 0
        self.has_redbull = False
        self.redbull_consumed = False

        # Money system
        self.money = 0  # Dollars
        
        # NPC interaction flags
        self.talked_to_ian = False
        self.talked_to_karen = False
        self.talked_to_marcus = False
        self.talked_to_william = False
        
        # Investigation flags
        self.checked_network_settings = False
        self.spotted_wrong_network = False
        self.checked_printer = False
        self.checked_logs = False
        self.checked_file_shares = False

        # Quest flags
        self.william_quest_started = False
        self.william_quest_complete = False
        self.donut_heist_started = False
        self.donut_heist_complete = False
        self.knows_needs_money = False  # Player has discovered they need $2

        # Solution implementation
        self.told_karen_about_network = False
        self.karen_problem_fixed = False
        self.karen_verified_working = False
        
        # Desktop computer state
        self.desktop_unlocked = False
        
        # Misc flags
        self.flags = {}
        
    def advance_time(self, minutes):
        """Advance game time by specified minutes"""
        self.minutes += minutes
        
    def get_time_string(self):
        """Get current in-game time as readable string"""
        total_minutes = self.start_time + self.minutes
        hours = total_minutes // 60
        mins = total_minutes % 60

        # Convert to 12-hour format
        period = "AM" if hours < 12 else "PM"
        display_hours = hours if hours <= 12 else hours - 12
        if display_hours == 0:
            display_hours = 12

        return f"{display_hours}:{mins:02d} {period}"

    def get_real_play_time(self):
        """Get real-world elapsed play time as readable string"""
        elapsed_seconds = int(time.time() - self.real_start_time)
        minutes = elapsed_seconds // 60
        seconds = elapsed_seconds % 60

        if minutes > 0:
            return f"{minutes} minute{'s' if minutes != 1 else ''} {seconds} second{'s' if seconds != 1 else ''}"
        else:
            return f"{seconds} second{'s' if seconds != 1 else ''}"

    def get_caffeine_level_name(self):
        """Get descriptive caffeine level"""
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

    def get_focus_description(self):
        """Get focus buff description"""
        if self.caffeine_level >= 6:
            return "CRITICAL - Seek medical attention"
        elif self.caffeine_level == 5:
            return "Dangerously overcaffeinated"
        elif self.redbull_consumed or self.caffeine_level >= 2:
            return "Focused (Enhanced perception)"
        elif self.caffeine_level == 1:
            return "Normal"
        else:
            return "Sluggish"

    def has_focus_buff(self):
        """Check if player has beneficial focus buff"""
        return self.caffeine_level >= 2 or self.redbull_consumed
        
    def add_score(self, points, reason=""):
        """Add points to score"""
        self.score += points
        if reason:
            print(f"\n+{points} points ({reason})")
            
    def set_flag(self, flag_name, value=True):
        """Set a flag"""
        self.flags[flag_name] = value
        
    def check_flag(self, flag_name):
        """Check if flag is set"""
        return self.flags.get(flag_name, False)
        
    def complete_step(self, step_num, points):
        """Mark a methodology step as complete"""
        if not self.steps_complete[step_num]:
            self.steps_complete[step_num] = True
            self.current_step = max(self.current_step, step_num)
            self.methodology_score += points
            self.score += points
            
    def check_step_1_unlock(self):
        """Check if Step 1 can be unlocked"""
        return (self.talked_to_ian and
                self.talked_to_karen and
                self.checked_network_settings)

    def check_step_2_unlock(self):
        """Check if Step 2 can be unlocked"""
        return self.steps_complete[1] and self.spotted_wrong_network
        
    def check_step_3_unlock(self):
        """Check if Step 3 can be unlocked"""
        return self.steps_complete[2]
        
    def check_step_4_unlock(self):
        """Check if Step 4 can be unlocked"""
        return self.steps_complete[3]
        
    def check_step_7_unlock(self):
        """Check if Step 7 (documentation) can be unlocked"""
        return (self.steps_complete[4] and 
                self.steps_complete[5] and 
                self.steps_complete[6])
                
    def check_win_condition(self):
        """Check if player has won"""
        return self.steps_complete[7]
        
    def calculate_final_score(self):
        """Calculate final score with all bonuses"""
        # Already tracked in self.score
        return self.score
        
    def get_rank(self):
        """Get rank based on final score"""
        score = self.score
        if score >= 950:
            return "MASTER TROUBLESHOOTER"
        elif score >= 850:
            return "EXPERT TECHNICIAN"
        elif score >= 750:
            return "SKILLED PROFESSIONAL"
        elif score >= 650:
            return "COMPETENT SUPPORT"
        elif score >= 500:
            return "ADEQUATE PERFORMANCE"
        else:
            return "NEEDS IMPROVEMENT"
