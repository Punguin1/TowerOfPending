import pyxel


class Draw_menu:
    def __init__(self):
        print("Menu Initialized")
    def draw(self):
        pyxel.text(50, 30, "Main Menu", pyxel.COLOR_WHITE) # draw the title
        pyxel.rect(50, 80, 80, 20, pyxel.COLOR_YELLOW) # draw a button
        pyxel.text(60, 85, "Play Game", pyxel.COLOR_BLACK) # add text to the button
    def update(self):
        print("test")
    
class Main:
    def __init__(self):
        self.GAME_STATE = "menu"
        self.draw_menu = Draw_menu()
        self.screen_width = 256
        self.screen_height = 240
        self.caption = "Gaming"

        pyxel.init(self.screen_width, self.screen_height, self.caption)
        pyxel.run(self.update, self.draw)
        # initialize game state here

    def draw(self):
        if self.GAME_STATE == "menu":
            self.draw_menu.draw()
        else:
            pyxel.cls(0)
            pyxel.rect(10, 10, 10, 10, 10)

    def update(self):
        if self.GAME_STATE == "menu":
            if pyxel.btn(pyxel.KEY_E):
                self.GAME_STATE == "quit"
        if self.GAME_STATE == "quit":
            pyxel.quit()
        if pyxel.btn(pyxel.KEY_P):
            print("test")

Main()