#Les fonctions:
#Les fonctions sont très utiles quand il s'agit de ré-utiliser des bouts de codes plusieurs fois dans nos programmes.

def ma_fonction():
	print("Bonjour !")
	
ma_fonction() #Ont appel la fonction que l'on à créé juste au dessus.
 	
#Pour définir notre fonction ci-dessus, nous avons utiliser le mot clé "def" en lui donnant le nom "ma_fonction", ont ajoute les parenthèses, puis les deux points pour préciser que la suite sera indenté.
#Ensuite, si ont veut utiliser notre fonction, il suffit de l'appeler comme l'exemple ci-dessus, en utilisant le nom de la fonction avec ces parenthèses.

#-------------------------------------------------------------------------------
#Les arguments de fonctions:
#Les arguments sont un peut comme des variables, tout simplement parce qu'un argument a besoin d'une valeur.

print("\nLes arguments de fonctions:")

def message(prenom): #Ont définit la fonction "message" en lui donnant un argument avec le nom "prenom".
	print(f"\nBonjour {prenom} !") #Ont affiche un message contenant la valeur de l'argument.

message("Jean") #Ont appel la fonction "message" tout en donnant une valeur à l'argument "prenom".
message("Tom")

#Autres exemples de fonctions:
#Exemple 1:

def clan(nom, nombre):
	print(f'\nVous appartenez au clan "{nom}" qui possède "{nombre}" membres !')

demande_nom = input("\nVeuillez indiquer le nom de votre clan: ")
demande_nombre = input("\nVeuillez indiqué le nombre de membre(s) dans votre clan: ")

clan(demande_nom, demande_nombre) #Attention, quand il y'a plusieurs arguments, l'ordre des valeurs données pour les arguments est importantes.

#Exemple 2:
#calculer l'aire d'un cercle:

def aire_cercle(rayon):
	print("\nL'aire du cercle est: ", 3.14 * rayon ** 2) #Ont affiche un message, puis ont calcul 3.14 x "le rayon donné" puissance 2, autrement dit, au carré.
	
aire_cercle(0.5) #Ont donne la valeur 0.5 pour l'argument "rayon".

#Exemple 3:
#Si jamais ont ne voit pas le nom des arguements d'une fonction, il est possible de les marquer dans la fonction, suivit par leurs valeurs.

def infos(prenom, temperature):
	print(f"\nBonjour {prenom}, il fait {temperature} °C")

infos(temperature=23, prenom="François") #Ont appel la fonction "infos" en lui donnant les valeurs "23" et "François" dans les arguments séléctionés.
# Dans le cas d'appel de fonction ci-dessus, l'ordre n'a plus d'importance car Python saura automatiquement comment donné les valeurs au arguements.

#-------------------------------------------------------------------------------
#Les valeurs par défauts des arguments:
#Les valeurs par défauts peuvent permettre de simplifier l'utilisation d'une fonction et nous permettent aussi de ne pas être obligé de donné des arguments quand ont appel une fonction.

print("\nLes valeurs par défauts des arguments: ")

def salutation(prenom = "Chris"): #Ci-contre, nous avons créé la fonction "salutation" qui contient l'argument "prenom" qui a pour valeur par défaut "Chris".
	print("Bonjour", prenom)
	
def message(temperature = 15, prenom = "Mathieu"): 
	print(f"Bonjour {prenom} la température est de {temperature} °C")

#Ci-dessus, nous avons créé la fonction "message" qui contient les arguments "temperature" et "prenom" qui ont pour valeur par défaut "15" et "Mathieu".
	
salutation()
message()

#Ci-dessus, nous appelons les fonctions "salutation" et "message" sans leurs préciser d'arguments car elle possèdent déjà des arguments par défaut.

salutation("Franck")
message(23, "Tibault")

#Comme dans l'exemple ci-dessus, il est quand même possible d'attribuer des valeurs à des arguements qui possèdent des valeurs par défauts, celà supprimera les valeurs par défaut et y ajoutera les nouvelles valeurs "Franck" à la place de "Chris" pour l'argument "prenom" de la fonction "salutation" et pareil pour les deux arguments de la fonction "message".

#-------------------------------------------------------------------------------
#L'instruction "return":
#L'instruction "return" est capable de retourner n'importe quels types de données.

print("\nL'instruction --> return:")

def carre1(nombre):
	print(f"Le carré de {nombre} est de {nombre * nombre}")
	
carre1(4)

#Dans le cas ci-dessus il est impossible pour nous de récupérer le résultat du calcul {nombre * nombre} car le résultat se trouve dans la fonction, dans ce cas précis, nous pouvons seulement l'afficher à l'écran.
#Si l'ont veut récupérer le résultat qui se trouve dans la fonction "carre" et l'utiliser n'importe ou dans notre code, il faudra utiliser l'instruction "return" comme dans l'exemple ci-dessous.

def carre2(nombre):
	return nombre * nombre #Ci-contre, le calcul nombre x nombre sera effectuer et le résultat sera retourner.
	
resultat = carre2(4) #Ci-contre, nous avons tout simplement donné la valeur "4" à l'argument "nombre" de notre fonction "carre2", tout en récupérant le résultat de l'instruction "return" dans la variable "resultat"

print("Le résultat de la fonction carre2 est de: ", resultat)
