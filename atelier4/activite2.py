class Etudiant:
    etudiants = []

    def __init__(self, matricule, nom, prenom, note):
        self.matricule = matricule
        self.nom = nom
        self.prenom = prenom
        self.note = note
        Etudiant.etudiants.append(self)

    def afficher(self):
        print("Matricule : ", self.matricule)
        print("Nom : ", self.nom)
        print("Prénom : ", self.prenom)
        print("Note : ", self.note)


etud1 = Etudiant("E001", "Hiba", "El Amrani", 15)
etud2 = Etudiant("E002", "Ali", "Benjelloun", 12)
somme = 0
for etud in Etudiant.etudiants:
    somme += etud.note
print("Somme des notes : ", somme)
moyenne = somme / len(Etudiant.etudiants)
print("Moyenne des notes : ", moyenne)
