try:                                    # runs smoothly if no error occur but if occurs it throws that in except
    a = int(input("Enter a number: "))
    print(float(a))

except Exception as e:
    print(e)                            # avoid the code to get crash

print("The end")