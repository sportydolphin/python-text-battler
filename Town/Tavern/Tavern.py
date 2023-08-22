from utils import clear_terminal, valid_input


def tavern(summoner):
    # controls whether the player is in the endless loop
    in_tavern = True

    while in_tavern:
        clear_terminal()
        print("You enter the tavern. It is dimly lit and slimy.")
        print(
            "You see several tables with people sitting at them. They all turn to look at you."
        )
        print("\nWhat would you like to do?")
        print("1. Talk to the bartender")
        print("2. Talk to the people at the tables")
        print("3. Exit the tavern")

        selection = input("Enter a number: ")
        selection = valid_input(selection, ["1", "2", "3"])
        clear_terminal()

        if selection == "1":
            summoner = bar(summoner)
        elif selection == "2":
            print("\nYou walk up to the tables.")
        elif selection == "3":
            clear_terminal()
            print("\nYou exit the tavern.")
            in_tavern = False

    return summoner


def bar(summoner):
    print(
        "You sit down at the bar. The bartender asks you what you would like to order.\n"
    )
    print("1. Food (restores health)")
    print("2. Drink (restores mana)")
    print("3. Never mind")
    selection = input("Enter a number: ")
    selection = valid_input(selection, ["1", "2", "3"])
    if selection == "1":
        # order food to heal health
        print("\nYou order some food.")
    elif selection == "2":
        # order drink to heal mana
        print("\nYou order some drink.")
    elif selection == "3":
        # return to previous menu
        print("\nYou decide not to order anything.")
    return summoner


def tables(summoner):
    print("\nYou sit down at a table. You see a group of people sitting at the table.")
    print("What would you like to do?")
    print("1. Talk to the group")
    print("2. Leave the table")
    selection = input("Enter a number: ")
    selection = valid_input(selection, ["1", "2"])
    if selection == "1":
        # talk to the group
        print("\nYou sit down at the table and talk to the group.")
    elif selection == "2":
        # leave the table
        print("\nYou leave the table.")
    return summoner
