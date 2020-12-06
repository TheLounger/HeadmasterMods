init -1 python:
    class Punish(UIWindow):
        @property
        def name(self):
            return "punish"


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
