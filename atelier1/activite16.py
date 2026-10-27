start = 5
for i in range(6):
    for j in range(6, i, -1):
        print(start, end=" ")
        start -= 1
    print()
    start = 5 - i
