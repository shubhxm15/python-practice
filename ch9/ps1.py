with open("demo.txt") as f:
    c = f.read()

if("twinkle" in c ):
    print("twinkle is present")
else:
    print("twinkle is not present")
