def simple_interest_calc(account, principle, interest_rate, months):
    calculation = round(principle * (1 + interest_rate * (months/12)), 2)
    print("\nSimple interest calculation:\nA = ${}\n\nAccount: {}\nPrinciple: ${}\nInterest Rate: {}%\n"
          "Months: {}".format(calculation, account, principle, interest_rate * 100, months))
    input("\nPress Enter to continue: ")


def compound_interest_calc(account, principle, interest_rate, months):
    months -= 1
    calculation = round(principle * (1 + interest_rate * (1/12)), 2)

    if months == 0:
        print(calculation)
        return

    compound_interest_calc(account, calculation, interest_rate, months)
