import pygame

## For help diagnosing any relative import issues, please see components.loggers.null.logger.
from ..renderer import Renderer

class PygameRenderer(Renderer):
    def createRenderTarget(this, length, height, bits = 32):
        return pygame.Surface((length, height), pygame.SRCALPHA, 32)

    def renderItemTo(this, target, item, coordinates):
        ## FIXME: Do some parameter verifications?
        target.blit(item, coordinates)
