from .map_generator import Generator
from .player import Player
from .coin import Coin
from .enemy import Enemy
from .weapons import Weapon
import random
enemies = ['Z', 'H', 'K']


class Game:
    def __init__(self, width=96, height=32):
        self._generator = Generator(width=width, height=height)
        self._generator.gen_level()
        self._generator.gen_tiles_level()
        self._map = self._generator.tiles_level

        self._player = Player()
        self._player.initPos( self._map )

        self.enemies=[]

        for i in range(15):
            c = Coin()
            c.initPos(self._map)

        for j in range(10):
            symbol = random.choice(enemies)
            e = Enemy(symbol)
            e.initPos(self._map)
            self.enemies.append(e)

        for j in range(10):
            w = Weapon()
            w.initPos(self._map)

    def getMap(self):
        return self._map

    def move(self, dx, dy):
        return self._player.move(dx, dy, self._map)

    def move_enemies(self):
        all_enemies_data = []
        for enemy in self.enemies:
            data = enemy.move_enemy(self._map)
            all_enemies_data.append(data)
        return all_enemies_data

    def getPlayer(self):
        return self._player