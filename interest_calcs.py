def simple_interest_calc(account, principle, interest_rate, months):
    """Calculates simple interest on one user's account.

    Args:
        account (str): Account to calculate.
        principle (float): Beginning amount before interest.
        interest_rate (float): Interest rate for account.
        months (int): Number of months to calculate for.

    """
    calculation = round(principle * (1 + interest_rate * (months/12)), 2)
    print("\nSimple interest calculation:\nA = ${}\n\nAccount: {}\nPrinciple: ${}\nInterest Rate: {}%\n"
          "Months: {}".format(calculation, account, principle, interest_rate * 100, months))
    input("\nPress Enter to continue: ")


def compound_interest_calc(account, calculation, interest_rate, months, principle):
    """Calculates compound interest on one user's account.

    Args:
        account (str): Account to calculate.
        calculation (float): Recursive calculation on principle
        principle (float): Beginning amount before interest.
        interest_rate (float): Interest rate for account.
        months (int): Number of months to calculate for.

    """
    months -= 1
    calculation = round(calculation * (1 + interest_rate * (1/12)), 2)

    if months == 0:
        print("\nCompound interest calculation:\nA = ${}\n\nAccount: {}\nPrinciple: ${}\nInterest Rate: {}%\n"
              "Months: {}".format(calculation, account, principle, interest_rate * 100, months))
        input("\nPress Enter to continue: ")
        return  # Returns back to main()

    compound_interest_calc(account, calculation, interest_rate, months, principle)
