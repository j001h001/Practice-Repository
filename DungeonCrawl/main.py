from monsters import Monster

# Instantiating two Monster objects
goblin = Monster("Goblin", 20, 5, ["rusty dagger", "3 gold coins"])
orc = Monster("Orc", 50, 10, ["crude axe", "10 gold coins"])
merchant = Monster("Merchant", 10, 0, ["Sharp Sword, Health Potion, Health Potion, Health Potion"])
merchant.IS_HOSTILE = False

print("--- Testing __str__ ---")
# When you print an object, Python automatically calls its __str__ method.
print(orc)
print(goblin)
print("-" * 20) # A separator for clarity