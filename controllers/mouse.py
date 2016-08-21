from controllers import Controller
from components.events.mouse import BUTTON_LEFT, BUTTON_MIDDLE, BUTTON_RIGHT

class MouseController(Controller):
    def __init__(this, inputComponent, cameraComponent, worldController):
        this.__input = inputComponent
        this.__camera = cameraComponent
        this.__wc = worldController
        this.__lastFramePosition = None
        this.__hoveredTileView = None

    def start(this):
        this.__worldView = this.__wc.getView()

    def update(this):
        framePosition = this.__input.getMousePosition()
        worldPosition = this.__camera.screenToWorldPosition(framePosition)

        # Clear the tile hover indicator if there was one.
        if not this.__hoveredTileView is None:
            this.__hoveredTileView.clearHover()
            this.__hoveredTileView = None

        # Set the new tile hover indicator if there is one.
        if not worldPosition is None:
            try:
                this.__hoveredTileView = this.__worldView.getTileViewAt(worldPosition[0], worldPosition[1], False)
                this.__hoveredTileView.onHover()
            except ValueError:
                pass

        # Handle mouse dragging.
        if this.__input.getMouseButtonDown(BUTTON_MIDDLE) or this.__input.getMouseButtonDown(BUTTON_RIGHT):

            # Calculate the differnce between the two positions, if possible.
            if not this.__lastFramePosition is None:
                delta = this.__lastFramePosition - framePosition

                # Move the camera.
                this.__camera.translate(delta)

        # Get the updated frame position, in case the camera moves.
        this.__lastFramePosition = framePosition
