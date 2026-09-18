#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
created on Sun Mar 16 13:19:24 2025

@author: Clara Gambardello
"""

import numpy as np


def crea_mat_vect():
    """
    Fonction permettant de saisir la taille de la matrice A
    ses coefficients et les vecteurs b et c dans l'optique de 
    résoudre un systeme de type:

    max<c, x>
    Ax<=b

    Returns
    -------
    mat_a : numpy.ndarray
        Matrice du système d'inéquations
    vect_b : numpy.ndarray : 
        Second membre du système
    vect_c : numpy.ndarray :
        Coefficients de la fonction a maximiser
    m_lin : int
        Nombre de lignes de A
    n_col : int
        Nombre de colonnes de A
    """
    m_n=input("Renseignez la taille de la matrice m x n avec un"
             "espace entre m et n :")
    m_n=list(m_n.split(' '))
    m_n=[int(i) for i in m_n]
    m_lin=m_n[0]
    n_col=m_n[1]

    mat_a=input("Renseignez les coefficients de la matrice A ligne"
            "par ligne avec un espace entre chaque coefficient :")
    mat_a=list(mat_a.split(' '))
    mat_a=[float(i) for i in mat_a]
    mat_a=np.reshape(mat_a, (m_lin, n_col))

    vect_b=input(
        f"Renseignez les coefficients du vecteur B de taille {m_lin}"
        " avec un espace entre chaque coefficient :")
    vect_b=list(vect_b.split(' '))
    vect_b=[float(i) for i in vect_b]

    vect_c=input(
        f"Renseignez les coefficients du vecteur C de taille {n_col}"
        " avec un espace entre chaque coefficient :")
    vect_c=list(vect_c.split(' '))
    vect_c=[float(i) for i in vect_c]

    return mat_a, vect_b, vect_c, m_lin, n_col



def affiche_tab(base, tab, m, n):
    """
    Affiche correctement le tableau avec noms de lignes et de colonnes.

    Paramètres :
    ------------
    base : list
        contient les indices des x dans la base.
    tab : numpy.ndarray
        tableau de résolution du probleme de programmation lineaire
        à l'étape actuelle.
    m : int
        nombre de lignes de la matrice A
    n : int
        nombre de colonnes de la matrice A

    """

    if len(np.transpose(tab))==n+m+1 :
        col_1=[]
        for ind in base :
            col_1.append(f"x{ind+1}")
        col_1.append(" ")

        print(f"{'Base':^12}", end="\t")
        for j in range(n+m) :
            print(f"{'x'+str(j+1):^12}", end="\t")
        print("b".center(12))

        for i, ligne in enumerate(tab) :
            print(f"{col_1[i]:^12}", end="\t")
            for j in ligne :
                print(f"{j:^12.2f}", end="\t")
            print()
        print()

    else :
        col_1=[]
        for ind in base :
            if ind=="y":
                col_1.append("y")
            else:
                col_1.append(f"x{ind+1}")
        col_1.append(" ")

        print(f"{'Base':^12}", end="\t")
        for j in range(n+m) :
            print(f"{'x'+str(j+1):^12}", end="\t")
        print("y".center(12), end="\t")
        print("b".center(12))

        for i, ligne in enumerate(tab) :
            print(f"{col_1[i]:^12}", end="\t")
            for j in ligne :
                print(f"{j:^12.2f}", end="\t")
            print()
        print()



def tableau_init(mat_a, vect_b, vect_c, m, n):
    """
    Création du tabelau initial utile a la résolution du problème
    de programmation linéaire.

    max<c, x>
    Ax<=b

    Parameters
        mat_a : numpy.ndarray
            Matrice du système d'inéquations
        vect_b : numpy.ndarray : 
            Second membre du système
        vect_c : numpy.ndarray :
            Coefficients de la fonction a maximiser
        m : int
            Nombre de lignes de A
        n : int
            Nombre de colonnes de A

    Returns
    -------
    tableau_initial : numpy.ndarray
        Permet de résoudre le problème de programmation linéaire.
    base : list
        Vecteur contenant les indices des x dans la base.

    """
    #On transforme b en matrice pour pouvoir concaténer
    vect_b=np.transpose([vect_b])

    #On ajoute les variables d'écarts au tableau
    tableau=np.concatenate((mat_a, np.eye(m)), axis=1)

    #On ajoute la colonne b a la fin du tableau
    tableau=np.concatenate((tableau, vect_b), axis=1)

    #On ajoute des 0 au vecteur c pour qu'il ai la bonne taille
    c_tab=np.concatenate((vect_c, np.zeros(m+1)))
    c_tab=[c_tab]

    #On ajoute la ligne c au tableau
    tableau_initial=np.concatenate((tableau, c_tab))

    #Vecteur de base
    base=list(range(n, m+n))

    return tableau_initial, base



def etape_pivot(tab, base, m, n):
    """
    Fonction permettant de trouver l'indice de x entrant en bases
    celui de x sortant de la base et avec le pivot obtenue en son croisement,
    d'annuler les coefficients de la colonne de ce pivot.

    Parameters
    ----------
    tab : numpy.ndarray
        tableau de résolution du probleme de programmation lineaire
        à l'étape actuel.
    base : list
        contient les indices des x dans la base.
    m : int
        nombre de variable d'écart.
    n : int
        Nombre de variable du système sans les variables d'écarts.

    Returns
    -------
    tab : numpy.ndarray
        tableau de résolution transformé après l'étape de pivot.
    base : numpy.ndarray
        contient les indices des x dans la base apres l'étape de pivot.

    """
    #On introduit tab_i_base pour ne pas considérer la derniere colonne
    tab_i_base=np.transpose(np.transpose(tab)[:-1])


    entre_en_base=np.argmax(tab_i_base[m])

    #Le résultat d'un where est un array d'array
    indice_base=entre_en_base

    #On divise la derniere colonne par la colonne de la variable qui entre en base
    sort_de_base=np.where(np.transpose(tab)[indice_base] != 0,
                        np.transpose(tab)[n+m]/np.transpose(tab)[indice_base],
                        0)

    #On cherche dans le résultat de cette division qui est le plus petit non nul
    sort=float('inf')
    for i in range (len(sort_de_base)-1):
        if (sort_de_base[i]>0) and (sort>sort_de_base[i]):
            indice_sort=i
            sort=sort_de_base[i]

    #On stock dans base les x entrant en base
    base[indice_sort]=indice_base

    #On renomme indice_base pour une meilleure compréhension
    indice_pivot=indice_base

    #On modifie maintenant la ligne du pivot, pour la diviser par ce pivot.
    tab[indice_sort]=tab[indice_sort]/tab[indice_sort][indice_base]

    #On modifie les lignes pour annuler la colonne du pivot
    for i, ligne in enumerate(tab):
        if i != indice_sort:
            coeff_pivot=-ligne[indice_pivot]
            tab[i]=ligne+(coeff_pivot*tab[indice_sort])

    return tab, base



def methode_simplexe(tab, base, m ,n):
    """
    Fonction de résolution du probleme de programmation linéaire dans le 
    cas ou tous les coefficients de b sont positifs.

    Parameters
    ----------
    tab : Array of float64
        tableau initial de résolution.
    base : list
        contient les indices des variables d'écarts.
    m : int
        nombre de lignes de la matrice A
    n : int
        nombre de colonnes de la matrice A

    Returns
    -------
    tab_i : Array of float64
        tableau final après toutes les étapes de résolution.
    sommet : Array of float64
        solutions finale avec les variables d'écarts'
    solution_finale : Array of float64
        solution du problème d'optimisation

    """
    #Tant que les coeff de la dernière lignes ne sont pas tous négatif ou nul
    #On prend une petite tolérance pour 0

    while not all(x<=1e-8 for x in tab[m][:-1]):
        tab, base=etape_pivot(tab, base, m, n)

    #On calcul le sommet selon les nombres dans base
    sommet=np.zeros(n+m)
    j=0
    for i in base:
        sommet[i]=tab[j][-1]
        j+=1

    #On tronque sommet pour avoir notre solution sans les variables d'écarts
    solution_finale=sommet[:n]

    #On trouve notre valeur finale dans le tableau
    val_finale=-tab[-1][-1]

    print("Tableau à la fin de la résolution")
    affiche_tab(base, tab, m, n)

    return tab, sommet, solution_finale, val_finale



def probleme_auxiliaire(mat_a, vect_b, vect_c, m, n):
    """
    Fonction permettant la création puis la résolution d'un problème
    auxiliaire dans le cadre d'un probleme de programmation linéaire
    avec un second membre quelconque, afin d'en déduire une solution 
    de base admissible initiale.

    Parameters
    ----------
    mat_a : numpy.ndarray
        Matrice du système d'inéquations
    vect_b : numpy.ndarray : 
        Second membre du système
    vect_c : numpy.ndarray :
        Coefficients de la fonction a maximiser
    m : int
        Nombre de lignes de A
    n : int
        Nombre de colonnes de A

    Returns
    -------
    tab : numpy.ndarray
        tableau de la solution 
        de base admissible initiale.
    base : list
        contient les indices des x dans la base après résolution du probleme 
        auxilliaire.

    """
    #On forme le tableau avec la colonne y
    der=np.zeros(len(vect_c))
    tab, base=tableau_init(mat_a, vect_b, der, m, n)
    tab=np.insert(tab, -1, -1, axis=1)

    #On cherche la ligne ou y entre en base
    indice_y=np.argmin(np.transpose(tab)[-1])

    #On ajoute y a base pour ensuite verifier quand il en sort
    base[indice_y]='y'

    print("Début du problème auxiliaire")
    affiche_tab(base, tab, m, n)

    #On cherche a obtenir 1 pour notre pivot
    tab[indice_y]=-tab[indice_y]

    #On cherche a annuler les coefficients de la colonne y
    for i, row in enumerate(tab):
        if i != indice_y:
            coeff_pivot=-row[-2]
            tab[i]=row+(coeff_pivot*tab[indice_y])

    #Tant que y est encore dans la base on utilise etape_pivot
    while "y" in base :
        tab, base=etape_pivot(tab, base, m, n)

    #On souhaite se ramener a un tableau exploitable par resolution_simplexe_1
    tab=np.delete(tab, -2, axis=1)
    tab[-1]=np.concatenate((vect_c, np.zeros(m+1)))

    #On verifie que les elements de la base soit nulle dans la dernière ligne
    for i, x_b in enumerate(base):
        if tab[-1][x_b] != 0:
            coeff_pivot=-tab[-1][x_b]
            tab[-1]=tab[-1]+(coeff_pivot*tab[i])

    #On calcule le dernier element du tableau selon la dernière colonnne et la base
    sommet_y=np.zeros(n+m)
    j=0
    for i in base:
        sommet_y[i]=tab[j][-1]
        j+=1

    tab[-1][-1]=-np.matmul(sommet_y, np.concatenate((vect_c, np.zeros(m))))

    return tab, base



if __name__=='__main__':

    matA, b_vect, c_vect, nbligne, nbcol=crea_mat_vect()

    b_qlq=[b_vect[i]<0 for i in range(len(b_vect))]

    if any(b_qlq):
        tableau_res, base_col=probleme_auxiliaire(
            matA, b_vect, c_vect, nbligne, nbcol)

        tab_final, sommet_fin, solution_fin, val_fin=methode_simplexe(
            tableau_res, base_col, nbligne, nbcol)

    else :
        tableau_res, base_col=tableau_init(
            matA, b_vect, c_vect, nbligne, nbcol)

        tab_final, sommet_fin, solution_fin, val_fin=methode_simplexe(
            tableau_res, base_col, nbligne, nbcol)

    print(f"La solution du problème d'optimisation est : {solution_fin}")
    print("La solution du problème d'optimisation avec "
          f"variable d'écart est : {sommet_fin}")
    print("La valeur de la fonction à maximiser avec la solution est : "
          f"{val_fin}")
