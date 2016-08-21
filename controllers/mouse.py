from controllers import Controller
from components.events.mouse import BUTTON_LEFT, BUTTON_MIDDLE, BUTTON_RIGHT

class MouseController(Controller):
    def __init__(this, inputComponent, cameraComponent, worldController):
        this.__input = inputComponent
        this.__camera = cameraComponent
        this.__wc = worldController
        this.__lastFramePosition = None
        this.__hoveredTileView = None
        this.__dragDebutPosition = None

    def start(this):
        this.__worldView = this.__wc.getView()

    def update(this):
        framePosition = this.__input.getMousePosition()
        worldPosition = this.__camera.screenToWorldPosition(framePosition)

        # Update the tile hover indicator.
        if not this.__hoveredTileView is None:
            this.__hoveredTileView.clearHover()
            this.__hoveredTileView = None

        if not worldPosition is None:
            try:
                this.__hoveredTileView = this.__worldView.getTileViewAt(worldPosition[0], worldPosition[1], False)
                this.__hoveredTileView.onHover()
            except ValueError:
                pass

        # Start drag selection.
        if this.__input.getMouseButtonPressed(BUTTON_LEFT):
            this.__dragDebutPosition = this.__camera.screenToWorldPosition(framePosition)

        # End drag selection.
        if this.__input.getMouseButtonReleased(BUTTON_LEFT):
            xDebut = this.__dragDebutPosition[0]
            yDebut = this.__dragDebutPosition[1]

            dragArretPosition = this.__camera.screenToWorldPosition(framePosition)
            xArret = dragArretPosition[0]
            yArret = dragArretPosition[1]

            # Swap the x coordinates if necessary.
            if xArret < xDebut:
                xDebut, xArret = xArret, xDebut

            # Swap the y coordinates if necessary.
            if yArret < yDebut:
                yDebut, yArret = yArret, yDebut

            # Python ranges are [inclusive, exclusive).
            for x in range(xDebut, xArret + 1):
                for y in range(yDebut, yArret + 1):
                    tileView = None
                    try:
                        tileView = this.__worldView.getTileViewAt(x, y, False)
                    except ValueError:
                        pass
                    if not tileView is None:
                        tileView.onDragSelectionComplete()

        # Handle mouse dragging.
        if this.__input.getMouseButtonDown(BUTTON_MIDDLE) or this.__input.getMouseButtonDown(BUTTON_RIGHT):

            # Calculate the differnce between the two positions, if possible.
            if not this.__lastFramePosition is None:
                delta = this.__lastFramePosition - framePosition

                # Move the camera.
                this.__camera.translate(delta)

        # Get the updated frame position, in case the camera moves.
        this.__lastFramePosition = framePosition
