class Voiture:
    def __init__(self, code, marque, puissance, kilometrage):
        self.code = code
        self.marque = marque
        self.puissance = puissance
        self.kilometrage = kilometrage

    def mod_kilo(self, kilometrage):
        self.kilometrage = kilometrage

    def mod_puissance(self, puissance):
        self.puissance = puissance

    def afficher(self):
        print(
            f"Code: {self.code}, Marque: {self.marque}, Puissance: {self.puissance}, Kilométrage: {self.kilometrage}"
        )


peugeot = Voiture(200, "Peugeot 208", 100, 45000)
volkswagen = Voiture(201, "Volkswagen Golf 7", 150, 82000)
bmw = Voiture(202, "BMW Série 3", 190, 115000)
peugeot.afficher()
volkswagen.afficher()
bmw.afficher()
peugeot.mod_kilo(1000)
bmw.mod_puissance(240)
peugeot.afficher()
bmw.afficher()
