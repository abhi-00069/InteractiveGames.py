class Chess:
    def __init__(self):
        self.board = [
            ['r','n','b','q','k','b','n','r'],
            ['p','p','p','p','p','p','p','p'],
            ['.','.','.','.','.','.','.','.'],
            ['.','.','.','.','.','.','.','.'],
            ['.','.','.','.','.','.','.','.'],
            ['.','.','.','.','.','.','.','.'],
            ['P','P','P','P','P','P','P','P'],
            ['R','N','B','Q','K','B','N','R']
        ]
        self.turn = 'white'

    def print_board(self):
        print()
        for i in range(8):
            print(8-i, end=" ")
            print(*self.board[i])
        print("  a b c d e f g h\n")

    def pos(self, s):
        col = ord(s[0]) - ord('a')
        row = 8 - int(s[1])
        return row, col

    def inside(self, r, c):
        return 0 <= r < 8 and 0 <= c < 8

    def clear_path(self, r1, c1, r2, c2):
        dr = (r2-r1)
        dc = (c2-c1)
        if dr != 0:
            dr //= abs(dr)
        if dc != 0:
            dc //= abs(dc)

        r = r1 + dr
        c = c1 + dc
        while (r, c) != (r2, c2):
            if self.board[r][c] != '.':
                return False
            r += dr
            c += dc
        return True

    def valid(self, r1, c1, r2, c2):
        if not (self.inside(r1,c1) and self.inside(r2,c2)):
            return False

        p = self.board[r1][c1]
        t = self.board[r2][c2]

        if p == '.':
            return False

        if self.turn == "white" and not p.isupper():
            return False
        if self.turn == "black" and not p.islower():
            return False

        if t != '.':
            if p.isupper() == t.isupper():
                return False

        dr = r2-r1
        dc = c2-c1
        piece = p.lower()

        if piece == 'p':
            d = -1 if p.isupper() else 1
            start = 6 if p.isupper() else 1

            if dc == 0:
                if dr == d and t == '.':
                    return True
                if r1 == start and dr == 2*d and t == '.' and self.board[r1+d][c1] == '.':
                    return True
            elif abs(dc) == 1 and dr == d and t != '.':
                return True
            return False

        if piece == 'r':
            return (dr == 0 or dc == 0) and self.clear_path(r1,c1,r2,c2)

        if piece == 'b':
            return abs(dr) == abs(dc) and self.clear_path(r1,c1,r2,c2)

        if piece == 'q':
            if dr == 0 or dc == 0 or abs(dr) == abs(dc):
                return self.clear_path(r1,c1,r2,c2)
            return False

        if piece == 'n':
            return (abs(dr), abs(dc)) in [(2,1),(1,2)]

        if piece == 'k':
            return max(abs(dr), abs(dc)) == 1

        return False

    def move(self, a, b):
        try:
            r1,c1 = self.pos(a)
            r2,c2 = self.pos(b)
        except:
            print("Invalid input.")
            return

        if not self.valid(r1,c1,r2,c2):
            print("Illegal move.")
            return

        self.board[r2][c2] = self.board[r1][c1]
        self.board[r1][c1] = '.'
        self.turn = "black" if self.turn == "white" else "white"

game = Chess()

while True:
    game.print_board()
    print(game.turn.capitalize(), "to move")
    s = input("Enter move (e2 e4) or quit: ").lower()

    if s == "quit":
        break

    try:
        a, b = s.split()
        game.move(a, b)
    except:
        print("Enter moves like: e2 e4")
