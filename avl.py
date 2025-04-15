from datetime import datetime, timedelta

class Connexion:
    def __init__(self, ip):
        self.ip = ip
        self.timestamp = datetime.now()

    def __lt__(self, other):
        return self.ip < other.ip

    def __str__(self):
        return f"{self.ip} - {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"

class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.bal = 0

class AVLTree:
    def insert(self, root, data):
        if not root:
            return AVLNode(data)
        if data < root.data:
            root.left = self.insert(root.left, data)
        elif data.ip > root.data.ip:
            root.right = self.insert(root.right, data)
        else:
            return root  # IP already exists
        return self.balance(root)

    def delete(self, root, ip):
        if not root:
            return None
        if ip < root.data.ip:
            root.left = self.delete(root.left, ip)
        elif ip > root.data.ip:
            root.right = self.delete(root.right, ip)
        else:
            # Suppression du nœud avec 0 ou 1 enfant
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            # Cas 2 enfants : on remplace par le plus petit de la branche droite
            temp = self.get_min_node(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data.ip)
        return self.balance(root)

    def search(self, root, ip):
        if not root:
            return None
        if ip < root.data.ip:
            return self.search(root.left, ip)
        elif ip > root.data.ip:
            return self.search(root.right, ip)
        else:
            return root

    def inorder(self, root):
        result = []
        if root:
            result += self.inorder(root.left)
            result.append(root.data)
            result += self.inorder(root.right)
        return result

    def nettoyage(self, root, seuil_minutes):
        if not root:
            return None
        now = datetime.now()
        # Traitement récursif sur les sous-arbres
        root.left = self.nettoyage(root.left, seuil_minutes)
        root.right = self.nettoyage(root.right, seuil_minutes)
        delta = now - root.data.timestamp
        # Suppression si inactif depuis plus que le seuil
        if delta > timedelta(minutes=seuil_minutes):
            return self.delete(root, root.data.ip)
        return root

    def save_to_file(self, root, filename):
        with open(filename, 'w') as f:
            for connexion in self.inorder(root):
                f.write(f"{connexion.ip};{connexion.timestamp.isoformat()}\n")

    def load_from_file(self, filename):
        import os
        root = None
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                for line in f:
                    ip, timestamp = line.strip().split(';')
                    connexion = Connexion(ip)
                    connexion.timestamp = datetime.fromisoformat(timestamp)
                    root = self.insert(root, connexion)
        return root

    def get_min_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    # AVL balancing
    def height(self, node):
        if not node:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def get_balance(self, node):
        # Calcul du facteur d'équilibrage : hauteur gauche - droite
        return self.height(node.left) - self.height(node.right) if node else 0

    def balance(self, node):
        node.bal = self.get_balance(node)
        # Cas déséquilibré à gauche
        if node.bal > 1:
            if self.get_balance(node.left) < 0:
                node.left = self.rotate_left(node.left)  # Double rotation gauche-droite
            return self.rotate_right(node)
        # Cas déséquilibré à droite
        if node.bal < -1:
            if self.get_balance(node.right) > 0:
                node.right = self.rotate_right(node.right)  # Double rotation droite-gauche
            return self.rotate_left(node)
        return node

    def rotate_left(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        # Mise à jour des facteurs d'équilibre après rotation
        z.bal = self.get_balance(z)
        y.bal = self.get_balance(y)
        return y

    def rotate_right(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        # Mise à jour des facteurs d'équilibre après rotation
        z.bal = self.get_balance(z)
        y.bal = self.get_balance(y)
        return y
