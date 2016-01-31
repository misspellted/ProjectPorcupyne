from controller import Controller
from components.events.mouse import BUTTON_LEFT, BUTTON_MIDDLE, BUTTON_RIGHT

class MouseController(Controller):
    def __init__(this, inputComponent, cameraComponent, uiView):
        this.__input = inputComponent
        this.__camera = cameraComponent
        this.__ui = uiView
        this.__lastFramePosition = None
        
    def start(this):
        pass

    def update(this):
        ## FIXME: Convert from ScreenCoords to WorldCoords.
        mousePosition = this.__input.getMousePosition()

        # Update the circle cursor position.
        this.__ui.setCursorPosition(mousePosition)

        # Handle mouse dragging.
        if this.__input.getMouseButtonDown(BUTTON_MIDDLE) or this.__input.getMouseButtonDown(BUTTON_RIGHT):

            # Calculate the differnce between the two positions, if possible.
            if not this.__lastFramePosition is None:
                delta = this.__lastFramePosition - mousePosition
            
                # Move the camera.
                this.__camera.translate(delta)

        ## FIXME: Get the updated frame position, in case the camera moves.
        this.__lastFramePosition = mousePosition
