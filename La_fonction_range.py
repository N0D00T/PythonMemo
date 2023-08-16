#Exploration de la fonction range().

for i in [0,1,2,3,4,5,6,7,8,9,10,11,12,"ect..."]:
	print(i)
#Dans le cas ci-dessus, ont peut vite remarquer que faire une liste de nombres peut devenir interminable, c'est donc pour cela que la fonction "range()" existe.

#Exemples de la fonction range:
for i in range(1000):
	print(i)
#Dans l'exemple ci-dessus, la fonction "range" va nous créé une succession de 1000 nombres qui iront de 0 à 999.

#Autres exemple:
for i in range(10, 100):
	print(i)
#Dans l'exemple ci-dessus, la fonction "range" va nous créé une succession de  nombres qui iront de 10 à 99.

#Pour finir, il est possible de spécifier l'incrément des nombres en ajoutant un 3ème paramètre.
for i in range(0,10,2):
	print(i)
#Ci-dessus, la boucle "for" va générer une liste de 10 nombres qui seront générer tout les 2 nombres (0,2,4,6,8).
