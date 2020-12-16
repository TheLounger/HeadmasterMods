screen hmmods_store_items:
    tag hmmods_store_items
    zorder 19
    modal True

    default name_tt = Tooltip("")

    drag:
        drag_name features.store_items.name
        dragged gm.windows.on_drag
        xpos features.store_items.position.x
        ypos features.store_items.position.y

        frame:
            style "menu_frame"

            # Categories
            vbox spacing 14:

                for k in StoreItems.categories:
                    vbox spacing 6:
                        text k style "menu_text"

                        # Item image buttons
                        hbox spacing 4:
                            for item in StoreItems.all_items[k]:
                                if not item.is_owned:
                                    imagebutton:
                                        auto "item_image_{}_%s".format(item.name)
                                        action Function(item.set_owned, not item.is_owned)
                                        hovered name_tt.Action(item.full_name)
                                else:
                                    imagebutton:
                                        auto "item_image_{}_purchased_%s".format(item.name)
                                        action Function(item.set_owned, not item.is_owned)
                                        hovered name_tt.Action(item.full_name)

                text name_tt.value xmaximum 726
