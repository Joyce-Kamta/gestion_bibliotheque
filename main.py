from livres import (
    afficher_livres,
    ajouter_livre,
    rechercher_livre,
    supprimer_livre
)


def afficher_menu():
    print("\n===== GESTION DE BIBLIOTHÈQUE =====")
    print("1. Afficher tous les livres")
    print("2. Ajouter un livre")
    print("3. Rechercher un livre")
    print("4. Supprimer un livre")
    print("5. Quitter")


def main():

    while True:
        afficher_menu()

        choix = input("\nVotre choix : ")

        if choix == "1":
            afficher_livres()

        elif choix == "2":
         titre = input("Titre du livre : ").strip()
         auteur = input("Nom de l'auteur : ").strip()

         if not titre or not auteur:
            print("Erreur : le titre et l'auteur sont obligatoires.")
            continue

         try:
             
             annee = int(input("Année de publication : "))

             if annee <= 0 or annee > 2026:
                 print("Erreur : veuillez saisir une année valide.")
                 continue

         except ValueError:
             print("Erreur : l'année doit être un nombre entier.")
             continue

         ajouter_livre(titre, auteur, annee)

        elif choix == "3":
            titre = input("Titre à rechercher : ").strip
            if not titre:
               print("Erreur : veuillez saisir un titre.")
               continue
              
            rechercher_livre(titre)

        elif choix == "4":
            try:
               
              id_livre = int(input("Identifiant du livre à supprimer : "))
              supprimer_livre(id_livre)

            except ValueError:
              print("Erreur : veuillez saisir un identifiant numérique.")

        elif choix == "5":
            print("Au revoir !")
            break

        else:
            print("Choix invalide. Réessayez.")


if __name__ == "__main__":
    main()