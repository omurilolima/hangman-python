import random
import gspread
from google.oauth2.service_account import Credentials

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
ALL_GUESSED_LETTERS = []
CORRECTLY_GUESSED_LETTERS = []


def get_word():
    """
    Randomly select a word from the word bank and return it.

    Returns: str - The said word.
    """
    random_index = random.randint(0, len(WORDS) - 1)

    return WORDS[random_index][0]


def print_dashed_word(word, letters_to_reveal):
    """
    Given a word, print a dashed representation of it.
    Exemple: For a word X with 4, the expected return is a
    dashed_representation of this word with 4 dashes.

    Returns: str - The word to "dashed"-print.
    """
    dashed_representation = ''

    for letter in word:
        if letter in letters_to_reveal:
            dashed_representation += f' {letter}'
        else:
            dashed_representation += ' _'

    print(dashed_representation)
    print('\n')


def get_user_guess():
    """
    Get user guess letter from the user's
    """
    while True:
        user_guess = input('Guess a letter: ')

        if validate_data(user_guess):
            ALL_GUESSED_LETTERS.append(user_guess)
            break
    return user_guess


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
                f'Enter a single roman letter. You entered: {guess}'
            )
        elif len(guess) != 1:
            raise ValueError(
                f'Enter a single roman letter. You provided {len(guess)}'
                )
        elif guess in ALL_GUESSED_LETTERS:
            raise ValueError(
                f'{guess} was already guessed. Try another letter.'
                )
    except ValueError as error:
        print(f'{error}, please try again. \n')
        return False

    return True


def check_answer(guess, word):
    """
    Check whether the letter is in the word.
    If is correct, append the letter in the
    CORRECTLY_GUESSED_LETTERS list.
    """
    if guess in word:
        CORRECTLY_GUESSED_LETTERS.append(guess)


def main():
    """
    Run all program functions
    """
    print('Game started... \n')
    word = get_word()
    attempts = 3
    while attempts != -1:
        print_dashed_word(word, CORRECTLY_GUESSED_LETTERS)
        guess = get_user_guess()
        check_answer(guess, word)
        attempts -= 1
        print(f'Attempts remaining: {attempts}')
    
    print('Game over')


main()
