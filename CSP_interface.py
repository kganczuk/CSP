class LatinSquare:

    def __init__(self, size):
        self.size = size
        self.board = self.generate_board()
        self.solved = False
        self.count = 0
        self.values = [i for i in range(self.size)]
        self.variables = [i for i in range(self.size)]
        self.previous_values = self.generate_empty_variables()

    def print_solution(self):
        print("Size:", self.size, "\nCount: ", self.count, '\nSuccess: ', self.solved)
        for row in self.board:
            print(row)
        print()

    def is_safe(self, value, variable):
        x, y = variable
        for iy in range(self.size):
            if self.board[x][iy] == value:
                return False

        for ix in range(self.size):
            if self.board[ix][y] == value:
                return False
        return True

    def generate_board(self):
        return [[-1 for _ in range(self.size)] for _ in range(self.size)]

    def generate_variables(self):
        variables = []
        for i in range(self.size):
            for j in range(self.size):
                variables.append((i,j))
        return variables

    def set_next_value(self, value, variable):
        x, y = variable
        self.previous_values[variable].append(self.board[x][y])
        self.board[x][y] = value
        self.count += 1

    def set_previous_value(self, value, variable):
        x, y = variable
        self.board[x][y] = self.previous_values[variable].pop()

    def generate_values(self):
        values = dict()
        for i in range(self.size):
            for j in range(self.size):
                values[(i, j)] = [k for k in range(self.size)]
        return values

    def generate_empty_variables(self):
        values = dict()
        for i in range(self.size):
            for j in range(self.size):
                values[(i, j)] = []
        return values

    def set_solved(self):
        self.solved = True
        return True

    def get_values(self):
        return self.values

    def get_variables(self):
        return self.variables
