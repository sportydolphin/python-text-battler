import os
from enum import Enum

import Armor


def create_progress_bar(name, value, maxValue):
    output = ''
    output += name + ': \t'
    if len(name) <= 5:
        output += '\t'
    pct = value / maxValue
    valueOutOf30 = (int(pct * 30))
    for i in range(valueOutOf30):
        output += '█'
    for j in range(30 - valueOutOf30):
        output += '□'
    output += ' ' + str(value) + '/' + str(maxValue)
    return output


def max_xp(level):
    return int(49 + 1.131 * level * level)


class Summoner:
    def __init__(self, name, cl, level, xp,
                 health, max_health,
                 mana, max_mana,
                 healthr, max_healthr,
                 manar, max_manar,
                 ad, max_ad,
                 ap, max_ap,
                 armor, max_armor,
                 mr, max_mr,
                 crit,
                 prio,
                 gold):
        self.name = name

        self.cl = cl
        self.clStr = Class(cl)

        if int(level) > 30:
            level = '30'
        self.level = level
        self.MAX_LEVEL = 30

        self.xp = xp
        self.MAX_XP = max_xp(level)

        self.health = health
        self.MAX_HEALTH = max_health

        self.mana = mana
        self.MAX_MANA = max_mana

        self.healthr = healthr
        self.MAX_HEALTHR = max_healthr

        self.manar = manar
        self.MAX_MANAR = max_manar

        self.ad = ad
        self.MAX_AD = max_ad

        self.ap = ap
        self.MAX_AP = max_ap

        self.armor = armor
        self.MAX_ARMOR = max_armor

        self.mr = mr
        self.MAX_MR = max_mr

        self.crit = crit

        self.gold = gold

        self.prio = prio  # higher prio goes first

        self.equipped = []  # items the player is wearing
        self.inventory = []  # items the player has stored

    # returns a string in format 'Name: [loading_bar] value/max®
    def printSummoner(self):
        print("________________________________________________________________")
        print("SUMMONER INFORMATION")
        print(("Name:\t\t" + self.name) + "\t\tClass " + self.get_class())  # summoner name

        print(create_progress_bar('Level', self.level, self.MAX_LEVEL))
        print(create_progress_bar('XP', self.xp, self.MAX_XP))
        print(create_progress_bar('Health', self.health, self.MAX_HEALTH))
        print(create_progress_bar('Mana', self.mana, self.MAX_MANA))
        output = '\n'
        output += '| ad: ' + str(self.ad) + \
                  ' | crit: ' + str(self.crit) + \
                  ' | ap: ' + str(self.ap) + \
                  ' | armor: ' + str(self.armor) + \
                  ' | mr: ' + str(self.mr) + \
                  ' | hp/turn: ' + str(self.healthr) + \
                  ' | mana/turn: ' + str(self.manar) + ' |'
        print(output)
        print('Gold: ' + str(self.gold))
        print("________________________________________________________________")

    # returns string of class of summoner
    def get_class(self):
        if self.cl == 0:
            return 'Mage'
        elif self.cl == 1:
            return 'Marksman'
        elif self.cl == 2:
            return 'Tank'
        elif self.cl == 3:
            return 'Fighter'
        else:
            return 'None'

    # change stats to their max version, minus hp and mana
    def reset_combat_stats(self):
        self.ad = self.MAX_AD
        self.ap = self.MAX_AP
        self.healthr = self.MAX_HEALTHR
        self.manar = self.MAX_MANAR
        self.armor = self.MAX_ARMOR
        self.mr = self.MAX_MR

    # return true if xp > xp needed to level up
    def check_level_up(self):
        if self.xp >= max_xp(self.level):
            self.level += 1
            return True
        return False

    # actions that happen when turns ends, i.e. check level up, reset stats
    def end_turn(self):
        if self.check_level_up():
            print("Congratulations, you leveled up! You are now level " + str(self.level))
            print("Stat changes: " + self.level_up_stats())
        self.reset_combat_stats()

    # set hp and mana to max values
    def full_heal(self):
        self.health = self.MAX_HEALTH
        self.mana = self.MAX_MANA

    # CHANGE WHEN ADDING STAT
    # adds stats accordingly, input is [['stat', value], ['stat', value]] format
    # returns a string in format '<stat> <change> | <stat> <change> | armor +20 | ap -15
    def stat_change(self, stats):
        # forms output string
        output = ''
        for i in range(len(stats)):
            change = stats[i][1]
            # change the stats
            if stats[i][0] == 'level':
                self.level += change
            if stats[i][0] == 'xp':
                self.xp += change
            if stats[i][0] == 'hp':
                self.health += change
            elif stats[i][0] == 'mana':
                self.mana += change
            elif stats[i][0] == 'max_hp':
                self.MAX_HEALTH += change
            elif stats[i][0] == 'max_mana':
                self.MAX_MANA += change
            elif stats[i][0] == 'healthr':
                self.healthr += change
            elif stats[i][0] == 'manar':
                self.manar += change
            elif stats[i][0] == 'max_healthr':
                self.MAX_HEALTHR += change
            elif stats[i][0] == 'max_manar':
                self.MAX_MANAR += change
            elif stats[i][0] == 'ad':
                self.ad += change
            elif stats[i][0] == 'max_ad':
                self.MAX_AD += change
            elif stats[i][0] == 'ap':
                self.ap += change
            elif stats[i][0] == 'max_ap':
                self.MAX_AP += change
            elif stats[i][0] == 'armor':
                self.armor += change
            elif stats[i][0] == 'max_armor':
                self.MAX_ARMOR += change
            elif stats[i][0] == 'mr':
                self.mr += change
            elif stats[i][0] == 'max_mr':
                self.MAX_MR += change
            elif stats[i][0] == 'crit':
                self.crit += change
            elif stats[i][0] == 'prio':
                self.prio += change
            elif stats[i][0] == 'gold':
                self.gold += change

            # make the output string
            output += stats[i][0] + ' '
            if stats[i][1] >= 0:
                output += '+'
            output += str(stats[i][1])
            if not i == len(stats) - 1:
                output += ' | '
        return output

    # each class' stat change upon leveling up
    # returns the string generated by stat_change (to be printed)
    def level_up_stats(self):
        if self.cl == 0:  # mage stats per level
            stats = [['max_hp', 2],
                     ['max_ap', 5],
                     ['max_mana', 10],
                     ['max_manar', 2]]
        elif self.cl == 1:  # marksman stats per level
            stats = [['max_hp', 2],
                     ['max_ad', 5],
                     ['crit', 1],
                     ['prio', 1]]
        elif self.cl == 2:  # tank
            stats = [['max_hp', 10],
                     ['max_armor', 2],
                     ['max_mr', 2],
                     ['max_healthr', 2]]
        elif self.cl == 3:  # fighter
            stats = [['max_hp', 5],
                     ['max_armor', 1],
                     ['max_mr', 1],
                     ['max_healthr', 1],
                     ['max_ad', 1]]
        else:
            stats = []
        stats.append(['xp', -self.xp])
        self.MAX_XP = max_xp(self.level)
        return self.stat_change(stats)

    # input 'ad', get the player's attack damage etc
    def get_statnum_fromstr(self, str):
        if str == 'hp':
            return self.hp
        elif str == 'mana':
            return self.mana
        elif str == 'max_hp':
            return self.MAX_AD
        elif str == 'max_mana':
            return self.MAX_MANA
        elif str == 'healthr':
            return self.healthr
        elif str == 'max_healthr':
            return self.MAX_HEALTHR
        elif str == 'manar':
            return self.manar
        elif str == 'max_manar':
            return self.MAX_MANAR
        elif str == 'ad':
            return self.ad
        elif str == 'max_ad':
            return self.MAX_AD
        elif str == 'ap:':
            return self.ap
        elif str == 'max_ap':
            return self.MAX_AP
        elif str == 'armor':
            return self.armor
        elif str == 'max_armor':
            return self.MAX_ARMOR
        elif str == 'mr':
            return self.mr
        elif str == 'max_mr':
            return self.MAX_MR
        elif str == 'crit':
            return self.crit
        elif str == 'prio':
            return self.prio
        elif str == 'gold':
            return self.gold

    # load the player's items from text files
    def load_items(self):
        items = os.listdir('saves/' + self.name + '/items/equipped')
        if len(items) > 1:  # account for .DS file in empty folder
            for item in items:
                if not item.startswith('.'):  # filter out any invalid files
                    # add all items in equipped folder to player's equipped item array
                    self.equipped.append(Armor.get_item_from_txt('saves/' + self.name + '/items/equipped/' + item))

    # equip item if free slot, or ask player to swap it or put in inventory
    def acquire_item(self, item):
        return True


class Class(Enum):
    MAGE = 0
    MARKSMAN = 1
    TANK = 2
    FIGHTER = 3
    NONE = 4


# input string, ie 'mage', output number, ie 0
def class_to_num(st):
    if st == 'mage':
        return 0
    if st == 'marksman':
        return 1
    if st == 'tank':
        return 2
    if st == 'fighter':
        return 3
    return 4
