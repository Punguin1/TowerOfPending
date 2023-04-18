import pyxel

GAME_STATE = "menu"
RETURN_COOLDOWN = 0
class Menu:
    def __init__(self, MENU_OPTIONS):
        print("Menu Initialized")
        self.menu_option_list = MENU_OPTIONS
        self.menu_option = 0
        self.rect_y = 85

    def draw(self):
        pyxel.cls(0)
        pyxel.text(50, 30, "Main Menu", pyxel.COLOR_WHITE) # draw the title
        pyxel.rect(40, 80, 80, 20, pyxel.COLOR_YELLOW) # draw a button
        pyxel.text(50, 85, "Play Game", pyxel.COLOR_BLACK) # add text to the button
        pyxel.text(50, 120, "Quit Game", pyxel.COLOR_WHITE)

        pyxel.rect(20, self.rect_y, 20, 10, 5)

    def update(self):
        global GAME_STATE
        if pyxel.btn(pyxel.KEY_0):
            pyxel.quit()
        if pyxel.btnp(pyxel.KEY_UP):
            if self.menu_option == len(self.menu_option_list)-1:
                self.menu_option = 0
            else:
                self.menu_option = self.menu_option + 1
        if pyxel.btnp(pyxel.KEY_DOWN):
            print(len(self.menu_option_list))
            if self.menu_option == 0:
                self.menu_option = len(self.menu_option_list)-1
            else:
                self.menu_option = self.menu_option - 1
        if self.menu_option_list[self.menu_option] == "start_game":
            self.rect_y = 85
            if pyxel.btnp(pyxel.KEY_RETURN):
                GAME_STATE = "game"
        if self.menu_option_list[self.menu_option] == "quit_game":
            self.rect_y = 120
            if pyxel.btnp(pyxel.KEY_RETURN):
                pyxel.quit()
        


class Game:
    def __init__(self, MENU_OPTIONS):
        print("Menu Initialized")
        self.menu_option_list = MENU_OPTIONS
        self.menu_option = 0
        self.rect_y = 85
        self.rect_x = 100
        self.show_frame = 0

    def draw(self):
        pyxel.cls(0)

        pyxel.blt(0, 0, 0, 0, 0, 240, 256)
        pyxel.rect(self.rect_x, self.rect_y, 20, 10, 2)
    
        if self.menu_option_list[self.menu_option] == "option0":
            if pyxel.btnp(pyxel.KEY_RETURN) and self.show_frame == 0:
                self.show_frame = 60
            if self.show_frame > 0:
                pyxel.blt(16, 15, 1, 0, 0, 109, 103)
                self.show_frame = self.show_frame-1
        if pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.KEY_DOWN):
            self.show_frame = 0
        

    def update(self):
        global GAME_STATE

        if pyxel.btnp(pyxel.KEY_O):
            GAME_STATE = "menu"
        if pyxel.btnp(pyxel.KEY_DOWN):
            print(self.menu_option_list[self.menu_option])
            if self.menu_option == len(self.menu_option_list)-1:
                self.menu_option = 0
            else:
                self.menu_option = self.menu_option + 1
        if pyxel.btnp(pyxel.KEY_UP):
            print(self.menu_option_list[self.menu_option])
            if self.menu_option == 0:
                self.menu_option = len(self.menu_option_list)-1
            else:
                self.menu_option = self.menu_option - 1
        if self.menu_option_list[self.menu_option] == "option0":
            self.rect_y = 155
            self.rect_x = 25
            


        if self.menu_option_list[self.menu_option] == "option1":
            self.rect_y = 185
            self.rect_x = 25
        if self.menu_option_list[self.menu_option] == "option2":
            self.rect_y = 225
            self.rect_x = 25
        if self.menu_option_list[self.menu_option] == "option3":
            self.rect_y = 155
            self.rect_x = 135
        if self.menu_option_list[self.menu_option] == "option4":
            self.rect_y = 185
            self.rect_x = 135
        if self.menu_option_list[self.menu_option] == "option5":
            self.rect_y = 225
            self.rect_x = 135
        
        
        

        

    
class Main:
    def __init__(self):
        global RETURN_COOLDOWN
        self.menu = Menu(["start_game", "quit_game"])
        self.game = Game(["option0", "option1", "option2", "option3", "option4", "option5"])
        self.screen_width = 240
        self.screen_height = 256
        self.caption = "Gaming"

        pyxel.init(self.screen_width, self.screen_height, self.caption, 60)
        pyxel.image(0).load(0, 0, "RatticusAscendingUI.png")
        pyxel.image(1).load(0, 0, "susguy109x103.jpg")
        pyxel.run(self.update, self.draw)


        # initialize game state here

    def draw(self):
        global GAME_STATE
        if GAME_STATE == "game":
           self.game.draw()

        if GAME_STATE == "menu":
            self.menu.draw()
            if self.menu == "start_game":
                print("gamestate changed")
                GAME_STATE == "game"

            
        

    def update(self):
        global GAME_STATE
        global RETURN_COOLDOWN
        if GAME_STATE == "menu":
            self.menu.update()
        if GAME_STATE == "game":
            self.game.update()

        if pyxel.btnp(pyxel.KEY_RETURN) and RETURN_COOLDOWN==0:
            RETURN_COOLDOWN = 20

        if RETURN_COOLDOWN != 0:
            RETURN_COOLDOWN = RETURN_COOLDOWN-1
        


Main()