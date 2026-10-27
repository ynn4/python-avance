start = 1
for i in range(1, 5):
    for j in range(i):
        print(start - j, end=" ")
    print()
    start += i + 1
