class TictactoeException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class Board:
    valid_moves = [
        "upper left", "upper center", "upper right",
        "middle left", "center", "middle right",
        "lower left", "lower center", "lower right"
    ]

    def __init__(self):
        self.board_array = [[" "] * 3 for _ in range(3)]
        self.turn = "X"

    def __str__(self):
        lines = []
        lines.append(f" {self.board_array[0][0]} | {self.board_array[0][1]} | {self.board_array[0][2]} \n")
        lines.append("-----------\n")
        lines.append(f" {self.board_array[1][0]} | {self.board_array[1][1]} | {self.board_array[1][2]} \n")
        lines.append("-----------\n")
        lines.append(f" {self.board_array[2][0]} | {self.board_array[2][1]} | {self.board_array[2][2]} \n")
        return "".join(lines)

    def move(self, move_string):
        if move_string not in Board.valid_moves:
            raise TictactoeException("That's not a valid move.")
        idx = Board.valid_moves.index(move_string)
        r, c = divmod(idx, 3)
        if self.board_array[r][c] != " ":
            raise TictactoeException("That spot is taken.")
        self.board_array[r][c] = self.turn
        self.turn = "O" if self.turn == "X" else "X"

    def whats_next(self):       
        cat = all(self.board_array[i][j] != " "
                  for i in range(3) for j in range(3))
        if cat:
            return True, "Cat's Game."
        # rows, cols, diags
        lines = (
            *self.board_array,
            *[[self.board_array[r][c] for r in range(3)] for c in range(3)],
            [self.board_array[i][i] for i in range(3)],
            [self.board_array[i][2 - i] for i in range(3)]
        )
        for line in lines:
            if line[0] != " " and line.count(line[0]) == 3:
                return True, f"{line[0]} wins!"
        return False, f"{self.turn}'s turn."

# ---------------- main game loop ----------------
if __name__ == "__main__":
    board = Board()
    print(board)
    while True:
        print()
        move = input(f"{board.turn}'s move (e.g. 'center'): ").strip().lower()
        try:
            board.move(move)
        except TictactoeException as e:
            print(e.message)
            continue

        print("\n" + str(board))
        done, msg = board.whats_next()
        if done:
            print(msg)
            break