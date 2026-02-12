n = int(input("Entrez la taille du tableau : "))
T = []

for i in range(n):
    val = int(input(f"Entrez T[{i}] : "))
    T.append(val)

if T[0] > T[1]:
    max1, max2 = T[0], T[1]
else:
    max1, max2 = T[1], T[0]

for i in range(2, n):
    if T[i] > max1:
        max2 = max1
        max1 = T[i]
    elif T[i] > max2:
        max2 = T[i]

print(f"Le deuxième plus grand nombre est : {max2}")