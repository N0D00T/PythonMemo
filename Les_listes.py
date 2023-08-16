#Les listes.

#Exemple de différentes listes:
liste_int = [12,54,47,26,38]
liste_float = [12.5,54.4,47.9,26.2,38.7]
liste_str = ["Paris","New York","Londres","Barcelone","Berlin"]
liste_mix = [450,260.5,"Voiture"]

print(liste_int)
print(liste_float)
print(liste_str)
print(liste_mix)

#-------------------------------------------------------------------------
#Accéder aux données d'une liste (indexage & tranchâge):

loto = [2,8,15,22,38]
villes = ["Paris","New York","Londres"]
liste_mix = [17,"voiture",45.6,"con"]
print("\nListes:")
print("Liste Loto:", loto)
print("Liste Villes:", villes)
print("Liste Mix:", liste_mix)

lenght = "Liste Loto: " + str(len(loto)), "Liste Villes: " + str(len(villes)), "Liste Mix: " + str(len(liste_mix))
print("Longueur de chaques listes:", lenght) #Il peut s'avérer utile de connaitre le nombres d'éléments qu'il y a dans nos listes.

print("Premier élément de la liste loto:", loto[0]) #Nous demandons d'afficher le premier élément de la liste "loto"

#Il est possible de changer la valeur d'un élément d'une liste, exemple:
villes[1] = "Madrid" #Ré-attribution de valeur du deuxième élément de la liste.
print("Nouvelles valeurs de la liste --> Villes:", villes)

#Il est possible d'utiliser l'indexage negatif pour récupérer un élément de la liste, exemple:
exemple_neg = [45,25,79,89,57,62,14]
print(exemple_neg[-1], exemple_neg[-2])

#Pour finir, nous allons utiliser le tranchage pour avoir accès à une tranche d'élément, par exemple du 2ème jusqu'au 8ème élément.
tranche = [45,96,12,78,569,624,7,73,34,10]
print(tranche[3:5]) #Ici nous tranchons au début du 3ème élément jusqu'à la fin du 4ème élément.
#Ce qui nous affichera [78, 569].

#-------------------------------------------------------------------------
#Ajouter des éléments dans une liste:
#Ajout avec la méthode ".append()":
var = ["Jean", "Marc", "Gaston"] #Liste de 3 éléments.

print("\nNombre d'éléments dans la liste:", len(var)) #Nombre d'élément dans la liste.
print("Elément de la liste:", var) #Affichage de la liste.

var.append("François") #Ajout d'un élément à la fin de la liste grace à la méthode ".append()".
#Cependant, cette méthode peut contenir qu'un seul argument il serait donc utile d'utiliser la boucle "for" pour ajouter plusieurs éléments avec cette méthode.

print("\nNombre d'éléments dans la nouvelle liste:", len(var))
print("Elément de la liste:", var)
#Maintenant, ont peut voir que la liste contient 4 éléments et que le nouvel élément s'est ajouter à la fin de la liste.

#Ajout avec la méthode de "l'opération +":
var2 = [45, 52, 69, 78]
print(var2)

var2 = var2 + [87, 25, 76] #Variable est égale à variable plus la liste d'éléments à ajouter dans la liste.
print(var2)
#Ont peut voir que la méthode de l'opération est utile lorsque l'ont veut ajouter plusieurs éléments dans notre liste.

#-------------------------------------------------------------------------
#Supprimer des éléments d'une liste:
#Supprimer avec la méthode ".remove()":

print("\nListe de marques automobiles:")
marques = ["Renault", "Peugeot", "Cadillac", "Citroën"]
print(marques)

marques.remove("Citroën") #Ont utilise la méthode ".remove()" en lui donnant l'argument que l'ont souhaite supprimer.
print(marques)

#Cependant il existe un problème, s'il y a plusieurs fois la même valeur dans une même liste, alors, toutes les veleurs du même nom ne seront pas supprimer, exemple:
print("\nListe de mots divers:")
divers = ["Couteau", "Google", "Manger", "Google", "Rouge", "Furoncle", "Google"] #Voici une liste avec trois fois le mot "Google".
print(divers)

divers.remove("Google")
print(divers)
#Ont peut voir que la méthode a supprimer uniquement le permier mot "google" de la liste mais pas les autres.

#Supprimer avec le mot clé "del":

print("\nListe de nombres:")
nmb = [10, 20, 30, 40, 50, 60]
print(nmb)

del nmb[3] #Ici ont souhaite supprimer le 4ème élément de la liste, donc, le nombre 40.
print(nmb)

#-------------------------------------------------------------------------
#Opérateur d'appartenance: in.
#Cet opérateur va nous permettre de vérifier si une valeur est présente dans une liste.

couleur = ["Rouge", "Bleu", "Vert"]

print("\nOpération in:")
print("Rouge" in couleur) #Ci-contre nous vérifions si la valeur "Rouge" se trouve bien dans la liste "couleur", cette vérification nous renvoie un booléen.

couleur_plus = input("Rechercher une couleur: ")

if couleur_plus in couleur: #Si la valeur de la variable "couleur_plus" est dans "couleur" alors...
	print(f"La couleur {couleur_plus} se trouve bien dans la liste !")
else: #Sinon
	couleur.append(couleur_plus) #Ont ajoute la valeur de la variable "couleur_plus" dans la variable/liste "couleur".
	print(f"La couleur {couleur_plus} est introuvable et a donc été ajouter à la liste !")
	print(couleur)
	
#-------------------------------------------------------------------------
#Utilisation de la boucle "for" avec les listes.

print('\nUtilisation de la boucle "for" et des listes:')
for i in [0,1,2,3,4,5,6,7,8,9]:
	print("Dans la boucle:", i)
	
for v in ["Paris", "Londres", "Barcelone", "Berlin"]:
	print("Dans la boucle:", v)
	print(v.upper()) #Ont utilise la méthode ".upper()" sur une chaîne de caractère pour mettre cette dernière en majuscule.
