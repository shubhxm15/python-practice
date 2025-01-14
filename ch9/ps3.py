n = int(input("Enter a number: "))

# with open("hiscore.txt", "a") as f:

with open(f"ch9/tables_{n}.txt", "w") as f:
    for i in range(11):
        f.write(f"{n} * {i} = {n * i}\n")

 