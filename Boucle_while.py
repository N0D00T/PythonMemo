#La boucle while.
#La boucle "for" va utiliser des séquences comme des listes ou même des dictionnaires pour itéré à travers les éléments de ses séquence là, alors que la boucle "while" va plutôt utiliser des conditions, pour faire simple la boucle "while" sera éxécuter tant que la conditions est valable.

#Exemple avec les booléens:
#False:
'''
while False: #Dans ce cas le booléeen "False" est utiliser.
	print("Pas dans la boucle !")
print("Fin!")
'''
#Dans le cas ci-dessus, ont peut voir que nôtre "print" n'est pas éxécuter car la boucle "while" est réglé sur "False".

#True:
'''
while True: #Dans ce cas le booléeen "False" est utiliser.
	print("Dans la boucle infini...")
'''
#Dans le cas ci-dessus, ont peut voir que "print" s'éxécute à l'infini car la boule est tout le temps "True".

#Exemple avec une variable et une opération:
i = 0 #Variable "i" qui est égale à 0.

while i < 100000: #Tant que la valeur de la variable "i" est plus petite que 10 alors..
	i = i + 1 #Ont récupère la variable pour lui ajouter + 1 à chaque répétition.
	print("Result:", i)
	
	if i == 100000: #Si "i" est égale à 100000 alors...
		print("La boucle est terminer !")
#Une fois que la valeur de la variable "i" est arrivé à 100000 la boucle se termine.
