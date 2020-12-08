init -2 python:
    class Vector2():
        def __init__(self, x=0, y=0):
            self.x = x
            self.y = y

        def copy(self):
            return Vector2(self.x, self.y)

        @staticmethod
        def half():
            return Vector2(0.5, 0.5)

        @staticmethod
        def one():
            return Vector2(1, 1)

        @staticmethod
        def zero():
            return Vector2(0, 0)
