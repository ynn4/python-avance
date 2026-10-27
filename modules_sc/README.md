# Analyse de la qualité industrielle (TP3)

Ce projet présente trois diagrammes réalisés à partir du fichier `qualite_industrielle_nettoyee.csv`. Chaque ligne du fichier correspond à un contrôle qualité effectué sur une ligne de production (50 contrôles au total), avec des informations comme le produit, la ligne de production, le nombre de défauts, le taux de défauts et le coût de non-qualité.

## 1. Histogramme du taux de défauts

**Ce qu'il montre :** la répartition des taux de défauts sur l'ensemble des 50 contrôles.

**Question posée :** le taux de défauts est-il généralement faible ou élevé, et y a-t-il des cas extrêmes ?

**Comment le lire :** l'axe horizontal représente des intervalles de taux de défauts, et la hauteur de chaque barre indique combien de contrôles tombent dans cet intervalle. La plupart des contrôles ont un taux bas (médiane d'environ 5,5 %), mais quelques-uns atteignent des valeurs très élevées (jusqu'à environ 34 %).

**Limite :** ce diagramme donne une vue d'ensemble, mais ne compare aucun groupe.

## 2. Diagramme en barres du taux de défauts moyen par ligne de production

**Ce qu'il montre :** le taux de défauts moyen de chacune des cinq lignes de production.

**Question posée :** quelle ligne produit le plus de défauts en moyenne ?

**Comment le lire :** chaque barre représente une ligne de production, et sa hauteur est le taux de défauts moyen de cette ligne. La barre la plus haute désigne la ligne la plus problématique. Le même principe permet de comparer les produits au lieu des lignes.

## 3. Nuage de points : coût de non-qualité selon le nombre de défauts

**Ce qu'il montre :** la relation entre le nombre de défauts et le coût de non-qualité, chaque contrôle étant représenté par un point.

**Question posée :** quand le nombre de défauts augmente, le coût augmente-t-il aussi ?

**Comment le lire :**
- des points qui montent de gauche à droite indiquent que plus de défauts entraîne plus de coût ;
- des points dispersés sans direction indiquent l'absence de lien visible ;
- un point très éloigné des autres signale un cas à examiner.

## Pour aller plus loin

- Ajouter une droite de tendance sur le nuage de points pour mesurer le lien plus précisément.
- Étudier d'autres relations, par exemple entre la température et le taux de défauts.
- Réaliser un graphique de contrôle sur la dimension ou le poids des pièces.
