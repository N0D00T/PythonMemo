#Les instructions de contrôle de flux.
#Instruction --> if.

username = "Gotaga"

if True:
	print("Bienvenue", username)
print("Fin!")
#Ont peut voir ci-dessus que "if" contient une condition qui est correcte, alors, le code indenté sera exécuter.
#Pour l'exemple ci-dessus "if" est correct grace au booléen "True".


#Autres exemples d'utilisation de l'instruction "if":
username = "Nemo"

if username == "Nemo": #Si "verif" est égale à "password" alors...
	print("Bienvenue", username)
print("Fin!")


#Pour l'exemple ci-dessous, ont demande si username se trouve dans la liste users.
username = "Jean"
users = ["Stephane", "Alex", "Jackie", "Romaric", "Jean"]#Le type de la donnée se trouvant dans la variable "users" est une liste.

print(username in users) #True car "Jean" se trouve dans la liste.
if username in users:
	print(username, "se trouve bien dans la liste !")
print("Fin!")


#Dernier exemple:
#Pour cet exemple, si le prix est plus grand que 10 alors...
prix = 12.5

if prix > 10:
	print("Le prix est élevé")
print("Fin!")


