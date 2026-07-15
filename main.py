# number guesser
# LAST UPDATED July 15 2026 - 2:23 PM

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# PROBLEM DECOMPOSITION
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Prompts user - "Welcome to a number guessing game. 
# The rules of the game are simple, you the user choose a whole number that is between 1 - 100. 
# The program will prompt the user in the teranial to either say if the number presented is the number you intaly chose, the user will respond with "Yes" or "No"
# If "Yes" then restart game
# If "No" the program will ask the user if there number is "Higher" or "Lower"

# Takes the number and status if higher or lower - based on what was indacted by the user
# Takes guess, determines if higher or lower then finds the difrence between the guess and range
# Sets the range from the guess and the upper ie 100 or lower ie 1 limite 
# Takes the difrence between the range and guess 
#  divids by two 
#  if higher adds that amount to the most recent
#  if lower subtracts that amount from the most recent guess
# prints the new guess - asks user is this your number?
# if Yes, print ("Good Game! Want to play another round?") 
# if no then prompts higher or lower 

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# LOGIC
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
print("Welcome to a number guessing game.")
print("Here are the rules.")
print("The user choose a whole number that is between 1 and 100.")
print("The program will try to guess the users number")
print("The program will ask the user if its guess is correct")

print("If it is, the users number, they will respond yes")
print("Good Game! Want to play another round?")


print("If it is not, the users number, they will respond no")
print("The program will ask the user if there number is higher or lower than the previous guess")

# if the user responds "higher" THAN it calculates the diffrence between the most recent guess and upper limit, 
# it divides the difference by two, assigns that number to the varible difference 
# 

# if higher add the diffrence to the most recent guess 
# if lower subtract the diffrence from the most recent guess 

print("is your number <<<INSERT>>>")

# if yes ---> print("Good Game! Want to play another round?")

# if no --> print("Is your number higher or lower") 
# repates logic 
# loops until the program corectly gusses the users number

"""
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# HELPER FUNCTIONS
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def get_yes_no_input(prompt):
    """given a prompt string
    return the raw user input, stripped and lowercased"""
    return input(prompt).strip().lower()


def is_yes(response):
    """given a response string
    return True if it means yes, False otherwise"""
    return response in ("yes", "y")


def is_higher(response):
    """given a response string
    return True if it means higher, False if it means lower"""
    return response in ("higher", "h")


def calculate_midpoint(low, high):
    """given a low and high bound
    return the midpoint between them"""
    return (low + high) // 2


def update_low(guess):
    """given the most recent guess
    return the new low bound"""
    return guess + 1


def update_high(guess):
    """given the most recent guess
    return the new high bound"""
    return guess - 1


def print_guess(guess):
    """given a guess
    print the question asking if it is the user's number"""
    print(f"Is your number {guess}?")


def print_intro():
    """print the welcome message and rules
    return nothing"""
    print("Welcome to the Number Guessing Game!")
    print("Think of a whole number between 1 and 100.")
    print("The program will try to guess your number.")
    print("After each guess, tell it 'Yes' if correct.")
    print("If not, tell it 'Higher' or 'Lower' to guide the next guess.")


def print_win_message():
    """print the message shown when the guess is correct
    return nothing"""
    print("Good game! Want to play another round?")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# MAIN FUNCTIONS
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

print_intro()

low = 1
high = 100
guess = calculate_midpoint(low, high)

while True:
    print_guess(guess)
    response = get_yes_no_input("Yes or No: ")

    if is_yes(response):
        print_win_message()
        break
    else:
        direction_response = get_yes_no_input("Higher or Lower: ")

        if is_higher(direction_response):
            low = update_low(guess)
        else:
            high = update_high(guess)

        guess = calculate_midpoint(low, high)

