from tile import TileView

class WorldView:
    def __init__(this, model, assets):
        this.__model = model
        this.__tiles = list()

        for y in range(model.getHeight()):
            for x in range(model.getLength()):
                this.__tiles.append(TileView(model.getTileAt(x, y), assets))

    def getLength(this):
        return this.__model.getLength()

    def getHeight(this):
        return this.__model.getHeight()

    def render(this, renderer):
        ## Length and height refer to tile counts, not pixel size.
        ## Therefore, calculate the pixel dimensions before creating the rendering.
        pxLen = TileView.TILE_LENGTH * this.getLength()
        pxHei = TileView.TILE_HEIGHT * this.getHeight()

        ## Start with a blank rendering.
        rendering = renderer.createRenderTarget(pxLen, pxHei)

        ## TODO: Add the tiles.
        tileX = 0
        tileY = 0
        for y in range(this.getHeight()):
            tileY += TileView.TILE_HEIGHT
            for x in range(this.getLength()):
                tileX += TileView.TILE_LENGTH
                renderer.renderItemTo(rendering, this.__tiles[y * this.getLength() + x].render(), (tileX, tileY))
            ## Reset for the next row of tiles.
            tileX = 0
        
        return rendering
