#Exercise, créer une calculatrice:

nombre_1 = input("\nVeuillez entrer un premier nombre: ")
nombre_2 = input("\nVeuillez entrer un second nombre: ")

nombre_1 = float(nombre_1)
nombre_2 = float(nombre_2)

addition = nombre_1 + nombre_2
soustraction = nombre_1 - nombre_2
multiplication = nombre_1 * nombre_2
division = nombre_1 / nombre_2

print("\nAddition:", addition)
print("\nSoustraction:", soustraction)
print("\nMultiplication:", multiplication)
print("\nDivision:", division)
