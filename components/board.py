from components.board_tile import BoardTile


class Board:
    def __init__(self):
        self.tiles = self.create_board()

    def create_board(self):
        tiles = []
        tiles.append(BoardTile(0, 6, 5, ('D', 'E'), [(3, ['A', 'B', 'C', 'F'])]))
        tiles.append(BoardTile(1, 4, 3, ('D', 'E'), [(1, ['A', 'B'])]))
        tiles.append(BoardTile(2, 4, 3, (), [(1, ['A', 'B']), (1, ['C', 'D']), (1, ['E', 'F'])]))
        tiles.append(BoardTile(3, 3, 2, ('A', 'E'), []))
        tiles.append(BoardTile(4, 6, 5, ('B',), [(4, ['A', 'C', 'D', 'E', 'F'])]))
        tiles.append(BoardTile(5, 3, 2, ('C', 'F'), []))
        tiles.append(BoardTile(6, 5, 4, (), [(4, ['A', 'C', 'D', 'E', 'F'])]))
        tiles.append(BoardTile(7, 4, 3, (), [(2, ['A', 'B', 'F']), (1, ['D', 'E'])]))
        tiles.append(BoardTile(8, 6, 5, ('A', 'B', 'C'), [(2, ['D', 'E', 'F'])]))
        tiles.append(BoardTile(9, 4, 3, ('A',), [(1, ['D', 'E']), (1, ['B', 'C'])]))
        tiles.append(BoardTile(10, 3, 2, ('D', 'F'), []))
        tiles.append(BoardTile(11, 4, 3, (), [(3, ['A', 'C', 'D', 'F'])]))
        tiles.append(BoardTile(12, 6, 5, ('B', 'C'), [(3, ['A', 'D', 'E', 'F'])]))
        tiles.append(BoardTile(13, 5, 4, (), [(4, ['A', 'B', 'C', 'D', 'E', 'F'])]))
        tiles.append(BoardTile(14, 4, 3, ('B', 'C', 'F'), []))
        tiles.append(BoardTile(15, 5, 4, (), [(2, ['B', 'C', 'E']), (2, ['A', 'D', 'F'])]))
        return tiles
