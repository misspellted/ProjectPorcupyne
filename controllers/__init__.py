# Define the Controller interface that mimics a MonoBehavior.
class Controller:
    def start(this):
        return NotImplemented

    def update(this):
        return NotImplemented

# Track controllers.
__active = list()

def add(controller):
    added = None
    if not controller is None and isinstance(controller, Controller):
        __active.append(controller)
        added = controller
    return added

def start():
    for controller in __active:
        controller.start()

def update():
    for controller in __active:
        controller.update()
