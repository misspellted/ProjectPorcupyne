import pygame

# For help diagnosing any relative import issues, please see components.loggers.null.logger.
from ..renderer import Renderer

class PygameRenderer(Renderer):
    def createRenderTarget(this, length, height, bits = 32):
        return pygame.Surface((length, height), pygame.SRCALPHA, 32)

    def renderItemTo(this, target, item, coordinates):
        ## FIXME: No parameter validations performed!
        target.blit(item, coordinates)

    def copyRegionFrom(this, source, coordinates, dimensions):
        ## FIXME: No parameter validations performed!
        length, height = dimensions
        rect = pygame.Rect(coordinates, dimensions)
        subsurface = source.subsurface(rect)
        copy = this.createRenderTarget(length, height)
        this.renderItemTo(copy, subsurface, (0, 0))
        return copy
