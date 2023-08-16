#Exercise, nombre pair ou impair:

nombre = int(input("Entrez un nombre: "))

check = (nombre % 2) #Pour rappel, l'opération modulo "%" calcul le reste d'une division.

if check == 0: #Si le reste est égale à 0 alors...
#Autre façon de faire --> if (nombre % 2) == 0:
	print(f"Le nombre {nombre} est pair !")
else: #Sinon...
	print(f"Le nombre {nombre} est impair !")
