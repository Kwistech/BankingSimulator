import json
import os


def menu_help():
    """Prints the menu help commands to the console."""
    summary = "Banking Simulator is a bank account simulator that can test banking practices over time.\n"
    more_info = "Once a user opens an account, they will have access to the following actions:\ndeposit, withdraw, " \
                "open account, close account.\n\nNOTE: A user opens their first account by first entering the " \
                "command 'account' and then following the steps displayed."
    header = "\nList of commands: "
    cmd_help = "'help' - Displays this help menu"
    cmd_account = "'account' - Goes to user's account and gains access to actions for account"
    cmd_info = "'info' - Display's the users account info"
    cmd_deposit = "'deposit' - If you have an account, you can deposit money into it"
    cmd_withdraw = "'withdraw' - If you have an account with money in it, you can withdraw money from it"
    cmd_open_account = "'open account' - Opens an account based on user selection"
    cmd_close_account = "'close account' - Closes an already opened account. DELETES THE ACCOUNT!!!"
    cmd_simulation = "'simulation' - If you have an account, runs banking simulation over a specified amount of time" \
                     "\n               Calculates either simple or compound interest over time."
    print("\n{summary}\n{more_info}\n{header}\n{cmd_help}\n{cmd_account}\n{cmd_info}\n{cmd_deposit}\n{cmd_withdraw}\n"
          "{cmd_open_account}\n{cmd_close_account}\n{cmd_simulation}".format(summary=summary, more_info=more_info,
                                                                             header=header, cmd_help=cmd_help,
                                                                             cmd_account=cmd_account, cmd_info=cmd_info,
                                                                             cmd_deposit=cmd_deposit,
                                                                             cmd_withdraw=cmd_withdraw,
                                                                             cmd_open_account=cmd_open_account,
                                                                             cmd_close_account=cmd_close_account,
                                                                             cmd_simulation=cmd_simulation))
    input("\nPress Enter to continue: ")


def error_check_int(item):
    """Attempts to convert item to int(item).

    Function reduces the number of instances of redundant try/except blocks.

    Args:
        item (str): String to be converted.

    Return:
        bool: True if error; else False.

    """
    try:
        int(item)
        return False
    except ValueError:
        print("ERROR: Input not valid.")
        return True


def error_check_float(item):
        """Attempts to convert item to float(item).

        Function reduces the number of instances of redundant try/except blocks.

        Args:
            item (str): String to be converted.

        Return:
            bool: True if error; else False.

        """
        try:
            float(item)
            return False
        except ValueError:
            print("ERROR: Input not valid.")
            return True


def save(account):
    """Saves all user's account information to a json file in user_accounts directory.

    Args:
        account (class): Current users account object information.

    """
    try:
        os.mkdir("./user_accounts")
    except FileExistsError:
        pass
    f = open("./user_accounts/{}_account.json".format(account.username.lower()), "w")
    json.dump(vars(account), f, indent=4)
    f.close()
