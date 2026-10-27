L1 = [1, 2, 3, 4, 5]
print(L1[4])
L1[1] = 17
L1[3] = L1[2] + L1[4]
print(L1[4])
print("Affichage horizontale: ", end="")
print(L1)
print("Affichage verticale: ")
for i in range(len(L1)):
    print(L1[i])
print("Affichage verticale inversée: ")
for i in range(len(L1) - 1, -1, -1):
    print(L1[i])
