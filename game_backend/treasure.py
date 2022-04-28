class Treasure:
    def __init__(self, symbol="T"):
        self._symbol = symbol
        self._x = None
        self._y = None

    def initPos(self, _map):
       
        n_row = len(_map) 
        n_col = len(_map[0])

        y_init = n_row//2
        found = False
        while found is False:
            y_init += 1
             # recherche proche de celle pour le joueur mais le trésor devrait se trouver plutôt à droite de l'écran d'où 
             # le parcours des possibilités en partant de la droite et plus de la gauche (utilisation de reversed())
            for i,c in enumerate(reversed(_map[y_init])):
                if c == ".":
                    x_init = n_col-1-i
                    found = True
                    break

        self._x = x_init
        self._y = y_init

        _map[self._y][self._x] = self._symbol
