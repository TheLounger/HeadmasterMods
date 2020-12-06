init -1 python:
    import imghdr

    class FileManager():
        def __init__(self, init_files=False):
            self.__files = [ ]
            self.__images = [ ]

            if init_files:
                self.refresh_files()
                self.refresh_images()

        @property
        def all(self):
            """
            Returns the current list of known files in the game
            """

            return self.__files

        @property
        def all_images(self):
            """
            Returns the current list of known files in the game's "images" folder
            """
            return self.__images

        def get_image(self, file_name):
            """
            Tries to find an ImageInfo instance of a file with name ``file_name``
            """

            if len(self.__images) == 0:
                self.refresh_images()

            if len(self.__images) > 0 and isinstance(file_name, unicode):
                file_name = file_name.lower()
                result = list(filter(lambda i: i.file_name.lower() in file_name, self.__images))

                if len(result) > 0:
                    return result[0]

        def refresh_files(self):
            """
            Refreshes the list of all files in the game
            """

            self.__files = Util.natural_sort(renpy.list_files())

        def refresh_images(self):
            """
            Refreshes the list of all files in the game's "images" folder
            """

            self.__images = [ ]
            self.refresh_files()

            if len(self.__files) > 0:
                for i in self.__files:
                    if i.startswith("images/"):
                        self.__images.append(ImageInfo(i, len(self.__images)))

        def __str__(self):
            return "files: %d, images: %d" % (len(self.__files), len(self.__images))


    class ImageInfo():
        def __init__(self, path, image_index):
            self.__type = None

            self.file_path = path
            self.index = image_index

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
