# hmmods_menu
# Version: 0.2.2
# Author: Lounger
# Game: The Headmaster v0.8.2.1public-pc
# Description:
#   Adds a menu that allows you to start a punishment game at all times,
#   without advancing the day. Also adds keybinds for modifying
#   Action Points required for punishments.
# WARNING:
#   Using anything in this menu while you haven't finished the game will LIKELY
#   skip certain scenes for you. For example, this mod will force you into the
#   punishment games, in a standard game-mode (not a replay). This means that you
#   can advance a character's level and potentially skip story elements.
#   Always back up your save games! You have been warned.


### Configuration ################################################################

# See http://www.pygame.org/docs/ref/key.html for all possible keys
define KEY_BINDS = {
    "cheat_decrease_ap": [ "K_MINUS" ],
    "cheat_increase_ap": [ "K_EQUALS" ],

    "toggle_mod_menu": [ "K_c" ]
}

define MENU_SCREEN_NAME = "hmmods_menu"


### Base initialization and helper functions #####################################

init -1 python:
    # Set this to True if you want to enable developer mode. For more info,
    # see https://www.renpy.org/doc/html/config.html#var-config.developer
    config.developer = "auto"

init python:
    ### Init ############################

    game_state = { }
    game_state.current_label = None
    game_state.ready = False
    game_state.day = None
    game_state.weekday = None
    game_state.daytime = None

    mod_menu_showing = False

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

    # Shows or hides the mod menu
    def show_menu(show_menu=True):
        global mod_menu_showing
        if show_menu and not mod_menu_showing:
            renpy.show_screen(MENU_SCREEN_NAME)
        elif not show_menu and mod_menu_showing:
            renpy.hide_screen(MENU_SCREEN_NAME)
        mod_menu_showing = show_menu

    # Toggles showing the mod menu, if the game is in the right state
    def toggle_menu():
        if is_game_ready():
            show_menu(not mod_menu_showing)

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
    config.underlay.append(renpy.Keymap(toggle_mod_menu = Function(toggle_menu)))

    # Bind the specified keys to the previously created keymaps
    for k, v in KEY_BINDS.items():
        config.keymap[k] = v


### Helper statements ############################################################

# Prepares for and starts a punishment game, then jumps to the default scene
# of the current game state, and thus not advancing the time of day
label start_punishment_game(character):

    # Store the map screen label name of the current day and daytime
    $ jump_back_to = get_current_premap_label()

    # Hide all screens
    call screen_hider
    $ show_menu(False)

    stop music

    # Start punishment game for the specified character
    call expression "%s_punish" % character

    # Jump to the default scene 
    $ renpy.jump(jump_back_to)


### Styles, screens and images ###########################################################

style menu_frame:
    xanchor 0
    yanchor 0
    xpadding 22
    ypadding 22
    xpos 145
    ypos 84
    background "#212121DD"

style menu_header_text is text:
    font "CinzelDecorative-Bold.ttf"
    color gui.hover_color
    size 26

style menu_text is text:
    font "CinzelDecorative-Regular.ttf"
    size 19

style menu_button_text is menu_text:
    font "CinzelDecorative-Regular.ttf"
    hover_color gui.hover_color
    size 19

screen hmmods_menu:
    tag hmmods_menu
    zorder 20
    modal True

    frame:
        style "menu_frame"
        vbox spacing 20:

            text _("Punish") style "menu_header_text"

            # Character image buttons
            hbox spacing 14:
                vbox spacing 6:
                    text "Amy" style "menu_text"
                    imagebutton:
                        auto "punish_image_amy_%s"
                        action Call("start_punishment_game", "amy")

                    text "Cassandra" style "menu_text"
                    imagebutton:
                        auto "punish_image_cass_%s"
                        action Call("start_punishment_game", "cass")

                vbox spacing 6:
                    text "Debbie" style "menu_text"
                    imagebutton:
                        auto "punish_image_debbie_%s"
                        action Call("start_punishment_game", "debbie")

                    text "Rachel" style "menu_text"
                    imagebutton:
                        auto "punish_image_rachel_%s"
                        action Call("start_punishment_game", "rachel")

# Initialze all images used by the menu and the gallery
init:
    image punish_image_amy_idle = im.Scale("amy photo_d1_face.jpg", 224, 126, bilinear=True)
    image punish_image_amy_hover = im.MatrixColor(ImageReference("punish_image_amy_idle"), im.matrix.brightness(0.11))

    image punish_image_cass_idle = im.Scale("cass photo_d1_face.jpg", 224, 126, bilinear=True)
    image punish_image_cass_hover = im.MatrixColor(ImageReference("punish_image_cass_idle"), im.matrix.brightness(0.11))

    image punish_image_debbie_idle = im.Scale("debbie photo_d1_face.jpg", 224, 126, bilinear=True)
    image punish_image_debbie_hover = im.MatrixColor(ImageReference("punish_image_debbie_idle"), im.matrix.brightness(0.11))

    image punish_image_rachel_idle = im.Scale("rachel photo_d1_face.jpg", 224, 126, bilinear=True)
    image punish_image_rachel_hover = im.MatrixColor(ImageReference("punish_image_rachel_idle"), im.matrix.brightness(0.11))
