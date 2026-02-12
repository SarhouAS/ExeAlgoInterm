nombre = int(input("Entrez un nombre entier positif : "))

somme = 0
temp = nombre

while temp > 0:
    somme += temp % 10
    temp //= 10

print(f"La somme des chiffres de {nombre} est : {somme}")