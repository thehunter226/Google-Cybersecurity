# Assigner 'import_file' au nom du fichier
import_file = "allow_list.txt"

# Construire l'instruction 'with' pour lire le contenu initial du fichier
with open(import_file, "r") as file:

    # Utiliser '.read()' pour lire le fichier importé et le stocker dans une variable nommée 'ip_addresses'
    ip_addresses = file.read()

# Utiliser '.split()' pour convertir 'ip_addresses' d'une chaîne de caractères à une liste
ip_addresses = ip_addresses.split()

# Construire l'instruction itérative (la boucle)
# Nommer la variable de boucle 'element'
# Parcourir la liste 'remove_list'
for element in remove_list:

    # Créer une condition pour évaluer si 'element' est présent dans 'ip_addresses'
    if element in ip_addresses:

        # Utiliser la méthode '.remove()' pour supprimer
        # les éléments de 'ip_addresses'
        ip_addresses.remove(element)

# Reconvertir 'ip_addresses' en chaîne de caractères pour qu'elle puisse être écrite dans le fichier texte
ip_addresses = "\n".join(ip_addresses)

# Construire l'instruction 'with' pour réécrire le fichier d'origine
with open(import_file, "w") as file:

    # Réécrire le fichier en remplaçant son contenu par 'ip_addresses'
    file.write(ip_addresses)