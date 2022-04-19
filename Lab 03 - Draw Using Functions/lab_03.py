

import arcade

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 425

def left_wall():
    arcade.draw_lrtb_rectangle_filled(0, 160, SCREEN_HEIGHT, 0, arcade.color.ASPARAGUS)

def wall_hole():
    arcade.draw_polygon_filled(((200, 340),
                                (200, 265),
                                (250, 235),
                                ),
                               arcade.csscolor.DARK_GREEN)

def slant_wall():
    arcade.draw_triangle_filled(0, 425, 0, 135, 160, 425, arcade.color.CADET_GREY)

def top_rect():
    arcade.draw_polygon_filled(((160, 425),
                                (-50, 85),
                                (125, 85),
                                (160, 150),
                                ),
                               arcade.color.CELADON)

def circle_window():
    arcade.draw_circle_filled(78, 200, 25, arcade.color.CADET_GREY)

    arcade.draw_circle_filled(85, 210, 25, arcade.color.BLACK)

    arcade.draw_circle_outline(78, 200, 30, arcade.color.CELADON, 4.5)

    arcade.draw_circle_outline(78, 200, 38.5, arcade.color.CELADON, 12)

def top_window():
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

def middle_wall_opening():
    arcade.draw_polygon_filled(((125, 368.5),
                                (160, 425),
                                (160, 65),
                                (125, 0),
                                ),
                               arcade.csscolor.DARK_GREEN)

def wall_shadow():
    arcade.draw_triangle_filled(250, 235, 200, 265, 250, 275, arcade.color.CADET_GREY)

def rect():
    arcade.draw_lrtb_rectangle_filled(0, 125, 85, 0, arcade.color.BLACK)

def rect_2():
    arcade.draw_polygon_filled(((125, 85),
                                (160, 150),
                                (0, 150),
                                (0, 85),
                                ),
                               arcade.color.CAMBRIDGE_BLUE)

def create_white_step(x: int, y: int):
    arcade.draw_polygon_filled(((x+25, y+5),
                                (x, y),
                                (x+50, y-30),
                                (x+75, y-25),
                                ),
                                arcade.color.ANTI_FLASH_WHITE)


def create_gray_stair(x: int, y:int):
    arcade.draw_polygon_filled(((x, y),
                                (x, y-25),
                                (x+50, y-55),
                                (x+50, y-30)),
                               arcade.color.ASH_GREY)

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing With Functions Lab 3")
# Set the background color + main green wall
    arcade.set_background_color((172, 214, 146))
# Get ready to draw
    arcade.start_render()

    left_wall()

    wall_hole()

    slant_wall()

    top_rect()

    circle_window()

    top_window()

    middle_wall_opening()

    wall_shadow()

    rect()

    rect_2()

    create_white_step(175, 260)
    create_white_step(150, 230)
    create_white_step(125, 200)
    create_white_step(100, 170)
    create_white_step(75, 140)
    create_white_step(50, 110)
    create_white_step(25, 80)
    create_white_step(0, 50)
    create_white_step(-25, 20)

    create_gray_stair(175, 260)
    create_gray_stair(150, 230)
    create_gray_stair(125, 200)
    create_gray_stair(100, 170)
    create_gray_stair(75, 140)
    create_gray_stair(50, 110)
    create_gray_stair(25, 80)
    create_gray_stair(0, 50)

# --- Finish drawing ---
    arcade.finish_render()

# Keep the window up until someone closes it.
    arcade.run()

main()