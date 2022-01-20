from enum import Enum


class Item:
    def __init__(self, name, slot, health, mana, healthr, manar, ad, ap, armor, mr, flavor):
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
        self.flavor = flavor


class Weapon(Item):
    def __init__(self, name, health, mana, healthr, manar, ad, ap, armor, mr, flavor, stat_scale, pct_scale, dmg_type, effects):
        super().__init__(Slot.WEAPON, name, health, mana, healthr, manar, ad, ap, armor, mr, flavor)
        self.stat_scale = stat_scale
        self.pct_scale = pct_scale
        self.dmg_type = dmg_type
        self.effects = effects  # things like armor shred, life steal, etc

    # calculates damage done by the weapon
    def calculate_outputdmg(self, p):
        player_dmg_base_value = p.get_statnum_fromstr(self.stat_scale)
        return player_dmg_base_value * self.pct_scale


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
        return 'CHEST'
    elif s == Slot.LEGS:
        return 'LEGS'
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
    elif s == 'CHEST':
        return Slot.CHEST
    elif s == 'LEGS':
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
    flavor = lines[i + 1]

    # if weapon, add extra parameters
    if slot_str == 'WEAPON':
        stat_scale = lines[i + 1]
        pct_scale = lines[i + 1]
        effects = lines[i + 1]
        return Weapon(name, health, mana, healthr, manar, ad, ap, armor, mr, flavor, stat_scale, pct_scale, effects)
    else:  # if armor
        return Item(name, get_slot_from_str(slot_str), mana, healthr, manar, ad, ap, armor, mr, flavor)


# write item to text file
def write_item_to_txt(path, item):
    with open(path + item.name, 'w') as f:
        f.write(item.name
                + '\n' + item.slot_str
                + '\n' + item.health
                + '\n' + item.mana
                + '\n' + item.healthr
                + '\n' + item.manar
                + '\n' + item.ad
                + '\n' + item.ap
                + '\n' + item.armor
                + '\n' + item.mr
                + '\n' + item.flavor)
