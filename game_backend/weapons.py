import random 

class Weapon:

    def __init__(self):
        self.symbol = 'W'
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
                
                if _map[y_init][x_init] == "." and _map[y_init][x_init+1] == "." and _map[y_init][x_init-1] == "." and _map[y_init+1][x_init] == "."and _map[y_init-1][x_init] == ".":
                    found = True
                    break

        self.x = x_init
        self.y = y_init
    
        _map[self.y][self.x] = self.symbol
    
    