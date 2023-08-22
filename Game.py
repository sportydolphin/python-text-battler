import shutil

from Battle import (
    battle,
    generate_name,
    generate_random_enemy,
    generate_random_weapon,
)
from Files import (
    create_save,
    delete_all_saves,
    delete_save,
    get_all_saves,
    load_save,
    save_summoner_to_file,
    show_all_saves,
)
import Town.Town as Town
from Summoner import class_to_num, create_default_summoner, create_test_summoner
from utils import valid_input


def town(p):
    return p


def explore(p):
    return p


# main menu each turn
def get_commands(p):
    selection = input("Input command (info/items/battle/town/explore/admin): ")
    selection = valid_input(
        selection, ["admin", "info", "items", "battle", "town", "explore"]
    )
    if selection == "admin":
        category = input("Which category are you looking for? (save/battle/cheat): ")
        category = valid_input(category, ["save", "battle", "cheat"])

        if category == "save":
            command = input(
                "Which commands are you looking for? (create save/delete save/show saves/switch save): "
            )
            command = valid_input(
                command, ["create save", "delete save", "show saves", "switch save"]
            )
            if command == "delete save":
                print("Which save to delete? (or type all)")
                show_all_saves()
                name = input("")
                if name == p.name:  # user tries to delete passed in player
                    print("Cannot delete currently loaded player!")
                if name == "all":
                    delete_all_saves(p)
                    print("All saves except " + p.name + " deleted.")
                elif delete_save(name) and not (name == p.name):
                    print("Deletion success")
                else:
                    print("That save was not found")
            if command == "create save":
                s = create_save()
                save_summoner_to_file(s)
                print("Summoner " + s.name + " created and saved!")
            if command == "show saves":
                print("Current save: ", p.name)
                show_all_saves()
            if command == "switch save":
                print("Which save would you like to switch to?")
                show_all_saves()
                selection = input("Enter save name:")
                selection = valid_input(selection, get_all_saves())
                return load_save(selection)
        elif category == "battle":
            command = input(
                "Which commands are you looking for? (rand name, rand weapon, rand enemy): "
            )
            command = valid_input(command, ["rand name", "rand weapon", "rand enemy"])
            if command == "rand name":
                command = input("Which type of random name? (summoner, weapon): ")
                command = valid_input(command, ["summoner", "weapon"])
                print("Randomly generated name: " + generate_name(command))
            elif command == "rand weapon":
                print(generate_random_weapon(p).print_stats_without_zero(p))
            elif command == "rand enemy":
                print(generate_random_enemy(p, 0).print())
        elif category == "cheat":
            command = input("Which commands are you looking for? (level up/add gold): ")
            command = valid_input(command, ["level up", "add gold"])
            if command == "level up":
                levels = input("How many times would you like to level up: ")
                for i in range(int(levels)):
                    p.level_up()
                    p.update_player_stats()
                p.full_heal()
                print("Leveled up " + levels + " times.")
            elif command == "add gold":
                gold = input("Enter gold to add: ")
                p.gold += int(gold)
                print("Added " + gold + " gold.")
    elif selection == "info":
        print(p.print())
    elif selection == "items":
        print(p.print_items())
    elif selection == "battle":
        p = battle(p)
    elif selection == "town":
        p = Town.town(p, "past")
    elif selection == "explore:":
        p = explore(p)
    # end the current command with a long line to indicate clearly
    line = ""
    columns, lines = shutil.get_terminal_size()
    for i in range(columns):
        line += "_"
    print(line)
    return p


# first prompt upon playing and returns current player. asks to load or create save
def initial_screen():
    selection = input("Load save or Create save? (l/c/t): ")
    selection = valid_input(selection, ["l", "c", "t"])

    if selection == "l":  # User is loading a save
        if get_all_saves()[0] == "No saves found":
            print("No saves found, creating new one...")
            p = create_save(True)
            return p
        print("Which save would you like to load?")
        show_all_saves()
        selection = input("Save file to load: ")
        selection = valid_input(selection, get_all_saves())
        return load_save(selection)
    elif selection == "c":
        return create_save(True)
    elif selection == "t":
        print("Welcome to Test Mode!")
        print("1. Town\n2. Battle\n3. Explore\n...")  # Add more as required
        test_selection = input("Select the function you want to test: ")
        # create a default player for testing or you can load a specific one
        p = create_save(lvlZero=True, isTest=True)
        save_summoner_to_file(p)

    if test_selection == "1":
        p = Town.town(p, "past")
    elif test_selection == "2":
        p = battle(p)
    elif test_selection == "3":
        p = explore(p)

    save_summoner_to_file(p)
    return p


# when a summoner is created for the first time to choose class, get a weapon
def first_play(p):
    print(
        "Welcome to GAME NAME HERE. If this is your first time playing, I highly recommend typing 'info' in order "
        "to familiarize yourself with the game. Otherwise, we can get started!"
    )
    selection = input("What would you like to do? (info/start): ")
    selection = valid_input(selection, ["info", "start"])
    if selection == "info":
        print(
            "You are currently level zero. In order to level up, you must gain experience from battling and "
            "exploring. You can buy items with gold to buff your stats. You will also unlock several abilities as "
            "you progress. Once level 30 is achieved, you will face off against a final boss to beat the game!"
        )
        selection = input(
            "\nIt's time to choose a class! Type in the name of a class (mage | marksman | tank | fighter) "
            "for information, and type 'choose' when ready!\nGet info on or 'choose': "
        )
        selection = valid_input(
            selection, ["mage", "marksman", "tank", "fighter", "choose"]
        )
    elif selection == "start":
        selection = "choose"

    while not selection == "choose":
        if selection == "mage":
            print(
                "Mages are powerful sorcerers that rely on spells and ability power to get the job done"
            )
        elif selection == "marksman":
            print(
                "Marksmen are masters of ranged weaponry and rely on high-damage attacks to slay their foes"
            )
        elif selection == "tank":
            print("Tanks are very beefy with large increases in health and defense")
        elif selection == "fighter":
            print(
                "Fighters are versatile, with balanced defenses and damage for sustained fighting"
            )
        selection = input("Selection: ")
    selection = input("Type the name of the class you' would like to be: ")
    selection = valid_input(
        selection, ["mage", "marksman", "tank", "fighter", "choose"]
    )
    p.cl = class_to_num(selection)
    p.level_up_stats()
    p.update_player_stats()
    print(
        "So you've chosen to be a "
        + p.get_class()
        + "! As a reward, here's 10 xp. Remember, you can always "
        "check your stats by typing info. Good luck out there, "
        "summoner!"
    )
    p.xp += 10
    p.reset_combat_stats()
    p.full_heal()
    save_summoner_to_file(p)
    return p


if __name__ == "__main__":
    # Initialize player
    player = initial_screen()

    # If it is first time playing, choose class
    if player.level == 1 and player.xp == 0:
        player = first_play(player)  # choose class

    # Testing section
    # Battle.generate_random_enemy(player, 0).printSummoner()
    # newWeapon = Battle.generate_random_weapon(player)
    # print('You are being given a gift of ' + newWeapon.name)
    # player.acquire_item(newWeapon)
    # Armor.write_item_to_txt('saves/' + player.name + '/items/equipped/', newWeapon)

    # Main loop, continuously update player
    while True:
        player = get_commands(player)

        # End of loop save to file
        player.end_turn()
        save_summoner_to_file(player)
