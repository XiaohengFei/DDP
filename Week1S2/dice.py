import random

def roll_dice ():
    
    return random.randint(1, 6)
    #return random.randrange(1,7)

dice_result = roll_dice()
print("The result of rolling dice:", dice_result)


