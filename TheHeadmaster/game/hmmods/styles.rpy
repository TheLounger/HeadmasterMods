style menu_frame:
    xanchor 0
    yanchor 0
    ymaximum 880
    xpadding 14
    ypadding 14
    xpos 145
    ypos 84
    background "#212121DD"

style menu_header_text is text:
    color "#69BFCE"
    outlines [ (1, "#244", 0, 0) ]
    font "CinzelDecorative-Regular.ttf"
    size 26

style menu_text is text:
    font "CinzelDecorative-Regular.ttf"
    size 19

style menu_text_small is menu_text:
    size 15

style menu_text_tiny is menu_text:
    size 13

style menu_button:
    background "#21212100"
    padding (0, 0, 0, 0)

style menu_button_text is menu_text:
    hover_color gui.hover_color
    xalign 0
    yalign 0.5

style menu_button_text_header is menu_header_text:
    color "#888"
    outlines [ (1, "#244", 0, 0) ]
    hover_color gui.hover_color
    xalign 0
    yalign 0.5

style menu_button_text_header_selected is menu_header_text:
    outlines [ (2, "#202020", 0, 0) ]
    xalign 0
    yalign 0.5

style menu_button_text_small is menu_button_text:
    size 15

style menu_button_text_tiny is menu_button_text:
    font gui.interface_text_font
    size 15

style menu_button_text_tiny_selected is menu_button_text_tiny:
    color "#69BFCE"
    outlines [ (1, "#000", 0, 0) ]

transform gallery_image_transform:
    xanchor 0.5
    yanchor 0.5
