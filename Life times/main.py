import datetime
print("Hello --\n"
      "-----------\n")

def age():
    global weeks, month, hours, minutes, seconds, current_day, days, months, year, current_year, current_month
    try:
        year = int(input("Your Birthday In A Year ? : ").strip())

        while year < 1:
            print("\nYour Birthday Must Be 1 Or Higher.\nTry Again.\n")
            year = int(input("Your Birthday In A Year ? : ").strip())

        while year > 9999:
            print("\nYour Birthday Should Be Less Than 9999 Years And More Than 1.\nTry Again.\n")
            year = int(input("Your Birthday In A Year ? : ").strip())

        months = int(input("In Month ? : ").strip())

        while months < 1:
            print("\nMonth Must Be From 1 To 12.\nTry Again.\n")
            months = int(input("In Month ? : ").strip())

        while months > 12:
            print("\nMonth Must Be From 1 To 12.\nTry Again.\n")
            months = int(input("In Month ? : ").strip())

        days = int(input("In Day ? : ").strip())

        while days < 1:
            print("\nDay Must Be From 1 To 31.\nTry Again.\n")
            days = int(input("In Day ? : ").strip())

        while days > 31:
            print("\nDay Must Be From 1 To 31.\nTry Again.\n")
            days = int(input("In Day ? : ").strip())

        print()
        print("-" * 20, "\n")

        current_year = int(input("Current Year ? : ").strip())

        while current_year < 1:
            print("\nCurrent Year Must Be 1 Or Higher.\nTry Again.\n")
            current_year = int(input("Current Year ? : ").strip())

        while current_year > 9999:
            print("\nCurrent Year Should Be Less Than 9999 Years And More Than 1.\nTry Again.\n")
            year = int(input("Current Year ? : ").strip())

        current_month = int(input("In Month ? : ").strip())

        while current_month < 1:
            print("\nMonth Must Be From 1 To 12.\nTry Again.\n")
            current_month = int(input("In Month ? : ").strip())

        while current_month > 12:
            print("\nMonth Must Be From 1 To 12.\nTry Again.\n")
            current_month = int(input("In Month ? : ").strip())

        current_day = int(input("In Day ? : ").strip())

        while current_day < 1:
            print("\nThe Day Must Be From 1 To 31.\nTry Again.\n")
            current_day = int(input("In Day ? : ").strip())

        while current_day > 31:
            print("\nThe Day Must Be From 1 To 31.\nTry Again.\n")
            current_day = int(input("In Day ? : ").strip())

    except:
        print()
        print("-" * 20)
        print("Invalid Input !\nJust Enter The Integers, Try Again.")
        print("-" * 20, "\n")
        global weeks, month, hours, minutes, seconds, next
        age()

    birth = datetime.datetime(year, months, days)
    date = datetime.datetime(current_year, current_month, current_day)

    day = round((date - birth).days) # 5, 193
    years = round(day / 365.2425)
    weeks = round(day / 7)
    month = round(day / 30.436)
    hours = round(day * 24)
    minutes = round(hours * 60)
    seconds = round(minutes * 60)

    years1 = int(day / 365.2425)
    day1 = round(day - years1 * 365.2425) # 80 day
    month1 = int(day1 / 30.436) # 2 month
    month2 = round(day1 - month1 * 30.436) # 22
    week1 = int(month2 / 7 ) # 3
    day2 = round(month2 - week1 * 7) # 3

    print()
    print("-" * 18, "\n")

    print("Your Birthday :\n")
    print(birth.strftime("| %Y/%m/%d\n"))
    print(birth.strftime("| Year: %Y"))
    print(birth.strftime("| Month: %B"))
    print(birth.strftime("| Day: %A\n"))

    print("-" * 18, "\n")

    print("You Lived Almost :\n")
    print(f"| {years:,} Year.")
    print(f"| {month:,} Month.")
    print(f"| {weeks:,} Week.")
    print(f"| {day:,} Day.")
    print(f"| {hours:,} Hour.")
    print(f"| {minutes:,} Minute.")
    print(f"| {seconds:,} Second.\n")
    print("-" * 22, "\n")
    print("Your Full Age :\n")

    if month1 == -11 and week1 == -4 and day2 == -2:
        print(f"| {years:,} Year.")
    elif month1 == 11 and week1 == 4 and day2 == 2:
        print(f"| {years:,} Year.")

    elif years1 > 0 and month1 == 0 and week1 == 0 and day2 == 0:
        print(f"| {years:,} Year.")
    elif years1 < 0 and month1 == 0 and week1 == 0 and day2 == 0:
        print(f"| {years:,} Year.")

    else:
        if years1 == 0 and month1 == 0 and week1 == 0 and day2 > 0:
            print(f"| {day2:,} Day.")
        elif years1 == 0 and month1 > 0 and week1 == 0 and day2 == 0:
            print(f"| {month1:,} Month.")
        elif years1 == 0 and month1 == 0 and week1 > 0 and day2 == 0:
            print(f"| {week1:,} Week.")

        elif years1 == 0 and month1 > 0 and week1 == 0 and day2 > 0:
            print(f"| {month1:,} Month, {day2:,} Day.")
        elif years1 == 0 and month1 > 0 and week1 > 0 and day2 == 0:
            print(f"| {month1:,} Month, {week1:,} Week.")
        elif years1 == 0 and month1 > 0 and week1 > 0 and day2 > 0:
            print(f"| {month1:,} Month, {week1:,} Week, {day2:,} Day.")

        elif years1 == 0 and month1 == 0 and week1 > 0 and day2 > 0:
            print(f"| {week1:,} Week, {day2:,} Day.")

        elif years1 > 0 and month1 == 0 and week1 == 0 and day2 > 0:
            print(f"| {years1:,} Year, {day2:,} Day.")
        elif years1 > 0 and month1 == 0 and week1 > 0 and day2 == 0:
            print(f"| {years1:,} Year, {week1:,} Week.")
        elif years1 > 0 and month1 > 0 and week1 == 0 and day2 == 0:
            print(f"| {years1:,} Year, {month1:,} Month.")
        elif years1 > 0 and month1 > 0 and week1 == 0 and day2 > 0:
            print(f"| {years1:,} Year, {month1:,} Month, {day2:,} Day.")
        elif years1 > 0 and month1 > 0 and week1 > 0 and day2 == 0:
            print(f"| {years1:,} Year, {month1:,} Month, {week1:,} Week.")
        elif years1 > 0 and month1 == 0 and week1 > 0 and day2 > 0:
            print(f"| {years1:,} Year, {week1:,} Week, {day2:,} Day.")
        elif years1 > 0 and month1 > 0 and week1 > 0 and day2 > 0:
            print(f"| {years1:,} Year, {month1:,} Month, {week1:,} Week, {day2:,} Day.")

        else:
            if years1 == 0 and month1 == 0 and week1 == 0 and day2 < 0:
                print(f"| {day2:,} Day.")
            elif years1 == 0 and month1 < 0 and week1 == 0 and day2 == 0:
                print(f"| {month1:,} Month.")
            elif years1 == 0 and month1 == 0 and week1 < 0 and day2 == 0:
                print(f"| {week1:,} Week.")

            elif years1 == 0 and month1 < 0 and week1 == 0 and day2 < 0:
                print(f"| {month1:,} Month, {day2:,} Day.")
            elif years1 == 0 and month1 < 0 and week1 < 0 and day2 == 0:
                print(f"| {month1:,} Month, {week1:,} Week.")
            elif years1 == 0 and month1 < 0 and week1 < 0 and day2 < 0:
                print(f"| {month1:,} Month, {week1:,} Week, {day2:,} Day.")

            elif years1 == 0 and month1 == 0 and week1 < 0 and day2 < 0:
                print(f"| {week1:,} Week, {day2:,} Day.")

            elif years1 < 0 and month1 == 0 and week1 == 0 and day2 < 0:
                print(f"| {years1:,} Year, {day2:,} Day.")
            elif years1 < 0 and month1 == 0 and week1 < 0 and day2 == 0:
                print(f"| {years1:,} Year, {week1:,} Week.")
            elif years1 < 0 and month1 < 0 and week1 == 0 and day2 == 0:
                print(f"| {years1:,} Year, {month1:,} Month.")
            elif years1 < 0 and month1 < 0 and week1 == 0 and day2 < 0:
                print(f"| {years1:,} Year, {month1:,} Month, {day2:,} Day.")
            elif years1 < 0 and month1 < 0 and week1 < 0 and day2 == 0:
                print(f"| {years1:,} Year, {month1:,} Month, {week1:,} Week.")
            elif years1 < 0 and month1 == 0 and week1 < 0 and day2 < 0:
                print(f"| {years1:,} Year, {week1:,} Week, {day2:,} Day.")
            elif years1 < 0 and month1 < 0 and week1 < 0 and day2 < 0:
                print(f"| {years1:,} Year, {month1:,} Month, {week1:,} Week, {day2:,} Day.")
    next = input()
    while True:
        if next == "" or not "" or "" \
                                   "" or not "" \
                                             "":
            print("-" * 20)
            print("\nDo You Want Again ?")
            print("For Return Select: Enter")

            next = input()

            if next == "" \
                       "":
                print("-" * 20, "\n")
                age()

            else:
                print("-" * 19)
                print("!Invalid Input.\nTry Again.")

age()