class Sudoku:

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
        if self.board[x][y] != -1 and self.previous_values[variable] == []:
            return False

        for x in range(self.size):
            if self.board[x][y] == value:
                return False

        box = (int(variable[0]/3), int(variable[1]/3))
        x_start, y_start = 3 * box[0], 3 * box[1]
        for x in range(x_start, x_start + 3):
            if x in range(0, self.size):
                if x == variable[0]:
                    if value in self.board[x]:
                        return False
                for y in range(y_start, y_start + 3):
                    if x < self.size and y < self.size:
                        if self.board[x][y] == value:
                            return False

        return True

    def generate_board(self):
        board = [[-1 for _ in range(self.size)] for _ in range(self.size)]
        # board = [[1, -1, -1, 5, -1, 6, 4, -1, -1],
        #          [-1, -1, -1, -1, -1, -1, -1, 8, 5],
        #          [5, -1, 6, -1, -1, 0, 2, -1, -1],
        #          [-1, 4, -1, 6, 2, 1, -1, -1, -1],
        #          [-1, 6, -1, -1, -1, -1, -1, 1, -1],
        #          [-1, -1, -1, 0, 7, 8, -1, 6, -1],
        #          [-1, -1, 2, 4, -1, -1, 5, -1, 3],
        #          [7, 3, -1, -1, -1, -1, -1, -1, -1],
        #          [-1, -1, 4, 1, -1, 5, -1, -1, 7]]

        return board

    def generate_variables(self):
        variables = []
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == -1:
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
                if self.board[i][j] > -1:
                    values[i, j] = []
                else:
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
