from datetime import datetime


class Employe:
    def __init__(self):
        self._identifiant = input("Entrez l'identifiant de l'employé : ")
        self._nom = input("Entrez le nom de l'employé : ")
        self._prenom = input("Entrez le prénom de l'employé : ")
        self._dateNaissance = input("Entrez la date de naissance (ex: JJ/MM/AAAA) : ")
        self._dateEmbauche = input("Entrez la date d'embauche (ex: JJ/MM/AAAA) : ")
        while True:
            try:
                self._salaire = float(input("Entrez le salaire de l'employé : "))
                break
            except ValueError:
                print("Erreur : Veuillez entrer un nombre valide pour le salaire.")

    # Définir à l’aide des propriétés les méthodes d’accès aux différents attributs de la classe.
    @property
    def identifiant(self):
        return self._identifiant

    @identifiant.setter
    def identifiant(self, value):
        self._identifiant = value

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, value):
        self._nom = value

    @property
    def prenom(self):
        return self._prenom

    @prenom.setter
    def prenom(self, value):
        self._prenom = value

    @property
    def dateNaissance(self):
        return self._dateNaissance

    @dateNaissance.setter
    def dateNaissance(self, value):
        self._dateNaissance = value

    @property
    def dateEmbauche(self):
        return self._dateEmbauche

    @dateEmbauche.setter
    def dateEmbauche(self, value):
        self._dateEmbauche = value

    @property
    def salaire(self):
        return self._salaire

    @salaire.setter
    def salaire(self, value):
        if value < 0:
            print("Erreur : Le salaire ne peut pas être négatif !")
        else:
            self._salaire = value

    # La méthode Age()
    def Age(self):
        naissance = datetime.strptime(self._dateNaissance, "%d/%m/%Y")
        aujourdhui = datetime.today()
        age = aujourdhui.year - naissance.year
        if (aujourdhui.month, aujourdhui.day) < (naissance.month, naissance.day):
            age -= 1
        return age

    def Anciennete(self):
        embauche = datetime.strptime(self._dateEmbauche, "%d/%m/%Y")
        aujourdui = datetime.today()
        anciennete = aujourdui.year - embauche.year
        if (aujourdui.month, aujourdui.day) < (embauche.month, embauche.day):
            anciennete -= 1
        return anciennete


if __name__ == "__main__":
    emp = Employe()

    print(f"Employé : {emp.prenom} {emp.nom}")
    print(f"Salaire: {emp.salaire}")
    print(f"Âge : {emp.Age()} ans")
    print(f"Ancienneté : {emp.Anciennete()} ans")
