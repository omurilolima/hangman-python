import random
import os
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
SCORE = 1


def get_word():
    """
    Randomly select a word from the word bank and return it.

    Returns: str - The said word.
    """
    random_index = random.randint(0, len(WORDS) - 1)

    return WORDS[random_index][0]


def dashe_word(word, letters_to_reveal):
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
    
    return dashed_representation


def get_user_guess():
    """
    Get user guess letter from the user's
    """
    while True:
        user_guess = input('Guess a letter: ')
        guess_lowercase = user_guess.lower()
        if validate_data(guess_lowercase):
            ALL_GUESSED_LETTERS.append(guess_lowercase)
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


def clear_screen():
    """
    Clear the screen to achieve a cleaner look
    """
    os.system("cls" if os.name == "nt" else "clear")


def guessed_letters():
 
    separator = ", "
    list = separator.join(ALL_GUESSED_LETTERS)

    return list


def main():
    """
    Run all program functions
    """
    print('Game started... \n')
    word = get_word()
    SCORE = 0
    attempts = len(word)
    print(f'Score: {SCORE} words guessed')
    print(f'Attempts remaining: {attempts} \n')
    dashed_word = dashe_word(word, CORRECTLY_GUESSED_LETTERS)
    print(f'{dashed_word}\n')

    while attempts > 0:
        print(word)
        guess = get_user_guess()
        check_answer(guess, word)
        clear_screen()

        print(f'Guessed letters: {guessed_letters()}')
        
        dashed_word = dashe_word(word, CORRECTLY_GUESSED_LETTERS)
        print(f'{dashed_word}\n')
        if dashed_word.count("_") == 0:
            SCORE += 1
            print(f'Congrats!!! Your new score is: {SCORE}')
            break
        else:
            attempts -= 1
            print(f'Attempts remaining: {attempts}')

    if attempts == 0:
        print(f'Game over: The word was: {word}')


main()