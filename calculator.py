from enum import IntEnum
from dotenv import load_dotenv
import os
import csv

history = []
fields = ['x', 'operation', 'y', 'result']
history_for_csv = []


def addition(x, y):
    history.append(f'{x} + {y} = {x + y}')
    history_for_csv.append([x, "addition", y, x + y])
    return x + y


def subtraction(x, y):
    history.append(f'{x} - {y} = {x - y}')
    history_for_csv.append([x, "subtraction", y, x - y])
    return x - y


def multiplication(x, y):
    history.append(f'{x} * {y} = {x * y}')
    history_for_csv.append([x, "multiplication", y, x * y])
    return x * y


def division(x, y):
    if y == 0:
        history.append('Error - division by 0')
        return "Error - division by 0"
    else:
        history.append(f'{x} / {y} = {x / y}')
        history_for_csv.append([x, "division", y, x / y])
        return x / y


def exponentiation(x, y):
    if y == 0:
        history.append(f'{x} ** {y} = 1')
        history_for_csv.append([x, "exponentiation", y, 1])
        return 1
    else:
        history.append(f'{x} ** {y} = {x ** y}')
        history_for_csv.append([x, "exponentiation", y, x ** y])
        return x ** y


def remainder(x, y):
    if y == 0:
        history.append('Error - division by 0')
        return "Error - division by 0"
    else:
        history.append(f'{x} % {y} = {x % y}')
        history_for_csv.append([x, "remainder", y, x % y])
        return x % y


def get_name():
    load_dotenv()
    name = os.getenv('USER_NAME')
    return name


def download_operations_history():
    with open("operations_history.csv", "w", encoding="UTF-8") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(fields)
        csv_writer.writerows(history_for_csv)


def calculator():

    name = get_name()
    print(f'Welcome in my calculator {name}!')

    while True:

        print("Choose an operation you want to execute:\n"
              "1 - addition\n"
              "2 - subtraction\n"
              "3 - multipliaction\n"
              "4 - division\n"
              "5 - exponentiation\n"
              "6 - remainder from division\n"
              "7 - download .csv file with history of operations\n"
              "8 - exit")

        operations = [
            "Addition",
            "Subtraction",
            "Multiplication",
            "Division",
            "Exponentiation",
            "Remainder",
            "Download_history",
            "Exit"]

        Menu = IntEnum("Menu", operations)

        print('History of operations: ')

        for operation in history:
            print(operation)

        choice = int(input("Number of operation you want to execute: "))

        if choice == Menu.Exit:
            print("Calculator has been closed.")
            break
        elif choice not in range(1, len(operations) + 1):
            print("There isn't such an operation, choose other one.")
        elif choice == Menu.Download_history:
            if len(history) > 0:
                download_operations_history()
                print("File with operation's history has been downloaded")
                print("Please remember copying history file to your personal directory before conducting another history downloading operation")
                print(
                    "Please note that operations that ended with 'Error' are not included in downloaded file")
            else:
                print(
                    "Conduct any operations to be able to download operation's history")
        else:

            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))

            if choice == Menu.Addition:
                print("Result: ", addition(x, y))
            elif choice == Menu.Subtraction:
                print("Result: ", subtraction(x, y))
            elif choice == Menu.Multiplication:
                print("Result: ", multiplication(x, y))
            elif choice == Menu.Division:
                print("Result: ", division(x, y))
            elif choice == Menu.Exponentiation:
                print("Result: ", exponentiation(x, y))
            elif choice == Menu.Remainder:
                print("Result: ", remainder(x, y))


if __name__ == "__main__":
    calculator()
