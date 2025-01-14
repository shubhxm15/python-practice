
with open("demo.txt") as f:
    demo = f.readlines()

line = 1

for lines in demo:
    if("python" in lines):
        print(f"yes python is in line {line}")
        break
    line+=1

else:
    print("no python doesnt not exist in the file")