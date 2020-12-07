init -1 python:
    # Set this to True if you want to enable developer mode. For more info,
    # see https://www.renpy.org/doc/html/config.html#var-config.developer
    config.developer = "auto"

    # All the keybinds that can be used in the mod.
    # See http://www.pygame.org/docs/ref/key.html for all possible keys
    # To disable a bind, just comment the line out
    KEY_BINDS = {
        "cheat_decrease_ap": [ "K_MINUS" ],
        "cheat_increase_ap": [ "K_EQUALS" ],

        "toggle_gallery_window": [ "K_g" ],
        "toggle_punish_window": [ "K_c" ],

        "gallery_prev_image": [ "K_KP1" ],
        "gallery_next_image": [ "K_KP3" ],
        "gallery_zoom_out": [ "K_KP7" ],
        "gallery_zoom_in": [ "K_KP9" ],
        "gallery_zoom_reset": [ "K_KP_DIVIDE" ],

        "gallery_move_left": [ "K_KP4" ],
        "gallery_move_right": [ "K_KP6" ],
        "gallery_move_up": [ "K_KP8" ],
        "gallery_move_down": [ "K_KP2" ],
        "gallery_move_reset": [ "K_KP5" ]
    }

    # Default values/settings
    DEFAULT_WINDOW_POSITION =  { "x": 145, "y": 84 }
    GALLERY_DEFAULT_ZOOM = 1.0
    GALLERY_DEFAULT_POSITION = { "x": 0.5, "y": 0.5 }
    GALLERY_DEFAULT_BG_ALPHA = 0.85
    GALLERY_DEFAULT_IMAGES = [
        "amy post_punish", "amy run13.jpg", "amy spank1.png", "bg os2.jpg", "board sue_manic1.jpg", "cass faye_hall2.jpg",
        "cass smug.png", "cass spy_smile18.jpg", "cds 7.jpg", "charles pervy.jpg", "charlotte happy.jpg",
        "claire door_pj4.jpg", "claire faye11.jpg", "dance l1.jpg", "debbie behaving8.jpg", "debbie dismissive.png",
        "dnd judge5.jpg", "donna drama3.jpg", "dyl liz4.jpg",
        "promo.jpg"
    ]

    # If True, will move gallery image from the player's POV (i.e.: 'down' moves image up)
    # Otherwise, will move the image in the selected direction
    GALLERY_TRANSFORM_NATURAL = False

    # How many items should be displayed at once on the gallery browser
    GALLERY_PAGE_ITEMS = 20
