from database import obtenir_connexion

try:
    connexion = obtenir_connexion()
    print("Connexion PostgreSQL réussie !")
    connexion.close()

except Exception as erreur:
    print("Erreur de connexion :", erreur)