init -1 python:
    import random

    class Gallery(UIWindow):
        @property
        def name(self):
            return "gallery"

        def __init__(self):
            super(Gallery, self).__init__()
            self.list_page = 1
            self.first_refresh = True
            self.image = None
            self.image_zoom = GALLERY_DEFAULT_ZOOM
            self.image_position = GALLERY_DEFAULT_POSITION
            self.bg_alpha = GALLERY_DEFAULT_BG_ALPHA
            self.show_browser = True

        def get_default_image(self):
            return gm.files.get_image(random.choice(GALLERY_DEFAULT_IMAGES))

        def get_list_page_count(self):
            count = len(gm.files.all_images)
            mod = count % GALLERY_PAGE_ITEMS
            remain = 1 if mod > 0 else 0
            return (count - mod) / GALLERY_PAGE_ITEMS + remain

        def get_list_page_for_image(self, image_index):
            return (image_index - image_index % GALLERY_PAGE_ITEMS) /  GALLERY_PAGE_ITEMS + 1

        def get_list_range(self):
            start_offset = (self.list_page - 1) * GALLERY_PAGE_ITEMS
            max_range = min(len(gm.files.all_images) - start_offset, GALLERY_PAGE_ITEMS)
            return range(start_offset, start_offset + max_range)

        def set_image(self, image_index=None):
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
                            self.image = gm.files.all_images[image_index]
                            image_page = self.get_list_page_for_image(image_index)
                            if self.list_page is not image_page:
                                self.set_list_page(image_page)
                            return

            self.image = None

        def set_list_prev_page(self):
            self.set_list_page(self.list_page - 1)

        def set_list_next_page(self):
            self.set_list_page(self.list_page + 1)

        def set_list_page(self, page=1):
            last = self.get_list_page_count()
            if page > last:
                page = 1
            elif page < 1:
                page = last
            self.list_page = max(1, min(last, page))

        def show_initial_image(self):
            if self.first_refresh:
                img = self.get_default_image();
                if img:
                    self.set_image(img.index)
                self.first_refresh = False
