import random
import sys

try:
    defending_troops = int(input("Defending troops: "))
    attacking_troops = int(input("Attacking troops: "))
except ValueError:
    print("Error: Invalid Input.")
    sys.exit(1)



if attacking_troops >= 3:
    attack_int1 = random.randint(1,6)
    attack_int2 = random.randint(1,6)
    attack_int3 = random.randint(1,6)
elif attacking_troops == 2:
    attack_int1 = random.randint(1,6)
    attack_int2 = random.randint(1,6)
else: 
    attack_int1 = random.randint(1,6)

if defending_troops >= 2:
    defense_int1 = random.randint(1,6)
    defense_int2 = random.randint(1,6)
else:
    defense_int1 = random.randint(1,6)


print("Attacking Dice: ", attack_int1, attack_int2, attack_int3)


print("Defending Dice: ", defense_int1, defense_int2)