n = int(input("Entrez la taille du tableau : "))
T = []

for i in range(n):
    val = int(input(f"Entrez T[{i}] : "))
    T.append(val)

X = int(input("Entrez le nombre X à chercher : "))

compteur = 0
for element in T:
    if element == X:
        compteur += 1

print(f"{X} apparaît {compteur} fois dans le tableau.")