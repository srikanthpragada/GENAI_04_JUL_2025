# Create code for number guessing game where user gets 3 attenpts to guess a number between 1 and 25
# Provide hints if the guess is too high or too low

import random
class NumberGuessingGame:
    def __init__(self):
        self.number_to_guess = random.randint(1, 25)
        self.attempts = 3

    def guess(self, user_guess):
        if user_guess < 1 or user_guess > 25:
            return "Please guess a number between 1 and 25."
        
        if self.attempts <= 0:
            return "No attempts left. Game over!"
        
        if user_guess < self.number_to_guess:
            self.attempts -= 1
            return f"Too low! You have {self.attempts} attempts left."
        elif user_guess > self.number_to_guess:
            self.attempts -= 1
            return f"Too high! You have {self.attempts} attempts left."
        else:
            return "Congratulations! You've guessed the number!"