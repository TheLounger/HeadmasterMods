init python:
    class GameStateManager():
        def __init__(self):
            self.__current_label = None
            self.__day = None
            self.__weekday = None
            self.__daytime = None

        @property
        def current_label(self):
            return self.__current_label

        @property
        def day(self):
            return self.__day

        @property
        def weekday(self):
            return self.__weekday

        @property
        def daytime(self):
            return self.__daytime

        # Returns a label name to enter the default scene (premap), built from the current game state
        def get_current_premap_label(self):
            return "%s_%s_premap" % (self.__weekday, self.__daytime)

        @staticmethod
        def is_game_ready(intro_completed=False, notify_unready=False):
            """
            Checks if we're not in a menu, and if some basic variables have been set,
            and thus the "start" has been executed
            """

            ready = True
            message = "Game isn't ready"

            # Check if we're in the main menu
            if main_menu:
                ready = False

            try:
                # Check if we're in any menu
                if renpy.context()._menu:
                    ready = False

                # Check if required globals have been set
                for v in [ "day", "weekday", "morning", "afternoon", "evening" ]:
                    if not v in globals():
                        ready = False

                # Check if globals that indicate that the intro has been completed have been set
                if intro_completed:
                    if not "first_morning" in globals() or not "update_check1" in globals() or update_check1 != True:
                        message = "Complete the intro first"
                        ready = False

            except Exception, e:
                print("GameStateManager::is_game_ready: (%s) %s" % (Exception, e))
                ready = False

            if notify_unready and not ready:
                renpy.notify(message)

            return ready

        def label_callback(self, current_label_name, abnormal):
            """
            Stores the state of the game every time a label is entered
            """

            self.__current_label = current_label_name

            if GameStateManager.is_game_ready():
                self.__day = day
                self.__weekday = weekday.lower()

                if morning:
                    self.__daytime = "morning"
                elif afternoon:
                    self.__daytime = "afternoon"
                else:
                    self.__daytime = "evening"

        def __str__(self):
            return "current_label: %s, day: %s, weekday: %d, daytime: %s" % (self.__current_label, self.__day, self.__weekday, self.__daytime)
