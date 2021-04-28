from Model.board import Board
from Attributes.game_attributes import reveal

board = Board(9, 9)

print("XRAY")
board.print_board_xray()

print()
print()

reveal(board, board.bitboard[4][4])

board.print_board()

print()
print()
