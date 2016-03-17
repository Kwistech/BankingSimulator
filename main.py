# Banking Simulator - Johnathon Kwisses (Kwistech)


def menu_help():
    summary = "Summary:\nBanking Simulator is a bank account simulator that can test banking practices over time.\n"
    more_info = "Once a user opens an account, they will have access to the following actions:\ndeposit, withdraw, " \
                "open account, close account.\n\nNOTE: A user opens their first account by first entering the " \
                "command 'account' and then following the steps displayed."
    header = "\nList of commands: "
    cmd_help = "'help' - Displays this help menu"
    cmd_account = "'account' - Goes to user's account and gains access to actions for account"
    cmd_info = "'info' - Display's the users account info"
    print("\n{0}\n{1}\n{2}\n{3}\n{4}\n{5}".format(summary, more_info, header, cmd_help, cmd_account, cmd_info))


def error_check_int(item):
    try:
        int(item)
        return False
    except ValueError:
        print("ERROR: Input not valid.")
        return True


class Account(object):

    def __init__(self, username="", password="", savings=False, chequings=False, tax_free=False):
        if not username:
            username = input("\nPlease enter your username: ")
        if not password:
            password = input("Please enter your password: ")
        self.username = username
        self.password = password

        self.account = False
        self.savings = savings
        self.chequings = chequings
        self.tax_free = tax_free

        self.savings_amount = 0
        self.chequings_amount = 0
        self.tax_free_amount = 0

        self.savings_max_amount = 250000
        self.chequings_max_amount = 1000000
        self.tax_free_max_amount = 50000

        self.savings_withdraws = 0
        self.savings_withdraws_total = 5
        self.chequings_withdraws = 0
        self.chequings_withdraws_total = 20
        self.tax_free_withdraws = 0
        self.tax_free_withdraws_total = 1

        self.savings_interest_rate = 0.0075
        self.chequings_interest_rate = 0.005
        self.tax_free_interest_rate = 0.025

    def __str__(self):
        print_out = "{} Bank Account".format(self.username)
        return print_out

    def menu_screen(self):
        top_menu = "\n\nBanking Simulator"
        menu_account = "Account: {}".format(self.username)
        top_spacer = "-" * len(top_menu)
        instruction = "Please enter a command \nEnter 'help' for more info"
        print("{}\n{}\n{}\n{}".format(top_menu, menu_account, top_spacer, instruction))

    def account_bridge(self):
        if not self.savings and not self.chequings and not self.tax_free:
            cmd_ab = input("\nYou do not have any accounts! Do you want to open one [y/n]? ")

            if cmd_ab == "y":
                self.open_account()
        else:
            self.account = True
            self.account_main()

    def account_main(self):
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
        print("\nWhat type of account do you want to open [savings, chequings, tax free]?")
        account_choice = input("For more info, type 'info': ")

        if account_choice == "savings":
            if not self.savings:
                print("\nOpened a Savings account!")
                self.savings = True
            else:
                print("\nERROR: Only one savings account allowed per user!")
        elif account_choice == "chequings":
            if not self.chequings:
                print("\nOpened a Chequings account!")
                self.chequings = True
            else:
                print("\nERROR: Only one chequings account allowed per user!")
        elif account_choice == "tax free":
            if not self.tax_free:
                print("\nOpened a Tax Free account!")
                self.tax_free = True
            else:
                print("\nERROR: Only one tax free account allowed per user!")
        elif account_choice == "info":
            self.account_type_info()
        else:
            print("\nERROR: Input not valid!")

    def close_account(self):
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
        account_deposit = input("\nWhich account would you like to deposit to [savings, chequings, tax free]? ")

        if account_deposit == "savings" and self.savings:
            deposit = input("Amount to deposit into savings account: ")
            error = error_check_int(deposit)

            if not error:
                if not int(deposit) + self.savings_amount > self.savings_max_amount:
                    print("\n${} successfully deposited into savings account!".format(deposit))
                    self.savings_amount += int(deposit)
                else:
                    print("\nERROR: Deposit: ${} + Account: ${} > total allowed ${}!".format(deposit,
                                                                                             self.savings_amount,
                                                                                             self.savings_max_amount))
            else:
                print("\nNote: Deposit did not work as '{}' is invalid!".format(deposit))

        elif account_deposit == "chequings" and self.chequings:
            deposit = input("Amount to deposit into chequings account: ")
            error = error_check_int(deposit)

            if not error:
                if not int(deposit) + self.chequings_amount > self.chequings_max_amount:
                    print("\n${} successfully deposited into chequings account!".format(deposit))
                    self.chequings_amount += int(deposit)
                else:
                    print("\nERROR: Deposit: ${} + Account: ${} > total allowed ${}!".format(deposit,
                                                                                             self.chequings_amount,
                                                                                             self.chequings_max_amount))
            else:
                print("\nNote: Deposit did not work as '{}' is invalid!".format(deposit))

        elif account_deposit == "tax free" and self.tax_free:
            deposit = input("Amount to deposit into tax free account: ")
            error = error_check_int(deposit)

            if not error:
                if not int(deposit) + self.tax_free_amount > self.tax_free_max_amount:
                    print("\n${} successfully deposited into tax free account!".format(deposit))
                    self.tax_free_amount += int(deposit)
                else:
                    print("\nERROR: Deposit: ${} + Account: ${} > total allowed ${}!".format(deposit,
                                                                                             self.tax_free_amount,
                                                                                             self.tax_free_max_amount))
            else:
                print("\nNote: Deposit did not work as '{}' is invalid!".format(deposit))

        else:
            print("\nERROR: you have not opened that account yet!")

    def withdraw(self):
        account_withdraw = input("\nWhich account would you like to withdraw from [savings, chequings, tax free]? ")

        if account_withdraw == "savings" and self.savings:
            withdraw = input("Amount to withdraw from savings account: ")
            error = error_check_int(withdraw)

            if not error:
                if int(withdraw) < self.savings_amount:
                    print("\nSuccessfully withdrew ${} from savings account!".format(withdraw))
                    self.savings_amount -= int(withdraw)
                    self.savings_withdraws += 1
                else:
                    print("\nERROR: Not enough money in this account for withdraw!")
            else:
                print("\nNote: Withdraw did not work as '{}' is invalid!".format(withdraw))

        elif account_withdraw == "chequings" and self.chequings:
            withdraw = input("Amount to withdraw from savings account: ")
            error = error_check_int(withdraw)

            if not error:
                if int(withdraw) < self.chequings_amount:
                    print("\nSuccessfully withdrew ${} from chequings account!".format(withdraw))
                    self.chequings_amount -= int(withdraw)
                    self.chequings_withdraws += 1
                else:
                    print("\nERROR: Not enough money in this account for withdraw!")
            else:
                print("\nNote: Withdraw did not work as '{}' is invalid!".format(withdraw))

        elif account_withdraw == "tax free" and self.tax_free:
            withdraw = input("Amount to withdraw from savings account: ")
            error = error_check_int(withdraw)

            if not error:
                if int(withdraw) < self.tax_free_amount:
                    print("\nSuccessfully withdrew ${} from chequings account!".format(withdraw))
                    self.tax_free_amount -= int(withdraw)
                    self.tax_free_withdraws += 1
                else:
                    print("\nERROR: Not enough money in this account for withdraw!")
            else:
                print("\nNote: Withdraw did not work as '{}' is invalid!".format(withdraw))

        else:
            print("\nERROR: you have not opened that account yet!")

    def savings_account(self):
        if self.savings:
            print("\nYour Savings account info:")
            print("Amount: ${}\nInterest Rate: {}\nWithdraws: {}/{}".format(self.savings_amount,
                                                                            self.savings_interest_rate,
                                                                            self.savings_withdraws,
                                                                            self.savings_withdraws_total))

    def chequings_account(self):
        if self.chequings:
            print("\nYour Chequings account info:")
            print("Amount: ${}\nInterest Rate: {}\nWithdraws: {}/{}".format(self.chequings_amount,
                                                                            self.chequings_interest_rate,
                                                                            self.chequings_withdraws,
                                                                            self.chequings_withdraws_total))

    def tax_free_account(self):
        if self.tax_free:
            print("\nYour Tax Free account info:")
            print("Amount: ${}\nInterest Rate: {}\nWithdraws: {}/{}".format(self.tax_free_amount,
                                                                            self.tax_free_interest_rate,
                                                                            self.tax_free_withdraws,
                                                                            self.tax_free_withdraws_total))

    def account_info(self):
        if self.account:
            print("\n{} Bank Information".format(self.username))
            self.savings_account()
            self.chequings_account()
            self.tax_free_account()
        else:
            print("\nERROR: You don't have any accounts!")


def main():
    top_menu = "\n\nWelcome to the Banking Simulator!"
    top_spacer = "-" * len(top_menu)
    print("{}\n{}".format(top_menu, top_spacer))
    account = Account()

    while True:
        account.menu_screen()
        cmd = input("> ")

        if cmd == "help":
            menu_help()
        elif cmd == "account":
            account.account_bridge()
        elif cmd == "info":
            account.account_info()
        else:
            print("\nERROR: Input not valid!")

if __name__ == "__main__":
    main()
