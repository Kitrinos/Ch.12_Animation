'''
SNOWFALL
--------
Try to create the snowfall animation by meeting
the following requirements:
# 1.) Create a 600 x 600 window with black background
2.) Window title equals "Snowfall"
3.) Crossbars 10 px wide. Snow must be outside!
4.) Make snowflake radius random between 1-3
5.) Randomly start snowflakes anywhere in the window.
6.) Random downward speed of -4 to -1
7.) Start snowflakes again at random x from 0-600 and random y from 600-700
8.) Generate 300 snowflakes
9.) Color snowflake #1 red just for fun.
10.) All other snowflakes should be white.
'''
import arcade
import random
SF = 200
SH = 600
SW = 600

class snow_ball:
    def __init__(self, pos_x, pos_y, dy, rad, col):
        self.radius = rad
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dy = dy
        self.col = col

    def draw_ball(self):
        arcade.draw_circle_filled(self.pos_x, self.pos_y, self.radius, self.col)

    def update_ball(self):
        self.pos_y += self.dy
        if self.pos_y<0:
            self.pos_x=random.randint(0,SW)
            self.pos_y= random.randint(SH, SW+100)

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)
        self.snowlist = []
        for i in range(SF):
            self.pos_x = random.randint(0, SW)
            self.pos_y = random.randint(0,SH) #0, SH
            self.dy = random.randint(-4,-1)
            self.rad = random.randint(1, 3)
            if i ==0:
                self.color = arcade.color.RED
            else:
                self.color = arcade.color.BUBBLES
            self.snow_ball = snow_ball(self.pos_x, self.pos_y, self.dy, self.rad, arcade.color.WHITE)
            self.snowlist.append(self.snow_ball)

    def on_draw(self):
        arcade.start_render()
        for item in self.snowlist:
            item.draw_ball()
        arcade.draw_rectangle_filled(SW/2,SH/2,10,SH,arcade.color.RED_BROWN) # Y
        arcade.draw_rectangle_filled(SW/2,SH/2,SW,10, arcade.color.RED_BROWN) # X

    def on_update(self, dt):
        for item in self.snowlist:
            item.update_ball()

def main():
    window = MyGame(SH,SW, "SnowFall")
    arcade.run()
if __name__== "__main__":
    main()
main()
