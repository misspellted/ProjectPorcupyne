from controllers import Controller
from models.world import WorldModel
import time
from views.world import WorldView

class WorldController(Controller):
    def __init__(this, length = 100, height = 100):
        this.__length = length
        this.__height = height

    def start(this):
        # Create the model of the world.
        this.__model = WorldModel(this.__length, this.__height)

        # Create the view of the world.
        this.__view = WorldView(this.__model)

        # Perform the first tile randomization (keep things interesting on-screen).
        this.__model.randomizeTiles()

        # Set the first time for the 2-second tile randomizer.
        this.__debut = time.time()

    def update(this):
        now = time.time()

        # Randomize the tiles every 2 seconds.
        if 2.0 <= now - this.__debut:
            this.__debut = now
            this.__model.randomizeTiles()

    def getView(this):
        return this.__view
