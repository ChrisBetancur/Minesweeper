from Model.board import Board


def reveal(board, input_tile):
    empty_body = [input_tile]
    if input_tile.is_bomb:
        board.is_lost = True
    else:
        if input_tile.bomb_counter == 0 and input_tile.is_bomb is False:
            empty_body = determine_empty_body(input_tile, empty_body, board)
            determine_border(empty_body, board)

    for tile in empty_body:
        tile.is_revealed = True

    board.print_board_xray()


'''def determine_empty_body(tile, list, board):
    
    
    radius = tile.determine_radius(board)

    for curr_tile in radius:
        if curr_tile.is_bomb is False:
            if curr_tile.bomb_counter > 0:
                list.append(curr_tile)
            else:
                list.append(curr_tile)
                determine_empty_body(curr_tile, list, board)
        else:
            return list'''


# Calculate all empty bodies using Breadth-First search, useless function
def determine_all_empty_body(tile, body, board):
    queue = []
    visited = []

    queue.append(tile)
    visited.append(tile)

    while queue:
        tile = queue.pop(0)

        for curr_tile in tile.determine_radius(board):
            present = False
            if len(visited) != 0:
                for visited_tile in visited:
                    if visited_tile.equals(curr_tile):
                        present = True

            if present is False and curr_tile.is_bomb is not True:
                visited.append(curr_tile)
                queue.append(curr_tile)
                if curr_tile.bomb_counter == 0:
                    body.append(curr_tile)

    return body


# After calculating empty body, minesweeper must reveal the border which is bomb counters
def determine_border(body, board):
    if body is not None:
        for tile in body:
            for neighbour in tile.determine_radius(board):
                if neighbour.is_bomb is False and neighbour.bomb_counter > 0:
                    neighbour.is_revealed = True


# Calculate the empty body where the user selected using Breadth-First search
def determine_empty_body(tile, body, board):
    queue = []
    visited = []

    queue.append(tile)
    visited.append(tile)

    while queue:
        tile = queue.pop(0)

        for curr_tile in tile.determine_radius(board):
            present = False
            if len(visited) != 0:
                for visited_tile in visited:
                    if visited_tile.equals(curr_tile):
                        present = True

            if present is False and curr_tile.is_bomb is not True and curr_tile.bomb_counter == 0:
                visited.append(curr_tile)
                queue.append(curr_tile)
                if curr_tile.bomb_counter == 0:
                    body.append(curr_tile)

    return body


def reset_board(title_bar, board):
    if title_bar.is_reset_board is True:
        new_board = Board(board.rows, board.columns)
        return new_board
    return board