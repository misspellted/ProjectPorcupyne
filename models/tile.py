from objects import InstalledObjectModel
from objects import LooseObjectModel

class TileTypes:
    Empty = 0
    Floor = 1

class TileModel:
    def __init__(this):
        this.__type = TileTypes.Empty
        this.__looseObject = None
        this.__installedObject = None
        this.__onTileTypeChanged = []

    def getTileType(this):
        return this.__type

    def setTileType(this, type):
        if type != this.__type:
            this.__type = type
            for callback in this.__onTileTypeChanged:
                callback(type)

    def registerTileTypeChangedCallback(this, callback):
        this.__onTileTypeChanged.append(callback)
