import random

print("You are playing the game right now")

score = random.randint(1, 100)     # generates any random number between 1 to 99

with open("hiscore.txt") as f:
    hiscore = f.read()
    if(hiscore != ""):
        hiscore = int(hiscore)
    else:
        hiscore = 0

print(f"Your current score is: {score}")
if(score>hiscore):
    with open("hiscore.txt", "w") as f:
        f.write(str(score))
    