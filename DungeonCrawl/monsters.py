class Monster:
    IS_HOSTILE = True

    def __init__ (self, name: str, hp: int, damage: int, loot_table: str):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.loot_table = loot_table

    def __gt__(self, other_monster):
        if not isinstance(other_monster, Monster):
            return NotImplemented
        return self.hp > other_monster.hp
    
    # comparing damage output
    def __gt__(self, other_monster):
        if not isinstance(other_monster, Monster):
            return NotImplemented
        return self.damage > other_monster.damage

    def __str__(self):
        # for the monster's emergence
       return f"A {self.name} has appeared!  It has {self.hp} hit points"

    def attack(self):
        # """Returns a string describing the monster's attack"""
        print(f"You were attacked by {self.name} for {self.damage} points of damage!")

    def take_damage(self, amount):
        # this is for the monster to get hit and take damage
        print(f"The {self.name} was hit and has taken {amount} of damage")
        self.hp -= amount

    def is_defeated(self):
        return self.hp <= 0
    pass