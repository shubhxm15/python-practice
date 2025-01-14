a = {
    "japjot": 20,
    "tapu": 30,       
    "masooda": 15,
    0: "aayush"       
}

print(a.items())
print(a.keys())
print(a.values())

a.update({"japjot": 18})
print(a)


# these both are not same
print(a.get("japjot"))          # if wrong returns none
print(a["japjot"])              # if wrong returns error

print(a.clear())                # clear the whole dict