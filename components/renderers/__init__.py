## Import the available renderers.
from piegame.renderer import PygameRenderer

## Define the available renderers.
__renderers = dict()
__renderers["pygame"] = PygameRenderer()

## Provide the ability to get the names of available renderer.
def getAvailableRendererNames():
    return __renderer.keys()

## Provides the ability to get an available renderer.
def getRenderer(rendererName):
    renderer = None
    if rendererName in __renderers.keys():
        renderer = __renderers[rendererName]
    return renderer
