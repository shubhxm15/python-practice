m1 = int(input("Enter your marks: "))
m2 = int(input("Enter your marks: "))
m3 = int(input("Enter your marks: "))
m4 = int(input("Enter your marks: "))
m5 = int(input("Enter your marks: "))

total_percentage = (100*(m1+m2+m3+m4+m5))/500

if(total_percentage>90):
    print("Your grade is A+", total_percentage)

elif(total_percentage>=80 and total_percentage<=90):
    print("Your grade is A", total_percentage)

elif(total_percentage>70 and total_percentage<=80):
    print("Your grade is B", total_percentage)

elif(total_percentage>60 and total_percentage<=70):
    print("Your grade is C", total_percentage)

elif(total_percentage>50 and total_percentage<=60):
    print("Your grade is D", total_percentage)

else:
    print("You're fail")