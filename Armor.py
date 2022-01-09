from enum import Enum


class Item:
    def __init__(self, slot, health, mana, healthr, manar, ad, ap, armor, mr, flavor):
        self.slot = slot
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
    def __init__(self, health, mana, healthr, manar, ad, ap, armor, mr, flavor, stat_scale, pct_scale, effects):
        super().__init__(Slot.WEAPON, health, mana, healthr, manar, ad, ap, armor, mr, flavor)
        self.stat_scale = stat_scale
        self.pct_scale = pct_scale
        self.effects = effects  # things like armor shred, life steal, etc

    # calculates damage done by the weapon
    def calculate_outputdmg(self, p):
        outputdmg = 0
        player_dmg_base_value = p.get_statnum_fromstr(self.stat_scale)
        return player_dmg_base_value * self.pct_scale


class Slot(Enum):
    WEAPON = 0
    HEAD = 1
    CHEST = 2
    LEGS = 3
    BOOTS = 4

# returns a weapon object from txt file
def get_item_from_txt(txt_path):
    lines = []
    with open((txt_path)) as f:
        for line in f:
            lines.append(line.strip())
    f.close()
    i = 0  # line number counter
    slot = lines[i]
    health = lines[i + 1]
    mana = lines[i + 1]
    healthr = lines[i + 1]
    manar = lines[i + 1]
    ad = lines[i + 1]
    ap = lines[i + 1]
    armor = lines[i + 1]
    mr = lines[i + 1]
    flavor = lines[i + 1]

