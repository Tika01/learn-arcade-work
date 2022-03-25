import arcade

SCREEN_WIDTH = 530
SCREEN_HEIGHT = 530
MOVEMENT_SPEED = 3


class Boat:
    def __init__(self, position_x, position_y, change_x, change_y):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = 25

    def draw(self):
        """ Draw the balls with the instance variables we have. """

        texture = arcade.load_texture("sailboat.png")
        arcade.draw_texture_rectangle(self.position_x, self.position_y, 50, 50, texture)

    def update(self):
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.position_x = self.radius

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius

        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius


class Moon:
    def __init__(self, position_x, position_y, radius, color):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        texture = arcade.load_texture("moon.png")
        arcade.draw_texture_rectangle(self.position_x, self.position_y, 26, 51, texture)


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        # Create our ball
        self.boat = Boat(200, 140, 0, 0)
        self.moon = Moon(80, 450, 15, arcade.color.AUBURN)



    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        # background credits to https://twitter.com/16pxl
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT,
                                      arcade.load_texture("background.png"))

        # arcade.start_render()
        self.boat.draw()
        self.moon.draw()

    def update(self, delta_time):
        self.boat.update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.boat.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.boat.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.boat.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.boat.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.boat.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.boat.change_y = 0

    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects.
        Happens approximately 60 times per second."""
        self.moon.position_x = x
        self.moon.position_y = y


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_WIDTH, "Drawing Example")
    arcade.run()


main()