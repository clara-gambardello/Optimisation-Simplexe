# Optimisation — Implémentation de l'algorithme du Simplexe

Projet d'optimisation - Résolution de problèmes de programmation linéaire, avec une implémentation "from scratch" de la méthode du Simplexe en Python, et des exemples d'application en Scilab.

## Le projet

Le problème traité est de la forme :

```
max <c, x>
Ax <= b
```

Le dépôt contient deux approches complémentaires :

* **`projet_simplexe_gambardello.py`** : implémentation manuelle complète de l'algorithme du Simplexe (construction du tableau, pivots, gestion du cas où `b` contient des coefficients négatifs)
* **`Projet_opti_Gambardello.sce`** : résolution de deux exemples de problèmes de programmation linéaire avec la fonction native `karmarkar` de Scilab, qui utilise la **méthode des points intérieurs** (une approche différente du Simplexe, mais résolvant le même type de problème)

### Version Python : implémentation du Simplexe

L'utilisateur saisit interactivement la matrice `A`, le second membre `b` et le vecteur de coûts `c`, et le programme calcule la solution optimale, en affichant le tableau à chaque étape.

* **Construction du tableau initial** : ajout des variables d'écart pour transformer les inégalités en égalités, puis assemblage du tableau standard du Simplexe
* **Étape de pivot** : recherche de la variable entrante (coefficient le plus grand sur la ligne des coûts) et de la variable sortante (règle du quotient minimal), puis élimination de Gauss autour du pivot
* **Boucle principale** : répétition des pivots jusqu'à ce que tous les coefficients de la ligne des coûts soient négatifs ou nuls (solution optimale atteinte)
* **Cas du second membre `b` négatif** : lorsque `b` contient des coefficients négatifs (pas de solution de base admissible évidente au départ), le programme résout d'abord un **problème auxiliaire** (introduction d'une variable artificielle `y`) pour trouver une solution de base admissible initiale, avant de lancer la méthode du Simplexe classique

Le programme affiche à chaque étape le tableau du Simplexe formaté (base, variables, second membre), puis en sortie : la solution optimale, la solution avec variables d'écart, et la valeur optimale de la fonction à maximiser.

### Version Scilab : résolution par points intérieurs

Le script applique la fonction `karmarkar` de Scilab sur deux problèmes d'exemple différents (l'un avec un second membre positif, l'autre avec des coefficients négatifs et des contraintes d'égalité mêlées) et affiche la solution optimale et la valeur optimale obtenues pour chacun.

## Structure du projet

* `projet_simplexe_gambardello.py` : implémentation Python (NumPy) de l'algorithme du Simplexe, écrite entièrement à la main
* `Projet_opti_Gambardello.sce` : exemples de résolution avec la fonction native `karmarkar` de Scilab

## Lancer le programme

### Version Python

1. Cloner le projet ou télécharger les fichiers
2. Installer la dépendance nécessaire

```
pip install numpy
```

3. Lancer le script et suivre les instructions saisies dans le terminal (dimensions de `A`, coefficients de `A`, `b` et `c`)

```
python projet_simplexe_gambardello.py
```

### Version Scilab

1. Ouvrir `Projet_opti_Gambardello.sce` dans [Scilab](https://www.scilab.org/)
2. Exécuter le script

## Auteur

Clara GAMBARDELLO
Projet d'Optimisation
