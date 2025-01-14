'''
stone = 0
paper = 1
scissor = -1
'''
import random

computer = random.choice([0, 1, -1])       # random function selects any random number from these 3

your = input("Enter your choice: ")

d1 = {
    "stone" : 0,
    "paper" : 1,
    "scissor" : -1
}

d = {
    0 : "stone",
    1 : "paper",
    -1 : "scissor"
}

you = d1[your.lower()]                # the key entered by user will be stored by its value as in d1

print(f"You choose '{d[you]}' and Computer choose '{d[computer]}'")

if(computer == you):
    print("Its a draw!!")

else:
    if(computer == 0 and you == 1):
        print("You win!!")
    elif(computer == 0 and you == -1):
        print("You lose!!") 
    elif(computer == 1 and you == 0):
        print("You lose!!")
    elif(computer == 1 and you == -1):
        print("You win!!")
    elif(computer == -1 and you == 0):
        print("You win!!")
    elif(computer == -1 and you == 1):
        print("You lose!!")