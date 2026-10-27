import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("qualite_industrielle_nettoyee.csv")

comptages, bords = np.histogram(df["Taux_Defauts_pct"], bins=10)
print(comptages)
print(bords)

moyennes = df.groupby("Ligne_Production")["Taux_Defauts_pct"].mean()
print(moyennes)

plt.hist(df["Taux_Defauts_pct"], bins=10)
plt.title("Distribution du taux de défauts")
plt.xlabel("Taux de défauts (%)")
plt.ylabel("Nombre de contrôles")
plt.show()

plt.bar(moyennes.index, moyennes)
plt.title("Taux de défauts moyen par ligne de production")
plt.xlabel("Ligne de production")
plt.ylabel("Taux de défauts moyen (%)")
plt.show()

plt.scatter(df["Nb_Defauts"], df["Cout_Non_Qualite_DH"], alpha=0.6)
plt.title("Coût de non-qualité selon le nombre de défauts")
plt.xlabel("Nombre de défauts")
plt.ylabel("Coût de non-qualité (DH)")
plt.show()