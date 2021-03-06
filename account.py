from general_functions import error_check_int, error_check_float
from interest_calcs import simple_interest_calc, compound_interest_calc


class Account(object):
    """User bank account filled with methods to do basic real-life bank transactions.  """

    def __init__(self, username="", savings=False, chequings=False, tax_free=False):
        """The parameters are all set to defaults so that a user can create an account without setting account
        properties to their defaults when they call this object.

        """
        if not username:
            username = input("\nPlease enter a username: ")

        # Not used as of yet. Will be used when back-end is developed.
        self.username = username

        # Toggle for account open/close; default is False (closed).
        self.account = False
        self.savings = savings
        self.chequings = chequings
        self.tax_free = tax_free

        # How much money the user has in their account.
        self.savings_amount = 0.0  # How do I round all calls of these variables to two decimal places?
        self.chequings_amount = 0.0
        self.tax_free_amount = 0.0

        # Maximum allowed money to be in account.
        self.savings_max_amount = 250000.00
        self.chequings_max_amount = 1000000.00
        self.tax_free_max_amount = 50000.00

        # Number of withdraws allowed for each user.
        self.savings_withdraws = 0
        self.savings_withdraws_total = 5
        self.chequings_withdraws = 0
        self.chequings_withdraws_total = 20
        self.tax_free_withdraws = 0
        self.tax_free_withdraws_total = 1

        # Interest rate per account; to be used with a time function soon.
        self.savings_interest_rate = 0.0075
        self.chequings_interest_rate = 0.005
        self.tax_free_interest_rate = 0.025

    def __str__(self):
        print_out = "{} Bank Account".format(self.username)
        return print_out

    def menu_screen(self):
        """Display the main command prompt information for the user NOT including the user input.  """
        top_header = "\n\nBanking Simulator"
        menu_account = "Account: {}".format(self.username)
        top_spacer = "-" * len(top_header)
        instruction = "Please enter a command \nEnter 'help' for more info"
        print("{}\n{}\n{}\n{}".format(top_header, menu_account, top_spacer, instruction))

    def account_bridge(self):
        """Create a 'bridge' between the user's input and the open/close condition of their account(s).  """
        if not self.savings and not self.chequings and not self.tax_free:
            cmd_ab = input("\nYou do not have any accounts! Do you want to open one [y/n]? ")

            if cmd_ab == "y":
                self.open_account()
        else:
            self.account = True
            self.account_main()

    def account_main(self):
        """Display basic commands for the users account; correlates to the classes methods.

        The functionality of this method is also accessible from main().

        """
        if self.account:
            print("\nWhat would you like to do?")
            account_main_choice = input("[deposit, withdraw, open account, close account, info]: ")

            if account_main_choice == "deposit":
                self.deposit()
            elif account_main_choice == "withdraw":
                self.withdraw()
            elif account_main_choice == "open account":
                self.open_account()
            elif account_main_choice == "close account":
                self.close_account()
            elif account_main_choice == "info":
                self.account_info()
            else:
                print("\nERROR: Input not recognized!")

    def account_type_info(self):
        """Displays the information for the different types of accounts that can be used.  """
        account_type = input("\nWhich account type do you want more info on [savings, chequings, tax free]? ")

        if account_type == "savings":
            print("\nSavings Account Info\nWithdraw Total: {}\nInterest Rate: {}\nMax Amount: ${}"
                  .format(self.savings_withdraws_total, self.savings_interest_rate, self.savings_max_amount))
        elif account_type == "chequings":
            print("\nChequings Account Info\nWithdraw Total: {}\nInterest Rate: {}\nMax Amount: ${}"
                  .format(self.chequings_withdraws_total, self.chequings_interest_rate, self.chequings_max_amount))
        elif account_type == "tax free":
            print("\nTax Free Account Info\nWithdraw Total: {}\nInterest Rate: {}\nMax Amount: ${}"
                  .format(self.tax_free_withdraws_total, self.tax_free_interest_rate, self.tax_free_max_amount))

    def open_account(self):
        """Opens an account for the user if that account is not opened already.  """
        print("\nWhat type of account do you want to open [savings, chequings, tax free]?")
        account_choice = input("For more info, type 'info': ")

        if account_choice == "savings":
            if not self.savings:
                print("\nOpened a Savings account!")
                self.savings = True
                self.account = True  # The user has at least 1 account.
            else:
                print("\nERROR: Only one savings account allowed per user!")
        elif account_choice == "chequings":
            if not self.chequings:
                print("\nOpened a Chequings account!")
                self.chequings = True
                self.account = True
            else:
                print("\nERROR: Only one chequings account allowed per user!")
        elif account_choice == "tax free":
            if not self.tax_free:
                print("\nOpened a Tax Free account!")
                self.tax_free = True
                self.account = True
            else:
                print("\nERROR: Only one tax free account allowed per user!")
        elif account_choice == "info":
            self.account_type_info()
        else:
            print("\nERROR: Input not valid!")

    def close_account(self):
        """Closes an account for the user if that account exists.  """
        if self.account:
            account_choice = input("Which account do you want to close? ")

            if account_choice == "savings":
                print("\nSavings account closed!")
                self.savings = False
            elif account_choice == "chequings":
                print("\nChequings account closed!")
                self.chequings = False
            elif account_choice == "tax free":
                print("\nTax Free account closed!")
                self.tax_free = False
            else:
                print("ERROR: Input not valid!")
        else:
            print("ERROR: You don't have any accounts to close!")

    def deposit(self):
        """Deposits money into one of the users accounts if that account is opened.

        Note: there is a max limit on how much money each account can hold.

        """
        account_deposit = input("\nWhich account would you like to deposit to [savings, chequings, tax free]? ")

        if account_deposit == "savings" and self.savings:
            deposit = input("Amount to deposit into savings account: ")
            error = error_check_float(deposit)  # Handles ValueError Exception

            if not error:
                if not float(deposit) + self.savings_amount > self.savings_max_amount:
                    print("\n${} successfully deposited into savings account!".format(deposit))
                    self.savings_amount += float(deposit)
                else:
                    print("\nERROR: Deposit: ${} + Account: ${} > total allowed ${}!".format(deposit,
                                                                                             self.savings_amount,
                                                                                             self.savings_max_amount))
            else:
                print("\nNote: Deposit did not work as '{}' is invalid!".format(deposit))

        elif account_deposit == "chequings" and self.chequings:
            deposit = input("Amount to deposit into chequings account: ")
            error = error_check_float(deposit)

            if not error:
                if not float(deposit) + self.chequings_amount > self.chequings_max_amount:
                    print("\n${} successfully deposited into chequings account!".format(deposit))
                    self.chequings_amount += float(deposit)
                else:
                    print("\nERROR: Deposit: ${} + Account: ${} > total allowed ${}!".format(deposit,
                                                                                             self.chequings_amount,
                                                                                             self.chequings_max_amount))
            else:
                print("\nNote: Deposit did not work as '{}' is invalid!".format(deposit))

        elif account_deposit == "tax free" and self.tax_free:
            deposit = input("Amount to deposit into tax free account: ")
            error = error_check_float(deposit)

            if not error:
                if not float(deposit) + self.tax_free_amount > self.tax_free_max_amount:
                    print("\n${} successfully deposited into tax free account!".format(deposit))
                    self.tax_free_amount += float(deposit)
                else:
                    print("\nERROR: Deposit: ${} + Account: ${} > total allowed ${}!".format(deposit,
                                                                                             self.tax_free_amount,
                                                                                             self.tax_free_max_amount))
            else:
                print("\nNote: Deposit did not work as '{}' is invalid!".format(deposit))

        else:
            print("\nERROR: you have not opened that account yet!")

    def withdraw(self):
        """Withdraws money from one of the users accounts if that account is opened and has money in it.

        Note: there is a max number of withdraws per account.

        """
        account_withdraw = input("\nWhich account would you like to withdraw from [savings, chequings, tax free]? ")

        if account_withdraw == "savings" and self.savings:
            withdraw_limit = self.withdraw_limit(check="savings")

            if not withdraw_limit:
                withdraw = input("Amount to withdraw from savings account: ")
                error = error_check_float(withdraw)  # Handles ValueError Exception

                if not error:
                    if float(withdraw) < self.savings_amount:
                        print("\nSuccessfully withdrew ${} from savings account!".format(withdraw))
                        self.savings_amount -= float(withdraw)
                        self.savings_withdraws += 1
                    else:
                        print("\nERROR: Not enough money in this account for withdraw!")
                else:
                    print("\nNote: Withdraw did not work as '{}' is invalid!".format(withdraw))

        elif account_withdraw == "chequings" and self.chequings:
            withdraw_limit = self.withdraw_limit(check="chequings")

            if not withdraw_limit:
                withdraw = input("Amount to withdraw from chequings account: ")
                error = error_check_float(withdraw)

                if not error:
                    if float(withdraw) < self.chequings_amount:
                        print("\nSuccessfully withdrew ${} from chequings account!".format(withdraw))
                        self.chequings_amount -= float(withdraw)
                        self.chequings_withdraws += 1
                    else:
                        print("\nERROR: Not enough money in this account for withdraw!")
                else:
                    print("\nNote: Withdraw did not work as '{}' is invalid!".format(withdraw))

        elif account_withdraw == "tax free" and self.tax_free:
            withdraw_limit = self.withdraw_limit(check="tax free")

            if not withdraw_limit:
                withdraw = input("Amount to withdraw from tax free account: ")
                error = error_check_float(withdraw)

                if not error:
                    if float(withdraw) < self.tax_free_amount:
                        print("\nSuccessfully withdrew ${} from tax free account!".format(withdraw))
                        self.tax_free_amount -= float(withdraw)
                        self.tax_free_withdraws += 1
                    else:
                        print("\nERROR: Not enough money in this account for withdraw!")
                else:
                    print("\nNote: Withdraw did not work as '{}' is invalid!".format(withdraw))

        else:
            print("\nERROR: you have not opened that account yet!")

    def withdraw_limit(self, check=""):
        """Checks to see if the withdraw limit on a user's account has been reached.

        Args:
            check (str): Defines what account will be checked.

        Return:
            bool: True if limit has been reached; else False.

        """
        if check == "savings":
            if self.savings_withdraws == self.savings_withdraws_total:
                print("\nERROR: Max amount of withdraws reached for savings account!")
                return True
            else:
                return False
        elif check == "chequings":
            if self.chequings_withdraws == self.chequings_withdraws_total:
                print("\nERROR: Max amount of withdraws reached for chequings account!")
                return True
            else:
                return False
        elif check == "tax free":
            if self.tax_free_withdraws == self.tax_free_withdraws_total:
                print("\nERROR: Max amount of withdraws reached for tax free account!")
                return True
            else:
                return False
        else:
            print("ERROR: '{}' not valid input!".format(check))

    def savings_account(self):
        """Displays the user's savings account information if the user has opened a savings account.  """
        if self.savings:
            print("\nYour Savings account info:")
            print("Amount: ${}\nInterest Rate: {}\nWithdraws: {}/{}".format(self.savings_amount,
                                                                            self.savings_interest_rate,
                                                                            self.savings_withdraws,
                                                                            self.savings_withdraws_total))

    def chequings_account(self):
        """Displays the user's chequings account information if the user has opened a chequings account.  """
        if self.chequings:
            print("\nYour Chequings account info:")
            print("Amount: ${}\nInterest Rate: {}\nWithdraws: {}/{}".format(self.chequings_amount,
                                                                            self.chequings_interest_rate,
                                                                            self.chequings_withdraws,
                                                                            self.chequings_withdraws_total))

    def tax_free_account(self):
        """Displays the user's tax free account information if the user has opened a tax free account.  """
        if self.tax_free:
            print("\nYour Tax Free account info:")
            print("Amount: ${}\nInterest Rate: {}\nWithdraws: {}/{}".format(self.tax_free_amount,
                                                                            self.tax_free_interest_rate,
                                                                            self.tax_free_withdraws,
                                                                            self.tax_free_withdraws_total))

    def account_info(self):
        """Displays all the user's account information; only displays opened accounts.  """
        if self.account:
            print("\n{} Bank Information".format(self.username))
            self.savings_account()
            self.chequings_account()
            self.tax_free_account()
        else:
            print("\nERROR: You don't have any accounts!")

    def time_simulation(self):
        """Calculates and prints the total amount of money accrued with interest over a specified amount of time.

        Requirements: the user must have at least one open bank account with funds in it. Called via main().

        The user can choose to use either simple or compound interest to use in their simulation and must provide a
        length of time in months.

        """
        if self.account:
            print("\nBanking Simulation")
            account = input("Which account do you want to simulate? ").lower()
            interest_type = input("What interest type [simple, compound]: ")
            months = input("How many months do you want to run the simulation? ")
            error = error_check_int(months)

            if not error and account in ["savings", "chequings", "tax free"]:
                months = int(months)

                if account == "savings" and interest_type == "simple":
                    simple_interest_calc(account="savings",
                                         principle=self.savings_amount,
                                         interest_rate=self.savings_interest_rate,
                                         months=months)
                elif account == "chequings" and interest_type == "simple":
                    simple_interest_calc(account="chequings",
                                         principle=self.chequings_amount,
                                         interest_rate=self.chequings_interest_rate,
                                         months=months)
                elif account == "tax free" and interest_type == "simple":
                    simple_interest_calc(account="tax free",
                                         principle=self.tax_free_amount,
                                         interest_rate=self.tax_free_interest_rate,
                                         months=months)

                elif account == "savings" and interest_type == "compound":
                    compound_interest_calc(account="savings",
                                           calculation=self.savings_amount,
                                           interest_rate=self.savings_interest_rate,
                                           months=months - 1,  # Interest doesn't start until after the first month.
                                           principle=self.savings_amount)
                elif account == "chequings" and interest_type == "compound":
                    compound_interest_calc(account="chequings",
                                           calculation=self.chequings_amount,
                                           interest_rate=self.chequings_interest_rate,
                                           months=months - 1,
                                           principle=self.chequings_amount)
                elif account == "tax free" and interest_type == "compound":
                    compound_interest_calc(account="tax free",
                                           calculation=self.tax_free_amount,
                                           interest_rate=self.tax_free_interest_rate,
                                           months=months - 1,
                                           principle=self.tax_free_amount)
            else:
                print("\nERROR: Time simulation did not work as {} is invalid!".format(account))
        else:
            print("\nERROR: You don't have any accounts!")
