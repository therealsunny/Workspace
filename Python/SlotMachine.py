import random

MIN_LINES = 1
MAX_LINES = 3

ROWS = 3
COLUMNS = 3

symbols_definition = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
    "E": 10
}


def get_deposit():

    while True:
        deposit = input("Enter Deposit $")
        if deposit.isdigit():
            deposit = int(deposit)
            if deposit > 0:
                break
            else:
                print("Input Value > 0")
        else:
            print("Not a Number")

    return deposit


def get_lines():

    while True:
        lines = input("Enter Lines to Bet ")
        if lines.isdigit():
            lines = int(lines)
            if MIN_LINES <= lines <= MAX_LINES:
                break
            else:
                print(f"Input Value between {MIN_LINES} and {MAX_LINES}")
        else:
            print("Not a Number")

    return lines


def get_bet(deposit, lines):

    while True:
        bet = input("Enter Bet $")
        if bet.isdigit():
            bet = int(bet)
            if deposit < lines * bet:
                print(
                    f"Total Bet ${lines*bet} cannot exceed balance amount ${deposit}")
            else:
                break
        else:
            print("Not a Number")

    return bet


def generate_matrix(rows, columns, symbols_definition):
    print("Generating Matrix")
    symbols_list = []
    for symbol, symbol_count in symbols_definition.items():
        for _ in range(symbol_count):
            symbols_list.append(symbol)

    # print(symbols_list)

    matrix_list = []
    for col in range(columns):
        interim_matrix_list = []
        interim_symbols_list = symbols_list[:]
        # print(f"Col: {col} | {interim_symbols_list[col]}")
        for row in range(rows):
            value = random.choice(interim_symbols_list)
            interim_symbols_list.remove(value)
            interim_matrix_list.append(value)
            # print(f"Row: {row} | Value: {value} | {interim_symbols_list[col]}")
        matrix_list.append(interim_matrix_list)

    # print(matrix_list)

    return (matrix_list)


def print_matrix(matrix):
    print(matrix)
    print("Col 1: ", matrix[0])
    print("Col 2: ", matrix[1])
    print("Col 3: ", matrix[2])
    # matrix.append("X")
    print(matrix, len(matrix))

    for row in range(len(matrix[0])):
        # print("X: ", col, len(col))
        for col in matrix:
            print(row, col)
            print(col[row], end=" | ")


def main():

    deposit = get_deposit()
    lines = get_lines()
    bet = get_bet(deposit, lines)
    matrix = generate_matrix(ROWS, COLUMNS, symbols_definition)
    print_matrix(matrix)

    print(
        f"Deposit ${deposit} Bet ${bet} Lines {lines} Total Bet ${bet*lines}")


main()
