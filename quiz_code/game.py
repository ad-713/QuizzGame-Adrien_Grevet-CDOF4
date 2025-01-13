import random
from colorama import init, Fore, Style
from .questions import QUESTIONS

init(autoreset=True)

class QuizGame:
    def __init__(self):
        self.score = 0
        self.questions = QUESTIONS.copy()
        random.shuffle(self.questions)
    
    def display_welcome(self):
        print(Fore.CYAN + "\n=== Welcome to the Quiz Game! ===\n" + Style.RESET_ALL)
        print("Answer the following questions by entering the number of your choice.\n")
    
    def display_question(self, question, options):
        print(Fore.YELLOW + f"\n{question}\n" + Style.RESET_ALL)
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")
    
    def get_answer(self):
        while True:
            try:
                choice = int(input("\nYour answer (1-4): "))
                if 1 <= choice <= 4:
                    return choice - 1
                print(Fore.RED + "Please enter a number between 1 and 4." + Style.RESET_ALL)
            except ValueError:
                print(Fore.RED + "Please enter a valid number." + Style.RESET_ALL)
    
    def play(self):
        self.display_welcome()
        
        for q in self.questions:
            self.display_question(q['question'], q['options'])
            user_answer = self.get_answer()
            
            if user_answer == q['correct']:
                self.score += 1
                print(Fore.GREEN + "Correct!" + Style.RESET_ALL)
            else:
                print(Fore.RED + f"Wrong! The correct answer was: {q['options'][q['correct']]}" + Style.RESET_ALL)
        
        self.display_final_score()
    
    def display_final_score(self):
        print(Fore.CYAN + "\n=== Game Over! ===\n" + Style.RESET_ALL)
        print(f"Your final score: {self.score}/{len(self.questions)}")
        percentage = (self.score / len(self.questions)) * 100
        print(f"Percentage: {percentage:.1f}%")
        
        if percentage == 100:
            print(Fore.GREEN + "Perfect score! Congratulations!" + Style.RESET_ALL)
        elif percentage >= 80:
            print(Fore.GREEN + "Great job!" + Style.RESET_ALL)
        elif percentage >= 60:
            print(Fore.YELLOW + "Not bad! Keep practicing!" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Better luck next time!" + Style.RESET_ALL)
