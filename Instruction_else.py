#Les instructions de contrôle de flux.
#Instruction --> else.

'''
if condition: #Si la condition est correcte alors...
	commande_1
else: #Sinon...
	commande_2
#L'instruction "else" sera forcément le contraire de "if", donc pas besoin d'y ajouter de condition.
'''

#Exemple:
username = input("Veuillez indiquer votre pseudo: ")
users = ["Fraku45", "Nemo896", "izi72h", "takeashot93", "fugudead69"]

if username in users:
	print("Bienvenue", username, "!")
	print("Voici les news...")
else:
	print("L'utilisateur:", username, ", n'est pas dans la liste !")

#Autre exemple:
prix = input("Veuillez indiquer le prix: ")
prix = float(prix)

if prix > 10:
	print("Le prix est élevé !")
else:
	print("Le prix est raisonnable !")
