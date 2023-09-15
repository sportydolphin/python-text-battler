import os
import random
from Items.Consumable import Consumable
from Summoner import Summoner, create_progress_bar
from Town.Tavern.tables import riddle_game
from utils import clear_terminal, valid_input


def tavern(summoner):
    # controls whether the player is in the endless loop
    in_tavern = True

    clear_terminal()
    print("You enter the tavern. It is dimly lit and slimy.")
    print(
        "You see several tables with people sitting at them. They all turn to look at you."
    )

    while in_tavern:
        print("\nWhat would you like to do?")
        print("\n1. Talk to the bartender")
        print("2. Talk to the people at the tables")
        print("3. Exit the tavern")

        selection = input("\nEnter a number: ")
        selection = valid_input(selection, ["1", "2", "3"])
        clear_terminal()

        if selection == "1":
            summoner = bar(summoner)
        elif selection == "2":
            print("\nWhich table would you like to approach?")
            print("\n1. Table of Conundrums")
            print("2. Table 2")
            print("3. Table 3")
            print("4. Never mind")

            selection = input("\nEnter a number: ")
            selection = valid_input(selection, ["1", "2", "3", "4"])
            clear_terminal()

            if selection == "1":
                riddle_game(summoner)
        elif selection == "3":
            clear_terminal()
            print("\nYou exit the tavern.")
            in_tavern = False

    return summoner


def bar(summoner: Summoner):
    print(
        "You sit down at the bar. The bartender asks you what you would like to order.\n"
    )
    print("1. Food (restores health)")
    print("2. Drink (restores mana)")
    print("3. Never mind")
    selection = input("\nEnter a number: ")
    selection = valid_input(selection, ["1", "2", "3"])
    if selection == "1":
        # order food to heal health
        clear_terminal()
        # retrieve 5 random food items
        foods = get_random_items(summoner, item_type="food", seed_value=1, num_items=3)
        print(
            "The bartender hands you a menu, its worn edges whispering stories of many a hungry traveler.\n"
        )
        print("What would you like to order? You have " + str(summoner.gold) + " gold.")
        print(
            create_progress_bar("Health", summoner.health, summoner.MAX_HEALTH) + "\n"
        )
        i = 1
        for food in foods:
            print(str(i) + ". " + str(food))
            i += 1

        # option to not order anything
        print(str(i) + ". Never mind")

        selection = input("\nEnter a number: ")
        selection = valid_input(selection, ["1", "2", "3", "4"])
        if selection == "4":
            # return to previous menu
            clear_terminal()
            print("You decide not to order anything.")
            return summoner
        else:
            if summoner.can_afford(foods[int(selection) - 1]):
                # acquire the item
                summoner.acquire_item(foods[int(selection) - 1])
            else:
                clear_terminal()
                print("You do not have enough gold to purchase this item.")
            return summoner
    elif selection == "2":
        # order drink to heal mana
        clear_terminal()
        # retrieve 5 random drink items
        drinks = get_random_items(
            summoner, item_type="drink", seed_value=1, num_items=3
        )
        print(
            "The bartender unveils an age-old drinks menu, each stain hinting at forgotten nights and liquid adventures.\n"
        )
        print("What would you like to order? You have " + str(summoner.gold) + " gold.")
        print(create_progress_bar("Mana", summoner.mana, summoner.MAX_MANA) + "\n")
        i = 1
        for drink in drinks:
            print(str(i) + ". " + str(drink))
            i += 1

        # option to not order anything
        print(str(i) + ". Never mind")

        selection = input("\nEnter a number: ")
        selection = valid_input(selection, ["1", "2", "3", "4"])
        if selection == "4":
            # return to previous menu
            clear_terminal()
            print("You decide not to order anything.")
            return summoner
        else:
            if summoner.can_afford(drinks[int(selection) - 1]):
                # acquire the item
                summoner.acquire_item(drinks[int(selection) - 1])
            else:
                clear_terminal()
                print("You do not have enough gold to purchase this item.")
            return summoner
    elif selection == "3":
        # return to previous menu
        clear_terminal()
        print("You decide not to order anything.")
    return summoner


def tables(summoner):
    print("\nYou sit down at a table. You see a group of people sitting at the table.")
    print("What would you like to do?")
    print("1. Talk to the group")
    print("2. Leave the table")
    selection = input("\nEnter a number: ")
    selection = valid_input(selection, ["1", "2"])
    if selection == "1":
        # talk to the group
        print("\nYou sit down at the table and talk to the group.")
    elif selection == "2":
        # leave the table
        print("\nYou leave the table.")
    return summoner


"""
Retrieve a specified number of random items (either foods or drinks) from the respective data files.

Parameters:
- item_type (str): Type of item to retrieve, either 'food' or 'drink'. Default is 'food'.
- seed_value (int, optional): Seed for the random number generator for reproducible results. Default is None (no seeding).
- num_items (int): Number of random items to retrieve. Default is 5.

Returns:
- list[str]: A list containing the randomly selected items.

Raises:
- ValueError: If the item_type is neither 'food' nor 'drink'.
- ValueError: If there are not enough items in the selected category to satisfy num_items.
"""


def get_random_items(summoner, item_type="food", seed_value=None, num_items=5):
    if seed_value is not None:
        random.seed(seed_value)

    item_names = []
    resource_restore = ""
    if item_type == "food":
        resource_restore = "health"
        filename = "Town/Tavern/foods_past.txt"
    elif item_type == "drink":
        resource_restore = "mana"
        filename = "Town/Tavern/drinks_past.txt"
    else:
        raise ValueError("Invalid item_type. Choose either 'food' or 'drink'.")

    with open(filename, "r") as f:
        for line in f:
            item_names.append(line.strip())

    # Check if there are enough items to sample from
    if len(item_names) < num_items:
        raise ValueError(
            f"Not enough items to select {num_items}. Only found {len(item_names)} items."
        )

    selected_names = random.sample(item_names, num_items)

    # Compute gold and health values for each item
    consumables = []
    for name in selected_names:
        # For gold amount
        mean_gold = 2.25 * summoner.level  # Middle of 0.5 and 4 times
        cost_in_gold = int(
            round(random.gauss(mean_gold, 0.7 * summoner.level))
        )  # Using standard deviation of 0.7*summoner.level
        cost_in_gold = max(
            0.5 * summoner.level, min(4 * summoner.level, cost_in_gold)
        )  # Clamping values

        # For health restored
        mean_health = 0.3 * summoner.MAX_HEALTH  # Middle of 0.1 and 0.5 times
        restore_amount = int(
            round(random.gauss(mean_health, 0.1 * summoner.MAX_HEALTH))
        )  # Using standard deviation of 0.1*summoner.MAX_HEALTH
        restore_amount = max(
            0.1 * summoner.MAX_HEALTH, min(0.5 * summoner.MAX_HEALTH, restore_amount)
        )  # Clamping values

        consumables.append(
            Consumable(name, cost_in_gold, resource_restore, restore_amount)
        )

    return consumables
