def remplacer_cellule(tableau, ancienne_valeur, nouvelle_valeur):
    for i in range(len(tableau)):
        for j in range(2):
            if tableau[i][j] == ancienne_valeur:
                tableau[i][j] = nouvelle_valeur

    return tableau

tableau = [
    ["Alice", 15],
    ["Bob", 12],
    ["Clara", 15]
]

print("Avant :", tableau)

resultat = remplacer_cellule(tableau, 15, 20)

print("Après :", resultat)
