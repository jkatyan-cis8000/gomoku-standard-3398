BLACK = 'B'
WHITE = 'W'
EMPTY = None
BOARD_SIZE = 15


class Board:
    def __init__(self):
        self.size = BOARD_SIZE
        self.board = [[EMPTY for _ in range(self.size)] for _ in range(self.size)]

    def place_stone(self, row, col, player):
        if not self.is_valid_move(row, col):
            return False
        self.board[row][col] = player.get_color() if hasattr(player, 'get_color') else player
        return True

    def is_valid_move(self, row, col):
        if row < 0 or row >= self.size:
            return False
        if col < 0 or col >= self.size:
            return False
        return self.board[row][col] is EMPTY

    def get_cell(self, row, col):
        return self.board[row][col]


class Game:
    def __init__(self):
        self.board = Board()
        self.current_player = BLACK

    def make_move(self, row, col):
        if self.board.place_stone(row, col, self.current_player):
            return True
        return False

    def check_win(self, row, col):
        player = self.board.get_cell(row, col)
        if player is EMPTY:
            return False

        directions = [
            [(0, 1), (0, -1)],
            [(1, 0), (-1, 0)],
            [(1, 1), (-1, -1)],
            [(1, -1), (-1, 1)]
        ]

        for direction_pair in directions:
            count = 1
            for direction in direction_pair:
                dr, dc = direction
                r, c = row + dr, col + dc
                while 0 <= r < 15 and 0 <= c < 15 and self.board.get_cell(r, c) == player:
                    count += 1
                    r += dr
                    c += dc
            if count >= 5:
                return True
        return False

    def is_board_full(self):
        for row in range(self.size):
            for col in range(self.size):
                if self.board.get_cell(row, col) is EMPTY:
                    return False
        return True

    def switch_player(self):
        if self.current_player == BLACK:
            self.current_player = WHITE
        else:
            self.current_player = BLACK
