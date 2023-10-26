from time import time
import numpy as np
print("            \\\\\\\\\\\\\\\\Hello////////\n")
def tim():
    global n1, n2
    try:
        n1 = int(input("Enter The First Number For Test: "));print()
        print("=" * 35)
        n2 = int(input("\nEnter The Second Number: "));print()
    except ValueError:
        print()
        print("-" * 40)
        print("Invalid Input! , Enter the Integers Numbers Only.")
        print("-" * 40, "\n")
        tim()

    while n2 <= n1:
        print("-" * 35)
        print("Invalid Input !\nEnter The First Number Less Than Second Number.")
        print("-" * 40 , "\n")
        tim()
    print(len(f"{n1}") * "=")

    def speed(test):
        now = time()
        test()
        end = time()
        print(len(f"{n2}") * "=", "\b=")
        print(f"\nResult Speed Time Test Is => {end - now}")
        return speed

    @speed
    def b():
        for m in range(n5, n6 + 1):
            print(f"{m}")

    next = input()
    while next != "" or next == "":
        print("=" * 20)
        print("For Return Select: Enter")
        print("=" * 20)
        next = input()

        if next == "" \
                   "":
            tim()

        else:
            print("=" * 20)
            print("!Invalid Input,\nTry Again.")
tim()