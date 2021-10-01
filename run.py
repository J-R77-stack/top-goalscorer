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
    print("Please enter row numbers from goalscorer sheet.")
    print("Data should be a numbers between 2 to 140, separated by commas")
    print("Example: 2, 10, 41 etc\n")

    data_str = input("Enter your row number here:")
    
    goalscorer_data = data_str.split(",")
    validate_data(goalscorer_data)

def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int, 
    and only allows 5 rows of data at a time.
    """
    try:
        [int(value)for value in values]
        if len(values) >= 6:
            raise ValueError(
                f"Only five or less rows of data allowed, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"invalid entry: {e} please enter 5 or less row numbers")        

get_goalscorer_data()      