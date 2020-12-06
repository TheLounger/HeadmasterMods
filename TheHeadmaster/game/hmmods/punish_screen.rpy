screen hmmods_punish:
    tag hmmods_punish
    zorder 19
    modal True

    drag:
        drag_name "punish"
        dragged gm.windows.on_drag

        frame:
            style "menu_frame"

            # Character image buttons
            hbox spacing 14:

                vbox spacing 6:

                    text "Amy" style "menu_text"
                    imagebutton:
                        auto "punish_image_amy_%s"
                        action [ Function(gm.windows.hide_all), Call("call_label", "amy_punish") ]

                    text "Cassandra" style "menu_text"
                    imagebutton:
                        auto "punish_image_cass_%s"
                        action [ Function(gm.windows.hide_all), Call("call_label", "cass_punish") ]

                vbox spacing 6:

                    text "Debbie" style "menu_text"
                    imagebutton:
                        auto "punish_image_debbie_%s"
                        action [ Function(gm.windows.hide_all), Call("call_label", "debbie_punish") ]

                    text "Rachel" style "menu_text"
                    imagebutton:
                        auto "punish_image_rachel_%s"
                        action [ Function(gm.windows.hide_all), Call("call_label", "rachel_punish") ]
