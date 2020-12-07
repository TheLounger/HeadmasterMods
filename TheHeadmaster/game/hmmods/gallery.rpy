init -1 python:
    import random

    class Gallery(UIWindow):
        def __init__(self):
            super(Gallery, self).__init__()

            self.__image = None
            self.__image_zoom = GALLERY_DEFAULT_ZOOM
            self.__image_position = GALLERY_DEFAULT_POSITION.copy()

            self.list_page = 1
            self.first_refresh = True
            self.bg_alpha = GALLERY_DEFAULT_BG_ALPHA
            self.show_browser = True

        @property
        def name(self):
            return "gallery"

        @property
        def showing_image(self):
            return self.showing and self.__image is not None

        @property
        def image(self):
            return self.__image

        @property
        def image_zoom(self):
            return self.__image_zoom

        @property
        def image_position(self):
            return self.__image_position

        def get_default_image(self):
            return gm.files.get_image(random.choice(GALLERY_DEFAULT_IMAGES))

        def show_initial_image(self):
            if self.first_refresh:
                img = self.get_default_image();
                if img:
                    self.set_image(img.index)
                self.first_refresh = False

        def set_list_page(self, page=1):
            last = self.get_list_page_count()
            if page > last:
                page = 1
            elif page < 1:
                page = last
            self.list_page = max(1, min(last, page))

        def set_list_prev_page(self):
            self.set_list_page(self.list_page - 1)

        def set_list_next_page(self):
            self.set_list_page(self.list_page + 1)

        def get_list_page_count(self):
            count = len(gm.files.all_images)
            mod = count % GALLERY_PAGE_ITEMS
            remain = 1 if mod > 0 else 0
            return (count - mod) / GALLERY_PAGE_ITEMS + remain

        def get_list_range(self):
            start_offset = (self.list_page - 1) * GALLERY_PAGE_ITEMS
            max_range = min(len(gm.files.all_images) - start_offset, GALLERY_PAGE_ITEMS)
            return range(start_offset, start_offset + max_range)

        def get_list_page_for_image(self, image_index):
            return (image_index - image_index % GALLERY_PAGE_ITEMS) /  GALLERY_PAGE_ITEMS + 1

        def set_image(self, image_index=None):
            """
            Sets the main image by file index
            """
            if image_index is not None:
                count = len(gm.files.all_images)

                if count == 0:
                    gm.files.refresh_images()
                    count = len(gm.files.all_images)

                if count > 0:
                    if image_index < 0:
                        image_index = count - 1
                    elif image_index >= count:
                        image_index = 0

                    file = gm.files.all_images[image_index].file_path

                    if file is None:
                        renpy.notify(_("Invalid image file"))
                    else:
                        if not renpy.loadable(file):
                            renpy.notify(_("Unable to load image: %s" % file))
                            return
                        else:
                            self.__image = gm.files.all_images[image_index]
                            image_page = self.get_list_page_for_image(image_index)
                            if self.list_page is not image_page:
                                self.set_list_page(image_page)
                            return

            self.__image = None

        def cycle_image(self, offset=0):
            """
            Sets the main image based on an offset in the file list
            """
            if self.showing:
                index = 0
                if self.__image is not None:
                    index = self.__image.index + offset
                elif self.first_refresh:
                    img = self.get_default_image()
                    if img:
                        index = img.index
                    self.first_refresh = False
                self.set_image(image_index=index)

        def set_image_zoom(self, zoom=1.0):
            """
            Sets the main image's zoom
            """
            if self.showing:
                self.__image_zoom = min(2.0, max(0.05, zoom))

        def modify_image_zoom(self, modifier=0.0):
            """
            Increases/decreases the main image's zoom
            """
            self.set_image_zoom(self.__image_zoom + modifier)

        def set_image_pos(self, x=None, y=None):
            """
            Sets the main image's position
            """
            if self.showing_image:
                pos = GALLERY_DEFAULT_POSITION.copy()

                if x is not None:
                    pos["x"] = x
                if y is not None:
                    pos["y"] = y

                self.__image_position["x"] = round(pos["x"], 2)
                self.__image_position["y"] = round(pos["y"], 2)

        def modify_image_pos(self, modifier=0.0, axis="x"):
            """
            Modifies the main image's position
            """
            if GALLERY_TRANSFORM_NATURAL:
                modifier = -modifier

            pos = self.__image_position.copy()
            pos[axis] = round(pos[axis] + modifier, 2)
            self.set_image_pos(pos["x"], pos["y"])
