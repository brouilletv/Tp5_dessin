"""
tp 5
Vincent Brouillet
groupe: 405
dessin avec arcade
"""

import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
WINDOW_TITLE = "pacman dessin"

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE)

arcade.set_background_color(arcade.color.BLACK)

arcade.start_render()

# map layout
map_list = [[150, 500, 50, 100], [50, 100, 100, 250], [50, 100, 300, 450], [50, 300, 500, 550], [150, 200, 450, 500],
            [450, 600, 500, 550], [150, 200, 250, 400], [350, 400, 250, 400], [200, 350, 250, 300],
            [200, 250, 350, 400], [300, 350, 350, 400], [200, 350, 150, 200], [500, 550, 150, 450],
            [450, 500, 150, 200]]  # chaqu'un est un mur

for i in map_list:
    arcade.draw_lrbt_rectangle_filled(i[0], i[1], i[2], i[3], arcade.color.OCEAN_BOAT_BLUE)

# pacman
pacman = [(450, 150), (425, 125), (450, 100),
          (425, 100), (400, 110), (400, 140), (425, 150)]

arcade.draw_polygon_filled(pacman, arcade.color.YELLOW)

# phantom
phantom_rouge = [[200, 300], [250, 300], [225, 350]]  # triangle
phantom_rose = [475, 425, 50, 50, 0, 180]  # arc
phantom_orange = [75, 75, 50, 30]  # ellipse

arcade.draw_triangle_filled(phantom_rouge[0][0], phantom_rouge[0][1], phantom_rouge[1][0], phantom_rouge[1][1],
                            phantom_rouge[2][0], phantom_rouge[2][1], arcade.color.RED)
arcade.draw_arc_filled(phantom_rose[0], phantom_rose[1], phantom_rose[2], phantom_rose[3],
                       arcade.color.ROSE_BONBON, phantom_rose[4], phantom_rose[5])
arcade.draw_ellipse_filled(phantom_orange[0], phantom_orange[1], phantom_orange[2], phantom_orange[3],
                           arcade.color.ORANGE)

# titre
titre = arcade.Text("Pacman low poly", 20, SCREEN_HEIGHT - 20, arcade.color.WHITE)
titre.draw()

arcade.draw_lines([(20, SCREEN_HEIGHT - 30), (1502, SCREEN_HEIGHT - 30)], arcade.color.WHITE)

arcade.finish_render()

arcade.run()
