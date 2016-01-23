from app import App
import assets
from components.events.mouse import *
import controllers
from controllers.mouse import MouseController
from controllers.world import WorldController

class Porcuthon(App):
    def hasRequiredComponents(this):
        available = not this.getViewer() is None
        available &= not this.getLoader() is None
        available &= not this.getRenderer() is None
        available &= not this.getCamera() is None
        available &= not this.getInput() is None
        return available

    def onRequiredComponentsAvailable(this):
        # Load assets before using them, logging the loading for debugging if necessary.
        assets.loadAssets(this.getLoader(), this.getLogger())

        # Define the final viewer pixel dimensions.
        viewer = this.getViewer()
        viewer.initialize((640, 480))

        # Attach the camera to the viewer, and also provide a renderer for displayed snapshots.
        this.getCamera().initialize(viewer, this.getRenderer())

        # Track the 3 main mouse buttons (no exotic MMORPG setups please).
        this.getInput().initialize([BUTTON_LEFT, BUTTON_MIDDLE, BUTTON_RIGHT])

        # Indicate that the game is ready to enter the main game loop.
        this.__ready = True

    def onRequiredComponentsNotAvailable(this):
        this.__ready = False

    def isReady(this):
        return this.__ready

    def play(this):
        if not this.__ready:
            logger = this.getLogger()
            if not logger is None:
                logger.debug("The required components are not available, and thus the game was not ready for playing.")
        else:        
            # Get the components used in the game loop.
            viewer = this.getViewer()
            camera = this.getCamera()
            input = this.getInput()

            # Add the world controller, caching the WorldView object.
            wc = controllers.add(WorldController(20, 15))
            mc = controllers.add(MouseController(input, camera))
            
            # Start up the controllers.
            controllers.start()
            
            # Grab a ref to the world view.
            wv = wc.getView()
            
            # Enter and maintain the game loop.
            quitting = False
            while not quitting:
                quitting = input.refresh()

                if not quitting:
                    # Update the controllers.
                    controllers.update()

                    # Clear the viewer.
                    viewer.clear()

                    # Update the viewer on what the camera sees.
                    camera.capture(wv)

                    # Refresh the viewer.
                    viewer.refresh()
                    
        # Clean up to shut down the game.
        this.getCamera().terminate()
        this.getViewer().terminate()

def main():
    Porcuthon().play()
        
