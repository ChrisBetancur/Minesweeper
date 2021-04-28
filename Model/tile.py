# Tile Class for Minesweeper

class Tile:
    def __init__(self, row, col, is_bomb):
        # The row and col of tile
        self.row = row
        self.col = col

        # Computer generated
        self.is_bomb = is_bomb

        # User Generated
        self.has_flag = False
        self.has_question = False
        self.is_revealed = False

        # Number of bombs next to tile
        self.bomb_counter = 0

    def find_bombs_in_radius(self, board):
        tiles = self.determine_radius(board)
        self.find_bombs(tiles)

    # Puts all tiles in radius in list
    def determine_radius(self, board):
        curr_row = self.row
        curr_col = self.col
        tiles = []

        if validate_position(curr_row + 1, curr_col, board):
            tiles.append(board.bitboard[curr_row + 1][curr_col])

        if validate_position(curr_row + 1, curr_col - 1, board):
            tiles.append(board.bitboard[curr_row + 1][curr_col - 1])

        if validate_position(curr_row, curr_col - 1, board):
            tiles.append(board.bitboard[curr_row][curr_col - 1])

        if validate_position(curr_row - 1, curr_col - 1, board):
            tiles.append(board.bitboard[curr_row - 1][curr_col - 1])

        if validate_position(curr_row - 1, curr_col, board):
            tiles.append(board.bitboard[curr_row - 1][curr_col])

        if validate_position(curr_row - 1, curr_col + 1, board):
            tiles.append(board.bitboard[curr_row - 1][curr_col + 1])

        if validate_position(curr_row, curr_col + 1, board):
            tiles.append(board.bitboard[curr_row][curr_col + 1])

        if validate_position(curr_row + 1, curr_col + 1, board):
            tiles.append(board.bitboard[curr_row + 1][curr_col + 1])

        return tiles

    # Counts tiles that contains bombs
    def find_bombs(self, tiles):
        counter = 0
        for tile in tiles:
            if tile.is_bomb and self.is_bomb is False:
                counter = counter + 1
        self.bomb_counter = counter

    def to_string(self):
        if self.is_bomb:
            return "B"

    def equals(self, tile):
        if self.row == tile.row and self.col == tile.col:
            return True
        return False


def validate_position(row, col, board):
    if board.rows > row >= 0 and board.columns > col >= 0:
        return True
    return False
