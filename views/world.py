from tile import TileView

class WorldView:
    def __init__(this, model): ##, assets):
        this.__length = model.getLength()
        this.__height = model.getHeight()
        this.__tiles = list()

        for y in range(this.__height):
            for x in range(this.__length):
                ##this.__tiles.append(TileView(model.getTileAt(x, y), assets))
                this.__tiles.append(TileView(model.getTileAt(x, y)))

    def getLength(this):
        return this.__length

    def getHeight(this):
        return this.__height

    def getTileAt(this, x, y):
        if 0 <= x < this.__length and 0 <= y < this.__height:
            return this.__tiles[y * this.__length + x]

        raise ValueError("Tile (" + x + ", " + y + ") is out of range.")

    def render(this, renderer):
        ## Length and height refer to tile counts, not pixel size.
        ## Therefore, calculate the pixel dimensions before creating the rendering.
        pxLen = TileView.TILE_LENGTH * this.__length
        pxHei = TileView.TILE_HEIGHT * this.__height

        ## Start with a blank rendering.
        rendering = renderer.createRenderTarget(pxLen, pxHei)

        ## TODO: Add the tiles.
        tileX = 0
        tileY = 0
        for y in range(this.__height):
            tileY += TileView.TILE_HEIGHT
            for x in range(this.__length):
                tileX += TileView.TILE_LENGTH
                renderer.renderItemTo(rendering, this.__tiles[y * this.__length + x].render(), (tileX, tileY))
            ## Reset for the next row of tiles.
            tileX = 0
        
        return rendering
