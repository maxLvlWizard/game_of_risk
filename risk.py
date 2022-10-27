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
total_attacking_troops_lost = 0 
total_defending_troops_lost = 0 
# generate random numbers for rolls depending on how many attacking/defending troops
while defending_troops > 0 and attacking_troops > 1:
    attackers_roll = []
    defenders_roll = []
    if attacking_troops >= 4:
        attack_int1 = random.randint(1,6)
        attack_int2 = random.randint(1,6)
        attack_int3 = random.randint(1,6)
        attackers_roll.append(attack_int1)
        attackers_roll.append(attack_int2)
        attackers_roll.append(attack_int3)
    elif attacking_troops == 3:
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
    # keep track of number of troops lost per round so it can be printed.
    attacking_troops_lost = 0
    defending_troops_lost = 0

    # if attackers and defenders could each roll at least two dice, compare the first and second highest numbers respectively.
    if len(defenders_roll) > 1 and len(attackers_roll) > 1:
        if defenders_roll[-1] >= attackers_roll[-1]:
            attacking_troops -= 1
            attacking_troops_lost += 1
            total_attacking_troops_lost += 1
        else:
            defending_troops -= 1
            defending_troops_lost += 1
            total_defending_troops_lost += 1

        if defenders_roll[-2] >= attackers_roll[-2]:
            attacking_troops -= 1
            attacking_troops_lost +=1
            total_attacking_troops_lost += 1
        else:
            defending_troops -= 1
            defending_troops_lost += 1
            total_defending_troops_lost += 1

    # if the attacking or defending team only rolls one die, this will compare it to the highest value for the other player. 
    else:
        if defenders_roll[-1] >= attackers_roll[-1]:
            attacking_troops -= 1
            attacking_troops_lost +=1
            total_attacking_troops_lost += 1
        else:
            defending_troops -= 1
            defending_troops_lost += 1
            total_defending_troops_lost += 1

    # print the number of troops lost per round aswell as the total number of troops lost.    
    print(f"Attacking troops lost: {attacking_troops_lost}      {total_attacking_troops_lost} : Total ataccking troops lost")
    print(f"Defending troops lost: {defending_troops_lost}      {total_defending_troops_lost} : Total defending troops lost")

# print the number of remaining troops aswell as the total number of troops lost
print(f"{defending_troops} remaining defending troops after losing {total_defending_troops_lost} in battle.")
print(f"{attacking_troops} remaining attacking troops after losing {total_attacking_troops_lost} in battle.")

print("1000")
