class Personne:
    def __init__(self, nom, adresse):
        self.nom = nom
        self.adresse = adresse

    def afficher(self):
        print("Nom : ", self.nom)
        print("Adresse : ", self.adresse)


class Employe(Personne):
    def __init__(self, nom, adresse, cnss):
        self.cnss = cnss
        Personne.__init__(self, nom, adresse)

    def afficher(self):
        Personne.afficher(self)
        print("CNSS : ", self.cnss)


class Enseignant(Personne):
    def __init__(self, nom, adresse, cnops):
        self.cnops = cnops
        Personne.__init__(self, nom, adresse)

    def afficher(self):
        Personne.afficher(self)
        print("CNOPS : ", self.cnops)


class Etudiant(Personne):
    def __init__(self, nom, adresse, cne):
        self.cne = cne
        Personne.__init__(self, nom, adresse)

    def afficher(self):
        Personne.afficher(self)
        print("CNE : ", self.cne)


pers = Personne("Hiba", "Tanger")
emp = Employe("Ali", "Rabat", "123456")
ens = Enseignant("Ahmed", "Casablanca", "654321")
etud = Etudiant("Sara", "Marrakech", "987654")
print("Informations de la personne :")
pers.afficher()
print()
print("Informations de l'employé :")
emp.afficher()
print()
print("Informations de l'enseignant :")
ens.afficher()
print()
print("Informations de l'étudiant :")
etud.afficher()
