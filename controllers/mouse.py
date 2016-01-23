from controller import Controller
from components.events.mouse import BUTTON_LEFT, BUTTON_MIDDLE, BUTTON_RIGHT

class MouseController(Controller):
    def __init__(this, inputComponent, cameraComponent):
        this.__input = inputComponent
        this.__camera = cameraComponent
        this.__lastFramePosition = None
        
    def start(this):
        pass

    def update(this):
        ## FIXME: Convert from ScreenCoords to WorldCoords.
        mousePosition = this.__input.getMousePosition()
            
        if this.__input.getMouseButtonDown(BUTTON_MIDDLE) or this.__input.getMouseButtonDown(BUTTON_RIGHT):

            # Calculate the differnce between the two positions, if possible.
            if not this.__lastFramePosition is None:
                delta = this.__lastFramePosition - mousePosition
            
                # Update the camera position.
                this.__camera.translate(delta)
            
        this.__lastFramePosition = mousePosition
