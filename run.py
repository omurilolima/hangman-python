"""
Imports
"""
# internal libraries
import random
import os
import sys

# external libraries
import gspread
from google.oauth2.service_account import Credentials
from colorama import Fore


"""
Linking a Google spreadsheet 
"""
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hangman-python')

leaderboard = SHEET.worksheet('leaderboard')
data = leaderboard.get_all_values()

words_bank = SHEET.worksheet('words')
WORDS = words_bank.get_all_values()


# Global variables
current_state = {
    "all_guessed_letters": [],
    "correctly_guessed_letters": [],
    "score": 0
}


def get_word():
    """
    Randomly select a word from the word bank and return it.

    Returns: str - The said word.
    """
    random_index = random.randint(0, len(WORDS) - 1)
    word = WORDS[random_index][0]
    WORDS.pop(random_index)
    return word


def dashe_word(word):
    """
    Given a word, print a dashed representation of it.
    Exemple: For a word X with 4, the expected return is a
    dashed_representation of this word with 4 dashes.

    Returns: str - The word to "dashed"-print.
    """
    dashed_representation = ''
    for letter in word:
        if letter in current_state["correctly_guessed_letters"]:
            dashed_representation += f' {letter}'
        else:
            dashed_representation += ' _'

    return dashed_representation


def get_user_guess():
    """
    Get user guess letter from the user's
    """
    while True:
        user_guess = input(Fore.YELLOW + 'Guess a letter: ').strip()
        guess_lowercase = user_guess.lower()
        if validate_data(guess_lowercase):
            current_state["all_guessed_letters"].append(guess_lowercase)
            break
    return guess_lowercase


def validate_data(guess):
    """
    Inside the try, converts all the guess into string.
    Raises ValueError if cannot be converterd into string.

    Input should be a single roman letter. If not, print an error message
    and give them another chance to enter a letter.
    """
    is_string = guess.isalpha()

    try:
        if not is_string:
            raise ValueError(
                Fore.RED + f'Enter a single letter. You entered: {guess}'
            )
        elif len(guess) != 1:
            raise ValueError(
                Fore.RED + f'Enter a single letter. You provided {len(guess)}'
                )
        elif guess in current_state["all_guessed_letters"]:
            raise ValueError(
                Fore.RED + f'{guess} was already guessed. Try another letter.'
                )
    except ValueError as error:
        print(Fore.RED + f'{error}, please try again. \n')
        return False

    return True


def check_answer(guess, word):
    """
    Check whether the letter is in the word.
    If is correct, append the letter in the
    correctly_guessed_letters list.
    """

    if guess in word:
        current_state["correctly_guessed_letters"].append(guess)


def clear_screen():
    """
    Clear the screen to achieve a cleaner look
    """
    os.system("cls" if os.name == "nt" else "clear")


def guessed_letters_string():
    """
    Join each char of an array in a new string
    separated by a comma
    """
    separator = ", "
    letters_string = separator.join(current_state["all_guessed_letters"])

    return letters_string


def ask_play_again():
    """
    Asks if the user want to play another round.
    If the user say yes ('Y'), call new_round.
    Else, exit the program.
    """
    again = input('Play again? (y = Yes / Anything else = Exit)\n').strip()
    if again.lower() != 'y':
        clear_screen()
        print(Fore.BLUE + 'Thanks for playing!!! See you :)')
        sys.exit()
    return True


def new_round():
    word = get_word()
    attempts = len(word) + 3
    dashed_word = dashe_word(word)
    print(Fore.YELLOW + f'{dashed_word}\n')
    print(Fore.WHITE + f'Attempts remaining: {attempts} \n')
    print(Fore.WHITE + f'Score: {current_state["score"]} words guessed\n')

    while attempts > 0:
        # print(f'Word is: {word} (HINT JUST FOR TESTING) :)\n')
        guess = get_user_guess()
        check_answer(guess, word)
        clear_screen()
        print(Fore.GREEN + f'Guessed letters: {guessed_letters_string()}\n')
        dashed_word = dashe_word(word)
        print(Fore.YELLOW + f'{dashed_word}\n')
        if dashed_word.count("_") == 0:
            current_state["score"] += 1
            print(Fore.BLUE + f'Congrats! Score: {current_state["score"]}\n')
            break
        else:
            attempts -= 1
            print(Fore.WHITE + f'Attempts remaining: {attempts}\n')
            print(f'Score: {current_state["score"]} words guessed\n')

    if attempts == 0:
        print(Fore.RED + f'Game over: The word was: {word}\n')
       
    return ask_play_again()


def main():
    """
    Run all program functions
    """
    print(Fore.BLUE + 'Welcome to the Tech Hangman Game')
    print(Fore.WHITE + 'By Murilo Lima\n')
    username = input(Fore.YELLOW + 'What is your name?\n')

    while len(WORDS) > 0:
        clear_screen()
        print(Fore.BLUE + f'Good luck, {username}!\n')
        play_again = new_round()

        if play_again:
            current_state["all_guessed_letters"] = []
            current_state["correctly_guessed_letters"] = []
        else:
            break


main()
