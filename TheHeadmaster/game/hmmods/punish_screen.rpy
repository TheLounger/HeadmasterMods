screen hmmods_punish:
    tag hmmods_punish
    zorder 19
    modal True

    drag:
        drag_name "punish"
        dragged gm.windows.on_drag
        xpos features.punish.position.x
        ypos features.punish.position.y

        frame:
            style "menu_frame"

            # Character image buttons
            vbox spacing 14:
                default keys = sorted(Punish.characters.keys())
                default count = len(keys)

                # Create rows of buttons
                for i in range(0, count, 2):
                    hbox spacing 14:

                        # Max two buttons per row
                        for j in range(0, min(count - i, 2)):
                            vbox spacing 6:

                                text Punish.characters[keys[i + j]] style "menu_text"
                                imagebutton:
                                    auto "punish_image_{}_%s".format(keys[i + j])
                                    action Function(features.punish.start_punish, keys[i + j])
