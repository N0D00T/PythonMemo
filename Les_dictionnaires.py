#Les dictionnaires.
#Un dictionnaire nous sert à sauvegarder des données sous la forme "clé - valeur".
#Les listes utilisent les caractères --> []
#Les dictionnaires utilisent les caractères --> {}

achats = {
	"pain": 5.4,
	"lait": 2.5,
	"oeuf": 3.4,
	"oranges": 4.5,
}
#Ci-dessus, nous avons créé notre dictionnaire "achats" qui contient des clés et leurs valeurs.
#il est possible d'utiliser des clés de type int, str ou même float.

print(type(achats)) #Ont affiche le type de donnée de "achats".
print(achats)

#Autre exemple de dictionnaire:

personne = {"nom": "Dupont", "Prenom": "Benois", "age": 30, "en couple": False}
print(personne)

departements = {1: "Ain", 62: "Pas-de-Calais", 45: "Loiret"}
print(departements)


#-------------------------------------------------------------------------------
#Lire les valeurs de dictionnaires:

dict1 = {"couleur1": "Rouge", "couleur2": "Bleu"}
dict2 = {1: "Vert", 2: "Jaune"}

print("\nLire des valeurs de dictionnaires:\n")
print(dict1)
print(dict2)

print(dict1["couleur1"]) #Ont demande d'afficher la valeur de la clé "couleur1" depuis le disctionnaire "dict1".
print(dict2[1]) #Ont demande d'afficher la valeur de la clé "1" depuis le disctionnaire "dict2".

#-------------------------------------------------------------------------------
#Modifier les valeurs de dictionnaires:

print("\Modifier des valeurs de dictionnaires:\n")

dict_modif = {1: "Fromage", 2: "Skate", 3: "Manger"} #Notre dictionnaire.
print(dict_modif) #Afficher le dictionnaire.

dict_modif[1] = "Test" #Ont sélectionne la clé "1" depuis le dictionnaire "dict_modif" et ont lui ré-affecte une nouvelle valeur "Test".
print(dict_modif)

#-------------------------------------------------------------------------------
#Ajouter/supprimer des éléments d'un dictionnaire:

print("\nAjouter/supprimer des valeurs de dictionnaires:\n")

dict_addsupr = {"fr": "Je parle français", "en": "I speak english"}
print(dict_addsupr)

#Pour ajouter un élément dans le dictionnaire, ont utilise la même commande que celle qui modifie la valeur d'une clé, cette dernière va automatiquement créé la clé manquante dans le dictionnaire.

dict_addsupr["ru"] = "Я говорю по-русски"
print(dict_addsupr)

del dict_addsupr["ru"] #Pour supprimer un élément, ont utilise le mot clé "del" comme pour les listes.
print(dict_addsupr)
