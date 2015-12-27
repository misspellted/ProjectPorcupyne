from models.world import WorldModel
from views.world import WorldView

class WorldController:
    def __init__(this, length = 100, height = 100):
        this.__model = WorldModel(length, height)
        this.__view = WorldView(this.__model)
        this.__model.randomizeTiles()

    def getView(this):
        return this.__view
