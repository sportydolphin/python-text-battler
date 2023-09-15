import utils
from .Tavern.Tavern import tavern


def town(summoner, era):
    utils.clear_terminal()
    if era == "past":
        print("Welcome to the primitive town of the past!")
    elif era == "present":
        print("Welcome to the modern town of the present!")
    elif era == "future":
        print("Welcome to the futuristic town of the future!")

    summoner = navigate(summoner)

    return summoner


def navigate(summoner):
    print("Where would you like to go?\n")
    print("1. Tavern")
    print("2. Shop")
    print("3. Inn")
    print("4. Exit")
    selection = input("\nEnter a number: ")
    selection = utils.valid_input(selection, ["1", "2", "3", "4"])
    if selection == "1":
        summoner = tavern(summoner)
    elif selection == "2":
        # summoner = shop(summoner)
        return summoner
    elif selection == "3":
        # summoner = shopinn(summoner)
        return summoner
    return summoner
