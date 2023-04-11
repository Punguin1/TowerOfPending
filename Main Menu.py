import pyxel


# class Menu():
#     def __init__(self):
#         pass
#     def update(self):
#         pass
    
#     def draw(self):
#         pyxel.cls(0) # clear the screen with color index 0 (black)
#         pyxel.text(50, 30, "Main Menu", pyxel.COLOR_WHITE) # draw the title
#         pyxel.rect(50, 80, 80, 20, pyxel.COLOR_YELLOW) # draw a button
#         pyxel.text(60, 85, "Play Game", pyxel.COLOR_BLACK) # add text to the button
    
#     def run(self):
#         pyxel.run(self.update, self.draw)
    

class Main:
    def __init__(self):
        draw_mainmenu = True
        self.screen_width = 256
        self.screen_height = 240
        self.caption = "Gaming"

        pyxel.init(self.screen_width, self.screen_height, self.caption)
        pyxel.run(self.update, self.draw)
        # initialize game state here

    def draw(self):
        pyxel.cls(0) # clear the screen with color index 0 (black)
        pyxel.rect(10, 10, 10, 10, 10)
        if self.draw_mainmenu():
            pyxel.text(20, 20, "Press E to die", 4)
        # draw game elements here

    def update(self):
        if self.draw_mainmenu():
            if pyxel.btn(pyxel.KEY_E):
                self.draw_mainmenu = False
        if pyxel.btn(pyxel.KEY_P):
            print("test")

Main()