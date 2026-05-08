from .core import EMPTY


class Display:
    def __init__(self, game):
        self.game = game

    def render(self):
        board = self.game.board
        print("\n   " + " ".join(f"{i:2d}" for i in range(15)))
        for i in range(15):
            row_str = f"{i:2d} "
            for j in range(15):
                cell = board.get_cell(i, j)
                if cell == 'B':
                    row_str += " B "
                elif cell == 'W':
                    row_str += " W "
                else:
                    row_str += " . "
            print(row_str)
        print()

    def show_status(self, current_player, game_over=False, winner=None):
        if game_over:
            if winner:
                print(f"\nGame Over! {winner} wins!")
            else:
                print("\nGame Over! It's a draw!")
        else:
            player_name = "Black" if current_player == 'B' else "White"
            print(f"\nCurrent player: {player_name} ({current_player})")
