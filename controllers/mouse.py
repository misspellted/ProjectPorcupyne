import assets
from controllers import Controller
from components.events.mouse import BUTTON_LEFT, BUTTON_MIDDLE, BUTTON_RIGHT

class MouseController(Controller):
    def __init__(this, inputComponent, cameraComponent, worldController):
        # Tracks used components and controllers.
        this.__input = inputComponent
        this.__input.setMouseListener(this)
        this.__camera = cameraComponent
        this.__wc = worldController

        # Tracks mouse positions
        this.__lastFramePosition = None
        this.__currentFramePosition = None
        this.__lastWorldPosition = None
        this.__currentWorldPosition = None
        this.__dragStartPosition = None
        this.__dragPreview = assets.getImage("cursor")

        # Tracks the tile views with a drag selection preview.
        this.__tileViewsInPreview = list()

    def start(this):
        this.__worldView = this.__wc.getView()

    def __updateDragPreview(this, active):
        # Stupid events not always working.
#        if this.__dragStartPosition is None:
#            return

        # Clear previous drag area preview.
        for tileView in this.__tileViewsInPreview:
            tileView.preview(None)

        del this.__tileViewsInPreview[:]

        # Break down the positions.
        xDebut = this.__dragStartPosition[0]
        yDebut = this.__dragStartPosition[1]

        currentPosition = this.__currentWorldPosition
        xArret = currentPosition[0]
        yArret = currentPosition[1]

        # Swap the x coordinates if necessary.
        if xArret < xDebut:
            xDebut, xArret = xArret, xDebut

        # Swap the y coordinates if necessary.
        if yArret < yDebut:
            yDebut, yArret = yArret, yDebut

        # Display a preview of the drag area.
        for x in range(xDebut, xArret + 1):
            for y in range(yDebut, yArret + 1):
                tileView = None

                try:
                    tileView = this.__worldView.getTileViewAt(x, y, False)
                except ValueError:
                    pass

                if not tileView is None:
                    tileView.preview(this.__dragPreview if active else None)
                    if active:
                        this.__tileViewsInPreview.append(tileView)
                    else:
                        tileView.onDragSelectionComplete()

    def __updateCameraMovement(this):
        # Calculate the differnce between the two positions, if possible.
        if not this.__lastFramePosition is None:
            delta = this.__lastFramePosition - this.__currentFramePosition

            # Move the camera.
            this.__camera.translate(delta)

    def update(this):
        this.__currentFramePosition = this.__input.getMousePosition()
        this.__currentWorldPosition = this.__camera.screenToWorldPosition(this.__currentFramePosition)

        # Only update drag preview if there is an active one.
        if not this.__dragStartPosition is None:
            this.__updateDragPreview(True)

        # Did the player move the camera?
        if this.__input.getMouseButtonDown(BUTTON_MIDDLE) or this.__input.getMouseButtonDown(BUTTON_RIGHT):
            this.__updateCameraMovement()

        this.__lastFramePosition = this.__input.getMousePosition()
        this.__lastWorldPosition = this.__camera.screenToWorldPosition(this.__currentFramePosition)

    ## The mouse button referenced was JUST pressed.
    def onMouseButtonPressed(this, button):
        # A drag preview was started.
        if button == BUTTON_LEFT:
            # Start a new drag preview.
            this.__dragStartPosition = this.__currentWorldPosition

    ## The mouse button referenced was JUST released.
    def onMouseButtonReleased(this, button):
        # A drag preview was completed.
        if button == BUTTON_LEFT:
            # Clear the preview.
            this.__updateDragPreview(False)

            # Clear the indication a drag preview is active.
            this.__dragStartPosition = None
