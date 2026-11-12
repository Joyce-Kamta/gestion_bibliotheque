import secrets

from database import obtenir_connexion

def afficher_livres():
    connexion = obtenir_connexion()

    try:
        with connexion.cursor() as curseur:
            curseur.execute("SELECT * FROM livres")

            livres = curseur.fetchall()

            for livre in livres:
                print(livre)

    finally:
        connexion.close()


def ajouter_livre(titre, auteur, annee):
    connexion = obtenir_connexion()

    try:
        with connexion.cursor() as curseur:

            for tentative in range(10):
                id_livre = secrets.randbelow(900000) + 100000

                curseur.execute(
                    """
                    INSERT INTO livres (id, titre, auteur, annee)
                    VALUES (%s, %s, %s, %s)
                    ON CONFLICT (id) DO NOTHING
                    """,
                    (id_livre, titre, auteur, annee)
                )

                if curseur.rowcount == 1:
                    connexion.commit()
                    print("Livre ajouté avec succès !")
                    print("Identifiant attribué :", id_livre)
                    return

            print("Impossible de générer un identifiant unique.")

    except Exception as erreur:
        connexion.rollback()
        print("Erreur lors de l'ajout :", erreur)

    finally:
        connexion.close()

def rechercher_livre(titre):
    connexion = obtenir_connexion()

    try:
        with connexion.cursor() as curseur:
            curseur.execute(
                """
                SELECT * FROM livres
                WHERE titre ILIKE %s
                """,
                (f"%{titre}%",)
            )

            resultats = curseur.fetchall()

            if resultats:
                print("\nLivres trouvés :")

                for livre in resultats:
                    print(livre)

            else:
                print("Aucun livre trouvé.")

    except Exception as erreur:
        print("Erreur lors de la recherche :", erreur)

    finally:
        connexion.close()

def supprimer_livre(id_livre):
    connexion = obtenir_connexion()

    try:
        with connexion.cursor() as curseur:
            curseur.execute(
                """
                DELETE FROM livres
                WHERE id = %s
                """,
                (id_livre,)
            )

            if curseur.rowcount > 0:
                connexion.commit()
                print("Livre supprimé avec succès !")

            else:
                print("Aucun livre trouvé avec cet identifiant.")

    except Exception as erreur:
        connexion.rollback()
        print("Erreur lors de la suppression :", erreur)

    finally:
        connexion.close()

