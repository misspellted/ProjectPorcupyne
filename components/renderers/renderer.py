class Renderer:
    def createRenderTarget(this, length, height, bits = 32):
        return NotImplemented

    def renderItemTo(this, target, item, coordinates):
        return NotImplemented

    def copyRegionFrom(this, source, coordinates, dimensions):
        return NotImplemented
