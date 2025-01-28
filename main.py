import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WINDOW_TITLE = "Tutoriel Arcade"

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE)

arcade.set_background_color(arcade.color.SKY_BLUE)

arcade.start_render()

arcade.draw.draw_lrbt_rectangle_filled(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT / 2,  arcade.csscolor.DARK_GREEN)
# draw tree
for i in range(4):
    r = arcade.rect.XYWH(200+i*100, SCREEN_HEIGHT / 2, 30, 60)
    arcade.draw.draw_rect_filled(r, arcade.csscolor.BROWN)

arcade.draw_circle_filled(200, SCREEN_HEIGHT / 2 + 50, 30, arcade.csscolor.FOREST_GREEN)

arcade.draw_ellipse_filled(300, SCREEN_HEIGHT / 2 + 50, 40, 100, arcade.csscolor.FOREST_GREEN)

arcade.draw.draw_arc_filled(400, SCREEN_HEIGHT / 2 + 20, 60, 100, arcade.csscolor.FOREST_GREEN, 0, 180)

y = SCREEN_HEIGHT / 2 + 40
arcade.draw.draw_triangle_filled(500, y + 40, 470, y - 20, 530, y - 20, arcade.color.FOREST_GREEN)

# tilt angle drawing test
arcade.draw.draw_circle_outline(200, 200, 60, arcade.color.BUBBLE_GUM, num_segments=8, tilt_angle=35)
arcade.draw.draw_circle_outline(400, 200, 60, arcade.color.BUBBLE_GUM, num_segments=8)

# draw line
arcade.draw.draw_line(SCREEN_WIDTH - 250, SCREEN_HEIGHT - 110, SCREEN_WIDTH, SCREEN_HEIGHT - 110, arcade.color.BANANA_YELLOW, 10)

points = [(700, 300), (750, 600), (345, 675)]
arcade.draw.draw_line_strip(points, arcade.color.BUFF)

line_list = [(139, 556), (720, 512), (773, 704), (710, 596)]
arcade.draw.draw_lines(line_list, arcade.color.FOREST_GREEN)

# draw polygone

points = [(700, 300), (750, 600), (345, 675)]
arcade.draw.draw_polygon_filled(points, arcade.color.AERO_BLUE)

points = [(200, 200), (350, 200), (345, 375), (23, 224), (222, 222)]
arcade.draw.draw_polygon_outline(points, arcade.color.ALIZARIN_CRIMSON, 10)

# draw text

affichage = arcade.Text("Ceci est une chaîne de caractère!", 20, SCREEN_HEIGHT - 40, arcade.color.BARBIE_PINK)
affichage.draw()

arcade.finish_render()

arcade.run()





