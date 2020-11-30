# custom_cheat_menu
# Version: 0.2
# Author: Lounger
# Game: The Headmaster v0.8.2.1public-pc
# Description:
#   Adds a menu that allows you to start a punishment game
#   at all times, without advancing the day. Also adds keybinds
#   for modifying Action Points required for punishments.


### Configuration ################################################################

# See http://www.pygame.org/docs/ref/key.html for all possible keys
define KEY_BINDS = {
    "cheat_decrease_ap": [ "K_MINUS", "K_KP_MINUS" ],
    "cheat_increase_ap": [ "K_EQUALS", "K_KP_PLUS" ],
    "show_cheat_menu": [ "K_c" ]
}

define MENU_SCREEN_NAME = "custom_cheat_menu"


### Base initialization and helper functions #####################################

init -1 python hide:
    # Set this to True if you want to enable developer mode
    config.developer = False

init 10 python:
    ### Init ############################

    game_state = { }
    game_state.current_label = None
    game_state.ready = False
    game_state.day = None
    game_state.weekday = None
    game_state.daytime = None

    cheat_menu_showing = False
    punish_character = None
    return_to_label = None

    ### Functions #######################

    # Checks if some basic variables have been set, and thus "label start:" has been ran
    def is_game_ready():
        if main_menu:
            return False
        try:
            if renpy.context()._menu:
                return False
            for v in [ "day", "weekday", "morning", "afternoon", "evening" ]:
                if not v in globals():
                    return False
            return True
        except Exception, e:
            print("is_game_ready(): (%s) %s" % (Exception, e))
            return False

    # Stores the state of the game every time a label is entered
    def label_callback(current_label_name, abnormal):
        game_state.current_label = current_label_name
        if is_game_ready():
            game_state.ready = True
            game_state.day = day
            game_state.weekday = weekday.lower()
            if morning:
                game_state.daytime = "morning"
            elif afternoon:
                game_state.daytime = "afternoon"
            else:
                game_state.daytime = "evening"

    # Shows or hides the cheat menu
    def show_menu(show_menu=True):
        global cheat_menu_showing
        if show_menu and not cheat_menu_showing:
            renpy.show_screen(MENU_SCREEN_NAME)
        elif not show_menu and cheat_menu_showing:
            renpy.hide_screen(MENU_SCREEN_NAME)
        cheat_menu_showing = show_menu

    # Toggles showing the cheat menu, if the game is in the right state
    def toggle_menu():
        if is_game_ready():
            show_menu(not cheat_menu_showing)

    # Returns a label name to enter the default scene (premap), built from the current game state
    def get_current_premap_label():
        return "%s_%s_premap" % (game_state.weekday, game_state.daytime)

    # Increases/decreases Action Points (a.k.a. Actions Remaining)
    def mod_action_points(modifier):
        set_action_points(ar + modifier)

    # Sets the Action Points
    def set_action_points(points):
        global ar
        ar = max(0, points)

    ### Setup config ####################

    # Sets what is called every time a label is entered
    config.label_callback = label_callback

    # Create keymaps. These define the actions to be performed when a keybind is pressed
    config.underlay.append(renpy.Keymap(cheat_decrease_ap = Function(mod_action_points, -1)))
    config.underlay.append(renpy.Keymap(cheat_increase_ap = Function(mod_action_points, 1)))
    config.underlay.append(renpy.Keymap(show_cheat_menu = Function(toggle_menu)))

    # Bind the specified keys to the previously create keymaps
    for k, v in KEY_BINDS.items():
        config.keymap[k] = v


### Helper statements ############################################################

# Prepares for and starts a punishment game, then jumps to the default scene
# of the current game state, and thus not advancing the time of day
label pre_punish:

    # Store the map screen label name of the current day and daytime
    $ return_to_label = get_current_premap_label()

    # Hide all screens
    call screen_hider
    $ show_menu(False)

    stop music

    # Start punishment game for the specified character
    $ renpy.call("%s_punish" % punish_character)

    # Reset and jump to the default scene 
    $ punish_character = None
    $ renpy.jump(return_to_label)


### Screens and styles ###########################################################

init:
    image punish_image_amy_idle = im.Scale("amy photo_d1_face.jpg", 224, 126, bilinear=True)
    image punish_image_amy_hover = im.MatrixColor(ImageReference("punish_image_amy_idle"), im.matrix.brightness(0.11))

    image punish_image_cass_idle = im.Scale("cass photo_d1_face.jpg", 224, 126, bilinear=True)
    image punish_image_cass_hover = im.MatrixColor(ImageReference("punish_image_cass_idle"), im.matrix.brightness(0.11))

    image punish_image_debbie_idle = im.Scale("debbie photo_d1_face.jpg", 224, 126, bilinear=True)
    image punish_image_debbie_hover = im.MatrixColor(ImageReference("punish_image_debbie_idle"), im.matrix.brightness(0.11))

    image punish_image_rachel_idle = im.Scale("rachel photo_d1_face.jpg", 224, 126, bilinear=True)
    image punish_image_rachel_hover = im.MatrixColor(ImageReference("punish_image_rachel_idle"), im.matrix.brightness(0.11))

style cheat_menu_frame:
    xanchor 0.0
    yanchor 0.0
    xpadding 22
    ypadding 22
    xpos 145
    ypos 84
    background "#212121DD"

style cheat_menu_header_text is text:
    font "CinzelDecorative-Bold.ttf"
    color gui.hover_color
    size 26

style cheat_menu_text is text:
    font "CinzelDecorative-Regular.ttf"
    size 19

style cheat_menu_button_text is text:
    font "CinzelDecorative-Regular.ttf"
    hover_color gui.hover_color
    size 19

screen custom_cheat_menu:
    tag custom_cheat_menu
    zorder 20
    modal True

    frame:
        style "cheat_menu_frame"
        vbox:
            spacing 14
            text _("Punish") style "cheat_menu_header_text"

            hbox:
                spacing 20
                vbox:
                    text "Amy" style "cheat_menu_text"
                    imagebutton:
                        auto "punish_image_amy_%s"
                        action [ SetVariable("punish_character", "amy"), Jump("pre_punish") ]
                vbox:
                    text "Cassandra" style "cheat_menu_text"
                    imagebutton:
                        auto "punish_image_cass_%s"
                        action [ SetVariable("punish_character", "cass"), Jump("pre_punish") ]
            hbox:
                spacing 20
                vbox:
                    text "Debbie" style "cheat_menu_text"
                    imagebutton:
                        auto "punish_image_debbie_%s"
                        action [ SetVariable("punish_character", "debbie"), Jump("pre_punish") ]
                vbox:
                    text "Rachel" style "cheat_menu_text"
                    imagebutton:
                        auto "punish_image_rachel_%s"
                        action [ SetVariable("punish_character", "rachel"), Jump("pre_punish") ]
