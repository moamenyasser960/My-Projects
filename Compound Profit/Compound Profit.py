print("Hello --------\n----------------->\n")
def number():
    global investment, profit, compound, s, investment1
    try:
        investment = float(str(input("Investment: ").replace(",", "").replace("_", "").strip(",~?><=|||}{:*/'!@#$%^&*() _").rstrip("+-")));print()
        investment1 = float(str(input("While Investment: ").replace(",", "").replace("_", "").strip(",~?><=|||}{:*/'!@#$%^&*() _").rstrip("+-")));print()
        profit = float(str(input("Profit% : ").replace(",", "").replace("_", "").strip(",~?><|||}{:*=/'!@#$%^&*() _").rstrip("+-")));print()
        compound = float(str(input("Compound Loop: ").replace(",", "").replace("_", "").strip(",~?><|||}{=:*/'!@#$%^&*() _").rstrip("+-")));print()
        print("-" * (16 + len(str(compound))))
    except ValueError:
        print()
        print("-" * 16, "\b>")
        print("Invalid Input!\nTry again.")
        print("-" * 16, "\b>\n")
        number()

    result = investment / 100 * profit + investment
    print(f"\n0 => {round(investment, 2):,}\n")

    for m in range(1, round(compound) + 1):
        s = f"{m} => {round(result, 2):,}"
        result = ((result + investment1) / 100) * profit + result + investment1
        print(s)
    print()

    re = input(len(s) * "-" + "-" * 2)
    if re == "" or " ":
        print()
        number()
number()