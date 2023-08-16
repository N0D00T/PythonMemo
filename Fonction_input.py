#Récupérer les entrées utilisateur avec "input".

prenom = input("Quel est votre prénom ?: ")
nom = input("Quel est votre nom ?: ")
age = input("Quel est votre age ?: ")
#La fonction input nous sert à demander à l'utilisateur de nous donnés des informations que l'ont pourra utiliser par la suite en récupérant l'info grâce à une variable.

print(f"Bonjour {prenom} {nom}, tu as {age} ans !\n")

#La fonction "input" utilisera toujours le type de donnée "str" par défaut.

print(prenom, type(prenom))
print(nom, type(nom))
print(age, type(age))

age = int(age) #Conversion de la variable "age" qui est de type "str" vers le type "int".

print("\n", age, type(age)) #Résultat de la conversion.
