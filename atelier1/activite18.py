i = 1
while i < 10:
    if i <= 5:
        stars = i
    else:
        stars = 10 - i
    j = 1
    while j <= stars:
        print("*", end="")
        j += 1
    print()
    i += 1
