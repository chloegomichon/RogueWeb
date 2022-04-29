from .map_generator import Generator
from .player import Player
from .coin import Coin
from .enemy import Enemy
from .weapons import Weapon
from .treasure import Treasure
import random
enemies = ['Z', 'H', 'K']


class Game:
    def __init__(self, width=96, height=32):
        self._generator = Generator(width=width, height=height)
        self._generator.gen_level()
        self._generator.gen_tiles_level()
        self._map = self._generator.tiles_level

        self._player1 = Player()
        self._player1.initPos( self._map )

        self._player2 = Player()
        self._player2.initPos( self._map )

        self.enemies=[]

        self._treasure = Treasure()
        self._treasure.initPos( self._map )

        

        for i in range(15):
            c = Coin()
            c.initPos(self._map)

        for j in range(20):
            symbol = random.choice(enemies)
            e = Enemy(symbol)
            e.initPos(self._map)
            self.enemies.append(e)

        for j in range(10):
            w = Weapon()
            w.initPos(self._map)

    def getMap(self):
        return self._map

    def move_P1(self, dx, dy):
        return self._player1.move(dx, dy, self._map)
    
    def move_P2(self, dx, dy):
        return self._player2.move(dx, dy, self._map)

    def move_enemies(self):
        all_enemies_data = []
        for enemy in self.enemies:
            data = enemy.move_enemy(self._map)
            all_enemies_data.append(data)
        return all_enemies_data, True 

    def getPlayer1(self):
        return self._player1

    def getPlayer2(self):
        return self._player2