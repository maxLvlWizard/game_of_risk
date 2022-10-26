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

# generate random numbers for rolls depending on how many attacking/defending troops
while defending_troops > 0 and attacking_troops > 0:
    attackers_roll = []
    defenders_roll = []
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

# sort attacking and random numbers so the highest numbers can be accessed with "list_name[-1]""
    attackers_roll = sorted(attackers_roll)
    defenders_roll = sorted(defenders_roll)
    
    print("=====================")
    print("Defending Troops: ", defending_troops)
    print("Attacking Troops: ", attacking_troops)
    print("Attacker's roll: ", attackers_roll)
    print("Defender's roll: ", defenders_roll)

    if len(defenders_roll) > 1 and len(attackers_roll) > 1:
        if defenders_roll[-1] >= attackers_roll[-1]:
            print(f"Defense rolled a {defenders_roll[-1]} which beats the attacking {attackers_roll[-1]}")
            attacking_troops -= 1
        else:
            print(f"Defense rolled a {defenders_roll[-1]} which loses to the attackers {attackers_roll[-1]}")
            defending_troops -= 1
        if defenders_roll[-2] >= attackers_roll[-2]:
            print(f"Defense rolled a {defenders_roll[-2]} which beats the attacking {attackers_roll[-2]}")
            attacking_troops -= 1
        else:
            print(f"Defense rolled a {defenders_roll[-2]} which loses to the attackers {attackers_roll[-2]}")
            defending_troops -= 1

    else:
        if defenders_roll[-1] >= attackers_roll[-1]:
            print(f"Defense rolled a {defenders_roll[-1]} which beats the attacking {attackers_roll[-1]}")
            attacking_troops -= 1
        else:
            print(f"Defense rolled a {defenders_roll[-1]} which loses to the attackers {attackers_roll[-1]}")
            defending_troops -= 1
        

    print("=====================")

print("Defending Troops: ", defending_troops)
print("Attacking Troops: ", attacking_troops)


