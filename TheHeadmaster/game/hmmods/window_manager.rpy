init -1 python:
    class WindowManager():
        def __init__(self):
            self.__windows = [ ]

        @property
        def all(self):
            return self.__windows.copy()

        def add(self, win):
            if win and not self.get(win.name):
                self.__windows.append(win)
                return True
            return False

        def get(self, name):
            result = list(filter(lambda win: win.name == name, self.__windows))
            if len(result) > 0:
                return result[0]

        def hide(self, name):
            win = self.get(name)
            if win:
                win.hide()

        def hide_all(self):
            for i in self.__windows:
                i.hide()

        def on_drag(self, drags, drop):
            # if not drop:
            #     return
            win = self.get(drags[0].drag_name)
            if win:
                win.position.x = drags[0].x
                win.position.y = drags[0].y

        def remove(self, name):
            win = self.get(name)
            if win:
                self.__windows.remove(win)
                return True
            return False

        def show(self, name):
            if gm.game_state.is_game_ready():
                win = self.get(name)
                if win:
                    win.show()

        def show_all(self):
            if gm.game_state.is_game_ready():
                for i in self.__windows:
                    i.show()

        def toggle(self, name):
            if gm.game_state.is_game_ready():
                win = self.get(name)
                if win:
                    if renpy.get_screen(win.screen_name):
                        win.hide()
                    else:
                        win.show()
