L3 = [1, 2, 3, 4, 5]
somme = 0
max = L3[0]
min = L3[0]
compteur = 0
print("Les éléments de la liste sont :")
for i in range(len(L3)):
    somme += L3[i]
    print(L3[i])
    if L3[i] > max:
        max = L3[i]
    if L3[i] < min:
        min = L3[i]
    if L3[i] % 3 == 0:
        compteur += 1
print("La somme des éléments de la liste est :", somme)
print("Le maximum des éléments de la liste est :", max)
print("Le minimum des éléments de la liste est :", min)
print("Le nombre de multiples de 3 est :", compteur)
produit = 1
for i in range(2, 5):
    produit *= L3[i]
print("Le produit des éléments de L3[2] à L3[4] est :", produit)
for i in range(len(L3) - 1, -1, -1):
    print(L3[i], end=" ")
