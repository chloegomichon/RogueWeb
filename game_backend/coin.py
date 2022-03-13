
import numpy as np
from symtable import Symbol


class Coin:
    def __init__(self, symbol='O'):
        self.symbol = symbol
        self.x = None
        self.y = None

    
    def initPos(self, _map):
        n_row = len(_map)

        y_init = np.randint(0, n_row)
        found = False
        while found is False:
            y_init += 1 %n_row
            for i,c in enumerate(_map[y_init]):
                if c == ".":
                    x_init = i
                    found = True
                    break

        self.x = x_init
        self.y = y_init

        _map[self.y][self.x] = self.symbol
        