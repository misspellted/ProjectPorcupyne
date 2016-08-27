from controllers import Controller
from components.events.mouse import BUTTON_LEFT, BUTTON_MIDDLE, BUTTON_RIGHT

class MouseController(Controller):
    def __init__(this, inputComponent, cameraComponent, worldController):
        # Tracks used components and controllers.
        this.__input = inputComponent
        this.__camera = cameraComponent
        this.__wc = worldController

        # Tracks mouse positions
        this.__lastFramePosition = None
        this.__currentFramePosition = None
        this.__lastWorldPosition = None
        this.__currentWorldPosition = None
        this.__dragStartPosition = None

        # TODO: Remove these.
        this.__hoveredTileView = None
        this.__dragDebutPosition = None

    def start(this):
        this.__worldView = this.__wc.getView()

    def __updateCursor(this):
        if not this.__hoveredTileView is None:
            this.__hoveredTileView.clearHover()
            this.__hoveredTileView = None

        worldPosition = this.__currentWorldPosition

        if not worldPosition is None:
            try:
                this.__hoveredTileView = this.__worldView.getTileViewAt(worldPosition[0], worldPosition[1], False)
                this.__hoveredTileView.onHover()
            except ValueError:
                pass

    def __updateDragging(this):
        # Start drag selection.
        if this.__input.getMouseButtonPressed(BUTTON_LEFT):
            this.__dragDebutPosition = this.__currentWorldPosition

        # End drag selection.
        if this.__input.getMouseButtonReleased(BUTTON_LEFT):
            xDebut = this.__dragDebutPosition[0]
            yDebut = this.__dragDebutPosition[1]

            dragArretPosition = this.__currentWorldPosition
            xArret = dragArretPosition[0]
            yArret = dragArretPosition[1]

            # Swap the x coordinates if necessary.
            if xArret < xDebut:
                xDebut, xArret = xArret, xDebut

            # Swap the y coordinates if necessary.
            if yArret < yDebut:
                yDebut, yArret = yArret, yDebut

            for x in range(xDebut, xArret + 1): # Python ranges are [inclusive, exclusive).
                for y in range(yDebut, yArret + 1):
                    tileView = None
                    try:
                        tileView = this.__worldView.getTileViewAt(x, y, False)
                    except ValueError:
                        pass
                    if not tileView is None:
                        tileView.onDragSelectionComplete()


    def __updateCameraMovement(this):
        # Handle mouse dragging.
        if this.__input.getMouseButtonDown(BUTTON_MIDDLE) or this.__input.getMouseButtonDown(BUTTON_RIGHT):

            # Calculate the differnce between the two positions, if possible.
            if not this.__lastFramePosition is None:
                delta = this.__lastFramePosition - this.__currentFramePosition

                # Move the camera.
                this.__camera.translate(delta)

    def update(this):
        this.__currentFramePosition = this.__input.getMousePosition()
        this.__currentWorldPosition = this.__camera.screenToWorldPosition(this.__currentFramePosition)

        # Update the position.
        this.__updateCursor()
        this.__updateDragging()
        this.__updateCameraMovement()

        this.__lastFramePosition = this.__input.getMousePosition()
        this.__lastWorldPosition = this.__camera.screenToWorldPosition(this.__currentFramePosition)
