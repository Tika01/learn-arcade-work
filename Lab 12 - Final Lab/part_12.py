
# The Game Explanation
# You had just died, from catching the deadly virus of the Corona.
# You know some friends that are in the afterlife that you want to vist.
# but you also have an enemy that you definitely don't want to see.
# Your enemy knows you are there and is trying to kill you. (How idk? you're already dead)
# But your friends have yet to know you have arrived.
# Your goal is to awaken all your friends before your enemy catches you.
# If your friends find out that your enemy is around (by you touching your enemy)
# Then they will all hide, and you'll have to start all over.
# Try not to vist your friends too much, or they'll be put back to sleep.
# Good luck!


import random
import arcade
import math
import os

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.02
SPRITE_SCALING_COIN = 0.002
SPRITE_SCALING_ENEMY = 0.002
COIN_COUNT = 50
SPRITE_SPEED = .5
ENEMY_COUNT = 1

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Find Your Homies!"

class Enemy(arcade.Sprite):
    """
    This class represents the coins on our screen. It is a child class of
    the arcade library's "Sprite" class.
    """

    def follow_sprite(self, player_sprite):
        """
        This function will move the current sprite towards whatever
        other sprite is specified as a parameter.

        We use the 'min' function here to get the sprite to line up with
        the target sprite, and not jump around if the sprite is not off
        an exact multiple of SPRITE_SPEED.
        """

        if self.center_y < player_sprite.center_y:
            self.center_y += min(SPRITE_SPEED, player_sprite.center_y - self.center_y)
        elif self.center_y > player_sprite.center_y:
            self.center_y -= min(SPRITE_SPEED, self.center_y - player_sprite.center_y)

        if self.center_x < player_sprite.center_x:
            self.center_x += min(SPRITE_SPEED, player_sprite.center_x - self.center_x)
        elif self.center_x > player_sprite.center_x:
            self.center_x -= min(SPRITE_SPEED, self.center_x - player_sprite.center_x)

class Coin(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):
        """ Constructor. """
        # Call the parent class (Sprite) constructor
        super().__init__(filename, sprite_scaling)

        # Current angle in radians
        self.circle_angle = 0

        # How far away from the center to orbit, in pixels
        self.circle_radius = 0

        # How fast to orbit, in radians per frame
        self.circle_speed = 0.008

        # Set the center of the point we will orbit around
        self.circle_center_x = 0
        self.circle_center_y = 0
        self.firstImage = True

    def update(self):

        """ Update the ball's position. """
        # Calculate a new x, y
        self.center_x = self.circle_radius * math.sin(self.circle_angle) \
            + self.circle_center_x
        self.center_y = self.circle_radius * math.cos(self.circle_angle) \
            + self.circle_center_y

        # Increase the angle in prep for the next round.
        self.circle_angle += self.circle_speed


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):

        super().__init__(width, height, title)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Sprite lists
        self.all_sprites_list = None
        self.coin_list = None

        # Set up the player
        self.score = 0
        self.player_sprite = None

        self.enemy_list = None

        self.game_over = None


    def start_new_game(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.all_sprites_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Set up the player
        self.score = 0
        self.life = 3
        self.game_over = False

        self.player_sprite = arcade.Sprite("ghost.png",
                                           SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 400
        self.player_sprite.center_y = 300
        self.all_sprites_list.append(self.player_sprite)

        for i in range(50):

            # Create the coin instancSo how do you do that I don't know where is the background K OK let's doe

            coin = Coin("rip.png", .01)

            # Position the center of the circle the coin will orbit
            coin.circle_center_x = random.randrange(SCREEN_WIDTH)
            coin.circle_center_y = random.randrange(SCREEN_HEIGHT)

            # Random radius from 10 to 200
            coin.circle_radius = random.randrange(10, 200)

            # Random start angle from 0 to 2pi
            coin.circle_angle = random.random() * 2 * math.pi

            # Add the coin to the lists
            self.all_sprites_list.append(coin)
            self.coin_list.append(coin)

        #Enemy
        # Create the coin instance
        # Coin image from kenney.nl
        enemy = Enemy("madghost.png", .1)

        # Position the coin
        enemy.center_x = random.randrange(SCREEN_WIDTH)
        enemy.center_y = random.randrange(SCREEN_HEIGHT)

        # Add the coin to the lists
        self.enemy_list.append(enemy)

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

    def on_draw(self):

        # This command has to happen before we start drawing
        self.clear()

        arcade.set_background_color((172, 214, 146))

        # Draw all the sprites.
        self.all_sprites_list.draw()

        # Drawing Enemy
        self.enemy_list.draw()

        # Put the text on the screen.
        output = "Score: " + str(self.score)
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

        life_output = f"Life: {self.life}"
        arcade.draw_text(life_output, 720, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def on_update(self, delta_time):
        """ Movement and game logic """

        if self.life > 0:
            # Call update on all sprites (The sprites don't do much in this
            # example though.)
            self.all_sprites_list.update()

            # Generate a list of all sprites that collided with the player.
            hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                            self.coin_list)

            # Loop through each colliding sprite, remove it, and add to the score.
            for coin in hit_list:
                # self.score += 1
                if coin.firstImage:
                    coin.texture = arcade.load_texture("ghost.png")
                    coin.firstImage = False
                else:
                    coin.texture = arcade.load_texture("rip.png")
                    coin.firstImage = True

            for enemy in self.enemy_list:
                enemy.follow_sprite(self.player_sprite)

            # Generate a list of all sprites that collided with the player.
            hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.enemy_list)

            # Loop through each colliding sprite, remove it, and add to the score.
            for enemy in hit_list:
                for coin in self.coin_list:
                    coin.texture = arcade.load_texture("rip.png")
                    coin.firstImage = True

def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.start_new_game()
    arcade.run()


if __name__ == "__main__":
    main()