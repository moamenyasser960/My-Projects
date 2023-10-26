print("Hello!", "_-" * 2)
print("-_" * 4, "\b-")
print("\nTell Us The Following Information\nto Calculate The amount:-")

def Total():
    global total_amount, amount, people
    try:
        people = float(input("\nNumber of people: "))
        amount = float(input("The amount: "))
        total_amount = float(input("Total amount: "))

    except ValueError:
        print("\_/" * 6, "\b\\")
        print("\nInvalid input!")
        print("Try again.")
        print("_-" * 12)
        Total()

    #الأجرة الكاملة
    total = people * amount

    #الأجرة المتبقية
    Excess = total- total_amount

    #عدد الأشخاص اللذي لم يدفع
    didt_pay = round(Excess / amount)

    #المبلغ الزائد
    increase = total_amount - total

    #الأشخاص الزائدين
    people_increase = round(increase / amount)

    if total_amount < total :
        print("_-" * 15)
        print("\nThe Amount Of", round(people) ,"People = " , total)
        print("Remaining Amount = ", Excess, "\n")
        print("There Are", didt_pay, "People Didn't Pay.")

    elif total_amount > total :
        print("_-" * 15)
        print("\nThe Amount Of", round(people) ,"People = " , total)
        print("Excess Amount = " , increase)
        print("\nThere Increase Of", round(people_increase), "People.")

    elif total_amount == total :
        print("_-" * 15)
        print("\nThe Amount Of", round(people) ,"People = " , total, "\nFull Amount Of People.")

    p = input("")

    if p == "" \
            "":
        print("_-" * 15)
        Total()

    else:
        print("_-" * 15)
        Total()

Total()