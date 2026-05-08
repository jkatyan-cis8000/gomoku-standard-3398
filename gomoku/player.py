from .core import BLACK, WHITE


class Player:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def get_name(self):
        return "Black" if self.color == BLACK else "White"


class PlayerManager:
    def __init__(self):
        self.players = [Player(BLACK), Player(WHITE)]
        self.current_index = 0

    def get_current_player(self):
        return self.players[self.current_index]

    def get_next_player(self):
        return self.players[1 - self.current_index]

    def switch(self):
        self.current_index = 1 - self.current_index

    def parse_move(self, input_str):
        """Parse user input like '5 5' or '5,5' into (row, col) tuple."""
        parts = input_str.strip().replace(',', ' ').split()
        if len(parts) != 2:
            return None, None
        try:
            row = int(parts[0])
            col = int(parts[1])
            if 0 <= row < 15 and 0 <= col < 15:
                return row, col
            return None, None
        except ValueError:
            return None, None
