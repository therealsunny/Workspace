
import pandas as pd
import csv
from datetime import datetime as dt
from data_entry import get_date, get_amount, get_category, get_description


class CSV:
    CSV_FILE = "finance_data.csv"
    COLUMNS = ["Date", "Amount", "Category", "Description"]
    FORMAT = "%d-%m-%Y"

    @classmethod
    def initialize_csv(cls):
        try:
            df = pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(
                columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)

    @classmethod
    def add_entry(cls, date, amount, category, description):
        new_entry = {
            "Date": date,
            "Amount": amount,
            "Category": category,
            "Description": description
        }
        with open(cls.CSV_FILE, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("Entry Added")

    @classmethod
    def get_transactions(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_FILE)
        df["Date"] = pd.to_datetime(df["Date"], format=cls.FORMAT)
        start_date = dt.strptime(start_date, cls.FORMAT)
        end_date = dt.strptime(end_date, cls.FORMAT)

        mask = (df["Date"] >= start_date) & (df["Date"] <= end_date)
        filtered_df = df.loc[mask]

        if filtered_df.empty:
            print(
                f"No transactions available from {start_date} and {end_date}")
        else:
            print(f"Transactions from {start_date} and {end_date}:")
            print(filtered_df)

        total_income = filtered_df[filtered_df["Category"]
                                   == "Income"]["Amount"].sum()
        total_expense = filtered_df[filtered_df["Category"]
                                    == "Expense"]["Amount"].sum()

        print("\nSummary: ")
        print(f"Total Income: $ {total_income:.2f}")
        print(f"Total Expense: $ {total_expense:.2f}")


def add():
    CSV.initialize_csv()
    date = get_date(allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_description()

    CSV.add_entry(date, amount, category, description)


CSV.get_transactions("01-01-2013", "31-12-2024")

# add()

# data_entry()
# CSV.add_entry("01-01-2013", 100.0, "Restaurant", "Tuesday Chic-Fil-A")
