class Viewer:
    def initialize(this, dimensions = None):
        return NotImplemented

    def getDimensions(this):
        return NotImplemented

    def toggleFullScreen(this):
        return NotImplemented

    def clear(this):
        return NotImplemented

    def draw(this, item, coordinates):
        return NotImplemented
    
    def refresh(this):
        return NotImplemented
        
    def terminate(this):
        return NotImplemented
