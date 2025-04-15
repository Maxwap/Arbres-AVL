from avl import AVLTree, Connexion
from datetime import datetime, timedelta

def creer_connexion_fictive(ip, minutes_dans_le_passe):
    conn = Connexion(ip)
    conn.timestamp = datetime.now() - timedelta(minutes=minutes_dans_le_passe)
    return conn

def test_nettoyage_et_affichage():
    tree = AVLTree()
    root = None

    # IPs actives (0 à 3 min)
    ip1 = creer_connexion_fictive("192.168.1.10", 1)
    ip2 = creer_connexion_fictive("192.168.1.12", 2)
    ip3 = creer_connexion_fictive("192.168.1.14", 0)

    # IPs inactives (15 à 45 min)
    ip4 = creer_connexion_fictive("10.0.0.1", 20)
    ip5 = creer_connexion_fictive("10.0.0.2", 45)

    # Insertion dans l'AVL
    for ip in [ip1, ip2, ip3, ip4, ip5]:
        root = tree.insert(root, ip)

    print(" Connexions AVANT nettoyage :")
    for conn in tree.inorder(root):
        print(conn)

    # Nettoyage des connexions inactives depuis >10 minutes
    root = tree.nettoyage(root, 10)

    print("\n Connexions APRÈS nettoyage (inactives > 10 min supprimées) :")
    for conn in tree.inorder(root):
        print(conn)

    # Test de recherche
    print("\n Recherche de l'IP 192.168.1.10 :")
    found = tree.search(root, "192.168.1.10")
    print(found.data if found else "Non trouvée.")

    print("\n Recherche de l'IP 10.0.0.2 (supprimée) :")
    found = tree.search(root, "10.0.0.2")
    print(found.data if found else "Non trouvée.")

if __name__ == "__main__":
    test_nettoyage_et_affichage()