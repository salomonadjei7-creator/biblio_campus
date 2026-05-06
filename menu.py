def afficher_menu():
    print("=== BiblioCampus ===")
    print("1. Gérer les livres")
    print("2. Gérer les emprunts")
    print("3. Voir les statistiques")
# Importer les fonctions nécessaires
from loans import emprunter_livre, rendre_livre
from books import lister_livres

# … (ton code menu existant)

def gerer_emprunts():
    print("=== Gérer les emprunts ===")
    livres = lister_livres()
    if not livres:
        print("Aucun livre disponible.")
        return
    
    for i, livre in enumerate(livres):
        dispo = "disponible" if livre["disponible"] else "emprunté"
        print(f"{i+1}. {livre['titre']} ({livre['auteur']}) - {dispo}")

    choix = int(input("Entrez le numéro du livre à emprunter/rendre : ")) - 1
    
    if 0 <= choix < len(livres):
        livre = livres[choix]
        if livre["disponible"]:
            emprunter_livre(livre)
            print(f"Vous avez emprunté : {livre['titre']}")
        else:
            rendre_livre(livre)
            print(f"Vous avez rendu : {livre['titre']}")
    else:
        print("Choix invalide.")

# Ajoute cette option dans ton menu
def afficher_menu():
    print("=== BiblioCampus ===")
    print("1. Gérer les livres")
    print("2. Gérer les emprunts")
    print("3. Voir les statistiques")

    choix = input("Choisissez une option : ")

    if choix == "1":
        # gestion des livres
        pass
    elif choix == "2":
        gerer_emprunts()
    elif choix == "3":
        afficher_stats()
