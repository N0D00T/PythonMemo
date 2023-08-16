#Les chaînes de caractères.

print("Hello world!")

prenom = 'Tom' #Guillemets simples
nom = "Cruse" #Guillemets doubles

print("Bonjour je m'apelle", prenom, nom)

print('Tom a dit: "Je suis le meilleur !"')
#Ont peut utiliser les guillemets simple par exemple pour afficher un dialogue à l'utilisateur, comme dans le cas ci-dessus.


#---------------------------------------------------------------------
#Récupérer le nombre de caractères.

mot = 'Voiture rouge' #Les espaces sont aussi compter comme des chaînes de caractères.
nombre = len(mot) #La fonction len() pour "lenght" qui veut dire "longueur".
print(nombre)

#Autre façon de faire:
print(len(mot))


#---------------------------------------------------------------------
#La concaténation.

nom = "Jackson"
prenom = "Mickael"
nom_complet_1 = prenom + nom #La concaténation se fait avec le "+" que l'on peut voir ci-contre.
nom_complet_2 = prenom + " " + nom

print(nom_complet_1) #La variable "nom_complet_1" ne possède pas d'espace entre les deux mots.
print(nom_complet_2) #La variable "nom_complet_2" remèdie au problème du dessus.

#La concaténation peut se faire uniquement avec des chaînes de caractères.
mot_1 = "Jambon"
mot_2 = "Camion"
nombre = 120 #Nous devons convertir ce nombre entier "int" en chaîne de caractères "str" pour ne pas avoir une erreur de type.

phrase = mot_1 + mot_2 + str(nombre) #Conversion de la variable "nombre" de "int" à "str"
print(phrase)

phrase_modif = mot_1 + " " + mot_2 + " " + str(nombre)
print(phrase_modif)


#---------------------------------------------------------------------
#Formatage f-string.

prenom = "Veronica"
age = 36

texte = f"Bonjour je m'apelle {prenom} j'ai {age} ans !" #Pas bessoin de convertir les variable de type "int" ou "float" avec le formatage f-string. 
print(texte)

#Autre façon de faire:
print(f"Bonjour je m'apelle {prenom} j'ai {age} ans !")

#Exercise:

prenom_exo = "Bruno"
nom_exo = "Mars"
age_exo = 38

texte_exo = f"Bonjour je m'apelle {prenom_exo} {nom_exo} j'ai {age_exo} ans !"
print(texte_exo)
