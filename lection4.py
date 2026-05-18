class PLayer:
    def __init__(self, name, hp, inventory=[]):
        self.name = name
        self.hp = hp
        self.inventory = inventory
    def pickup(self, **args):
        self.args = args
        return self.inventory.append(args)
    def has(self, item):
        return item in self.inventory
    def __str__(self):
        return f"<{self.name.title()}> hp: {self.hp}, items: {len(self.inventory)}"
steve = PLayer("steve", 20)
steve.pickup(["apple", "cherry"])
