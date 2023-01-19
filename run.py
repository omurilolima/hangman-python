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

    return WORDS[random_index]


def main():

    print('Game started')
    word = get_word()
    print(word)


main()