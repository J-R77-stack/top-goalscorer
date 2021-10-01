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
SHEET = GSPREAD_CLIENT.open('top_goalscorer')

def get_goalscorer_data():
    """
    Get goal scorer row number from user
    """
    print("Please enter row number from goalscorer sheet.")
    print("Data should be a number between 2 to 140")
    print("Example: 2, 10, 41 etc\n")

    data_str = input("Enter your cell data here:")
    print(f"The data provided is {data_str}")

get_goalscorer_data()      