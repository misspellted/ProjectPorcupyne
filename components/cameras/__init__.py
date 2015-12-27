## Import the available cameras.
from piegame.camera import PygameCamera

## Define the available cameras.
__cameras = dict()
__cameras["pygame"] = PygameCamera()

## Provide the ability to get the names of available cameras.
def getAvailableCameraNames():
    return __cameras.keys()

## Provides the ability to get an available camera.
def getCamera(cameraName):
    camera = None
    if cameraName in __cameras.keys():
        camera = __cameras[cameraName]
    return camera
