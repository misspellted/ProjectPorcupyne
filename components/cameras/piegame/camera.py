import math
import pygame
from components.geometry.vectors import Vector2

# For help diagnosing any relative import issues, please see components.loggers.null.logger.
from ..camera import Camera

class PygameCamera(Camera):
    def __init__(this):
        # Set values indicating lack of initialization.
        this.__viewer = None
        this.__renderer = None
        this.__position = Vector2()

    def initialize(this, viewer, renderer):
        this.__viewer = viewer
        this.__renderer = renderer

    def capture(this, view):
        # Get a snapshot of the view using the renderer.
        dimensions, rendering = view.render(this.__renderer)

        ## TODO: Properly handle different dimension mismatches.

        if not rendering is None:
            # Create a padded rendering (rendering surrounded by padding relative to camera dimensions).
            vwr = this.__viewer.getDimensions()

            ## FIXME: Assume that any dimension tuples are not None.
            rl, rh = dimensions
            vl, vh = vwr

            # Create the padded rendering.
            padded = this.__renderer.createRenderTarget(rl + vl, rh + vh, (0, 0, 0, 0))

            # Calculate the start position of the rendering in the padded rendering.
            rsx, rsy = int(math.floor(vl / 2.0)), int(math.floor(vh / 2.0))

            # Copy the rendering into the padded rendering.
            this.__renderer.renderItemTo(padded, rendering, (rsx, rsy))

            # Delete the rendering (not needed anymore, since now in padded rendering).
            rendering = None

            # Clamp the camera position.
            if rl < this.__position[0]:
                this.__position[0] = rl
            if rh < this.__position[1]:
                this.__position[1] = rh

            # Convert the Vector2 into a tuple.
            position = (this.__position[0], this.__position[1])

            # Get the region that should be displayed to the viewer.
            viewable = this.__renderer.copyRegionFrom(padded, position, vwr)

            # Delete the padded region (not needed anymore, since the viewable region is captured).
            padded = None

            # Draw the viewable region to the viewer. 
            this.__viewer.draw(viewable, (0, 0))

            # Delete the viewable region (not needed anymore, since now in viewer).
            viewable = None

        dimensions = None

    def translate(this, delta):
        newPosition = this.__position + delta
        if newPosition[0] < 0:
            newPosition[0] = 0
        if newPosition[1] < 0:
            newPosition[1] = 0
        this.__position = newPosition
        newPosition = None

    def terminate(this):
        this.__viewer = None
        this.__renderer = None
        this.__position = None
