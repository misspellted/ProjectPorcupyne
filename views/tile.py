import assets
from models.tile import TileTypes

class TileView:
    ## Define the visual dimensions of the tile here (for now).
    TILE_LENGTH = 32
    TILE_HEIGHT = 32

    def __init__(this, model):
        model.registerTileTypeChangedCallback(this.onTileTypeChanged)
        this.onTileTypeChanged(model)
        this.__model = model

    def onTileTypeChanged(this, tile):
        tileType = tile.getTileType()

        if tileType == TileTypes.Empty:
            this.__sprite = assets.getImage("empty_tile")
        else:
            this.__sprite = assets.getImage("floor_tile")

    def render(this, renderer):
        rendering = renderer.createRenderTarget(TileView.TILE_LENGTH, TileView.TILE_HEIGHT, (0, 0, 0))

        ## Copy the sprite.
        renderer.renderItemTo(rendering, this.__sprite, (0, 0))

        return rendering

    def onDragSelectionComplete(this):
        this.__model.setTileType(TileTypes.Floor)
