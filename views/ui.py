import assets
from components.geometry.vectors import Vector2
import math

class UiView:
    def __init__(this, viewerComponent):
        this.__cursor = assets.getImage("cursor")
        this.__cursorDims = this.__cursor.get_size()
        this.__cursorPosition = Vector2()
        this.__viewer = viewerComponent

    def setCursorPosition(this, position):
        ## FIXME: No parameter validation performed.
        if not position is None:
            this.__cursorPosition = position

    def draw(this):
        # Convert the Vector2 into a tuple.
        cx, cy = this.__cursorPosition[0], this.__cursorPosition[1]

        # Adjust for the size of the cursor to center on the actual mouse cursor.
        cl, ch = this.__cursorDims
        position = (cx - int(math.floor(cl / 2.0)), cy - int(math.floor(ch / 2.0)))

        # Draw the cursor at the specified position.
        this.__viewer.draw(this.__cursor, position)
