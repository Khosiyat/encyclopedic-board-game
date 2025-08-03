import arcade

def load_sounds(asset_folder):
    dice_roll = arcade.load_sound(asset_folder + "dice_roll.wav")
    movement = arcade.load_sound(asset_folder + "movement.wav")
    winning = arcade.load_sound(asset_folder + "winning.wav")
    return dice_roll, movement, winning
