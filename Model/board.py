import numpy as np

# Default size of board
from Model.tile import Tile

DEFAULT_ROWS = 20
DEFAULT_COLUMNS = 20

# Bit representations
BOMB = 'B'
EMPTY = '-'

UNREVEALED = '#'
QUESTION = '?'
FLAG = '!'

# Default chances of tile having bomb
BOMB_CHANCE = 15

# Minimum of bombs, might have conflict with bomb chances
BOMB_MIN = 3


# Board class including all properties
class Board:
    def __init__(self, rows=None, columns=None):
        # If no row and columns inputted then use default values other wise use input
        if rows is not None and columns is not None:
            self.rows = rows
            self.columns = columns
            self.num_of_tiles = rows * columns
        else:
            self.rows = DEFAULT_ROWS
            self.columns = DEFAULT_COLUMNS
            self.num_of_tiles = DEFAULT_ROWS * DEFAULT_COLUMNS

        # Bit representation of board
        self.bitboard = []

        # Init Board
        self.init_board()

        # Check if user lost
        self.is_lost = False

        # Generate Bomb counters
        self.init_bomb_counters()

    # Method to init board
    def init_board(self):
        # Make bitboard with appropriate dimensions and adding tile to all
        for row in range(self.rows):
            column = []
            for col in range(self.columns):
                tile = self.generate_tile(row, col)
                column.append(tile)

            self.bitboard.append(column)
        self.check_minimum_bombs()

    # Generate tile with bomb or without
    def generate_tile(self, row, col):
        val = np.random.randint(100)
        if val <= BOMB_CHANCE:
            tile = Tile(row, col, True)
        else:
            tile = Tile(row, col, False)
        return tile

    # Makes sure board meets the minimum requirement of bombs
    def check_minimum_bombs(self):
        counter = 0
        for row in self.bitboard:
            for tile in row:
                if tile.is_bomb:
                    counter = counter + 1
        if counter < BOMB_MIN:
            print(BOMB_MIN - counter)
            for i in range(BOMB_MIN - counter):
                self.generate_bomb()

    # Generates the rest of the bombs
    def generate_bomb(self):
        rand_row = np.random.randint(self.rows)
        rand_col = np.random.randint(self.columns)

        if self.bitboard[rand_row][rand_col].is_bomb:
            self.generate_bomb()

        self.bitboard[rand_row][rand_col] = Tile(rand_row, rand_col, True)

    # Initialize bomb counter on each tile unless it is a bomb
    def init_bomb_counters(self):
        for row in range(len(self.bitboard)):
            for col in range(len(self.bitboard[0])):
                self.bitboard[row][col].find_bombs_in_radius(self)

    def reset_bitboard(self):
        self.init_board()
        self.init_bomb_counters()

    # Print bit board
    def print_board_xray(self):
        print(end="     ")
        for col in range(self.columns):
            print(col, end=" ")
        print()
        print()
        for row in range(len(self.bitboard)):
            print(row, "  ", end=" ")
            for col in range(len(self.bitboard[0])):
                if self.bitboard[row][col].is_bomb:
                    print(BOMB, end=" ")
                elif self.bitboard[row][col].bomb_counter != 0:
                    print(self.bitboard[row][col].bomb_counter, end=" ");
                else:
                    print(EMPTY, end=" ")
            print()

    def print_board(self):
        print(end="     ")
        for col in range(self.columns):
            print(col, end=" ")
        print()
        print()
        for row in range(len(self.bitboard)):
            print(row, "  ", end=" ")
            for col in range(len(self.bitboard[0])):
                if self.bitboard[row][col].is_revealed is False:
                    print(UNREVEALED, end=" ")
                else:
                    if self.bitboard[row][col].is_bomb:
                        print(BOMB, end=" ")
                    elif self.bitboard[row][col].bomb_counter != 0:
                        print(self.bitboard[row][col].bomb_counter, end=" ");
                    else:
                        print(EMPTY, end=" ")
            print()

