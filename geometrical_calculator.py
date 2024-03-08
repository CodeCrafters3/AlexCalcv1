from enum import IntEnum
import math
import csv

geo_history = []
fields = ["figure", "area/peri", "result", "math formula", "a", "b", "c", "h", "r"]
history_for_csv = []

def calculate_circle_area(r, history):
    if r > 0:
        area = math.pi * r ** 2
        history.append(f'Circle area where r = {r}: {math.pi} * {r} ** 2 = {math.pi * r ** 2}')
        geo_history.append(f'Circle area where r = {r}: {math.pi} * {r} ** 2 = {math.pi * r ** 2}')
        history_for_csv.append(['circle', 'area', math.pi * r ** 2, 'π * r ** 2', '-', '-', '-', '-', r])
        return area
    else:
        print('Error - parameters must be positive figures')
        history.append(f'Circle area where r = {r}: Error - parameters must be positive figures')
        geo_history.append(f'Circle area where r = {r}: Error - parameters must be positive figures')

def calculate_triangle_area(a, h, history):
    if a > 0 and h > 0:
        area = a * h * 0.5
        history.append(f'Triangle area where a = {a} and h = {h}: {a} * {h} * 0.5 = {a * h * 0.5}')
        geo_history.append(f'Triangle area where a = {a} and h = {h}: {a} * {h} * 0.5 = {a * h * 0.5}')
        history_for_csv.append(['triangle', 'area', a * h * 0.5, 'a * h * 0.5', a, '-', '-', h, '-'])
        return area
    else:
        print('Error - parameters must be positive figures')
        history.append(f'Triangle area where a = {a} and h = {h}: Error - parameters must be positive figures')
        geo_history.append(f'Triangle area where a = {a} and h = {h}: Error - parameters must be positive figures')

def calculate_square_area(a, history):
    if a > 0:
        area = a ** 2
        history.append(f'Square area where a = {a}: {a} ** 2 = {a ** 2}')
        geo_history.append(f'Square area where a = {a}: {a} ** 2 = {a ** 2}')
        history_for_csv.append(['square', 'area', a ** 2, 'a ** 2', a, '-', '-', '-', '-'])
        return area
    else:
        print('Error - parameters must be positive figures')
        history.append(f'Square area where a = {a}: Error - parameters must be positive figures')
        geo_history.append(f'Square area where a = {a}: Error - parameters must be positive figures')

def calculate_rectangle_area(a, b, history):
    if a > 0 and b > 0:
        area = a * b
        history.append(f'Rectangle area where a = {a} and b = {b}: {a} * {b} = {a * b}')
        geo_history.append(f'Rectangle area where a = {a} and b = {b}: {a} * {b} = {a * b}')
        history_for_csv.append(['rectangle', 'area', a * b, 'a * b', a, b, '-', '-', '-'])
        return area
    else:
        print('Error - parameters must be positive figures')
        history.append(f'Rectangle area where a = {a} and b = {b}: Error - parameters must be positive figures')
        geo_history.append(f'Rectangle area where a = {a} and b = {b}: Error - parameters must be positive figures')

def calculate_rhombus_area(a, h, history):
    if a > 0 and h > 0:
        area = a * h
        history.append(f'Rhombus area where a = {a} and h = {h}: {a} * {h} = {a * h}')
        geo_history.append(f'Rhombus area where a = {a} and h = {h}: {a} * {h} = {a * h}')
        history_for_csv.append(['rhombus', 'area', a * h, 'a * h', a, '-', '-', h, '-'])
        return area
    else:
        print('Error - parameters must be positive figures')
        history.append(f'Rhombus area where a = {a} and h = {h}: Error - parameters must be positive figures')
        geo_history.append(f'Rhombus area where a = {a} and h = {h}: Error - parameters must be positive figures')

def calculate_pentagon_area(a, history):
    if a > 0:
        area = a ** 2 / 4 * (25 + 10 * 5 ** 0.5) ** 0.5
        history.append(f'Pentagon area where a = {a}: {a} ** 2 / 4 * (25 + 10 * 5 ** 0.5) **0.5 = {a ** 2 / 4 * (25 + 10 * 5 ** 0.5) ** 0.5}')
        geo_history.append(f'Pentagon area where a = {a}: {a} ** 2 / 4 * (25 + 10 * 5 ** 0.5) **0.5 = {a ** 2 / 4 * (25 + 10 * 5 ** 0.5) ** 0.5}')
        history_for_csv.append(['pentagon', 'area', a ** 2 / 4 * (25 + 10 * 5 ** 0.5) ** 0.5, 'a ** 2 / 4 * (25 + 10 * 5 ** 0.5) ** 0.5', a, '-', '-', '-', '-'])
        return area
    else:
        print('Error - parameters must be positive figures')
        history.append(f'Pentagon area where a = {a}: Error - parameters must be positive figures')
        geo_history.append(f'Pentagon area where a = {a}: Error - parameters must be positive figures')

def calculate_hexagon_area(a, history):
    if a > 0:
        area = (3 * a ** 2 * 3 ** 0.5) / 2
        history.append(f'Hexagon area where a = {a}: (3 * {a} ** 2 * 3 ** 0.5) / 2 = {(3 * a ** 2 * 3 ** 0.5) / 2}')
        geo_history.append(f'Hexagon area where a = {a}: (3 * {a} ** 2 * 3 ** 0.5) / 2 = {(3 * a ** 2 * 3 ** 0.5) / 2}')
        history_for_csv.append(['hexagon', 'area', (3 * a ** 2 * 3 ** 0.5) / 2, '(3 * a ** 2 * 3 ** 0.5) / 2', a, '-', '-', '-', '-'])
        return area
    else:
        print('Error - parameters must be positive figures')
        history.append(f'Hexagon area where a = {a}: Error - parameters must be positive figures')
        geo_history.append(f'Hexagon area where a = {a}: Error - parameters must be positive figures')

def calculate_cuboid_area(a, b, h, history):
    if a > 0 and b > 0 and h > 0:
        area = 2 * (a * b + a * h + b * h)
        history.append(f'Cuboid area where a = {a}, b = {b} and h = {h}: 2 * ({a} * {b} + {a} * {h} + {b} * {h}) = {2 * (a * b + a * h + b * h)}')
        geo_history.append(f'Cuboid area where a = {a}, b = {b} and h = {h}: 2 * ({a} * {b} + {a} * {h} + {b} * {h}) = {2 * (a * b + a * h + b * h)}')
        history_for_csv.append(['cuboid', 'area', 2 * (a * b + a * h + b * h), '2 * (a * b + a * h + b * h)', a, b, '-', h, '-'])
        return area
    else:
        print('Error - parameters must be positive figures')
        history.append(f'Cuboid area where a = {a}, b = {b} and h = {h}: Error - parameters must be positive figures')
        geo_history.append(f'Cuboid area where a = {a}, b = {b} and h = {h}: Error - parameters must be positive figures')

def calculate_circle_perimeter(r, history):
    if r > 0:
        perimeter = 2 * math.pi * r
        history.append(f'Circle perimeter where r = {r}: 2 * {math.pi} * {r} = {2 * math.pi * r}')
        geo_history.append(f'Circle perimeter where r = {r}: 2 * {math.pi} * {r} = {2 * math.pi * r}')
        history_for_csv.append(['circle', 'peri', 2 * math.pi * r, '2 * π * r', '-', '-', '-', '-', r])
        return perimeter
    else:
        print('Error - parameters must be positive figures')
        history.append(f'Circle perimeter where r = {r}: Error - parameters must be positive figures')
        geo_history.append(f'Circle perimeter where r = {r}: Error - parameters must be positive figures')

def calculate_triangle_perimeter(a, b, c, history):
    if a > 0 and b > 0 and c > 0:
        perimeter = a + b + c
        history.append(f'Triangle perimeter where a = {a}, b = {b} and c = {c}: {a} + {b} + {c} = {a + b + c}')
        geo_history.append(f'Triangle perimeter where a = {a}, b = {b} and c = {c}: {a} + {b} + {c} = {a + b + c}')
        history_for_csv.append(['triangle', 'peri', a + b + c, 'a + b + c', a, b, c, '-', '-'])
        return perimeter
    else:
        print('Error - parameters must be positive figures')
        history.append(f'Triangle perimeter where a = {a}, b = {b} and c = {c}: Error - parameters must be positive figures')
        geo_history.append(f'Triangle perimeter where a = {a}, b = {b} and c = {c}: Error - parameters must be positive figures')

def calculate_square_perimeter(a, history):
    if a > 0:
        perimeter = 4 * a
        history.append(f'Square perimeter where a = {a}: 4 * {a} = {4 * a}')
        geo_history.append(f'Square perimeter where a = {a}: 4 * {a} = {4 * a}')
        history_for_csv.append(['square', 'peri', 4 * a, '4 * a', a, '-', '-', '-', '-'])
        return perimeter
    else:
        print('Error - parameters must be positive figures')
        history.append(f'Square perimeter where a = {a}: Error - parameters must be positive figures')
        geo_history.append(f'Square perimeter where a = {a}: Error - parameters must be positive figures')

def calculate_rectangle_perimeter(a, b, history):
    if a > 0 and b > 0:
        perimeter = 2 * a + 2 * b
        history.append(f'Rectangle perimeter where a = {a} and b = {b}: 2 * {a} + 2 * {b} = {2 * a + 2 * b}')
        geo_history.append(f'Rectangle perimeter where a = {a} and b = {b}: 2 * {a} + 2 * {b} = {2 * a + 2 * b}')
        history_for_csv.append(['rectangle', 'peri', 2 * a + 2 * b, '2 * a + 2 * b', a, b, '-', '-', '-'])
        return perimeter
    else:
        print('Error - parameters must be positive figures')
        history.append(f'Rectangle perimeter where a = {a} and b = {b}: Error - parameters must be positive figures')
        geo_history.append(f'Rectangle perimeter where a = {a} and b = {b}: Error - parameters must be positive figures')

def calculate_rhombus_perimeter(a, history):
    if a > 0:
        perimeter = 4 * a
        history.append(f'Rhombus perimeter where a = {a}: 4 * {a} = {4 * a}')
        geo_history.append(f'Rhombus perimeter where a = {a}: 4 * {a} = {4 * a}')
        history_for_csv.append(['rhombus', 'peri', 4 * a, '4 * a', a, '-', '-', '-', '-'])
        return perimeter
    else:
        print('Error - parameters must be positive figures')
        history.append(f'Rhombus perimeter where a = {a}: Error - parameters must be positive figures')
        geo_history.append(f'Rhombus perimeter where a = {a}: Error - parameters must be positive figures')

def calculate_pentagon_perimeter(a, history):
    if a > 0:
        perimeter = 5 * a
        history.append(f'Pentagon perimeter where a = {a}: 5 * {a} = {5 * a}')
        geo_history.append(f'Pentagon perimeter where a = {a}: 5 * {a} = {5 * a}')
        history_for_csv.append(['pentagon', 'peri', 5 * a, '5 * a', a, '-', '-', '-', '-'])
        return perimeter
    else:
        print('Error - parameters must be positive figures')
        history.append(f'Pentagon perimeter where a = {a}: Error - parameters must be positive figures')
        geo_history.append(f'Pentagon perimeter where a = {a}: Error - parameters must be positive figures')

def calculate_hexagon_perimeter(a, history):
    if a > 0:
        perimeter = 6 * a
        history.append(f'Hexagon perimeter where a = {a}: 6 * {a} = {6 * a}')
        geo_history.append(f'Hexagon perimeter where a = {a}: 6 * {a} = {6 * a}')
        history_for_csv.append(['hexagon', 'peri', 6 * a, '6 * a', a, '-', '-', '-', '-'])
        return perimeter
    else:
        print('Error - parameters must be positive figures')
        history.append(f'Hexagon perimeter where a = {a}: Error - parameters must be positive figures')
        geo_history.append(f'Hexagon perimeter where a = {a}: Error - parameters must be positive figures')

def calculate_cuboid_perimeter(a, b, h, history):
    if a > 0 and b > 0 and h > 0:
        perimeter = 4 * a + 4 * b + 4 * h
        history.append(f'Cuboid perimeter where a = {a}, b = {b} and h = {h}: 4 * {a} + 4 * {b} + 4 * {h} = {4 * a + 4 * b + 4 * h}')
        geo_history.append(f'Cuboid perimeter where a = {a}, b = {b} and h = {h}: 4 * {a} + 4 * {b} + 4 * {h} = {4 * a + 4 * b + 4 * h}')
        history_for_csv.append(['cuboid', 'peri', 4 * a + 4 * b + 4 * h, '4 * a + 4 * b + 4 * h', a, b, '-', h, '-'])
        return perimeter
    else:
        print('Error - parameters must be positive figures')
        history.append(f'Cuboid perimeter where a = {a}, b = {b} and h = {h}: Error - parameters must be positive figures')
        geo_history.append(f'Cuboid perimeter where a = {a}, b = {b} and h = {h}: Error - parameters must be positive figures')

def download_operations_history():
    with open("operations_history_geomatrical.csv", "w", encoding="UTF-8") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(fields)
        csv_writer.writerows(history_for_csv)

def geometrical_calculator(history):

    figures = ["Circle", "Triangle", "Square", "Rectangle", "Rhombus", "Pentagon", "Hexagon", "Cuboid", "Show_operations_history", "Back_to_previous_menu"]

    Figures_menu = IntEnum("Figures_menu", figures)

    figures_menu_display = ["Choose geometric figure or operation:",
                      "1 - circle",
                      "2 - triangle",
                      "3 - square",
                      "4 - rectangle",
                      "5 - rhombus",
                      "6 - pentagon",
                      "7 - hexagon",
                      "8 - cuboid",
                      "9 - show operations history from geometrical calculator",
                      "10 - back to previous menu"]

    while True:

        print("Choose what type of operations you want to perform:\n"
              "1 - surface area calculator\n"
              "2 - perimeter calculator\n"
              "3 - show operations history from geomatrical calculator\n"
              "4 - download .csv file with history of operations from geometrical calculator\n"
              "5 - back to previous menu")

        operations_type = ["Surface_area", "Perimeter", "Show_operations_history", "Download_history", "Back_to_previous_menu"]

        Operations_menu = IntEnum("Operations_menu", operations_type)

        operation_choice = int(input("Number of operation's type you want to execute: "))

        if operation_choice == Operations_menu.Back_to_previous_menu:
            break
        elif operation_choice not in range(1, len(operations_type) + 1):
            print("There is no such operation, choose other one.")
        elif operation_choice == Operations_menu.Download_history:
            if len(history_for_csv) > 0:
                download_operations_history()
                print("File with operation's history has been downloaded")
                print("Please remember copying history file to your personal directory before conducting another history downloading operation")
                print(
                    "Please note that operations that ended with 'Error' are not included in downloaded file")
            else:
                print(
                    "Conduct any operations to be able to download operation's history")
            
        elif operation_choice == Operations_menu.Show_operations_history:
            print('History of operations from geomatrical calculator: ')
            for operation in geo_history:
                print(operation)    
        elif operation_choice == Operations_menu.Surface_area:
            while True:

                for operation in figures_menu_display:
                    print(operation)

                figure_choice = int(input("Choose figure: "))

                if figure_choice == Figures_menu.Circle:
                    r = float(input("Enter the length of the radius of the circle: "))
                    print("Surface area: ", calculate_circle_area(r, history))
                elif figure_choice ==  Figures_menu.Triangle:
                    a = float(input("Enter the length of the triangle's base: "))
                    h = float(input("Enter the length of the triangle's height: "))
                    print("Surface area: ", calculate_triangle_area(a, h, history))
                elif figure_choice == Figures_menu.Square:
                    a = float(input("Enter the length of the square's side: "))
                    print("Surface area: ", calculate_square_area(a, history))
                elif figure_choice == Figures_menu.Rectangle:
                    a = float(input("Enter the length of the rectangle's side: "))
                    b = float(input("Enter the length of the other rectangle's side: "))
                    print("Surface area: ", calculate_rectangle_area(a, b, history))
                elif figure_choice == Figures_menu.Rhombus:
                    a = float(input("Enter the length of the rhombus side: "))
                    h = float(input("Enter the length of the rhombus height: "))
                    print("Surface area: ", calculate_rhombus_area(a, h, history))
                elif figure_choice == Figures_menu.Pentagon:
                    a = float(input("Enter the length of the pentagon's side: "))
                    print("Surface area: ", calculate_pentagon_area(a, history))
                elif figure_choice == Figures_menu.Hexagon:
                    a = float(input("Enter the length of the hexagon's side: "))
                    print("Surface area: ", calculate_hexagon_area(a, history))
                elif figure_choice == Figures_menu.Cuboid:
                    a = float(input("Enter the length of the cuboid's base: "))
                    b = float(input("Enter the length of the other cuboid's base: "))
                    h = float(input("Enter the length of the cuboid's height: "))
                    print("Surface area: ", calculate_cuboid_area(a, b, h, history))
                elif figure_choice == Figures_menu.Show_operations_history:
                    print('History of operations from geometrical calculator: ')
                    for operation in geo_history:
                        print(operation)    
                elif figure_choice == Figures_menu.Back_to_previous_menu:
                    break
                elif figure_choice not in range(1, len(figures) + 1):
                    print("There is no such figure.")
            

        elif operation_choice == Operations_menu.Perimeter:
            while True:
                
                for operation in figures_menu_display:
                    print(operation)

                figure_choice = int(input("Choose figure: "))

                if figure_choice == Figures_menu.Circle:
                    r = float(input("Enter the length of the radius of the circle: "))
                    print("Perimeter: ", calculate_circle_perimeter(r, history))
                elif figure_choice ==  Figures_menu.Triangle:
                    a = float(input("Enter the length of the triangle's first side: "))
                    b = float(input("Enter the length of the triangle's second side: "))
                    c = float(input("Enter the length of the triangle's third side: "))
                    print("Perimeter: ", calculate_triangle_perimeter(a, b, c, history))
                elif figure_choice == Figures_menu.Square:
                    a = float(input("Enter the length of the square's side: "))
                    print("Perimeter: ", calculate_square_perimeter(a, history))
                elif figure_choice == Figures_menu.Rectangle:
                    a = float(input("Enter the length of the rectangle's side: "))
                    b = float(input("Enter the length of the other rectangle's side: "))
                    print("Perimeter: ", calculate_rectangle_perimeter(a, b, history))
                elif figure_choice == Figures_menu.Rhombus:
                    a = float(input("Enter the length of the rhombus' side: "))
                    print("Perimeter: ", calculate_rhombus_perimeter(a, history))
                elif figure_choice == Figures_menu.Pentagon:
                    a = float(input("Enter the length of the pentagon's side: "))
                    print("Perimeter: ", calculate_pentagon_perimeter(a, history))
                elif figure_choice == Figures_menu.Hexagon:
                    a = float(input("Enter the length of the hexagon's side: "))
                    print("Perimeter: ", calculate_hexagon_perimeter(a, history))
                elif figure_choice == Figures_menu.Cuboid:
                    a = float(input("Enter the length of the cuboid's base: "))
                    b = float(input("Enter the length of the other cuboid's base: "))
                    h = float(input("Enter the length of the cuboid's height: "))
                    print("Perimeter: ", calculate_cuboid_perimeter(a, b, h, history))
                elif figure_choice == Figures_menu.Show_operations_history:
                    print('History of operations: ')
                    for operation in geo_history:
                        print(operation)    
                elif figure_choice == Figures_menu.Back_to_previous_menu:
                    break
                elif figure_choice not in range(1, len(figures) + 1):
                    print("There is no such figure.")
                  
                        


if __name__ == "__main__":
    history = []
    geometrical_calculator(history)
