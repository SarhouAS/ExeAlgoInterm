def moyenne_tableau_2d(tableau):
    somme = 0
    compteur = 0

    for ligne in tableau:
        for element in ligne:
            somme += element
            compteur += 1

    return somme / compteur

tableau = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

resultat = moyenne_tableau_2d(tableau)
print(f"La moyenne est : {resultat}")
