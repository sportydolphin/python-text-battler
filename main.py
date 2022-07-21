import os
import os.path
import shutil
import random

import Battle
import Armor
from Summoner import Summoner
from Summoner import max_xp
from Summoner import class_to_num


# check if a file with file_name exists in saves folder
def find_file(file_name, cur_dir='saves'):
    while True:
        file_list = os.listdir('saves')
        parent_dir = os.path.dirname(cur_dir)
        if file_name in file_list:
            return True
        else:
            if cur_dir == parent_dir:  # if dir is root dir
                return False
            else:
                cur_dir = parent_dir


# input poop, output 112 111 111 112
def get_ASCII(inputstring):
    output = ''
    for i in range(len(inputstring)):
        output += str(ord(inputstring[i:i + 1])) + ' '
    return output


# input poop, output 112 111 111 112.txt
def get_file_name(inputstring):
    return get_ASCII(inputstring) + '.txt'


# check if selection is the same as any element of actual, return user input (may ask for re-input if invalid)
def valid_input(selection, actual):
    valid = False
    for i in actual:
        if selection == i:
            valid = True
    while not valid:
        selection = input('Invalid input. Try again: ')
        for i in actual:
            if selection == i:
                valid = True
    return selection


# ask for name and create save if not exist, load summoner if save exists (return summoner)
# load summoner items
def load_save(name):
    saveFileName = get_file_name(name)

    if find_file(name):  # Save file is found
        print('Save found.')
        player = get_summoner_from_file(name)
        player.load_items()
    else:  # Save file is not found
        selection = input('Save file not found. Create new save? (y/n): ')
        selection = valid_input(selection, ['y', 'n'])
        if selection == 'n':
            print('Oh. Why the fuck did you play this game then?')
            quit()
        player = create_default_summoner(name)
        save_summoner_to_file(player)
        print('Summoner ' + player.name + ' created at level ' + player.level)
    print(player.print())
    return player


# returns a string array of all saves
def get_all_saves():
    saves = os.listdir('saves')
    names = []
    if len(saves) > 1:
        for save in saves:
            if not save.startswith('.'):  # commented code is from when each user didn't have own folder
                # name = ''
                # justNums = save[0:len(save) - 4]
                # numList = justNums.split()
                # for asciinum in numList:
                #     name += chr(int(asciinum))
                # names.append(name)
                names.append(save)
        return names
    else:
        return ['No saves found']


# print a list of all saves
def show_all_saves():
    saves = get_all_saves()
    output = '| '
    for save in saves:
        output += save + ' | '
    print(output)


#     //////////////////////////////////////////  WHEN ADDING NEW STAT, UPDATE THESE 4: \\\\\\\\\\\\\\\\\\\\\\\\\\
# write a summoner object to a txt file in saves
def save_summoner_to_file(s):
    with open('saves/' + s.name + '/' + get_file_name(s.name), 'w+') as f:
        f.write('Name: ' + s.name
                + '\n' + str(s.cl)
                + '\n' + str(s.level)
                + '\n' + str(s.xp)
                + '\n' + str(s.b_health)
                + '\n' + str(s.health)
                + '\n' + str(s.MAX_HEALTH)
                + '\n' + str(s.b_mana)
                + '\n' + str(s.mana)
                + '\n' + str(s.MAX_MANA)
                + '\n' + str(s.b_healthr)
                + '\n' + str(s.healthr)
                + '\n' + str(s.MAX_HEALTHR)
                + '\n' + str(s.b_manar)
                + '\n' + str(s.manar)
                + '\n' + str(s.MAX_MANAR)
                + '\n' + str(s.b_ad)
                + '\n' + str(s.ad)
                + '\n' + str(s.MAX_AD)
                + '\n' + str(s.b_ap)
                + '\n' + str(s.ap)
                + '\n' + str(s.MAX_AP)
                + '\n' + str(s.b_armor)
                + '\n' + str(s.armor)
                + '\n' + str(s.MAX_ARMOR)
                + '\n' + str(s.b_mr)
                + '\n' + str(s.mr)
                + '\n' + str(s.MAX_MR)
                + '\n' + str(s.b_crit)
                + '\n' + str(s.crit)
                + '\n' + str(s.b_prio)
                + '\n' + str(s.prio)
                + '\n' + str(s.gold))

    # add folders for equipped items and inventory items if not already there
    if not os.path.exists('saves/' + s.name + '/items'):
        os.mkdir('saves/' + s.name + '/items')
    if not os.path.exists('saves/' + s.name + '/items/equipped'):
        os.mkdir('saves/' + s.name + '/items/equipped')
    if not os.path.exists('saves/' + s.name + '/items/inventory'):
        os.mkdir('saves/' + s.name + '/items/inventory')


# return a summoner with default values
def create_default_summoner(name):
    player = Summoner(name,
                      cl=4,
                      level=1,
                      xp=0,
                      b_health=10,
                      health=10,
                      max_health=10,
                      b_mana=10,
                      mana=10,
                      max_mana=10,
                      b_healthr=0,
                      healthr=0,
                      max_healthr=0,
                      b_manar=0,
                      manar=0,
                      max_manar=0,
                      b_ad=0,
                      ad=0,
                      max_ad=0,
                      b_ap=0,
                      ap=0,
                      max_ap=0,
                      b_armor=0,
                      armor=0,
                      max_armor=0,
                      b_mr=0,
                      mr=0,
                      max_mr=0,
                      b_crit=0,
                      crit=0,
                      b_prio=0,
                      prio=0,
                      gold=0)
    return player


# ask for input for each field and create a summoner with those inputs
# if lvlZero is true, creates default
def create_save(lvlZero=False):
    saves = get_all_saves()
    name = input("Enter a name: ")
    for save in saves:
        if name == save:
            print("Save already exists. Loading summoner ", name)
            return get_summoner_from_file(name)
    if lvlZero:
        os.mkdir('saves/' + name)  # create save folder
        os.mkdir('saves/' + name + '/items')
        os.mkdir('saves/' + name + '/items/equipped')
        os.mkdir('saves/' + name + '/items/inventory')
        p = create_default_summoner(name)
        save_summoner_to_file(p)
        return p
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

    player = Summoner(name, cl, level, xp,
                      health, health, health,
                      mana, mana, mana,
                      healthr, healthr, healthr,
                      manar, manar, manar,
                      ad, ad, ad,
                      ap, ap, ap,
                      armor, armor, armor,
                      mr, mr, mr,
                      crit, crit,
                      prio, prio,
                      gold)
    return player


# return summoner given name, assumes it exists
def get_summoner_from_file(name):
    saveFileName = get_file_name(name)
    with open(('saves/' + name + '/' + saveFileName)) as f:
        lines = []
        for line in f:
            lines.append(line.strip())
    i = 0
    name = lines[i]
    i += 1
    cl = lines[i]
    i += 1
    level = lines[i]
    i += 1
    xp = lines[i]
    i += 1
    b_health = lines[i]
    i += 1
    health = lines[i]
    i += 1
    max_hp = lines[i]
    i += 1
    b_mana = lines[i]
    i += 1
    mana = lines[i]
    i += 1
    max_mana = lines[i]
    i += 1
    b_healthr = lines[i]
    i += 1
    healthr = lines[i]
    i += 1
    max_healthr = lines[i]
    i += 1
    b_manar = lines[i]
    i += 1
    manar = lines[i]
    i += 1
    max_manar = lines[i]
    i += 1
    b_ad = lines[i]
    i += 1
    ad = lines[i]
    i += 1
    max_ad = lines[i]
    i += 1
    b_ap = lines[i]
    i += 1
    ap = lines[i]
    i += 1
    max_ap = lines[i]
    i += 1
    b_armor = lines[i]
    i += 1
    armor = lines[i]
    i += 1
    max_armor = lines[i]
    i += 1
    b_mr = lines[i]
    i += 1
    mr = lines[i]
    i += 1
    max_mr = lines[i]
    i += 1
    b_crit = lines[i]
    i += 1
    crit = lines[i]
    i += 1
    b_prio = lines[i]
    i += 1
    prio = lines[i]
    i += 1
    gold = lines[i]
    player = Summoner(name[6:len(name)],
                      int(cl),
                      int(level),
                      int(xp),
                      int(b_health),
                      int(health),
                      int(max_hp),
                      int(b_mana),
                      int(mana),
                      int(max_mana),
                      int(b_healthr),
                      int(healthr),
                      int(max_healthr),
                      int(b_manar),
                      int(manar),
                      int(max_manar),
                      int(b_ad),
                      int(ad),
                      int(max_ad),
                      int(b_ap),
                      int(ap),
                      int(max_ap),
                      int(b_armor),
                      int(armor),
                      int(max_armor),
                      int(b_mr),
                      int(mr),
                      int(max_mr),
                      int(b_crit),
                      int(crit),
                      int(b_prio),
                      int(prio),
                      int(gold))
    return player


# delete all save files
def delete_all_saves(p):
    files = [f for f in os.listdir('saves/')]
    for save in files:
        if not save == p.name and not save == '.DS_Store':
            delete_save(save)


# delete a file, if exists, with inputted name
def delete_save(name):
    if os.path.exists('saves/' + name):
        shutil.rmtree('saves/' + name)
        return True
    else:
        return False


def town(p):
    return p


def explore(p):
    return p


# main menu each turn
def get_commands(p):
    selection = input('Input command (info/items/battle/town/explore/admin): ')
    selection = valid_input(selection, ['admin', 'info', 'items', 'battle', 'town', 'explore'])
    if selection == 'admin':
        category = input('Which category are you looking for? (save/battle/cheat): ')
        category = valid_input(category, ['save', 'battle', 'cheat'])

        if category == 'save':
            command = input('Which commands are you looking for? (create save/delete save/show saves/switch save): ')
            command = valid_input(command, ['create save', 'delete save', 'show saves', 'switch save'])
            if command == 'delete save':
                print('Which save to delete? (or type all)')
                show_all_saves()
                name = input('')
                if name == p.name:  # user tries to delete passed in player
                    print('Cannot delete currently loaded player!')
                if name == 'all':
                    delete_all_saves(p)
                    print('All saves except ' + p.name + ' deleted.')
                elif delete_save(name) and not (name == p.name):
                    print('Deletion success')
                else:
                    print('That save was not found')
            if command == 'create save':
                s = create_save()
                save_summoner_to_file(s)
                print('Summoner ' + s.name + ' created and saved!')
            if command == 'show saves':
                print('Current save: ', p.name)
                show_all_saves()
            if command == 'switch save':
                print('Which save would you like to switch to?')
                show_all_saves()
                selection = input('Enter save name:')
                selection = valid_input(selection, get_all_saves())
                return load_save(selection)
        elif category == 'battle':
            command = input('Which commands are you looking for? (rand name, rand weapon, rand enemy): ')
            command = valid_input(command, ['rand name', 'rand weapon', 'rand enemy'])
            if command == 'rand name':
                command = input('Which type of random name? (summoner, weapon): ')
                command = valid_input(command, ['summoner', 'weapon'])
                print('Randomly generated name: ' + Battle.generate_name(command))
            elif command == 'rand weapon':
                print(Battle.generate_random_weapon(p).print_stats_without_zero(p))
            elif command == 'rand enemy':
                print(Battle.generate_random_enemy(p, 0).print())
        elif category == 'cheat':
            command = input('Which commands are you looking for? (level up/add gold): ')
            command = valid_input(command, ['level up', 'add gold'])
            if command == 'level up':
                levels = input('How many times would you like to level up: ')
                for i in range(int(levels)):
                    p.level_up()
                    p.update_player_stats()
                p.full_heal()
                print('Leveled up ' + levels + ' times.')
            elif command == 'add gold':
                gold = input('Enter gold to add: ')
                p.gold += int(gold)
                print('Added ' + gold + ' gold.')
    elif selection == 'info':
        print(p.print())
    elif selection == 'items':
        print(p.print_items())
    elif selection == 'battle':
        p = Battle.battle(p)
    elif selection == 'town':
        p = town(p)
    elif selection == 'explore:':
        p = explore(p)
    # end the current command with a long line to indicate clearly
    line = ''
    columns, lines = shutil.get_terminal_size()
    for i in range(columns):
        line += '_'
    print(line)
    return p


# first prompt upon playing and returns current player. asks to load or create save
def initial_screen():
    selection = input('Load save or Create save? (l/c): ')
    selection = valid_input(selection, ['l', 'c'])

    if selection == 'l':  # User is loading a save
        if get_all_saves()[0] == 'No saves found':
            print('No saves found, creating new one...')
            p = create_save(True)
            return p
        print('Which save would you like to load?')
        show_all_saves()
        selection = input('Save file to load: ')
        selection = valid_input(selection, get_all_saves())
        return load_save(selection)
    else:
        return create_save(True)


# when a summoner is created for the first time to choose class, get a weapon
def first_play(p):
    print('Welcome to GAME NAME HERE. If this is your first time playing, I highly recommend typing \'info\' in order '
          'to familiarize yourself with the game. Otherwise, we can get started!')
    selection = input('What would you like to do? (info/start): ')
    selection = valid_input(selection, ['info', 'start'])
    if selection == 'info':
        print('You are currently level zero. In order to level up, you must gain experience from battling and '
              'exploring. You can buy items with gold to buff your stats. You will also unlock several abilities as '
              'you progress. Once level 30 is achieved, you will face off against a final boss to beat the game!')
        selection = input(
            '\nIt\'s time to choose a class! Type in the name of a class (mage | marksman | tank | fighter) '
            'for information, and type \'choose\' when ready!\nGet info on or \'choose\': ')
        selection = valid_input(selection, ['mage', 'marksman', 'tank', 'fighter', 'choose'])
    elif selection == 'start':
        selection = 'choose'

    while not selection == 'choose':
        if selection == 'mage':
            print('Mages are powerful sorcerers that rely on spells and ability power to get the job done')
        elif selection == 'marksman':
            print('Marksmen are masters of ranged weaponry and rely on high-damage attacks to slay their foes')
        elif selection == 'tank':
            print('Tanks are very beefy with large increases in health and defense')
        elif selection == 'fighter':
            print('Fighters are versatile, with balanced defenses and damage for sustained fighting')
        selection = input('Selection: ')
    selection = input('Type the name of the class you\' would like to be: ')
    selection = valid_input(selection, ['mage', 'marksman', 'tank', 'fighter', 'choose'])
    p.cl = class_to_num(selection)
    p.level_up_stats()
    p.update_player_stats()
    print('So you\'ve chosen to be a ' + p.get_class() + '! As a reward, here\'s 10 xp. Remember, you can always '
                                                         'check your stats by typing info. Good luck out there, '
                                                         'summoner!')
    p.xp += 10
    p.reset_combat_stats()
    p.full_heal()
    save_summoner_to_file(p)
    return p


if __name__ == '__main__':
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
