import random
import subprocess

MAX_LINE = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

symbol_values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}

balance = 0

def check_winning(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += bet * values[symbol]
            winning_lines.append(line + 1)

    return winnings, winning_lines

def get_slot_machine_spins(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()

def deposit():
    while True:
        amount = input("What would you like to deposit, $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Must be greater than 0.")
        else:
            print("Please enter a number")

    return amount

def get_numbers_of_lines():
    while True:
        lines = input(f"Enter the number of lines you wish to bet on (1-{MAX_LINE})? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINE:
                break
            else:
                print(f"Must be between 1 and {MAX_LINE}")
        else:
            print("Please enter a number")
    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet, $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Must be Between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter a number")

    return amount

def spin(balance):
    lines = get_numbers_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough money to bet ${bet} on {lines} lines, your balance is ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is ${total_bet}")

    slots = get_slot_machine_spins(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winning(slots, lines, bet, symbol_values)
    print(f"You won {winnings}")
    print(f"You won on lines:", *winning_lines)
    return balance + winnings - total_bet

def main():
    global balance
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            print("Thanks for playing!")
            break
        balance = spin(balance)

    print(f"You left with ${balance}")

if __name__ == "__main__":
    main()
