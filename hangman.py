import random

WORDS = ["python", "hangman", "keyboard", "elephant", "guitar"]
MAX_WRONG_GUESSES = 6

HANGMAN_PICS = [
    """
       ------
       |    |
       |
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    --------
    """,
]

def choose_word():
    return random.choice(WORDS)


def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def play_hangman():
    word = choose_word()
    guessed_letters = []
    wrong_guesses = 0

    print("Welcome to Hangman!")
    print("Try to guess the word one letter at a time.")
    print(f"You have {MAX_WRONG_GUESSES} incorrect guesses allowed.\n")

    while wrong_guesses < MAX_WRONG_GUESSES:
        print(HANGMAN_PICS[wrong_guesses])
        print("Word: " + display_word(word, guessed_letters))
        print(f"Wrong guesses left: {MAX_WRONG_GUESSES - wrong_guesses}")
        if guessed_letters:
            print("Guessed letters: " + ", ".join(sorted(guessed_letters)))

        guess = input("\nGuess a letter: ").lower().strip()

        # Basic input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.\n")
            # Check for win
            if all(letter in guessed_letters for letter in word):
                print(HANGMAN_PICS[wrong_guesses])
                print("Word: " + display_word(word, guessed_letters))
                print(f"\nCongratulations! You guessed the word: {word}")
                return
        else:
            wrong_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.\n")

    # Player ran out of guesses
    print(HANGMAN_PICS[wrong_guesses])
    print(f"\nGame over! You've used all {MAX_WRONG_GUESSES} incorrect guesses.")
    print(f"The word was: {word}")


def main():
    play_again = "y"
    while play_again == "y":
        play_hangman()
        play_again = input("\nPlay again? (y/n): ").lower().strip()
    print("Thanks for playing!")


if __name__ == "__main__":
    main()