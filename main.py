# Banking Simulator - Johnathon Kwisses (Kwistech)


def menu_screen():
    top_menu = "Banking Simulator"
    top_spacer = "-" * len(top_menu)
    instruction = "Please enter a command \nEnter 'help' for more info"
    print("{}\n{}\n{}".format(top_menu, top_spacer, instruction))


def menu_help():
    summary = "Banking Simulator is a bank account simulator that can test banking practices over time"
    header = "Here is a list of commands: "
    cmd_account = "'account' - Goes to the user's account; requires username and password"
    print("\n{0}\n{1}\n\n{2}".format(summary, header, cmd_account))


class Account(object):

    def __init__(self, username, password):
        self.username = username
        self.password = password


def main():
    menu_screen()
    cmd = input("> ")

    if cmd == "help":
        menu_help()
    elif cmd == "account":
        pass

if __name__ == "__main__":
    main()
