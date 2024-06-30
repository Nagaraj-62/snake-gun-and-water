# lets create a game called snake gun and water 

import random

def swg(com,mine):
    if (com == mine):
        return None
# s = snake, g = gun, w = water  
    if (com == "snake"and mine=="gun"): 
        return True
    elif (com == "water"and mine=="snake"):
        return True
    elif (com == "gun"and mine=="water"):
        return True
    else :
        return False
    
choice = ("snake","water","gun")
com = random.randint(0,2)
com = choice[com]
mine = input("choose your item snake,water,or gun :")

win = swg(com,mine)
print(f"you choose {mine} and the computer choose {com}")
if win is None :
    print("match drawn")

if win:
    print("you won the game")
else :
    print("you loose")
