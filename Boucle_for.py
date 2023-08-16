#La boucle --> for.

#Voici deux exemple, un avec des str et l'autre avec des int:
#exemple str:
mot = ["Voiture", "Camion", "Moto", "Avion"] #Liste de mots.

for i in mot: #Pour chaques mots de la liste:
	print(i) #Ont affiche le mot.

#exemple int:
number = [0,1,2,3,4,5] #Liste de nombres.

for i in number: #Pour chaques nombres de la liste:
	print(i * 2) #Ont affiche le nombre de la liste multiplié par 2.


#Autre exemple plus complexe:
nombre = [0,1,2,3,4,5,6,7,8,9,10] #Liste de nombres.

#Pour l'exemple ci-dessous, ont créer une variable "i" qui représente chaques nombres de la liste.
for i in nombre: #Donc, pour chaques éléments dans la liste:
	calcul = i ** 2 #Pour chaques éléments de la liste, ont calcul le carré du nombre (puissance 2).
	nb_list = f"Le carré de {nombre[i]}" #Toujours pour chaques élément de la liste, ont affiche un message contenant l'élément de la variable "i" qui change de valeur à chaque nouvel élément de la liste qui sera séléctionner.
	print(nb_list, f"est de: {calcul}") #Et encore pour chaques élément, ont affiche le résultat de la variable "calcul"


#PS: Il est possible de séléctioner un seul élément de la liste, exemple:

ma_liste = [0,10,20,30,40,50]

print(ma_liste[0]) #Afficher le 1er élément de la liste.
print(ma_liste[2]) #Afficher le 3ème élément de la liste.
