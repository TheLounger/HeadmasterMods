init -1 python:
    class ItemDefinition():
        def __init__(self, name, full_name, owned_var, ordered_var, images):
            self.name = name
            self.full_name = full_name
            self.owned_var = owned_var
            self.ordered_var = ordered_var
            self.images = images

        @property
        def is_ordered(self):
            return self.ordered_var in globals() and globals()[self.ordered_var] == True

        @property
        def is_owned(self):
            return self.owned_var in globals() and globals()[self.owned_var] == True

        def set_owned(self, owned=True):
            # Set the item as owned/not owned
            globals()[self.owned_var] = owned

            # Also set ordered/not ordered, except for "viagra_ordered" as this
            # is the only variable that may be False after you own the item.
            if self.ordered_var != "viagra_ordered":
                globals()[self.ordered_var] = owned

    class StoreItems(UIWindow):
        categories = [ "Electronics", "Clothing", "Health", "Sex Toys" ]
        all_items = {
            "Electronics": [
                ItemDefinition("camera", "Dickon SM3000 HD Digital Camera", "have_camera", "camera_ordered", ["camera2.png", "camera2_hover.png", "camera_purchased.png"]),
                ItemDefinition("pistol", "Water Pistol (Natural Rubber)", "have_pistol", "pistol_ordered", ["buy_pistol.png", "buy_pistol_hover.png", "buy_pistol_purchased.png"])
            ],
            "Clothing": [
                ItemDefinition("maid_outfit", "Maid Outfit", "have_maid_outfit", "maid_outfit_ordered", ["buy_maid_outfit.png", "buy_maid_outfit_hover.png", "buy_maid_outfit_purchased.png"]),
                ItemDefinition("apron", "Apron", "have_apron", "apron_ordered", ["buy_apron.png", "buy_apron_hover.png", "buy_apron_purchased.png"]),
                ItemDefinition("uniform_samples", "School Swimwear Samples", "have_uniform_samples", "uniform_samples_ordered", ["buy_uniform_samples.png", "buy_uniform_samples_hover.png", "buy_uniform_samples_purchased.png"]),
                ItemDefinition("cat_ears", "Cat Ears", "have_cat_ears", "cat_ears_ordered", ["buy_cat_ears.png", "buy_cat_ears_hover.png", "buy_cat_ears_purchased.png"]),
                ItemDefinition("chastity", "Chastity Panties", "have_chastity", "chastity_ordered", ["buy_chastity.png", "buy_chastity_hover.png", "buy_chastity_purchased.png"])
            ],
            "Health": [
                ItemDefinition("viagra", "Viagra", "have_viagra", "viagra_ordered", ["viagra.png", "viagra_hover.png", "viagra_purchased.png"]),
                ItemDefinition("ointment", "Aloe Vera Cream", "have_ointment", "ointment_ordered", ["buy_ointment.png", "buy_ointment_hover.png", "buy_ointment_purchased.png"])
            ],
            "Sex Toys": [
                ItemDefinition("paddle", "Paddle", "have_paddle", "paddle_ordered", ["buy_paddle.png", "buy_paddle_hover.png", "buy_paddle_purchased.png"]),
                ItemDefinition("butt_plug", "Butt Plug", "have_butt_plug", "butt_plug_ordered", ["buy_butt_plug.png", "buy_butt_plug_hover.png", "buy_butt_plug_purchased.png"]),
                ItemDefinition("cane", "Cane", "have_cane", "cane_ordered", ["buy_cane.png", "buy_cane_hover.png", "buy_cane_purchased.png"])
            ]
        }

        @property
        def name(self):
            return "store_items"

    # Initialize items window images
    for k, array in StoreItems.all_items.items():
        for item in array:
            renpy.image(
                "item_image_{}_idle".format(item.name),
                Crop((8, 8, 142, 114),
                Image(item.images[0])))
            # Create our own Hover image instead of using the existing (inconsistent) ones
            renpy.image(
                "item_image_{}_hover".format(item.name),
                Crop((8, 8, 142, 114),
                    im.MatrixColor(Image(item.images[0]),
                        im.matrix.brightness(0.11))))
            renpy.image(
                "item_image_{}_purchased_idle".format(item.name),
                Crop((8, 8, 142, 114),
                    Image(item.images[2])))
            renpy.image(
                "item_image_{}_purchased_hover".format(item.name),
                Crop((8, 8, 142, 114),
                    im.MatrixColor(Image(item.images[2]),
                        im.matrix.brightness(0.11))))
