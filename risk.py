import random
import sys

# Ask for number of attacking/defending troops. 

try:
    defending_troops = int(input("Defending troops: "))
    attacking_troops = int(input("Attacking troops: "))
except ValueError:
    print("Error: Invalid Input.")
    sys.exit(1)

attackers_roll = []
defenders_roll = []

while defending_troops > 0 and attacking_troops > 0:
    if attacking_troops >= 3:
        attack_int1 = random.randint(1,6)
        attack_int2 = random.randint(1,6)
        attack_int3 = random.randint(1,6)
        attackers_roll.append(attack_int1)
        attackers_roll.append(attack_int2)
        attackers_roll.append(attack_int3)
    elif attacking_troops == 2:
        attack_int1 = random.randint(1,6)
        attack_int2 = random.randint(1,6)
        attackers_roll.append(attack_int1)
        attackers_roll.append(attack_int2)
    else: 
        attack_int1 = random.randint(1,6)
        attackers_roll.append(attack_int1)

    if defending_troops >= 2:
        defense_int1 = random.randint(1,6)
        defense_int2 = random.randint(1,6)
        defenders_roll.append(defense_int1)
        defenders_roll.append(defense_int2)
    else:
        defense_int1 = random.randint(1,6)
        defenders_roll.append(defense_int1)

    print("Attacker's roll: ", attackers_roll)
    print("Defender's roll: ", defenders_roll)

    defending_troops -= 100


