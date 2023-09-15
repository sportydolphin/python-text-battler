class Consumable:
    def __init__(self, name, cost_in_gold, resource, restore_amount):
        self.name = name
        self.cost_in_gold = cost_in_gold
        self.resource = resource
        self.restore_amount = restore_amount

    def __str__(self):
        return f"{self.name} - {self.cost_in_gold} gold - Restores {self.restore_amount} {self.resource}"

    def print(self):
        return f"{self.name} - Restores {self.restore_amount} {self.resource}"
