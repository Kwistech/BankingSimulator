def simple_interest_calc(account, principle, interest_rate, months):
    calculation = round(principle * (1 + interest_rate * (months/12)), 2)
    print("\nSimple interest calculation:\nA = ${}\n\n"
          "Account: {}\nPrinciple: ${}\nInterest Rate: {}%\nMonths: {}".format(calculation, account, principle,
                                                                               interest_rate * 100, months))
    input("\nPress Enter to continue: ")


def compound_interest_calc():
    pass
