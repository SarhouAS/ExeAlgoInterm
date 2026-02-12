def remplacer_par_zero(chaine, n):
    nouvelle_chaine = ""

    for i in range(len(chaine)):
        if (i + 1) % n == 0:
            nouvelle_chaine += "0"
        else:
            nouvelle_chaine += chaine[i]

    return nouvelle_chaine


# Test
chaine = input("Entrez une chaîne : ")
n = int(input("Entrez n : "))

resultat = remplacer_par_zero(chaine, n)
print(f"Résultat : {resultat}")