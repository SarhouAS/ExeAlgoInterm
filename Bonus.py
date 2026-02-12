def tri_par_insertion(tableau):
    for i in range(1, len(tableau)):
        cle = tableau[i]
        j = i - 1

        while j >= 0 and tableau[j] > cle:
            tableau[j + 1] = tableau[j]
            j -= 1

        tableau[j + 1] = cle

    return tableau

# Test
T = [5, 2, 9, 1, 5]
print(f"Avant : {T}")

resultat = tri_par_insertion(T)
print(f"Après : {resultat}")

