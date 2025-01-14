try:                                   
    a = int(input("Enter a number: "))
    print(float(a))

except Exception as e:
    print(e)

else:                 # runs only if try doesnt throw any error
    print("The end")