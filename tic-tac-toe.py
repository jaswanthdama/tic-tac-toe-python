class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]  # 3x3 board as a list
        self.current_player = "X"

    def display_board(self):
        print()
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print("|".join(row))
            print("-" * 5)
        print()

    def make_move(self, position):
        if self.board[position] == " ":
            self.board[position] = self.current_player
            return True
        return False

    def check_winner(self):
        b = self.board
        lines = [
            [b[0], b[1], b[2]], [b[3], b[4], b[5]], [b[6], b[7], b[8]],  # rows
            [b[0], b[3], b[6]], [b[1], b[4], b[7]], [b[2], b[5], b[8]],  # cols
            [b[0], b[4], b[8]], [b[2], b[4], b[6]]                       # diagonals
        ]
        return [self.current_player]*3 in lines

    def is_draw(self):
        return " " not in self.board

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def play(self):
        print("🎮 Welcome to Tic-Tac-Toe!")
        self.display_board()

        while True:
            try:
                position = int(input(f"Player {self.current_player}, enter position (1-9): ")) - 1
                if position not in range(9):
                    print("⚠️ Invalid position! Choose from 1 to 9.")
                    continue
                if not self.make_move(position):
                    print("❌ Spot already taken!")
                    continue
            except ValueError:
                print("⚠️ Please enter a number.")
                continue

            self.display_board()

            if self.check_winner():
                print(f"🎉 Player {self.current_player} wins!")
                break
            elif self.is_draw():
                print("🤝 It's a draw!")
                break

            self.switch_player()

# Run the game
if __name__ == "__main__":
    game = TicTacToe()
    game.play()
