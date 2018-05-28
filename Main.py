from NQueens import *
from LatinSquare import *
from Sudoku import *
from CSP import *
import time
import cProfile


if __name__ == "__main__":


    # file_name = 'CSP_results_final2'
    #
    # with open('./'+file_name+'.csv', 'w+') as file:
    #     file.write(';;Size;Success;Count;Time\n')
    #     for x in range(4, 20+1):
    #         start = time.time()
    #         solution, success = solve(NQueens(x), 'BT')
    #         end = time.time()
    #
    #         file.write(';;' + str(x) + ';' + str(success) + ';' + str(solution.count) + ';' +
    #                    str(end - start).replace('.', ',') + '\n')
    #     print('Backtracking end')
    #     for var_h in range(len(variable_heuristics)):
    #         for val_h in range(len(value_heuristics)):
    #             file.write('\nVariable Heuristic;Value Heuristic;Size;Success;Count;Time\n')
    #             for x in range(4, 20+1):
    #                 start = time.time()
    #                 solution, success = solve(NQueens(x), 'FC', var_h, val_h)
    #                 end = time.time()
    #                 file.write(variable_heuristics[var_h] + ';' + value_heuristics[val_h] + ';' + str(x) + ';' +
    #                            str(success) + ';' + str(solution.count) + ';' + str(end - start).replace('.', ',') + '\n')
    #             print('Forward checking ', variable_heuristics[var_h], ' ', value_heuristics[val_h], ' end')

    size = 0
    loop = True
    while size > 0 or loop:
        loop = False
        print ('1: N Que1ens, 2: Latin Square, 3: Sudoku, 4: Exit')
        problem = int(input('Problem CSP: '))
        if problem == 4:
            break
        size = int(input('Rozmiar tablicy: '))
        print ('1: Backtracking, 2: Forward Checking')
        algorithm_id = int(input('Algorytm: '))
        algorithm = var_h = val_h = None
        if algorithm_id == 1:
            algorithm = 'BT'
        elif algorithm_id == 2:
            algorithm = 'FC'
            print('0: FIRST,1: MEDIUM, 2: MOST_CONSTRAINED, 3: LESS CONSTRAINED')
            var_h = int(input('Heurystyka wyboru zmiennej: '))
            val_h = int(input('Heurystyka wyboru wartości: '))
        else:
            pass
        print('Working...')

        if problem == 1:
            CSP = NQueens(size)
        elif problem == 2:
            CSP = LatinSquare(size)
        elif problem == 3:
            CSP = Sudoku(size)

        start = time.time()
        solution, success = solve(CSP, algorithm, var_h, val_h)
        end = time.time()
        print('Time: ', end-start)
        solution.print_solution()
        # cProfile.run('solve(NQueens(size), algorithm, var_h, val_h)')
