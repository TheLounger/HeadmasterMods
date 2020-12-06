init -1 python:
    class GameManager(NoRollback):
        def __init__(self):
            self.__game_state = GameStateManager()
            self.__files = FileManager()
            self.__windows = WindowManager()

        @property
        def game_state(self):
            return self.__game_state

        @property
        def files(self):
            return self.__files

        @property
        def windows(self):
            return self.__windows
