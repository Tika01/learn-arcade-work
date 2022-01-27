"""
This is a sample program to show how to draw using the Python programming
language and the Arcade library.
"""

# Import the "arcade" library
from turtle import color

import arcade

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the and dimensions (width and height)
arcade.open_window(300, 425, "Drawing Lab 2")

# Set the background color + main green wall
arcade.set_background_color((172, 214, 146))

# Get ready to draw
arcade.start_render()

# left wall
arcade.draw_lrtb_rectangle_filled(0, 160, 425, 0, arcade.color.ASPARAGUS)

# Wall hole
arcade.draw_polygon_filled(((200, 340),
                            (200, 265),
                            (250, 235),
                            (250, 315),
                            ),
                           arcade.csscolor.DARK_GREEN)

# Top Slanted wall

arcade.draw_triangle_filled(0, 425, 0, 135, 160, 425, arcade.color.CADET_GREY)

# top of rectangle

arcade.draw_polygon_filled(((160, 425),
                            (-50, 85),
                            (125, 85),
                            (160, 150),
                             ),
                            arcade.color.CELADON)

# Circle Window

arcade.draw_circle_filled(78, 200, 25, arcade.color.CADET_GREY)

arcade.draw_circle_filled(85, 210, 25, arcade.color.BLACK)

arcade.draw_circle_outline(78, 200, 30, arcade.color.CELADON, 4.5)

arcade.draw_circle_outline(78, 200, 38.5, arcade.color.CELADON, 12)

# Top Window

arcade.draw_lrtb_rectangle_filled(25, 100, 400, 360, arcade.color.WHITE)

arcade.draw_polygon_filled(((25, 360),
                            (25, 380),
                            (75, 380),
                            (100, 360),
                             ),
                            arcade.color.BLACK)

arcade.draw_polygon_filled(((75, 380),
                            (75, 400),
                            (100, 400),
                            (100, 360),
                             ),
                            arcade.color.CELADON)


# Middle Wall Opening

arcade.draw_polygon_filled(((125, 368.5),
                            (160, 425),
                            (160, 65),
                            (125, 0),
                            ),
                           arcade.csscolor.DARK_GREEN)

# wall shadow
arcade.draw_triangle_filled(250, 235, 200, 265, 250, 275, arcade.color.CADET_GREY)

# rectangle cube
# rectangle (125, 85)

arcade.draw_lrtb_rectangle_filled(0, 125, 85, 0, arcade.color.BLACK)

# 2nd rectangle cube

arcade.draw_polygon_filled(((125, 85),
                            (160, 150),
                            (0, 150),
                            (0, 85),
                            ),
                           arcade.color.CAMBRIDGE_BLUE)




# Stairs
arcade.draw_polygon_filled(((200, 265),
                            (175, 260),
                            (225, 230),
                            (250, 235),
                             ),
                            arcade.color.ANTI_FLASH_WHITE)

arcade.draw_polygon_filled(((175, 235),
                            (150, 230),
                            (200, 200),
                            (225, 205),
                             ),
                            arcade.color.ANTI_FLASH_WHITE)

arcade.draw_polygon_filled(((150, 205),
                            (125, 200),
                            (175, 170),
                            (200, 175),
                             ),
                            arcade.color.ANTI_FLASH_WHITE)

arcade.draw_polygon_filled(((125, 175),
                            (100, 170),
                            (150, 140),
                            (175, 145),
                             ),
                            arcade.color.ANTI_FLASH_WHITE)

arcade.draw_polygon_filled(((100, 145),
                            (75, 140),
                            (125, 110),
                            (150, 115),
                             ),
                            arcade.color.ANTI_FLASH_WHITE)

arcade.draw_polygon_filled(((75, 115),
                            (50, 110),
                            (100, 80),
                            (125, 85),
                             ),
                            arcade.color.ANTI_FLASH_WHITE)

arcade.draw_polygon_filled(((50, 85),
                            (25, 80),
                            (75, 50),
                            (100, 55),
                             ),
                            arcade.color.ANTI_FLASH_WHITE)

arcade.draw_polygon_filled(((25, 55),
                            (0, 50),
                            (50, 20),
                            (75, 25),
                             ),
                            arcade.color.ANTI_FLASH_WHITE)

arcade.draw_polygon_filled(((0, 25),
                            (-25, 20),
                            (25, -10),
                            (50, -5),
                             ),
                            arcade.color.ANTI_FLASH_WHITE)
# Stairs Shadow
arcade.draw_polygon_filled(((175, 260),
                            (175, 235),
                            (225, 205),
                            (225, 230),
                             ),
                            arcade.color.ASH_GREY)

arcade.draw_polygon_filled(((150, 230),
                            (150, 205),
                            (200, 175),
                            (200, 200),
                             ),
                            arcade.color.ASH_GREY)

arcade.draw_polygon_filled(((125, 200),
                            (125, 175),
                            (175, 145),
                            (175, 170),
                             ),
                            arcade.color.ASH_GREY)

arcade.draw_polygon_filled(((100, 170),
                            (100, 145),
                            (150, 115),
                            (150, 140),
                             ),
                            arcade.color.ASH_GREY)

arcade.draw_polygon_filled(((75, 140),
                            (75, 115),
                            (125, 85),
                            (125, 110),
                             ),
                            arcade.color.ASH_GREY)

arcade.draw_polygon_filled(((50, 110),
                            (50, 85),
                            (100, 55),
                            (100, 80),
                             ),
                            arcade.color.ASH_GREY)

arcade.draw_polygon_filled(((25, 80),
                            (25, 55),
                            (75, 25),
                            (75, 50),
                             ),
                            arcade.color.ASH_GREY)

arcade.draw_polygon_filled(((0, 50),
                            (0, 25),
                            (50, -5),
                            (50, 20),
                             ),
                            arcade.color.ASH_GREY)




# --- Finish drawing ---
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()