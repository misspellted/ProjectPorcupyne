## Import the available inputs.
from piegame.input import PygameInput

## Define the available inputs.
__inputs = dict()
__inputs["pygame"] = PygameInput()

## Provide the ability to get the names of available inputs.
def getAvailableInputNames():
    return __inputs.keys()

## Provides the ability to get an available input.
def getInput(inputName):
    input = None
    if inputName in __inputs.keys():
        input = __inputs[inputName]
    return input
