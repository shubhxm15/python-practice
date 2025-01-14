import random

n = random.randint(1, 100)
a = -1
guess = 0

while(a != n):
    a = int(input("Guess the number: "))
    guess += 1

    if(a > n):
        print("Lower number please")

    else:
        print("Higher number please")


print(f"You guessed the number in {guess} attempts")