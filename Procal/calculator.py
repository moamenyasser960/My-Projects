print("Welcome To Calculator.")
print("-_" * 12, "\n")
def calculate():
    global num1, num2, operator
    try:
        num1 = float(str(input("Enter The First Number: ").replace(",", "").replace("_", "").strip(",~?><|||}{:*/='!@#$%^&*() _").rstrip("+-")));print()
        operator = str(input("Enter The Operator: ").strip("~?><|||=:}{.'!@#$&()_"));print()
        num2 = float(str(input("Enter The Second Number: ").replace(",", "").replace("_", "").strip(",~?><|||}{:*=/'!@#$%^&*() _").rstrip("+-")));print()

        if operator == "%": print(" =", f"{num1 % num2:,}")
        elif operator == "+": print(" =", f"{num1 + num2:,}")
        elif operator == "-": print(" =", f"{num1 - num2:,}")
        elif operator == "*": print(" =", f"{num1 * num2:,}")
        elif operator == "/": print(" =", f"{num1 / num2:,}")
        elif operator == "^": print(" =", f"{num1 ** num2:,}")
        elif operator == ",":
            from math import sqrt
            print(" =", f"{sqrt(num1):,}")
        elif operator == "//":print(" =", f"{num1 // num2:,}")
        else:
            print("-" * 16)
            print("Wrong operator Try again.")
            print("-" * 16, "\n")
            calculate()
    except:
        print()
        print(">" * 16, "\b>")
        print("Invalid Input!\nTry again.")
        print(">" * 16, "\b>", "\n")
        calculate()

    again = input()
    if again.upper() == "" or " ":
        print("-" * 12, "\n")
        calculate()
calculate()