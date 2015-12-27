import assets
from models.tile import TileTypes

class TileView:
    ## Define the visual dimensions of the tile here (for now).
    TILE_LENGTH = 32
    TILE_HEIGHT = 32
    
    def __init__(this, model):
        model.registerTileTypeChangedCallback(this.onTileTypeChanged)
        this.onTileTypeChanged(model.getTileType())

    def onTileTypeChanged(this, type):
        if type == TileTypes.Empty:
            this.__sprite = assets.getImage("empty_tile")
        else:
            this.__sprite = assets.getImage("floor_tile")

    def render(this):
        return this.__sprite
