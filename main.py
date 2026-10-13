
# Application console de gestion de bibliothèque

import json
import os

bibliotheque = []
prochain_id = 1


def sauvegarder_livres():
    with open("bibliotheque.json", "w", encoding="utf-8") as fichier:
        json.dump(bibliotheque, fichier, ensure_ascii=False, indent=4)


def charger_livres():
    global prochain_id

    if not os.path.exists("bibliotheque.json"):
        return

    try:
        with open("bibliotheque.json", "r", encoding="utf-8") as fichier:
            livres_charges = json.load(fichier)

        if not isinstance(livres_charges, list):
            print("Erreur : le fichier JSON ne contient pas une liste.")
            return

        bibliotheque.clear()
        bibliotheque.extend(livres_charges)

        if bibliotheque:
            prochain_id = max(livre["id"] for livre in bibliotheque) + 1

    except (json.JSONDecodeError, OSError, KeyError, TypeError):
        print("Erreur lors du chargement des livres.")


def afficher_menu():
    print("\n===== GESTION DE BIBLIOTHÈQUE =====")
    print("1. Ajouter un livre")
    print("2. Afficher tous les livres")
    print("3. Rechercher un livre")
    print("4. Supprimer un livre")
    print("5. Quitter")


def ajouter_livre():
    global prochain_id

    titre = input("Titre du livre : ").strip()
    auteur = input("Nom de l'auteur : ").strip()

    if titre == "" or auteur == "":
        print("Erreur : le titre et l'auteur sont obligatoires.")
        return

    livre = {
        "id": prochain_id,
        "titre": titre,
        "auteur": auteur
    }

    bibliotheque.append(livre)
    prochain_id += 1
    sauvegarder_livres()

    print("Livre ajouté avec succès !")


def afficher_livres():
    if len(bibliotheque) == 0:
        print("La bibliothèque est vide.")
        return

    print("\n===== LISTE DES LIVRES =====")

    for livre in bibliotheque:
        print(f"ID : {livre['id']}")
        print(f"Titre : {livre['titre']}")
        print(f"Auteur : {livre['auteur']}")
        print("----------------------------")


def rechercher_livre():
    recherche = input("Saisis un titre ou un auteur : ").strip().lower()

    if recherche == "":
        print("La recherche ne peut pas être vide.")
        return

    resultats = []

    for livre in bibliotheque:
        if (
            recherche in livre["titre"].lower()
            or recherche in livre["auteur"].lower()
        ):
            resultats.append(livre)

    if len(resultats) == 0:
        print("Aucun livre trouvé.")
    else:
        print("\n===== RÉSULTATS DE LA RECHERCHE =====")

        for livre in resultats:
            print(
                f"ID : {livre['id']} | "
                f"Titre : {livre['titre']} | "
                f"Auteur : {livre['auteur']}"
            )


def supprimer_livre():
    afficher_livres()

    if len(bibliotheque) == 0:
        return

    try:
        identifiant = int(input("ID du livre à supprimer : "))
    except ValueError:
        print("Erreur : saisis un numéro valide.")
        return

    for livre in bibliotheque:
        if livre["id"] == identifiant:
            bibliotheque.remove(livre)
            sauvegarder_livres()
            print("Livre supprimé avec succès !")
            return

    print("Aucun livre ne correspond à cet ID.")

charger_livres()

while True:
    afficher_menu()

    choix = input("Votre choix : ").strip()

    if choix == "1":
        ajouter_livre()

    elif choix == "2":
        afficher_livres()

    elif choix == "3":
        rechercher_livre()

    elif choix == "4":
        supprimer_livre()

    elif choix == "5":
        print("Merci d'avoir utilisé la bibliothèque. Au revoir !")
        break

    else:
        print("Choix invalide. Saisis un nombre entre 1 et 5.")
