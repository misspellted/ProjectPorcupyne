import pygame

## For help diagnosing any relative import issues, please see components.loggers.null.logger.
from ..loader import Loader

class PygameLoader(Loader):
    def loadImage(this, filePath):
        return pygame.image.load(filePath)

    def loadAudio(this, filePath):
        return pygame.mixer.Sound(filePath)
