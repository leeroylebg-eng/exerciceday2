# Ensemble de mes nombres favoris
my_fav_numbers = {3, 7, 12, 42, 99}
print("Départ :", my_fav_numbers)

# Ajouter deux nombres
my_fav_numbers.add(15)
my_fav_numbers.add(28)
print("Après ajout :", my_fav_numbers)

# Supprimer le dernier ajouté
my_fav_numbers.remove(28)
print("Après suppression :", my_fav_numbers)

# Ensemble de l'ami
friend_fav_numbers = {5, 7, 21, 33, 50}

# Union des deux ensembles
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print("Ensemble commun :", our_fav_numbers)my_tuple = (1, 2, 3, 4, 5)
my_tuple = my_tuple + (6, 7)
print("Nouveau tuple :", my_tuple)# La liste de départ
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
print("Départ :", basket)

# Supprimer "Banana"
basket.remove("Banana")
print("Après suppression de Banana :", basket)

# Supprimer "Blueberries"
basket.remove("Blueberries")
print("Après suppression de Blueberries :", basket)

# Ajouter "Kiwi" à la fin
basket.append("Kiwi")
print("Après ajout de Kiwi :", basket)

# Ajouter "Apples" au début
basket.insert(0, "Apples")
print("Après ajout de Apples au début :", basket)

# Compter combien de fois "Apples" apparaît
nombre_apples = basket.count("Apples")
print("Nombre de Apples :", nombre_apples)

# Vider la liste
basket.clear()
print("Liste finale :", basket)# Générer la séquence sans tout écrire manuellement
sequence = []

for i in range(3, 11):  # de 3 à 10
    sequence.append(i / 2)

print("La séquence :", sequence)
# Afficher tous les nombres de 1 à 20
print("Tous les nombres de 1 à 20 :")
for i in range(1, 21):
    print(i)

# Afficher les nombres où l'index est pair
print("\nNombres avec un index pair :")
for i in range(1, 21):
    if i % 2 == 0:
        print(i)
        while True:
    name = input("Entrez votre nom : ")
    
    # Vérifier si le nom est valide
    if name.isdigit():
        print("Erreur : le nom ne peut pas être un nombre !")
    elif len(name) < 3:
        print("Erreur : le nom doit contenir au moins 3 lettres !")
    else:
        print("Merci !", name)
        break
# Demander les fruits favoris
fruits_input = input("Entrez vos fruits favoris (séparés par des espaces) : ")

# Stocker dans une liste
fruits_favoris = fruits_input.split()
print("Vos fruits favoris :", fruits_favoris)

# Demander un fruit
fruit_choisi = input("Entrez le nom d'un fruit : ")

# Vérifier si le fruit est dans la liste
if fruit_choisi in fruits_favoris:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")
# Liste des toppings et prix de base
toppings = []
prix_base = 10
prix_topping = 2.50

# Boucle pour ajouter les toppings
while True:
    topping = input("Entrez un topping (ou 'quit' pour arrêter) : ")
    
    if topping == "quit":
        break
    else:
        print(f"Adding {topping} to your pizza.")
        toppings.append(topping)

# Afficher les toppings et le prix total
print("\nVos toppings :")
for t in toppings:
    print(f"- {t}")

prix_total = prix_base + (len(toppings) * prix_topping)
print(f"\nPrix total : ${prix_total}")
# Liste des ages de la famille
ages = []
prix_total = 0

# Demander les ages
while True:
    age = input("Entrez l'age d'un membre (ou 'quit' pour arrêter) : ")
    
    if age == "quit":
        break
    else:
        ages.append(int(age))

# Calculer le prix total
for age in ages:
    if age < 3:
        prix_total += 0
        print(f"Age {age} : Gratuit")
    elif age <= 12:
        prix_total += 10
        print(f"Age {age} : $10")
    else:
        prix_total += 15
        print(f"Age {age} : $15")

print(f"\nPrix total des billets : ${prix_total}")
