screen hmmods_gallery:
    tag hmmods_gallery
    zorder 19
    modal True

    # Background
    add "#000000":
        alpha features.gallery.bg_alpha

    # Main image
    if features.gallery.image is None:
        text _("No image selected") at gallery_image_transform:
            xalign 0.5
            yalign 0.5
    else:
        add "[features.gallery.image.file_path]" at gallery_image_transform:
            xpos features.gallery.image_position["x"]
            ypos features.gallery.image_position["y"]
            zoom features.gallery.image_zoom

    # Image file browser
    if features.gallery.show_browser:
        drag:
            drag_name "gallery"
            dragged gm.windows.on_drag
            xpos features.gallery.position.x
            ypos features.gallery.position.y

            frame:
                style "menu_frame"

                vbox spacing 8:

                    textbutton _("Refresh file list"):
                        style "menu_button"
                        text_style "menu_button_text"
                        action [
                            Function(gm.files.refresh_images),
                            Function(features.gallery.show_initial_image)
                        ]

                    $ image_count = len(gm.files.all_images)

                    text _("Image count: {b}[image_count]{/b}") style "menu_text_small"

                    if image_count > 0:
                        vbox spacing 8:

                            # Pagination
                            hbox spacing 14:

                                imagebutton:
                                    auto "minus_mini_%s"
                                    action Function(features.gallery.set_list_prev_page)

                                imagebutton:
                                    auto "plus_mini_%s"
                                    action Function(features.gallery.set_list_next_page)

                                textbutton "{b}Page: %d / %d{/b}" % (features.gallery.list_page, features.gallery.get_list_page_count()):
                                    style "menu_button"
                                    text_style "menu_button_text"
                                    action Function(features.gallery.set_list_page, 1)

                                null height 30

                            # File list
                            vbox spacing 0:

                                for i in features.gallery.get_list_range():

                                    if features.gallery.image and i == features.gallery.image.index:
                                        textbutton "{}: {}".format(i + 1, features.gallery.image.file_name):
                                            style "menu_button"
                                            text_style "menu_button_text_tiny_selected"
                                            action NullAction()
                                    else:
                                        textbutton "{}: {}".format(i + 1, gm.files.all_images[i].file_name):
                                            style "menu_button"
                                            text_style "menu_button_text_tiny"
                                            # action NullAction() #Function(show_gallery, image_index=i)
                                            # action SetVariable("features.gallery.image", gm.files.all_images[i])
                                            action Function(features.gallery.set_image, i)
