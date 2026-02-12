nombre = int(input("Entrez un nombre entier positif : "))

print(f"Nombre initial : {nombre}")

while nombre >= 10:
    somme = 0
    temp = nombre
    while temp > 0:
        somme += temp % 10
        temp //= 10
    print(f"Somme des chiffres : {somme}")
    nombre = somme

print(f"Résultat final : {nombre}")