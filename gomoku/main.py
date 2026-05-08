from .core import Game, BLACK, WHITE
from .player import PlayerManager
from .display import Display


def play_gomoku():
    game = Game()
    player_manager = PlayerManager()
    display = Display(game)
    
    print("=== Gomoku Game ===")
    print("Players alternate placing stones on a 15x15 board.")
    print("First to get 5 stones in a row (horizontally, vertically, or diagonally) wins!")
    print("Enter moves as 'row col' (e.g., '7 7')\n")
    
    while True:
        display.render()
        
        current_player = player_manager.get_current_player()
        display.show_status(current_player.get_color())
        
        move_input = input("Enter move (row col): ")
        row, col = player_manager.parse_move(move_input)
        
        if row is None or col is None:
            print("Invalid input. Please enter two numbers between 0 and 14, separated by space.")
            continue
        
        if not game.make_move(row, col):
            print("Invalid move. Position is already occupied or out of bounds.")
            continue
        
        # Check for win
        if game.check_win(row, col):
            display.render()
            display.show_status(game.current_player, game_over=True, winner=current_player.get_name())
            break
        
        # Check for draw
        if game.is_board_full():
            display.render()
            display.show_status(game.current_player, game_over=True, winner=None)
            break
        
        player_manager.switch()


if __name__ == "__main__":
    play_gomoku()
