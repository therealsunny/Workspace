
import pandas as pd
import csv


class CSV:
    CSV_FILE = "finance_data.csv"
    COLUMNS = ["Date", "Amount", "Category", "Description"]

    @classmethod
    def initialize_csv(cls):
        try:
            df = pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)


CSV.initialize_csv()

"""
if __name__ == "__main__":
    main()

1. Add a new transaction
2. View transactions and summary within a date range
3. Exit
"""
