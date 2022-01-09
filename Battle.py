import random
import string
from Summoner import Summoner
import main


def get_name_list():
    with open('fantasy_names/fantasy_names.txt') as f:
        names = []
        for line in f:
            names.append(line.strip())
    f.close()
    return names


def generate_name():
    name = ''
    nameList = get_name_list()

    random.seed()
    rand = random.randrange(len(nameList))
    enemyName = nameList[rand]
    rand = random.randrange(len(nameList))
    enemyName += ' ' + nameList[rand]
    return enemyName


# If type is 0, returns a random summoner as enemy
def generate_random_enemy(p, type):
    name = ''
    if type == 0:  # summoner
        name = generate_name()
        summ = main.create_default_summoner(name)

        # random class
        random.seed()
        rand = random.randrange(0,4)
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


def generate_random_weapon(p, type):
    return p


def battle(p):
    # random chance of encountering a monster or enemy summoner
    random.seed()
    rand = random.randrange(100)  # generate number 0-99

    if rand < 40:  # 40% chance to encounter enemy summoner
        p = generate_random_enemy(p,0)
    return p