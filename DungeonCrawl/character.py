class Character:
    max_level = 50

    def __init__ (self, name, level, health):
        self.name = name
        self.level = level
        self._health = health #protected attribute
        self._inventory = []

    @property
    def inventory(self):
        # returns the inventory list
        return self._inventory.copy()

    @property
    def health(self):
        # getter for the health attribute
        return self._health
    
    @health.setter
    def health(self, value):
        # setter for health with validation
        if value < 0:
            self._health = 0
        else:
            self._health = value

    def add_item(self, item):
        self._inventory.append(item)
        print(f"{item} was added to your inventory.")
    




