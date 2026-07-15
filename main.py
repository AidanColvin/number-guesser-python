# Number Guesser


def guess_number(current_guess):
    """Ask user if the guess is correct.
    Takes: current_guess (int) - the number to guess
    Returns: bool - True if user says yes, False otherwise
    """
    while True:
        response = input(f"Is your number {current_guess}? (yes/no): ").strip().lower()
        if response in ("yes", "y"):
            return True
        if response in ("no", "n"):
            return False
        print("Please answer yes or no.")


def get_direction():
    """Ask user if number is higher or lower.
    Takes: nothing
    Returns: str - "higher" or "lower"
    """
    while True:
        direction = input("Higher or Lower? ").strip().lower()
        if direction in ("higher", "h"):
            return "higher"
        if direction in ("lower", "l"):
            return "lower"
        print("Please answer higher or lower.")


def midpoint(low, high):
    """Calculate midpoint between two numbers.
    Takes: low (int), high (int)
    Returns: int - midpoint value
    """
    return (low + high) // 2


def binary_search_guess(low, high, guesses_left):
    """Recursively guess a number using binary search.
    Takes: low (int), high (int), guesses_left (int)
    Returns: bool - True if number found, False if guesses run out
    """
    if guesses_left == 0:
        return False
    current_guess = midpoint(low, high)
    if guess_number(current_guess):
        return True
    direction = get_direction()
    if direction == "higher":
        return binary_search_guess(current_guess + 1, high, guesses_left - 1)
    else:
        return binary_search_guess(low, current_guess - 1, guesses_left - 1)


def play_round():
    """Run one full round of the game.
    Takes: nothing
    Returns: nothing
    """
    print("Choose a number between 1 and 100")
    if binary_search_guess(1, 100, 7):
        print("Got it! Nice one.")
    else:
        print("Out of guesses! Thanks for playing.")


def main():
    """Main game loop for number guesser."""
    while True:
        play_round()
        again = input("Wanna play again? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()