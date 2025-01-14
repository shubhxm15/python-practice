l = [10, 30, 50, 70, 90]

# index = 0
# for item in l:
#     index += 1
#     print(f"The value of item in index {index} is {item}")

# the same can be done by using enumerate function

for index, item in enumerate(l):
    print(f"The value of item in index {index} is {item}")