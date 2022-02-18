import random
import string
from Summoner import Summoner
from Summoner import Class
from Armor import Weapon
import main


def get_name_list(type):
    file = 'fantasy_names.txt'
    if type == 'summoner':
        file = 'fantasy_names.txt'
    elif type == 'weapon':
        file = 'weapon_names.txt'
    with open('fantasy_names/' + file) as f:
        names = []
        for line in f:
            names.append(line.strip())
    f.close()
    return names


# type = summoner, weapon, armor
def generate_name(type):
    name = ''
    nameList = get_name_list(type)

    random.seed()
    rand = random.randrange(len(nameList))
    enemyName = nameList[rand]
    if type == 'summoner':
        rand = random.randrange(len(nameList))
        enemyName += ' ' + nameList[rand]
    return enemyName


# If type is 0, returns a random summoner as enemy
def generate_random_enemy(p, type):
    name = ''
    if type == 0:  # summoner
        name = generate_name('summoner')
        summ = main.create_default_summoner(name)

        # random class
        random.seed()
        rand = random.randrange(0, 4)
        summ.cl = rand

        # setting level conditions
        if p.level <= 4:  # if player is level 4 or below, enemy is not above player level
            lwrBound = p.level - 3
            uprBound = p.level
        else:  # otherwise level is random in range:
            lwrBound = p.level - 5  # at least 5 levels lower than player
            uprBound = p.level + 2  # at most 2 levels above player

        if lwrBound < 1:  # ensuring no negative or 0 level
            lwrBound = 1

        # create level of enemy
        rand = random.randrange(lwrBound, uprBound + 1)
        summ.level = rand

        # level up stats acccording to class
        for i in range(summ.level):
            summ.level_up_stats()
        summ.full_heal()
        summ.reset_combat_stats()
    return summ


# generate a weapon based on class of summoner p
def generate_random_weapon(p):
    # generate random weapon name
    name = generate_name('weapon')
    # generate some flavor text // TODO //
    flavor = 'A cool weapon!'
    allStatStrings = ['health', 'mana', 'healthr', 'manar', 'ad', 'ap', 'armor', 'mr', 'prio', 'crit']
    allStatNums = []
    # for i in range(len(allStatStrings)):  # populate stat increases with all 0 for now
    #    allStatNums.append(0)

    # depending on class, increase likelihood of certain stats increasing
    biasStats = []
    if p.clStr == Class.MAGE:
        biasStats = ['ap', 'mana', 'manar']
    elif p.clStr == Class.TANK:
        biasStats = ['health', 'healthr', 'armor', 'mr']
    elif p.clStr == Class.FIGHTER:
        biasStats = ['hp', 'ad', 'armor', 'mr']
    elif p.clStr == Class.MARKSMAN:
        biasStats = ['ad', 'prio', 'crit']

    for stat in allStatStrings:
        coef = 0  # coefficient for current stat being iterated on
        if stat in biasStats:  # if current stat gets 50% chance of increase
            rand = random.randint(0, 1)
        else:  # if current stat gets 10% chance of increase
            rand = random.randint(0, 9)
        if rand == 0:  # if chance of increase succeeds
            coef = random.randint(0, 50)  # change this to change stat increases, currently 0-5x player level
            coef = coef / 10  # coef is between 0 and 5 in increments of 0.1
        allStatNums.append(p.level * coef)  # add stat change to stat array to be passed to weapon constructor

    # determine stat scaling
    rand = random.randint(1, 10)
    stat_scale = 'ad'  # default ad just in case random breaks
    if rand <= 6:  # 60% chance it'll scale off of a bias stat
        x = random.randint(0,len(allStatStrings) - 3)  # subtract 3 to prevent scaling from prio and crit
        stat_scale = allStatStrings[x]
    else:
        x = random.randint(0,len(biasStats) - 1)
        stat_scale = biasStats[x]

    # determine pct stat scaling
    x = random.randint(0, 100)
    x = x / 10  # x is between 0 and 10 by increments of 0.1
    pct_scale = pow(1.6, x)

    # determine physical or magic damage
    rand = random.randint(0, 1)
    dmg_type = ''
    if rand == 0:
        dmg_type = 'physical'
    else:
        dmg_type = 'magic'

    # determine effects
    effects = ['None']

    # create weapon
    weapon = Weapon(name, allStatNums[0], allStatNums[1], allStatNums[2], allStatNums[3], allStatNums[4],
                    allStatNums[5], allStatNums[6], allStatNums[7], allStatNums[8], allStatNums[9], flavor, stat_scale,
                    pct_scale, dmg_type, effects)

    return weapon


def battle(p):
    # random chance of encountering a monster or enemy summoner
    random.seed()
    rand = random.randint(1,100)  # generate number 0-99

    if rand < 40:  # 40% chance to encounter enemy summoner
        p = generate_random_enemy(p, 0)
    return p
