from tile import TileModel
from tile import TileTypes
import random

class WorldModel:
    def __init__(this, length = 100, height = 100):
        this.__length = length
        this.__height = height
        this.__tiles = list()

        for y in range(height):
            for x in range(length):
                this.__tiles.append(TileModel())

    def getLength(this):
        return this.__length

    def getHeight(this):
        return this.__height

    def getTileAt(this, x, y):
        if 0 <= x < this.__length and 0 <= y < this.__height:
            return this.__tiles[y * this.__length + x]
        else:
            raise ValueError("Tile (" + x + ", " + y + ") is out of range.")

    def randomizeTiles(this):
        for y in range(this.__height):
            for x in range(this.__length):
                this.getTileAt(x, y).setTileType(TileTypes.Empty if random.randint(0, 1) == 0 else TileTypes.Floor)
