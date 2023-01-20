import gspread
from google.oauth2.service_account import Credentials
import random

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

def get_word():
    """
    Randomly select a word from the word bank and return it.
    
    Returns: str - The said word.
    """
    random_index = random.randint(0,len(WORDS) - 1)

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
        print(f'Your guess is: {user_guess}')

    #     if validate_data(guess):
    #         print('Data is valid!')
    #         break
    # return guess

def main():

    print('Game started... \n')
    word = get_word()
    correctly_guessed_letters = []
    print_dashed_word(word, correctly_guessed_letters)
    guess = get_user_guess()
    

main()