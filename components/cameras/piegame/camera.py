import pygame

## For help diagnosing any relative import issues, please see components.loggers.null.logger.
from ..camera import Camera

class PygameCamera(Camera):
    def __init__(this):
        ## Set values indicating lack of initialization.
        this.__viewer = None
        this.__renderer = None

    def initialize(this, viewer, renderer):
        this.__viewer = viewer
        this.__renderer = renderer

    def capture(this, view):
        # Get a snapshot of the view using the renderer.
        dimensions, rendering = view.render(this.__renderer)

        ## TODO: Properly handle different dimension mismatches.

        if not rendering is None:
            this.__viewer.draw(rendering, (0, 0))
            rendering = None

        dimensions = None

    def terminate(this):
        this.__viewer = None
        this.__renderer = None
