rows = 5
i = rows
while i >= 1:
    spaces = rows - i
    s = 1
    while s <= spaces:
        print(" ", end="")
        s += 1
    j = 1
    while j <= i:
        print("* ", end="")
        j += 1
    print()
    i -= 1
i = 1
while i <= rows:
    spaces = rows - i
    s = 1
    while s <= spaces:
        print(" ", end="")
        s += 1
    j = 1
    while j <= i:
        print("* ", end="")
        j += 1
    print()
    i += 1
