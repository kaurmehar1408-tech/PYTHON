# Q19. Write a program to check the type of triangle based on sides: 
# ● Equilateral: All sides equal 
# ● Isosceles: Two sides equal 
# ● Scalene: No sides equal

side1 = float(input("Enter length of first side: "))
side2 = float(input("Enter length of second side: "))
side3 = float(input("Enter length of third side: "))
if side1 == side2 == side3:
    print("The triangle is Equilateral.")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("The triangle is Isosceles.")
else:
    print("The triangle is Scalene.")
    