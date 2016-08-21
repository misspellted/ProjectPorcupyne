import pygame
from components.geometry.vectors import Vector2

## For help diagnosing any relative import issues, please see components.loggers.null.logger.
from components.inputs import Input
from ...events.mouse import *

class PygameInput(Input):
    def __init__(this):
        ## Track the last mouse event to occur per button.
        this.__buttons = dict()
        this.__position = None

    def initialize(this, buttonList):
        ## Start off all mouse buttons in the Up state.
        for button in buttonList:
            this.__buttons[button] = MouseButtonUp()

    def __getAgnosticButton(this, mouseEvent):
        button = None
        if mouseEvent.button == 1:
            button = BUTTON_LEFT
        elif mouseEvent.button == 2:
            button = BUTTON_MIDDLE
        elif mouseEvent.button == 3:
            button = BUTTON_RIGHT
        return button

    def __setPosition(this, position):
        this.__position = Vector2()
        x, y = position
        this.__position[0] = x
        this.__position[1] = y

    def refresh(this):
        quitting = False

        for event in pygame.event.get():
            quitting = event.type == pygame.QUIT

            if not quitting:
                ## Was a mouse button just pressed?
                if event.type == pygame.MOUSEBUTTONDOWN:
                    this.__setPosition(event.pos)

                    button = this.__getAgnosticButton(event)

                    if not button is None:
                        this.__buttons[button] = MouseButtonPressed()

                ## Was a mouse button just released?
                elif event.type == pygame.MOUSEBUTTONUP:
                    this.__setPosition(event.pos)

                    button = this.__getAgnosticButton(event)

                    if not button is None:
                        this.__buttons[button] = MouseButtonReleased()

                ## What is the state of the buttons when the mouse moved?
                elif event.type == pygame.MOUSEMOTION:
                    this.__setPosition(event.pos)

                    ## event.buttons is a tuple of (left, middle, right).
                    left, middle, right = event.buttons

                    this.__buttons[BUTTON_LEFT] = MouseButtonDown() if left == 1 else MouseButtonUp()
                    this.__buttons[BUTTON_MIDDLE] = MouseButtonDown() if middle == 1 else MouseButtonUp()
                    this.__buttons[BUTTON_RIGHT] = MouseButtonDown() if right == 1 else MouseButtonUp()
        
        return quitting

    def getMouseButtonPressed(this, button):
        pressed = False
        event = this.__buttons[button]
        if not event is None:
            pressed = isinstance(event, MouseButtonPressed)
        return pressed
    
    def getMouseButtonDown(this, button):
        down = False
        event = this.__buttons[button]
        if not event is None:
            down = isinstance(event, MouseButtonDown)
        return down

    def getMouseButtonReleased(this, button):
        released = False
        event = this.__buttons[button]
        if not event is None:
            released = isinstance(event, MouseButtonReleased)
        return released

    def getMousePosition(this):
        return this.__position
