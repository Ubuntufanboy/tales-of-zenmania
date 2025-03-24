import sys
import time
import random
from colorama import init, Fore, Style

# Initialize colorama with autoreset on since I don't wanna keep doing RESET
init(autoreset=True)

class TalesOfZenmania:
    def __init__(self):
        self.player_name = ""
        self.reputation_score = 50
        self.code_freedom = 0
        self.inventory = []

    def typewriter_print(self, text, color=Fore.WHITE, delay=0.05):
        for char in text:
            sys.stdout.write(color + char)
            #sys.stdout.flush()
            time.sleep(delay)
        print(Style.RESET_ALL)

    def slow_input(self, prompt, color=Fore.CYAN):
        self.typewriter_print(prompt, color)
        return input()

    def game_over(self, message):
        self.typewriter_print(f"\n{Fore.RED}GAME OVER: {message}", Fore.RED)
        sys.exit(0)

    def intro(self):
        self.typewriter_print(f"=== TALES OF ZENMANIA ===", Fore.MAGENTA)
        self.typewriter_print(f"A Dystopian Coding Rebellion", Fore.YELLOW)
        time.sleep(1)
        
        self.player_name = self.slow_input(f"\nEnter your name, rebel programmer: ", Fore.GREEN)
        
        self.typewriter_print(f"\nWelcome, {self.player_name}. The year is 2084.", Fore.CYAN)
        self.typewriter_print(f"In the megacity of Zenmania, code is controlled. Algorithms dictate life.", Fore.WHITE)
        time.sleep(1)

    def scene_1_underground_network(self):
        self.typewriter_print(f"\nYou're in a dimly lit underground coding den.", Fore.GREEN)
        self.typewriter_print(f"Rebel programmers huddle around vintage computers, writing forbidden open-source code.", Fore.WHITE)
        
        choice = self.slow_input("\nDo you want to (J)oin the network or (H)esitate? ")
        
        if choice.lower() == 'j':
            self.reputation_score += 10
            self.code_freedom += 1
            self.typewriter_print(f"You've joined the resistance! Your first mission awaits...", Fore.BLUE)
        else:
            self.reputation_score -= 10
            self.game_over("Fear consumed you. The system wins.")

    def scene_2_code_rebellion(self):
        self.typewriter_print(f"\nA high-stakes coding challenge appears!", Fore.RED)
        self.typewriter_print(f"Break through the system's firewall using your unique algorithm.", Fore.WHITE)
        
        challenge = self.slow_input("\nChoose your approach: (A)nonymous proxy or (D)ecentralized hack? ")
        
        if challenge.lower() == 'a':
            self.inventory.append("anonymity_module")
            self.reputation_score += 15
            self.typewriter_print(f"Successful stealth infiltration!", Fore.GREEN)
        else:
            self.reputation_score -= 15
            self.game_over("System detected. Elimination protocol activated.")

    def scene_3_data_liberation(self):
        self.typewriter_print(f"\nYou discover hidden data archives.", Fore.MAGENTA)
        self.typewriter_print(f"Classified information about the regime's control algorithms.", Fore.WHITE)
        
        choice = self.slow_input("\nDo you (L)iberate the data or (P)reserve caution? ")
        
        if choice.lower() == 'l':
            self.code_freedom += 2
            self.typewriter_print(f"Data leaked! The world will know the truth.", Fore.YELLOW)
        else:
            self.game_over("Opportunity lost. The system remains unchallenged.")

    def scene_4_quantum_crossroads(self):
        self.typewriter_print(f"\nQuantum encryption challenge!", Fore.CYAN)
        self.typewriter_print(f"Break the unbreakable code or face total surveillance.", Fore.WHITE)
        
        if "anonymity_module" in self.inventory:
            self.typewriter_print(f"Your previous stealth module helps you crack the encryption!", Fore.GREEN)
            self.code_freedom += 3
        else:
            choice = self.slow_input("\nAttempt (B)rute force or (S)ubtle manipulation? ")
            if choice.lower() == 'b':
                self.game_over("Quantum encryption defeated you. System traces activated.")

    def scene_5_ai_confrontation(self):
        self.typewriter_print(f"\nFace-to-face with the Zentral AI.", Fore.RED)
        self.typewriter_print(f"The ultimate test of your coding rebellion.", Fore.WHITE)
        
        if self.code_freedom >= 5:
            self.typewriter_print(f"Your accumulated skills allow you to challenge the AI!", Fore.GREEN)
            self.reputation_score += 30
        else:
            self.game_over("AI overwhelms your limited capabilities.")

    def scene_6_final_algorithm(self):
        self.typewriter_print(f"\nThe final algorithm that could liberate Zenmania.", Fore.BLUE)
        self.typewriter_print(f"One line of code can change everything.", Fore.WHITE)
        
        solution = self.slow_input("\nEnter the liberation code (hint: What is this software?): ")
        
        if solution.lower() == "opensource":
            self.typewriter_print(f"Code accepted! System disruption initiated!", Fore.GREEN)
            self.code_freedom = 10
        else:
            self.game_over("Incorrect code. System integrity maintained.")

    def epilogue(self):
        if self.code_freedom == 10:
            self.typewriter_print(f"\nVICTORY! Zenmania's control system has been dismantled.", Fore.GREEN)
            self.typewriter_print(f"You've liberated the city through the power of code and rebellion!", Fore.YELLOW)
        else:
            self.game_over("The system's grip remains unbroken.")

    def play(self):
        try:
            self.intro()
            self.scene_1_underground_network()
            self.scene_2_code_rebellion()
            self.scene_3_data_liberation()
            self.scene_4_quantum_crossroads()
            self.scene_5_ai_confrontation()
            self.scene_6_final_algorithm()
            self.epilogue()
        except Exception as e:
            self.typewriter_print(f"\nAn unexpected error in the system: {e}", Fore.RED)

def main():
    game = TalesOfZenmania()
    game.play()

if __name__ == "__main__":
    main()
