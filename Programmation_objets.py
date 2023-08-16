#La programmation orientée objets.
#Voir --> https://www.youtube.com/watch?v=_TVrC_HCkTE&t=15503s à 4:11:41

class Personne:
	
	nom = "Willis"
	prenom = "Bruce"
	age = 65

print(Personne.prenom) #Affichage de la variable "prenom" de la classe "Personne".

bruce = Personne() #Ci-contre, nous avons créer un objet* que l'on appel "bruce". *Un objet est tout simplement une variable contenant une classe.
print(bruce.prenom) #Ci-contre, ont affiche donc l'objet "bruce" qui contient la variable "prenom" de la classe "Personne".
#Cependant, le code présent ci-dessus n'est pas la bonne méthode pour utiliser une classe, l'exemple ci-dessus permet simplement de nous faire comprendre le fonctionnement d'une classe. Exemple du problème de l'exemple ci-dessus:

alice = Personne() #Création d'un nouvel objet "alice" qui contient la class "Personne".
print(alice.prenom) #Pour ce "print" le prénom donné sera toujours "Bruce".

#-------------------------------------------------------------------------------

#La méthode de classe --> __init__():
#Une méthode de classe est tout simplement le nom que l'on donne à une fonction qui se trouve à l'intérieur d'une classe.

class Personne2: #Création de la classe "Personne2".

	def __init__(self, nom, prenom, age): #Création de la méthode "__init__" avec le mot clé "self" que l'on expliquera plus bas.
		
		self.nom = nom
		self.prenom = prenom
		self.age = age
		
user1 = Personne2("Gabin", "Jean", 68) #Création de l'objet "user1".
user2 = Personne2("Sidney", "Anna", 22)#Création de l'objet "user2".

print(user1.nom, user1.prenom, user1.age)
print(user2.nom, user2.prenom, user2.age)
		
#La méthode "__init__()" est une méthode bien particulière de Python, elle sera la première des méthodes de la classe à être éxécuter.
#Le mot clé "self" est obliguatoire lorsque l'on utilise des méthode de classe.
#Le paramètre self représente en fait l'objet cible, c'est-à-dire que c'est une variable qui contient une référence vers l'objet qui est en cours de création, donc, les objets user1 et user2 pour cet exemple.

#FIN--------
