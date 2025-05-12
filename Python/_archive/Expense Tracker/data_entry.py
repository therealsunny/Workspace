
from datetime import datetime as dt


date_format = "%d-%m-%Y"
CATEGORIES = {
    "I": "Income",
    "E": "Expense"
}


def get_date(allow_default=False):
    date_str = input("Input Date or ENTER for today's date: ")

    if allow_default and not date_str:
        return dt.today().strftime(date_format)

    try:
        valid_date = dt.strptime(date_str, date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("Please enter the date in dd-MM-YYYY format")
        return get_date(allow_default)


def get_amount():
    try:
        amount = float(input("Enter Amount: "))
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")
        return amount
    except ValueError as e:
        print(f"Enter a valid number - {e}")
        return get_amount()


def get_category():
    category = input("Enter the category 'I' for Income or 'E' for Expense: ")

    if category in CATEGORIES:
        return CATEGORIES[category]
    else:
        print("Invalid Category")
        return get_category()


def get_description():
    return input("Enter optional description: ")


# get_date()

# get_amount()

# get_category()
