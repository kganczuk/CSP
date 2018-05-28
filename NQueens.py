class NQueens:
    COUNTER = 0

    def __init__(self, size):
        self.size = size
        self.board = self.generate_board()
        self.solved = False
        self.count = 0
        self.values = [i for i in range(self.size)]
        self.variables = [i for i in range(self.size)]

    def print_solution(self):
        print("Size:", self.size, "\nCount: ", self.count)
        for row in self.board:
            print(str(row).replace('1', 'X').replace(', ', '|').replace('[', '|').replace(']', '|').replace('0', ' '))
        print()

    def is_safe(self, row, col):
        for iy in range(self.size):
            if self.board[row][iy] == 1:
                return False

        ix, iy = row, col
        while ix >= 0 and iy >= 0:
            if self.board[ix][iy] == 1:
                return False
            ix-=1
            iy-=1

        jx, jy = row,col
        while jx < self.size and jy >= 0:
            if self.board[jx][jy] == 1:
                return False
            jx+=1
            jy-=1

        kx, ky = row,col
        while kx < self.size and ky < self.size:
            if self.board[kx][ky] == 1:
                return False
            kx+=1
            ky+=1

        lx, ly = row,col
        while lx >= 0 and ly < self.size:
            if self.board[lx][ly] == 1:
                return False
            lx-=1
            ly+=1

        return True

    def generate_variables(self):
        return [i for i in range(self.size)]

    def generate_board(self):
        return [[0 for _ in range(self.size)] for _ in range(self.size)]

    def set_next_value(self, value, variable):
        self.board[value][variable] = 1
        self.count += 1

    def set_previous_value(self, value, variable):
        self.board[value][variable] = 0

    def generate_values(self):
        return dict([(i, [j for j in range(self.size)]) for i in range(self.size)])

    def generate_empty_variables(self):
        return dict([(i, []) for i in range(self.size)])

    def set_solved(self):
        self.solved = True
        return True

    def get_values(self):
        return self.values

    def get_variables(self):
        return self.variables
