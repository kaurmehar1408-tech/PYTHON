# while loops
i = 0
while i < 5:
    print("hello")
    i = i + 1

# for loops
l = [1,7,8]
for item in l:
    print(item)


# for loops using range() function
for i in range(0,7):
    print(i)

# break statement
for i in range (0,80):
    print(i)

    if i==3:
        break

# continue statement
for i in range(4):
    print("printing")

    if i==2:
        continue

    print(i)

# pass statement
for i in range(4):
    if(i==2):
        pass

    print(i)