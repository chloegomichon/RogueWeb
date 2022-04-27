
import random
from symtable import Symbol

enemies = ['Z', 'W']

class Enemy:
    def __init__(self, symbol):
        self._symbol = symbol
        self._x = None
        self._y = None

    
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
                if self._symbol !='H' and _map[y_init][x_init] == "." :
                    found = True
                    break
                if self._symbol =='H' and _map[y_init][x_init] == "." and _map[y_init][x_init+1] == "." and _map[y_init][x_init-1] == "." and _map[y_init+1][x_init] == "."and _map[y_init-1][x_init] == ".":
                    found = True
                    break

        self._x = x_init
        self._y = y_init
    
        _map[self._y][self._x] = self._symbol
    
    def move_enemy(self, _map):

        new_x = self._x + random.randint(-1,1)
        new_y = self._y + random.randint(-1,1)

        contained = False
        while contained == False:
            if _map[new_y][new_x] == "." or _map[new_y][new_x] == "x" or _map[new_y][new_x] == "P":
                contained = True
            else:
                new_x = self._x + random.randint(-1,1)
                new_y = self._y + random.randint(-1,1)

        _map[new_y][new_x] = self._symbol
        _map[self._y][self._x] = "."
        data = [{"i": f"{self._y}", "j":f"{self._x}", "content":"."}, {"i": f"{new_y}", "j":f"{new_x}", "content":self._symbol}]
        self._x = new_x
        self._y = new_y


        #direction = (1,0)
        #x,y = self.x, self.y 
        #new_x =  self.x + direction[0]
        #new_y = self.y + direction[1]
        #map[x][y]= '.'
        #map[new_y][new_x] = 'H'
        #self.x = new_x
        #self.y = new_y
        #ret = True
        #data = [{"i": f"{self._y}", "j":f"{self._x}", "content":"x"}, {"i": f"{new_y}", "j":f"{new_x}", "content":self._symbol}, self.money, self.life]
        

        return data