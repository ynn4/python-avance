machines = {
    "m1": "192.168.0.1",
    "m2": "192.168.0.2",
    "m3": "192.168.0.3",
    "m4": "192.168.0.4",
    "m5": "192.168.0.5",
}
print("L'adresse IP de la machine m2 est :", machines["m2"])
print(f"Dans le repertoire des machines, il y a {len(machines)} machines.")
machines["m6"] = "192.168.0.6"
del machines["m4"]
if "m5" in machines:
    print("La machine m5 est présente dans le repertoire.")
else:
    print("La machine m5 n'est pas présente dans le repertoire.")
print("Les machines présentes dans le repertoire sont :")
for machine in machines:
    print(machine, ":", machines[machine])
print("Entrez le nom d'une machine : ")
nom_machine = input()
if nom_machine in machines:
    print(f"L'adresse IP de {nom_machine} est : {machines[nom_machine]}")
else:
    print(f"La machine {nom_machine} n'est pas répertoriée.")
