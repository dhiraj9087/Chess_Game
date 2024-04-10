import pygame
import sys
from const import *
from game import Game
from square import *

class Main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption("Chess")
        self.game = Game()
    
    def mainloop(self):
        
        screen = self.screen
        game = self.game
        board = self.game.board
        dragger = self.game.dragger


        while True:
            self.game.show_bg(screen)
            self.game.show_pieces(screen)


            for event in pygame.event.get():

                if event.type==pygame.MOUSEBUTTONDOWN:       ## click
                    dragger.update_mouse(event.pos)
                    # print(event.pos)                        ## it is the position we click on board

                    clicked_row = dragger.mouseY // SQSIZE
                    clicked_col = dragger.mouseX // SQSIZE

                    if board.squares[clicked_row][clicked_col].has_piece():     ## if clicked square has a piece 
                        piece = board.squares[clicked_row][clicked_col].piece

                elif event.type==pygame.MOUSEMOTION:         ## mouse motion
                    pass
            
                elif event.type==pygame.MOUSEBUTTONUP:       ## click release
                    pass

                elif event.type==pygame.QUIT:                ## quit application
                    pygame.quit()
                    sys.exit()



            
            pygame.display.update()

main = Main()
main.mainloop()