## Import the available viewers.
from piegame.viewer import PygameViewer

## Define the available viewers.
__viewers = dict()
__viewers["pygame"] = PygameViewer()

## Provide the ability to get the names of available viewers.
def getAvailableViewerNames():
    return __viewers.keys()

## Provides the ability to get an available viewer.
def getViewer(viewerName):
    viewer = None
    if viewerName in __viewers.keys():
        viewer = __viewers[viewerName]
    return viewer
