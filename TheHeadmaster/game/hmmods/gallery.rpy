init -1 python:
    import imghdr
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

    class ImageInfo():
        def __init__(self, path, image_index):
            self.__type = None

            self.file_path = path
            self.image_index = image_index

            # Just chop off "images/", we still want subfolders in the path
            if path.startswith("images/"):
                self.file_name = path[7:]
            else:
                self.file_name = path

        def get_image_type(self):
            """
            Tries to find the image type by reading it's file header
            """

            if self.__type is not False and not isinstance(self.__type, str):
                try:
                    with renpy.file(self.file_path) as file:
                        header = file.read(32)
                        type = imghdr.what(None, header)

                        if type is None:
                            type = Util.is_webp_header(header)

                        self.__type = type

                except Exception, e:
                    print("ImageInfo::get_image_type: (%s) %s" % (Exception, e))
                    self.__type = None

            if self.__type is None:
                self.__type = False

            return self.__type
