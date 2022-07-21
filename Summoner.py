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
                 b_health, health, max_health,
                 b_mana, mana, max_mana,
                 b_healthr, healthr, max_healthr,
                 b_manar, manar, max_manar,
                 b_ad, ad, max_ad,
                 b_ap, ap, max_ap,
                 b_armor, armor, max_armor,
                 b_mr, mr, max_mr,
                 b_crit, crit,
                 b_prio, prio,
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

        self.b_health = b_health
        self.health = health
        self.MAX_HEALTH = max_health

        self.b_mana = b_mana
        self.mana = mana
        self.MAX_MANA = max_mana

        self.b_healthr = b_healthr
        self.healthr = healthr
        self.MAX_HEALTHR = max_healthr

        self.b_manar = b_manar
        self.manar = manar
        self.MAX_MANAR = max_manar

        self.b_ad = b_ad
        self.ad = ad
        self.MAX_AD = max_ad

        self.b_ap = b_ap
        self.ap = ap
        self.MAX_AP = max_ap

        self.b_armor = b_armor
        self.armor = armor
        self.MAX_ARMOR = max_armor

        self.b_mr = b_mr
        self.mr = mr
        self.MAX_MR = max_mr

        self.b_crit = b_crit
        self.crit = crit

        self.gold = gold

        self.b_prio = b_prio
        self.prio = prio  # higher prio goes first

        self.equipped = []  # items the player is wearing
        self.inventory = []  # items the player has stored

    # returns all player info
    def print(self):
        output = "________________________________________________________________"
        output += "\nSUMMONER INFORMATION:"
        output += ("\nName:\t\t" + self.name) + "\t\tClass: " + self.get_class() + "\t\tGold: " + str(self.gold)  # summoner name

        output += '\n' + create_progress_bar('Level', self.level, self.MAX_LEVEL)
        output += ('\n' + create_progress_bar('XP', self.xp, self.MAX_XP))
        output += ('\n' + create_progress_bar('Health', self.health, self.MAX_HEALTH))
        output += ('\n' + create_progress_bar('Mana', self.mana, self.MAX_MANA))
        output += '\n'
        output += '| ad: ' + str(self.ad) + \
                  ' | crit: ' + str(self.crit) + \
                  ' | ap: ' + str(self.ap) + \
                  ' | armor: ' + str(self.armor) + \
                  ' | mr: ' + str(self.mr) + \
                  ' | hp/turn: ' + str(self.healthr) + \
                  ' | mana/turn: ' + str(self.manar) + ' |'
        output += "\n________________________________________________________________\n"
        return output

    # returns all equipped items in a str
    def print_items(self):
        output = '\nEquipped items:\n\n'
        for it in self.equipped:
            output += it.print_stats_without_zero(self)
        output += '\n'
        return output

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
            return True
        return False

    # if check_level_up, add
    def level_up(self):
        self.level += 1
        return self.level_up_stats()

    # actions that happen when turns ends, i.e. check level up, reset stats
    def end_turn(self):
        if self.check_level_up():
            print("Congratulations, you leveled up! You are now level " + str(self.level))
            print("Stat changes: " + self.level_up())
            self.update_player_stats()
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
            elif stats[i][0] == 'xp':
                self.xp += change
            elif stats[i][0] == 'b_health':
                self.b_health += change
            elif stats[i][0] == 'health':
                self.health += change
            elif stats[i][0] == 'b_mana':
                self.b_mana += change
            elif stats[i][0] == 'mana':
                self.mana += change
            elif stats[i][0] == 'max_hp':
                self.MAX_HEALTH += change
            elif stats[i][0] == 'max_mana':
                self.MAX_MANA += change
            elif stats[i][0] == 'b_healthr':
                self.b_healthr += change
            elif stats[i][0] == 'healthr':
                self.healthr += change
            elif stats[i][0] == 'b_manar':
                self.b_manar += change
            elif stats[i][0] == 'manar':
                self.manar += change
            elif stats[i][0] == 'max_healthr':
                self.MAX_HEALTHR += change
            elif stats[i][0] == 'max_manar':
                self.MAX_MANAR += change
            elif stats[i][0] == 'b_ad':
                self.b_ad += change
            elif stats[i][0] == 'ad':
                self.ad += change
            elif stats[i][0] == 'max_ad':
                self.MAX_AD += change
            elif stats[i][0] == 'b_ap':
                self.b_ap += change
            elif stats[i][0] == 'ap':
                self.ap += change
            elif stats[i][0] == 'max_ap':
                self.MAX_AP += change
            elif stats[i][0] == 'b_armor':
                self.b_armor += change
            elif stats[i][0] == 'armor':
                self.armor += change
            elif stats[i][0] == 'max_armor':
                self.MAX_ARMOR += change
            elif stats[i][0] == 'b_mr':
                self.b_mr += change
            elif stats[i][0] == 'mr':
                self.mr += change
            elif stats[i][0] == 'max_mr':
                self.MAX_MR += change
            elif stats[i][0] == 'b_crit':
                self.b_crit += change
            elif stats[i][0] == 'crit':
                self.crit += change
            elif stats[i][0] == 'b_prio':
                self.b_prio += change
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

    # set all MAX_STATS to base_stat + item bonuses
    # call when leveling up or equipping item
    def update_player_stats(self):
        health, mana, healthr, manar, ad, ap, armor, mr, crit, prio = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        # add up item bonuses
        for item in self.equipped:
            health += item.health
            mana += item.mana
            healthr += item.healthr
            manar += item.manar
            ad += item.ad
            ap += item.ap
            armor += item.armor
            mr += item.mr
            crit += item.crit
            prio += item.prio

        # add base stats + item bonuses
        self.MAX_HEALTH = self.b_health + health
        self.MAX_MANA = self.b_mana + health
        self.MAX_HEALTHR = self.b_healthr + healthr
        self.MAX_MANAR = self.b_manar + manar
        self.MAX_AD = self.b_ad + ad
        self.MAX_AP = self.b_ap + ap
        self.MAX_ARMOR = self.b_armor + armor
        self.MAX_MR = self.b_mr + mr
        self.crit = self.b_crit + crit
        self.prio = self.b_prio + prio

    # each class' stat change upon leveling up
    # returns the string generated by stat_change (to be printed)
    def level_up_stats(self):
        if self.cl == 0:  # mage stats per level
            stats = [['b_health', 2],
                     ['b_ap', 5],
                     ['b_mana', 10],
                     ['b_manar', 2]]
        elif self.cl == 1:  # marksman stats per level
            stats = [['b_health', 2],
                     ['b_ad', 5],
                     ['b_crit', 1],
                     ['b_prio', 1]]
        elif self.cl == 2:  # tank
            stats = [['b_health', 10],
                     ['b_armor', 2],
                     ['b_mr', 2],
                     ['b_healthr', 2]]
        elif self.cl == 3:  # fighter
            stats = [['b_health', 5],
                     ['b_armor', 1],
                     ['b_mr', 1],
                     ['b_healthr', 1],
                     ['b_ad', 1]]
        else:
            stats = []
        stats.append(['xp', -self.xp])
        self.MAX_XP = max_xp(self.level)
        return self.stat_change(stats)

    # input 'ad', get the player's attack damage etc
    def get_statnum_fromstr(self, st):
        if st == 'b_health':
            return self.b_health
        elif st == 'b_mana':
            return self.b_mana
        elif st == 'health':
            return self.health
        elif st == 'mana':
            return self.mana
        elif st == 'max_hp':
            return self.MAX_AD
        elif st == 'max_mana':
            return self.MAX_MANA
        elif st == 'healthr':
            return self.healthr
        elif st == 'max_healthr':
            return self.MAX_HEALTHR
        elif st == 'manar':
            return self.manar
        elif st == 'max_manar':
            return self.MAX_MANAR
        elif st == 'b_ad':
            return self.b_ad
        elif st == 'ad':
            return self.ad
        elif st == 'max_ad':
            return self.MAX_AD
        elif st == 'b_ap':
            return self.b_ap
        elif st == 'ap':
            return self.ap
        elif st == 'max_ap':
            return self.MAX_AP
        elif st == 'b_armor':
            return self.b_armor
        elif st == 'armor':
            return self.armor
        elif st == 'max_armor':
            return self.MAX_ARMOR
        elif st == 'b_mr':
            return self.b_mr
        elif st == 'mr':
            return self.mr
        elif st == 'max_mr':
            return self.MAX_MR
        elif st == 'b_crit':
            return self.b_crit
        elif st == 'crit':
            return self.crit
        elif st == 'b_prio':
            return self.b_prio
        elif st == 'prio':
            return self.prio
        elif st == 'gold':
            return self.gold

    # load the player's items from text files
    def load_items(self):
        items = os.listdir('saves/' + self.name + '/items/equipped')
        if len(items) > 0:  # account for .DS file in empty folder
            for item in items:
                if not item.startswith('.'):  # filter out any invalid files
                    # add all items in equipped folder to player's equipped item array
                    self.equipped.append(Armor.get_item_from_txt('saves/' + self.name + '/items/equipped/' + item))

    # equip item if free slot, or ask player to swap it or put in inventory
    # save item to appropriate equipped or inventory folder
    def acquire_item(self, item):
        # if player equipped item, call update_player_stats
        # check if player already has an item of the same slot equipped
        can_equip = True
        existing_item = None
        for i in self.equipped:
            if i.slot == item.slot:
                can_equip = False
                existing_item = i
        if can_equip:
            self.equipped.append(item)
            print('You equipped ' + item.name + '!')
            Armor.write_item_to_txt(self, item, 'equipped')
        else:
            print('You already have an item equipped in your ' + item.slot_str
                  + ' slot. Would you like to replace it with ' + item.name + '?')
            print('Current ' + existing_item.slot_str.lower() + ' stats:\n' + existing_item.print_stats())
            print(item.name + ' stats:\n' + item.print_stats())
            selection = input('Choice (y/n): ')
            selection = valid_input(selection, ['y', 'n'])
            if selection == 'y':
                self.inventory.append(existing_item)
                self.equipped.remove(existing_item)
                self.equipped.append(item)
                print('You equipped ' + item.name + '!')
                Armor.write_item_to_txt(self, item, 'equipped')
            else:
                self.inventory.append(item)
                print('You stored ' + item.name + ' in your inventory.')
                Armor.write_item_to_txt(self, item, 'inventory')


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