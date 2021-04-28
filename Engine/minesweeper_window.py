import pygame
import os

from Attributes.game_attributes import reset_board
from Engine.GUI import Button, reveal, BoardPanel, TilePanel, TitleBar, hit
from Model.board import Board

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
GREY = (165, 165, 165)

TILE_SIZE = 25

board = None

board = Board()

WINDOW_HEIGHT = board.rows * 25
WINDOW_WIDTH = board.columns * 25

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT + 50))
os.environ['SDL_VIDEO_CENTERED'] = '100'

board_panel = BoardPanel(board, WINDOW_WIDTH, WINDOW_HEIGHT)
title_bar = TitleBar(board_panel, command=hit)

def main():
    screen.fill(GREY)

    running = True
    # board_panel.draw_board(screen)

    while running:
        global board
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            board_panel.get_event(event, board)
            title_bar.get_event(event, board)

        #global board

        # reset_board(title_bar, board)
        if title_bar.is_reset_board is True:
            print("Hello")
            new_row = board.rows
            new_col = board.columns
            board = Board(new_row, new_col)
            # board.reset_bitboard()
        board_panel.draw_board(screen)
        title_bar.draw(screen)
        pygame.display.update()


main()
