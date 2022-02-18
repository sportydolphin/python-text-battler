from enum import Enum


class Item:
    def __init__(self, name, slot, health, mana, healthr, manar, ad, ap, armor, mr, crit, prio, flavor):
        self.name = name
        self.slot = slot
        self.slot_str = get_slot_str(slot)
        self.health = health
        self.mana = mana
        self.healthr = healthr
        self.manar = manar
        self.ad = ad
        self.ap = ap
        self.armor = armor
        self.mr = mr
        self.crit = crit
        self.prio = prio
        self.flavor = flavor

        self.stat_arr = [['name', self.name], ['slot', self.slot_str], ['health', self.health], ['mana', self.mana],
                         ['healthr', self.healthr], ['manar', self.manar], ['ad', self.ad], ['ap', self.ap],
                         ['armor', self.armor], ['mr', self.mr], ['crit', self.crit], ['prio', self.prio],
                         ['flavor', self.flavor]]

    # create string of name, slot and stats
    def print(self):
        return 'Name: ' + self.name + '\tSlot: ' + self.slot_str + '\n' + self.flavor + '\nStats: ' + self.print_stats()

    # return string of stats, with extras if weapon
    def print_stats(self):
        out = 'hp: ' + str(self.health) + ' | mana: ' + str(self.mana) + ' | ad: ' + str(self.ad) + ' | ap: ' \
              + str(self.ap) + ' | armor: ' + str(self.armor) + ' | mr: ' + str(self.mr) + ' | crit: ' \
              + str(self.crit) + '% | prio: ' + str(self.prio)
        if isinstance(self, Weapon):
            out += 'damage type: ' + self.dmg_type + ' | scaling: ' + str(100 * self.pct_scale) + '% of ' \
                   + self.stat_scale
        return out

    # return string of stats, with extras if weapons, exclude all stats that are 0
    def print_stats_without_zero(self):
        out = '| '
        for i in range(len(self.stat_arr)):
            if self.stat_arr[i][1] != 0:
                out += self.stat_arr[i][0] + ':' + str(self.stat_arr[i][1]) + ' | '
        if isinstance(self, Weapon):
            out += 'damage type: ' + self.dmg_type + ' | scaling: ' + str(100 * self.pct_scale) + '% of ' \
                   + self.stat_scale
        return out


class Weapon(Item):
    def __init__(self, name, health, mana, healthr, manar, ad, ap, armor, mr, crit, prio, flavor, stat_scale, pct_scale,
                 dmg_type, effects):
        super().__init__(name, Slot.WEAPON, health, mana, healthr, manar, ad, ap, armor, mr, crit, prio, flavor)
        self.stat_scale = stat_scale  # string that will indicate which stat its damage is based on, ie 'ap', 'armor'
        self.pct_scale = pct_scale
        self.dmg_type = dmg_type
        self.effects = effects  # things like armor shred, life steal, etc
        self.stat_arr = [['name', self.name], ['slot', self.slot_str], ['health', self.health], ['mana', self.mana],
                         ['healthr', self.healthr], ['manar', self.manar], ['ad', self.ad], ['ap', self.ap],
                         ['armor', self.armor], ['mr', self.mr], ['crit', self.crit], ['prio', self.prio],
                         ['flavor', self.flavor], ['stat scale', self.stat_scale], ['pct scale', self.pct_scale],
                         ['dmg type', self.dmg_type], ['effects', self.effects]]

    # calculates damage done by the weapon
    def calculate_outputdmg(self, p):
        player_scaling_stat_num = p.get_statnum_fromstr(self.stat_scale)
        return player_scaling_stat_num * self.pct_scale


class Slot(Enum):
    WEAPON = 0
    HELMET = 1
    CHEST = 2
    LEGS = 3
    BOOTS = 4


def get_slot_str(s):
    if s == Slot.WEAPON:
        return 'WEAPON'
    elif s == Slot.HELMET:
        return 'HELMET'
    elif s == Slot.CHEST:
        return 'CHESTPLATE'
    elif s == Slot.LEGS:
        return 'LEGGINGS'
    elif s == Slot.BOOTS:
        return 'BOOTS'
    else:
        return 'NONE'


# return Slot, input is string i.e. 'WEAPON', 'HELMET'
def get_slot_from_str(s):
    if s == 'WEAPON':
        return Slot.WEAPON
    elif s == 'HELMET':
        return Slot.HELMET
    elif s == 'CHESTPLATE':
        return Slot.CHEST
    elif s == 'LEGGINGS':
        return Slot.LEGS
    elif s == 'BOOTS':
        return Slot.BOOTS


# returns an item object from txt file
def get_item_from_txt(txt_path):
    lines = []
    with open(txt_path) as f:
        for line in f:
            lines.append(line.strip())
    f.close()

    # all generic item stats
    i = 0  # line number counter
    name = lines[i]
    slot_str = lines[i + 1]
    health = lines[i + 1]
    mana = lines[i + 1]
    healthr = lines[i + 1]
    manar = lines[i + 1]
    ad = lines[i + 1]
    ap = lines[i + 1]
    armor = lines[i + 1]
    mr = lines[i + 1]
    crit = lines[i + 1]
    prio = lines[i + 1]
    flavor = lines[i + 1]

    # if weapon, add extra parameters
    if slot_str == 'WEAPON':
        stat_scale = lines[i + 1]
        pct_scale = lines[i + 1]
        effects = lines[i + 1]
        return Weapon(name, health, mana, healthr, manar, ad, ap, armor, mr, prio, flavor, stat_scale, pct_scale,
                      effects)
    else:  # if armor
        return Item(name, get_slot_from_str(slot_str), health, mana, healthr, manar, ad, ap, armor, mr, prio, flavor)


# write item to text file
def write_item_to_txt(path, item):
    with open(path + item.name, 'w') as f:
        f.write(item.name
                + '\n' + item.slot_str
                + '\n' + str(item.health)
                + '\n' + str(item.mana)
                + '\n' + str(item.healthr)
                + '\n' + str(item.manar)
                + '\n' + str(item.ad)
                + '\n' + str(item.ap)
                + '\n' + str(item.armor)
                + '\n' + str(item.mr)
                + '\n' + str(item.crit)
                + '\n' + str(item.prio)
                + '\n' + str(item.flavor))
