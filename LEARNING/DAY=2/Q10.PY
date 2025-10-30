# Q10. Take age as input and print "Child" if age < 13, "Teenager" if age 13-19, otherwise "Adult". 

age = int(input("Enter your age: "))
if age < 13:
    print("Child")
elif 13 <= age <= 19:
    print("Teenager")
else:
    print("Adult")
    