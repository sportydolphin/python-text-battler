# check if a file with file_name exists in saves folder
import os
import pickle
import shutil
from Summoner import Summoner, create_default_summoner, create_test_summoner, max_xp
from utils import get_file_name, valid_input


def find_file(file_name, cur_dir="saves"):
    while True:
        file_list = os.listdir("saves")
        parent_dir = os.path.dirname(cur_dir)
        if file_name in file_list:
            return True
        else:
            if cur_dir == parent_dir:  # if dir is root dir
                return False
            else:
                cur_dir = parent_dir


# ask for name and create save if not exist, load summoner if save exists (return summoner)
# load summoner items
def load_save(name):
    if find_file(name):  # Save file is found
        print("Save found.")
        player = get_summoner_from_file(name)
        player.load_items()
    else:  # Save file is not found
        selection = input("Save file not found. Create new save? (y/n): ")
        selection = valid_input(selection, ["y", "n"])
        if selection == "n":
            print("Oh. Why the fuck did you play this game then?")
            quit()
        player = create_default_summoner(name)
        save_summoner_to_file(player)
        print("Summoner " + player.name + " created at level " + player.level)
    print(player.print())
    return player


# returns a string array of all saves
def get_all_saves():
    saves = os.listdir("saves")
    names = []
    if len(saves) > 1:
        for save in saves:
            # commented code is from when each user didn't have own folder
            if not save.startswith("."):
                # name = ''
                # justNums = save[0:len(save) - 4]
                # numList = justNums.split()
                # for asciinum in numList:
                #     name += chr(int(asciinum))
                # names.append(name)
                names.append(save)
        return names
    else:
        return ["No saves found"]


# print a list of all saves
def show_all_saves():
    saves = get_all_saves()
    output = "| "
    for save in saves:
        output += save + " | "
    print(output)

    #     //////////////////////////////////////////  WHEN ADDING NEW STAT, UPDATE THESE 4: \\\\\\\\\\\\\\\\\\\\\\\\\\


# write a summoner object to a txt file in saves
def save_summoner_to_file(s):
    # Check if the main save folder exists, if not, create it
    if not os.path.exists("saves"):
        os.mkdir("saves")

    # Check if the specific summoner save directory exists, if not, create it
    if not os.path.exists("saves/" + s.name):
        os.mkdir("saves/" + s.name)

    # Save the summoner to the file
    save_file_path = "saves/" + s.name + "/" + s.name + ".pickle"
    with open(save_file_path, "wb") as f:
        pickle.dump(s, f, protocol=pickle.HIGHEST_PROTOCOL)

    # Add folders for equipped items and inventory items if not already there
    if not os.path.exists("saves/" + s.name + "/items"):
        os.mkdir("saves/" + s.name + "/items")
    if not os.path.exists("saves/" + s.name + "/items/equipped"):
        os.mkdir("saves/" + s.name + "/items/equipped")
    if not os.path.exists("saves/" + s.name + "/items/inventory"):
        os.mkdir("saves/" + s.name + "/items/inventory")


# ask for input for each field and create a summoner with those inputs
# if lvlZero is true, creates default
def create_save(lvlZero=False, isTest=False):
    if isTest:
        name = "tester"
    else:
        name = input("Enter a name: ")

    existing_saves = get_all_saves()
    if name in existing_saves:
        print("Save already exists. Loading summoner", name)
        return get_summoner_from_file(name)

    if isTest and lvlZero:
        return create_test_summoner()
    elif lvlZero and not isTest:
        return create_default_summoner(name)
    else:
        cl = input("Enter a class (0 mage | 1 marksman | 2 tank | 3 fighter): ")
        level = input("Enter a level: ")
        xp = input(("Enter XP out of " + str(max_xp(int(level))) + ":"))
        health = input("Enter health: ")
        mana = input("Enter mana: ")
        healthr = input("Enter health regeneration: ")
        manar = input("Enter mana regeneration: ")
        ad = input("Enter attack damage: ")
        ap = input("Enter ability power: ")
        armor = input("Enter armor: ")
        mr = input("Enter magic resist: ")
        crit = input("Enter crit chance: ")
        prio = input("Enter prio: ")
        gold = input("Enter gold: ")

    player = Summoner(
        name,
        cl,
        level,
        xp,
        health,
        health,
        health,
        mana,
        mana,
        mana,
        healthr,
        healthr,
        healthr,
        manar,
        manar,
        manar,
        ad,
        ad,
        ad,
        ap,
        ap,
        ap,
        armor,
        armor,
        armor,
        mr,
        mr,
        mr,
        crit,
        crit,
        prio,
        prio,
        gold,
    )
    return player


# return summoner given name, assumes it exists
def get_summoner_from_file(name):
    saveFileName = name
    with open("saves/" + name + "/" + saveFileName + ".pickle", "rb") as f:
        player = pickle.load(f)
    return player


# delete all save files
def delete_all_saves(p):
    files = [f for f in os.listdir("saves/")]
    for save in files:
        if not save == p.name and not save == ".DS_Store":
            delete_save(save)


# delete a file, if exists, with inputted name
def delete_save(name):
    if os.path.exists("saves/" + name):
        shutil.rmtree("saves/" + name)
        return True
    else:
        return False
