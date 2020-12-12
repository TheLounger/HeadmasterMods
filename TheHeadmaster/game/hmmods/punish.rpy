init -1 python:
    class Punish(UIWindow):
        characters = {
            "amy": "Amy",
            "cass": "Cassandra",
            "debbie": "Debbie",
            "rachel": "Rachel"
        }

        @property
        def name(self):
            return "punish"

        @staticmethod
        def is_game_ready():
            return "first_morning" in globals() and "update_check1" in globals() and update_check1 == True

        def start_punish(self, character):
            global first_morning

            if not Punish.is_game_ready():
                renpy.notify("Complete the intro first")
                return

            if character in Punish.characters:
                gm.windows.hide_all()
                renpy.call("call_label", "{}_punish".format(character))

            return


# Initialze punish window images
init:
    image punish_image_amy_idle = im.Scale("amy photo_d1_face.jpg", 224, 126, bilinear=True)
    image punish_image_amy_hover = im.MatrixColor(ImageReference("punish_image_amy_idle"), im.matrix.brightness(0.11))
    image punish_image_cass_idle = im.Scale("cass photo_d1_face.jpg", 224, 126, bilinear=True)
    image punish_image_cass_hover = im.MatrixColor(ImageReference("punish_image_cass_idle"), im.matrix.brightness(0.11))
    image punish_image_debbie_idle = im.Scale("debbie photo_d1_face.jpg", 224, 126, bilinear=True)
    image punish_image_debbie_hover = im.MatrixColor(ImageReference("punish_image_debbie_idle"), im.matrix.brightness(0.11))
    image punish_image_rachel_idle = im.Scale("rachel photo_d1_face.jpg", 224, 126, bilinear=True)
    image punish_image_rachel_hover = im.MatrixColor(ImageReference("punish_image_rachel_idle"), im.matrix.brightness(0.11))
