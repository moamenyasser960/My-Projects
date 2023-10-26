import random

print("////// Hello \\\\\\\\\\\\\n")

def rand():
    global num1, num2
    try:
        num1 = int(input("First Random Number: "))
        print("=" * 20)
        print()

        num2 = int(input("Second Random Number: "))
        print(f"\n| {random.randint(num1, num2)} |")

    except ValueError:
        print()
        print("*" * 20)
        print("Invalid Input !\nJust Enter The Integers, Try Again.")
        print("*" * 20)
        print()
        rand()

    re = input()

    while True:
        if re == "" \
                 "":
            print(f"\n| {random.randint(num1, num2)} |")

            re = input()

        elif re == "q" or "f":
            print("-" * 20)
            print("\nDo You Want Again ?")
            print("For Return Select: Enter")

            re = input()

            if re == "" \
                     "":
                print("-" * 20)
                print()
                rand()

            else:
                print("*" * 19)
                print("!Invalid Input.\nJust Select Enter, Try Again.")
rand()