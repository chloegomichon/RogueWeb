
import random
from symtable import Symbol

enemies = ['Z', 'W']

class Enemy:
    def __init__(self, symbol):
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
            direction = random.choice([1,-1])
            for i in range(n_col):
                x_init = (x_init + direction*i) %n_col
                if self.symbol !='H' and _map[y_init][x_init] == "." :
                    found = True
                    break
                if self.symbol =='H' and _map[y_init][x_init] == "." and _map[y_init][x_init+1] == "." and _map[y_init][x_init-1] == "." and _map[y_init+1][x_init] == "."and _map[y_init-1][x_init] == ".":
                    found = True
                    break

        self.x = x_init
        self.y = y_init
    
        _map[self.y][self.x] = self.symbol
    
    def move_enemy(self, map):

        direction = (1,0)
        x,y = self.x, self.y 
        new_x =  self.x + direction[0]
        new_y = self.y + direction[1]
        map[x][y]= '.'
        map[new_y][new_x] = 'H'
        self.x = new_x
        self.y = new_y
        ret = True
        data = [{"i": f"{self._y}", "j":f"{self._x}", "content":"x"}, {"i": f"{new_y}", "j":f"{new_x}", "content":self._symbol}, self.money, self.life]
        

        return data, ret