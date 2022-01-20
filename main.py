import os
import os.path
import shutil

import Battle
from Summoner import Summoner
from Summoner import max_xp


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


# BIG METHOD
# ask for name and create save if not exist, load summoner if save exists (return summoner)
def load_save(name):
    saveFileName = get_file_name(name)

    if find_file(name):  # Save file is found
        print('Save found.')
        player = get_summoner_from_file(name)
    else:  # Save file is not found
        selection = input('Save file not found. Create new save? (y/n): ')
        selection = valid_input(selection, ['y', 'n'])
        if selection == 'n':
            print('Oh. Why the fuck did you play this game then?')
            quit()
        player = create_default_summoner(name)
        save_summoner_to_file(player)
        print('Summoner ' + player.name + ' created at level ' + player.level)
    player.printSummoner()
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
    with open('saves/' + s.name + '/' + get_file_name(s.name), 'w') as f:
        f.write('Name: ' + s.name
                + '\nClass: ' + str(s.cl)
                + '\nLevel: ' + str(s.level)
                + '\nXP: ' + str(s.xp)
                + '\nHealth: ' + str(s.health)
                + '\nMax Health: ' + str(s.MAX_HEALTH)
                + '\nMana: ' + str(s.mana)
                + '\nMax Mana: ' + str(s.MAX_MANA)
                + '\nHealth Regen: ' + str(s.healthr)
                + '\nMax Health Regen: ' + str(s.MAX_HEALTHR)
                + '\nMana Regen: ' + str(s.manar)
                + '\nMax Mana Regen: ' + str(s.MAX_MANAR)
                + '\nAttack Damage: ' + str(s.ad)
                + '\nMax Attack Damage: ' + str(s.MAX_AD)
                + '\nAbility Power: ' + str(s.ap)
                + '\nMax Ability Power: ' + str(s.MAX_AP)
                + '\nArmor: ' + str(s.armor)
                + '\nMax Armor: ' + str(s.MAX_ARMOR)
                + '\nMagic Resist: ' + str(s.mr)
                + '\nMax Magic Resist: ' + str(s.MAX_MR)
                + '\nCrit Chance: ' + str(s.crit)
                + '\nPrio: ' + str(s.prio)
                + '\nGold: ' + str(s.gold))


# return a summoner with default values
def create_default_summoner(name):
    player = Summoner(name,
                      cl=4,
                      level=1,
                      xp=0,
                      health=100,
                      max_health=100,
                      mana=100,
                      max_mana=100,
                      healthr=0,
                      max_healthr=0,
                      manar=0,
                      max_manar=0,
                      ad=0,
                      max_ad=0,
                      ap=0,
                      max_ap=0,
                      armor=0,
                      max_armor=0,
                      mr=0,
                      max_mr=0,
                      crit=0,
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
        os.mkdir('saves/' + name + '/items/equpped')
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
                      health, health,
                      mana, mana,
                      healthr, healthr,
                      manar, manar,
                      ad, ad,
                      ap, ap,
                      armor, armor,
                      mr, mr,
                      crit,
                      prio,
                      gold)
    return player


# return summoner given name, assumes it exists
def get_summoner_from_file(name):
    saveFileName = get_file_name(name)
    with open(('saves/' + name + '/' + saveFileName)) as f:
        lines = []
        for line in f:
            lines.append(line.strip())
    name = lines[0]
    cl = lines[1]
    level = lines[2]
    xp = lines[3]
    health = lines[4]
    max_hp = lines[5]
    mana = lines[6]
    max_mana = lines[7]
    healthr = lines[8]
    max_healthr = lines[9]
    manar = lines[10]
    max_manar = lines[11]
    ad = lines[12]
    max_ad = lines[13]
    ap = lines[14]
    max_ap = lines[15]
    armor = lines[16]
    max_armor = lines[17]
    mr = lines[18]
    max_mr = lines[19]
    crit = lines[20]
    prio = lines[21]
    gold = lines[22]
    player = Summoner(name[6:len(name)],
                      int(cl[6:len(cl)]),
                      int(level[7:len(level)]),
                      int(xp[4:len(xp)]),
                      int(health[8:len(health)]),
                      int(max_hp[12:len(max_hp)]),
                      int(mana[6:len(mana)]),
                      int(max_mana[10:len(max_mana)]),
                      int(healthr[14:len(healthr)]),
                      int(max_healthr[18:len(max_healthr)]),
                      int(manar[12:len(manar)]),
                      int(max_manar[16:len(max_manar)]),
                      int(ad[14:len(ad)]),
                      int(max_ad[18:len(max_ad)]),
                      int(ap[15:len(ap)]),
                      int(max_ap[19:len(max_ap)]),
                      int(armor[7:len(armor)]),
                      int(max_armor[11:len(max_armor)]),
                      int(mr[14:len(mr)]),
                      int(max_mr[18:len(max_mr)]),
                      int(crit[13:len(crit)]),
                      int(prio[6:len(prio)]),
                      int(gold[6:len(mana)]))
    return player


# delete all save files
def delete_all_saves(p):
    files = [f for f in os.listdir('saves/')]
    for save in files:
        if not save == p.name:
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
    selection = input('Input command (battle/town/explore/info/admin): ')
    selection = valid_input(selection, ['admin', 'info', 'battle', 'town', 'explore'])
    if selection == 'admin':
        category = input('Which category are you looking for? (save/battle): ')
        category = valid_input(category, ['save', 'battle'])

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
            command = input('Which commands are you looking for? (rand name): ')
            command = valid_input(command, ['rand name'])
            if command == 'rand name':
                print('Randomly generated name: ' + Battle.generate_name())
    elif selection == 'info':
        p.printSummoner()
    elif selection == 'battle':
        p = Battle.battle(p)
    elif selection == 'town':
        p = town(p)
    elif selection == 'explore:':
        p = explore(p)
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


# when a summoner is created for the first time to choose class
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
    p.cl = p.class_to_num(selection)
    p.level_up_stats()
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

    # Main loop, continuously update player
    while True:
        player = get_commands(player)

        # End of loop save to file
        player.end_turn()
        save_summoner_to_file(player)
