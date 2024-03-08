from enum import IntEnum
import csv

classic_history = []
fields = ['x', 'operation', 'y', 'result']
history_for_csv = []


def addition(x, y, history):
    history.append(f'{x} + {y} = {x + y}')
    classic_history.append(f'{x} + {y} = {x + y}')
    history_for_csv.append([x, "addition", y, x + y])
    return x + y


def subtraction(x, y, history):
    history.append(f'{x} - {y} = {x - y}')
    classic_history.append(f'{x} - {y} = {x - y}')
    history_for_csv.append([x, "subtraction", y, x - y])
    return x - y


def multiplication(x, y, history):
    history.append(f'{x} * {y} = {x * y}')
    classic_history.append(f'{x} * {y} = {x * y}')
    history_for_csv.append([x, "multiplication", y, x * y])
    return x * y


def division(x, y, history):
    if y == 0:
        history.append(f'{x} / {y} - error - division by 0')
        classic_history.append(f'{x} / {y} - error - division by 0')
        return "Error - division by 0"
    else:
        history.append(f'{x} / {y} = {x / y}')
        classic_history.append(f'{x} / {y} = {x / y}')
        history_for_csv.append([x, "division", y, x / y])
        return x / y


def exponentiation(x, y, history):
    if y == 0:
        history.append(f'{x} **{y} = 1')
        classic_history.append(f'{x} **{y} = 1')
        history_for_csv.append([x, "exponentiation", y, 1])
        return 1
    else:
        history.append(f'{x} ** {y} = {x ** y}')
        classic_history.append(f'{x} ** {y} = {x ** y}')
        history_for_csv.append([x, "exponentiation", y, x ** y])
        return x ** y


def remainder(x, y, history):
    if y == 0:
        history.append(f'{x} / {y} - error - division by 0')
        classic_history.append(f'{x} / {y} - error - division by 0')
        return "Error - division by 0"
    else:
        history.append(f'{x} % {y} = {x % y}')
        classic_history.append(f'{x} % {y} = {x % y}')
        history_for_csv.append([x, "remainder", y, x % y])
        return x % y


def download_operations_history():
    with open("operations_history_classic.csv", "w", encoding="UTF-8") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(fields)
        csv_writer.writerows(history_for_csv)


def classic_calculator(history):

    while True:

        print("Choose an operation you want to execute:\n"
              "1 - addition\n"
              "2 - subtraction\n"
              "3 - multipliaction\n"
              "4 - division\n"
              "5 - exponentiation\n"
              "6 - remainder from division\n"
              "7 - show operations history from classic calculator\n"
              "8 - download .csv file with history of operations from classic calculator\n"
              "9 - back to previous menu")

        operations = [
            "Addition",
            "Subtraction",
            "Multiplication",
            "Division",
            "Exponentiation",
            "Remainder",
            "Show_operations_history",
            "Download_history",
            "Back_to_previous_menu"]

        Operations_menu = IntEnum("Operations_menu", operations)

        choice = int(input("Number of operation you want to execute: "))

        if choice == Operations_menu.Back_to_previous_menu:
            break
        elif choice not in range(1, len(operations) + 1):
            print("There isn't such an operation, choose other one.")
        elif choice == Operations_menu.Show_operations_history:
            print('History of operations from classic calculator: ')
            for operation in classic_history:
                print(operation)    
        elif choice == Operations_menu.Download_history:
            if len(history_for_csv) > 0:
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

            if choice == Operations_menu.Addition:
                print("Result: ", addition(x, y, history))
            elif choice == Operations_menu.Subtraction:
                print("Result: ", subtraction(x, y, history))
            elif choice == Operations_menu.Multiplication:
                print("Result: ", multiplication(x, y, history))
            elif choice == Operations_menu.Division:
                print("Result: ", division(x, y, history))
            elif choice == Operations_menu.Exponentiation:
                print("Result: ", exponentiation(x, y, history))
            elif choice == Operations_menu.Remainder:
                print("Result: ", remainder(x, y, history))
                

if __name__ == "__main__":
    history = []
    classic_calculator()

