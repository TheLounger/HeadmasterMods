init -1 python:
    import random

    class Gallery(UIWindow):
        @property
        def name(self):
            return "gallery"

        def __init__(self):
            self.list_page = 1
            self.first_refresh = True
            self.image = None
            self.zoom = GALLERY_DEFAULT_ZOOM
            self.position = GALLERY_DEFAULT_POSITION
            self.bg_alpha = GALLERY_DEFAULT_BG_ALPHA

        def get_default_image():
            return get_image_index(random.choice(GALLERY_DEFAULT_IMAGES))
