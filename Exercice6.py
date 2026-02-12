while True:
    n = int(input("Entrez le nombre de lignes n : "))
    if n > 0:
        break
    print("Veuillez entrer un nombre positif.")

while True:
    m = int(input("Entrez le nombre de colonnes m : "))
    if m > 0:
        break
    print("Veuillez entrer un nombre positif.")

T = []
for i in range(n):
    ligne = []
    for j in range(m):
        ligne.append(0)
    T.append(ligne)

# Affichage du tableau
for i in range(n):
    for j in range(m):
        print(T[i][j], end=" ")
    print()