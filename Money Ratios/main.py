print("Hello!\n\ncxx{}::::::::::>\n")

def cu():

    pay1 = []
    sell1 = []
    tax1 = []

    try:
        while True:
            try:
                pay = float(str(input(f"How Much Did You Bay It: ").replace(",", "").replace("_", "").strip(",~?><|||}{=:*/'!@#$%^&*() _").rstrip(" +- ")))
                print("")

                sell = float(str(input(f"How Much Did You Sell It: ").replace(",", "").replace("_", "").strip(",~?><|||}{=:*/'!@#$%^&*() _").rstrip(" +- ")))
                print("")

                tax = float(str(input(f"How Much Is This Tax? : ").replace(",", "").replace("_", "").strip(",~?><|||}{=:*/'!@#$%^&*() _").rstrip(" +- ")))
                print("")

                print("-" * 25, "\n")

                pay1.append(pay)
                sell1.append(sell)
                tax1.append(tax)

                pay3 = sum(pay1)
                sell3 = sum(sell1)
                tax3 = sum(tax1)

            except ValueError:
                re =  float(pay3 / 100) # 1
                re1 = float(sell3 / re - 100) # %
                ta = float(tax3 / re)

                print("-" * 22)

                if re1 <= 0:
                    if tax > 0 :
                        print(f'\n\nThe Results Are:-\n\nLoss Percentage Plus Taxes Is = [ %{float(re1 - ta)} ] -> {float(sell3 - tax3 - pay3)} .\n\n'
                              f'The Tax Loss Percentage Of The Purchase Amount Is = [ %-{ta} ] -> -{tax3} .\n\n'
                              f'Loss Percentage Without Tax = [ %{float(re1)} ] -> {float(sell3 - pay3)} .')
                    else:
                        print(f'\n\nThe Result Is:-\n\nLoss Percentage is = [ %{float(re1)} ] -> {float(sell3 - pay3)} .')

                elif re1 > 0:
                    if tax > 0 :
                        print(f'\n\nThe Results Are:-\n\nThe Profit Percentage Minus Taxes Is = [ %{float(re1 - ta)} ] -> {float(sell3 - tax3 - pay3)} .\n\n'
                              f'The Tax Loss Percentage Of The Purchase Amount Is = [ %-{ta} ] -> -{tax3} .\n\n'
                              f'Profit Rate Without Tax = [ %{float(re1)} ] -> {float(sell3 - pay3)} .')
                    else:
                        print(f'\n\nThe Result Is:-\n\nThe Profit Percentage is = [ %{float(re1)} ] -> {float(sell3 - pay3)} .')

                ro = input()
                if ro == "" or " ":
                    print("")
                    print("-" * 32, "\n")
                    cu()

    except UnboundLocalError:
        print("-" * 25, "\n")
        cu()

cu()