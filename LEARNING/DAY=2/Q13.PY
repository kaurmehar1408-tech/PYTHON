# Q13. Create a grade calculator: Take marks as input and print grade: 
# ● A: 90-100 
# ● B: 75-89 
# ● C: 60-74 
# ● D: 40-59 
# ● F: Below 40 

marks = int(input("Enter your marks: "))
if 90 <= marks <= 100:
    print("Grade: A")
elif 75 <= marks < 90:
    print("Grade: B")
elif 60 <= marks < 75:
    print("Grade: C")
elif 40 <= marks < 60:
    print("Grade: D")
else:
    print("Grade: F")
    