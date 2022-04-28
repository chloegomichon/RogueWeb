
import random

class Player:
    def __init__(self, symbol="P"):
        self._symbol = symbol
        self._x = None
        self._y = None
        self.money = 0
        self.life = 100 #points de vie
        self.compteur = 0 # va servir à perdre de la vie dans les déplacements
        self.weapons = 0
        self.treasure = False

    def initPos(self, _map):
        n_row = len(_map) 
        #n_col = len(_map[0])

        y_init = n_row//2
        found = False
        while found is False:
            y_init += 1
            for i,c in enumerate(_map[y_init]):
                if c == ".":
                    x_init = i
                    found = True
                    break

        self._x = x_init
        self._y = y_init

        _map[self._y][self._x] = self._symbol

    def move(self, dx, dy, map):
        self.compteur = (self.compteur + 1)%5
        if self.compteur == 0 :
            self.life = self.life - 1 # perte d'un point de vie tous les trois déplacements
 
        if self.life <= 0 or self.treasure == True:
            # arrêt du joueur si plus de points de vie ou si trésor trouvé
            new_x = self._x
            new_y = self._y 
            if self.life <= 0:
                self.life=0
        
        else : 
            new_x = self._x + dx
            new_y = self._y + dy    


        if map[new_y][new_x] == "." or map[new_y][new_x] == "x" or map[new_y][new_x] == "P":
            ret =True
            map[new_y][new_x] = self._symbol
            map[self._y][self._x] = "x"
            data = [{"i": f"{self._y}", "j":f"{self._x}", "content":"x"}, {"i": f"{new_y}", "j":f"{new_x}", "content":self._symbol, "pass_on_cash": False, "treasure":self.treasure},self.money,self.life,self.weapons]
            self._x = new_x
            self._y = new_y

        
        elif map[new_y][new_x] == 'O' :
            self.money += 1
            ret =True
            map[new_y][new_x] = self._symbol
            map[self._y][self._x] = "x"
            data = [{"i": f"{self._y}", "j":f"{self._x}", "content":"x"}, {"i": f"{new_y}", "j":f"{new_x}", "content":self._symbol, "pass_on_cash":True,"treasure":self.treasure},self.money,self.life,self.weapons]
            self._x = new_x
            self._y = new_y

        elif map[new_y][new_x] == "W" :
            ret =True
            self.weapons = self.weapons + 1 
            map[new_y][new_x] = self._symbol
            map[self._y][self._x] = "x"
            data = [{"i": f"{self._y}", "j":f"{self._x}", "content":"x"}, {"i": f"{new_y}", "j":f"{new_x}", "content":self._symbol, "pass_on_cash": False,"treasure":self.treasure},self.money,self.life, self.weapons]
            self._x = new_x
            self._y = new_y

        elif map[new_y][new_x] == 'Z' : #méchant qui inflige dommages directs, avec une certaine probabilité
            prob = random.randint(0,2)
            if prob != 0:
                self.life -= 2
            ret =True
            map[new_y][new_x] = self._symbol
            map[self._y][self._x] = "x"
            data = [{"i": f"{self._y}", "j":f"{self._x}", "content":"x"}, {"i": f"{new_y}", "j":f"{new_x}", "content":self._symbol, "pass_on_cash": False,"treasure":self.treasure},self.money,self.life,self.weapons]
            self._x = new_x
            self._y = new_y

        elif map[new_y][new_x] == 'K' : #méchant qui vole des pièces
            self.money -= 1
            ret =True
            map[new_y][new_x] = self._symbol
            map[self._y][self._x] = "x"
            data = [{"i": f"{self._y}", "j":f"{self._x}", "content":"x"}, {"i": f"{new_y}", "j":f"{new_x}", "content":self._symbol, "pass_on_cash": False,"treasure":self.treasure}, self.money, self.life,self.weapons]
            self._x = new_x
            self._y = new_y

        elif map[new_y][new_x] == 'H' : #méchant qui se met à bouger pendant sur 4 déplacements (à coder)
            prob = random.randint(0,2)
            if prob == 0: # je réussis à tuer le méchant
                self.life -= 1
                map[new_y][new_x] = self._symbol
                map[self._y][self._x] = "x"
                data = [{"i": f"{self._y}", "j":f"{self._x}", "content":"x"}, {"i": f"{new_y}", "j":f"{new_x}", "content":self._symbol, "pass_on_cash": False,"treasure":self.treasure}, self.money, self.life,self.weapons]
                self._x = new_x
                self._y = new_y
                ret =True
       
        elif map[new_y][new_x] == 'T' :
            self.treasure = True
            ret =True
            map[new_y][new_x] = self._symbol
            map[self._y][self._x] = "x"
            data = [{"i": f"{self._y}", "j":f"{self._x}", "content":"x"}, {"i": f"{new_y}", "j":f"{new_x}", "content":self._symbol, "pass_on_cash": False,"treasure":self.treasure},self.money,self.life,self.weapons]
            self._x = new_x
            self._y = new_y

        else:
            ret = False
            data = []
        return data, ret

    def getMoney(self):
        return(self.money)

    def getLife(self):
        return(self.life)