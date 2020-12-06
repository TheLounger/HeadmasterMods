init -1 python:
    class Util():
        @staticmethod
        def add_underlay_keymap(**keymap):
            """
            Add keymaps to config.underlay, while checking if names don't exist
            in config.keymap, in which case they will be ignored
            """

            # Filter out args that aren't in config.keymap
            keymap = { k: v for k, v in keymap.items() if k in config.keymap }

            if len(keymap) > 0:
                config.underlay.append(renpy.Keymap(**keymap))

        @staticmethod
        def is_webp_header(h):
            """
            Tests whether a file header looks like WebP
            "imghdr.what" only supports WebP since Python 3.5
            """

            if h.startswith(b'RIFF') and h[8:12] == b'WEBP':
                return 'webp'

            return None

        @staticmethod
        def natural_sort(list): 
            convert = lambda text: int(text) if text.isdigit() else text.lower() 
            alphanum_key = lambda key: [ convert(c) for c in re.split("([0-9]+)", key) ] 
            return sorted(list, key=alphanum_key)


# General label caller. Remembers current game state (day/time), stops music, hides all screens and
# then calls the specified label. When call returns, it will jump back to the default
# screen of the game state before the call.
label call_label(label_name):
    $ jump_back_to = gm.game_state.get_current_premap_label()
    call screen_hider
    stop music
    call expression "%s" % label_name
    $ renpy.jump(jump_back_to)
