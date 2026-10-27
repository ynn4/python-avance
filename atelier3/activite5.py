def F1(n=1):
    for i in range(n):
        print("Bonjour")


def F2(n):
    if n % 10 == 0:
        print(f"{n} est divisible par 10.")
    else:
        print(f"{n} n'est pas divisible par 10.")


def F3(text):
    compteur = 0
    for l in text:
        if l in "aieouy":
            compteur += 1
    return f"Le texte contient {compteur} voyelles."


def F4(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * F4(n - 1)


def F5(n):
    print(f"Table de multiplication de {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")


def F6(mot):
    compteur = 0
    for l in mot:
        compteur += 1
    return f"Le mot {mot} contient {compteur} caractères."


def F7(n):
    if n == 0 or n == 1:
        return 1
    else:
        return F7(n - 1) + F7(n - 2)


F1()
F2(20)
text = "Ceci est un texte avec des voyelles."
print(text, F3(text))
nbr = 3
print(f"{nbr}! = {F4(nbr)}")
F5(5)
print(F6("Python"))
print(f"Le nombre de Fibonacci pour 5 est {F7(5)}")
