from app import App
import assets
from components.events.mouse import *
from controllers.world import WorldController

def main():
    app = App()
    logger = app.getLogger()
    loggerName = "none" if logger is None else logger.__class__.__name__
    logger.debug("Configured logger: " + loggerName)
    viewer = app.getViewer()
    viewerName = "none" if viewer is None else viewer.__class__.__name__
    logger.debug("Configured viewer: " + viewerName)
    loader = app.getLoader()
    loaderName = "none" if loader is None else loader.__class__.__name__
    logger.debug("Configured loader: " + loaderName)
    renderer = app.getRenderer()
    rendererName = "none" if renderer is None else renderer.__class__.__name__
    logger.debug("Configured renderer: " + rendererName)
    input = app.getInput()
    inputName = "none" if input is None else input.__class__.__name__
    logger.debug("Configured input: " + inputName)

    # Load assets before using them.
    assets.loadAssets(loader, logger)

    wc = WorldController(20, 15)

    ## Create the screen if the viewer component was loaded.
    hasViewer = not viewer is None
    if hasViewer:
        viewer.initialize((640, 480))

    ## Track mouse buttons if the input component was loaded.
    hasInput = not input is None
    if hasInput:
        input.initialize([BUTTON_LEFT, BUTTON_MIDDLE, BUTTON_RIGHT])

    ## Enter and maintain the application loop.
    quitting = False
    while not quitting:
        if hasInput:
            quitting = input.refresh()

        if not quitting:
            if hasViewer:
                viewer.clear()

                ## Render the world view.
                renderedWorld = wc.getView().render(renderer)

                ## Update the viewer.
                if not renderedWorld is None:
                    ## TODO: Update the target coordinates when the rendering is larger than the viewer.
                    viewer.draw(renderedWorld, (0, 0))
                
                viewer.refresh()

    ## Clean up to shut down the application.
    if hasViewer:
        viewer.terminate()
