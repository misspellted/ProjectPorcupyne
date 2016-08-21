from tile import TileView

class WorldView:
    def __init__(this, model):
        this.__length = model.getLength()
        this.__height = model.getHeight()
        this.__tileViews = list()

        for y in range(this.__height):
            for x in range(this.__length):
                this.__tileViews.append(TileView(model.getTileAt(x, y)))

    def getLength(this):
        return this.__length

    def getHeight(this):
        return this.__height

    def getTileViewAt(this, x, y):
        if 0 <= x < this.__length and 0 <= y < this.__height:
            return this.__tileViews[y * this.__length + x]

        raise ValueError(str.format("Tile ({0}, {1} is out of range.", x, y))

    def render(this, renderer):
        ## Length and height refer to tile counts, not pixel size.
        ## Therefore, calculate the pixel dimensions before creating the rendering.
        pxLen = TileView.TILE_LENGTH * this.__length
        pxHei = TileView.TILE_HEIGHT * this.__height

        ## Start with a blank rendering.
        rendering = renderer.createRenderTarget(pxLen, pxHei, (0, 0, 0, 0))

        ## Add the tiles.
        tileX = 0
        tileY = 0
        for y in range(this.__height):
            for x in range(this.__length):
                ## Render the current tile view.
                renderer.renderItemTo(rendering, this.__tileViews[y * this.__length + x].render(renderer), (tileX, tileY))

                ## Ready the next column.
                tileX += TileView.TILE_LENGTH

            ## Ready the next row.
            tileY += TileView.TILE_HEIGHT

            ## Reset for the next row of tiles.
            tileX = 0

        return ((pxLen, pxHei), rendering)
