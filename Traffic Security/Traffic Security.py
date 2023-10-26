import string, random
def pas():
    global characters_number, characters_number
    try:
        characters_number = int(input("\nHow Many Characters For The Password?: "));print()
        if characters_number > 156:print("The Number Must Not Exceed 156 Numbers.");pas();print()
    except ValueError:print("\n!Enter The Numbers Integers Only.");pas()
    def num():
        s1 = list((string.ascii_lowercase + string.ascii_uppercase + string.digits) * 2 + string.punctuation);random.shuffle(s1)
        password = []
        for i in range (characters_number):password.append(s1[i])
        password = "".join(password[0:])
        print(characters_number * "-", "\b-")
        print(password)
        print(characters_number * "-", "\b-")
    num();retarn = input()
    while True:
        if retarn == "" \
                     "":num();retarn = input()
        elif retarn == "q" or "f":
            print("_-" * 14, "\b_", "\n\nDo You Want Again ?", "\nFor Return Select: Enter");retarn = input()
            if retarn == "" \
                         "":print("_-" * 14, "\b_");pas()
            else:print("_-" * 14, "\b_", "\n!Invalid Input.\nJust Select Enter, Try Again.")
pas()