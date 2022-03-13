
import random
from symtable import Symbol


class Coin:
    def __init__(self, symbol='O'):
        self.symbol = symbol
        self.x = None
        self.y = None

    
    def initPos(self, _map):
        n_row = len(_map)
        n_col = len(_map[0])

        y_init = random.randint(0, n_row)
        x_init = random.randint(0, n_col)
        found = False
        
        while found is False:
            y_init = (y_init + 1) %n_row
            for i in range(n_col):
                x_init = (x_init + i) %n_col
                if _map[y_init][x_init] == ".":
                    found = True
                    break

        self.x = x_init
        self.y = y_init

        _map[self.y][self.x] = self.symbol
        