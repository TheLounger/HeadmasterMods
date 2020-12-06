init -2 python:
    from abc import ABCMeta, abstractmethod, abstractproperty

    SCREEN_NAME_PREFIX = "hmmods_"

    class UIWindow():
        __metaclass__ = ABCMeta

        def __init__(self):
            self.position = { }
            self.position.x = DEFAULT_WINDOW_POSITION["x"]
            self.position.y = DEFAULT_WINDOW_POSITION["y"]

        @abstractproperty
        def name(self):
            pass

        @property
        def screen_name(self):
            return SCREEN_NAME_PREFIX + self.name

        # @abstractmethod
        def hide(self):
            renpy.hide_screen(self.screen_name)

        # @abstractmethod
        def show(self):
            renpy.show_screen(self.screen_name)
