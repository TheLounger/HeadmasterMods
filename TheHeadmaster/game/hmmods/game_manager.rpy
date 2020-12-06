init -1 python:
    class GameManager(NoRollback):
        def __init__(self):
            self.__game_state = GameStateManager()
            self.__windows = WindowManager()

            self.files = [ ]
            self.images = [ ]
            self.images_filtered = [ ]

        @property
        def game_state(self):
            return self.__game_state

        @property
        def windows(self):
            return self.__windows

        def __str__(self):
            return "all_files: %d, all_images: %d, images_filtered: %d" % (len(self.files), len(self.images), len(self.images_filtered))
