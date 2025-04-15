from avl import AVLTree, Connexion
import sys

FICHIER_CONNEXIONS = "connexions.log"

def afficher_menu():
    print("\n===== MENU =====")
    print("1. Ajouter une connexion IP")
    print("2. Supprimer une IP")
    print("3. Nettoyer les IP inactives (> X min)")
    print("4. Rechercher une IP")
    print("5. Afficher toutes les connexions")
    print("6. Quitter et sauvegarder")

def main():
    avl = AVLTree()
    root = avl.load_from_file(FICHIER_CONNEXIONS)

    while True:
        afficher_menu()
        choix = input("Choix : ")

        if choix == "1":
            ip = input("Adresse IP à ajouter : ")
            conn = Connexion(ip)
            root = avl.insert(root, conn)
            print("IP ajoutée.")

        elif choix == "2":
            ip = input("Adresse IP à supprimer : ")
            root = avl.delete(root, ip)
            print("IP supprimée.")

        elif choix == "3":
            try:
                x = int(input("Inactivité en minutes (X) : "))
                root = avl.nettoyage(root, x)
                print("Nettoyage terminé.")
            except ValueError:
                print("Entrez un nombre valide.")

        elif choix == "4":
            ip = input("Adresse IP à rechercher : ")
            result = avl.search(root, ip)
            if result:
                print("Trouvée :", result.data)
            else:
                print("IP non trouvée.")

        elif choix == "5":
            print("\nConnexions triées :")
            for conn in avl.inorder(root):
                print(conn)

        elif choix == "6":
            avl.save_to_file(root, FICHIER_CONNEXIONS)
            print("Sauvegarde effectuée. À bientôt !")
            sys.exit()

        else:
            print("Choix invalide, réessayez.")

if __name__ == "__main__":
    main()
