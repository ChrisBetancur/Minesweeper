import pygame

from Attributes.game_attributes import reveal
from Model.board import Board

DEFAULT_PATH = "C:/Users/chris/PycharmProjects/Minesweeper Game/Images/"
DEFAULT_NUMBERS_PATH = "C:/Users/chris/PycharmProjects/Minesweeper Game/Images/DisplayNumbers/"

UNREVEALED = "C:/Users/chris/PycharmProjects/Minesweeper Game/Images/unRevealed.png"
BOMB = "C:/Users/chris/PycharmProjects/Minesweeper Game/Images/bomb.png"
SMILEY = "C:/Users/chris/PycharmProjects/Minesweeper Game/Images/smiley.png"
DEAD_SMILEY = "C:/Users/chris/PycharmProjects/Minesweeper Game/Images/deadsmiley.png"


class Button:
    def __init__(self, command, image_path, x_pos, y_pos, tile):
        self.tile = tile
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.center = (x_pos, y_pos)
        self.function = command
        self.is_paused = None

    def set_paused(self, is_paused):
        self.is_paused = is_paused

    def get_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return self.on_click(event)

    def on_click(self, event):
        if self.rect.collidepoint(event.pos):
            self.function()

    def draw(self, surf):
        surf.blit(self.image, self.rect)


class TilePanel:
    def __init__(self, command, image_path, tile):
        self.tile = tile
        self.x_pos = 0
        self.y_pos = 0
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.function = command
        self.is_paused = None

    def set_pos(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        # print(self.x_pos, ",", self.y_pos)
        self.rect.center = (x_pos, y_pos)

    def set_paused(self, is_paused):
        self.is_paused = is_paused

    def get_event(self, event, board):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.on_click(event, board)

    def on_click(self, event, board):
        if self.rect.collidepoint(event.pos):
            self.function(self, board)

    def draw(self, surf):
        surf.blit(self.image, self.rect)


def reveal_tile(tile_panel, board):
    if board.is_lost is False:
        reveal(board, tile_panel.tile)


def flag_tile():
    print()


def question_tile():
    print()


class BoardPanel:
    def __init__(self, board, window_width, window_height):
        self.board_tiles = []
        self.board = board
        self.width = window_width
        self.height = window_height

        for row in board.bitboard:
            for tile in row:
                tile_rep = TilePanel(command=reveal_tile, image_path=UNREVEALED, tile=tile)
                self.board_tiles.append(tile_rep)

    def draw_board(self, screen):
        increment = 25

        index = 0
        for x in range(0, self.width, increment):
            for y in range(0, self.height, increment):
                self.board_tiles[index].set_pos(y + 12, x + 62)
                self.board_tiles[index].draw(screen)
                index = index + 1

    def get_event(self, event, board):
        for tile_panel in self.board_tiles:
            tile_panel.get_event(event, board)
        self.update()

    def update(self):
        for tile_panel in self.board_tiles:
            if tile_panel.tile.is_revealed:
                if tile_panel.tile.is_bomb:
                    tile_panel.image = pygame.image.load(BOMB)
                if tile_panel.tile.bomb_counter == 0 and tile_panel.tile.is_bomb is False:
                    tile_panel.image = pygame.image.load(DEFAULT_PATH + "0.png")
                if tile_panel.tile.bomb_counter > 0:
                    tile_panel.image = pygame.image.load(DEFAULT_PATH + str(tile_panel.tile.bomb_counter) + ".png")


class TitleBar:
    def __init__(self, board_panel, command):
        self.image = pygame.image.load(SMILEY)
        self.is_smiley = True
        self.is_reset_board = False
        self.function = command
        self.rect = self.image.get_rect()
        self.rect.center = (board_panel.width / 2, 25)

    def draw(self, surf):
        surf.blit(self.image, self.rect)

    def get_event(self, event, board):
        reveal_if_lost(self, board)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.on_click(event, board)

    def on_click(self, event, board):
        if self.rect.collidepoint(event.pos):
            self.function(self, board)

    def draw(self, surf):
        surf.blit(self.image, self.rect)


def hit(title_bar, board):
    title_bar.image = None
    if title_bar.is_smiley:
        title_bar.image = pygame.image.load(DEAD_SMILEY)
        title_bar.is_smiley = False
    else:
        title_bar.image = pygame.image.load(SMILEY)
        #board = Board()
        board.init_board()
        # title_bar.is_reset_board = True
        title_bar.is_smiley = True


def reveal_if_lost(title_bar, board):
    if board.is_lost is True:
        title_bar.image = pygame.image.load(DEAD_SMILEY)
        title_bar.is_smiley = False
