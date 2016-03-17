# Banking Simulator - Johnathon Kwisses (Kwistech)
from account import Account
from general_functions import menu_help


def main():
    """Runs program with account.py and general_functions.py.

    When the program starts, it asks the user for a username and a password. This will be the account the user will use
    for this program. Note: The full user back-end is not programmed yet and so the users info is not saved!

    """
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
        elif cmd == "deposit":
            account.deposit()
        elif cmd == "withdraw":
            account.withdraw()
        elif cmd == "open account":
            account.open_account()
        elif cmd == "close account":
            account.close_account()
        else:
            print("\nERROR: Input not valid!")

if __name__ == "__main__":
    main()
