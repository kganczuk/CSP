from copy import deepcopy

#heuristic:
NORMAL = 0
MEDIUM = 1
MOST_CONSTRAINED = 2
LESS_CONSTRAINED = 3


variable_heuristics = {0: 'NORMAL',1: 'MEDIUM', 2: 'MOST_CONSTRAINED', 3: 'LESS CONSTRAINED'}
value_heuristics = {0: 'NORMAL', 1: 'MEDIUM', 2: 'MOST CONSTRAINED', 3: 'LESS CONSTRAINED'}


def backtracking(CSP, variables_left):
    if len(variables_left) == 0:
        return CSP.set_solved()
    variable = min(variables_left)
    for value in CSP.get_values():
        if CSP.is_safe(value, variable):
            CSP.set_next_value(value, variable)
            variables_left.remove(variable)
            if backtracking(CSP, variables_left):
                return True
            else:
                variables_left.append(variable)
                CSP.set_previous_value(value, variable)
    return False


def forward_checking(CSP, variable_heuristic, value_heuristic, locked_values, variables_left, values_left):
    if len(variables_left) == 0:
        # CSP.print_solution()
        return CSP.set_solved()

    if variable_heuristic == NORMAL:
        variable = min(variables_left)
    if variable_heuristic == MEDIUM:
        variables_left = sorted(variables_left)
        variable = variables_left[int(len(variables_left)/2)]
    if variable_heuristic == MOST_CONSTRAINED:
        variable = get_most_constrained_variable(CSP, variables_left, values_left)
    if variable_heuristic == LESS_CONSTRAINED:
        variable = get_less_constrained_variable(CSP, variables_left, values_left)

    while len(values_left[variable]) > 0:
        if value_heuristic == NORMAL:
            value = values_left[variable].pop(0)
        if value_heuristic == MEDIUM:
            values_left[variable] = sorted(values_left[variable])
            value = values_left[variable].pop(int(len(values_left[variable])/2))
        if value_heuristic == MOST_CONSTRAINED:
            all_locked = []
            for i in locked_values:
                all_locked.extend(locked_values[i])
            max_count = -1
            for val in sorted(values_left[variable]):
                count = all_locked.count(val)
                if count > max_count:
                    max_count = count
                    value = val
            values_left[variable].remove(value)
        if value_heuristic == LESS_CONSTRAINED:
            all_locked = []
            for i in locked_values:
                all_locked.extend(locked_values[i])
            min_count = len(CSP.get_values())
            for val in values_left[variable]:
                count = all_locked.count(val)
                if count < min_count:
                    min_count = count
                    value = val
            values_left[variable].remove(value)

        if value not in locked_values[variable]:
            if CSP.is_safe(value, variable):
                CSP.set_next_value(value, variable)
                variables_left.remove(variable)
                if check_forward(CSP, variables_left, values_left):
                    if forward_checking(CSP, variable_heuristic, value_heuristic, deepcopy(locked_values), variables_left, deepcopy(values_left)):
                        return True
                    else:
                        CSP.set_previous_value(value, variable)
                        variables_left.append(variable)
                        locked_values[variable].append(value)
                else:
                    CSP.set_previous_value(value, variable)
                    variables_left.append(variable)
                    locked_values[variable].append(value)
                # else:
                    for v in CSP.get_variables():
                        if v not in variables_left:
                            locked_values[v] = []
    # values_left[variable] = [i for i in CSP.get_values()]
    return False


def check_forward(CSP, variables_left, values_left):
    for variable in variables_left:
        ok = True
        for value in values_left[variable]:
            if not CSP.is_safe(value, variable):
                ok = False
            else:
                ok = True
                break
        if not ok:
            return False
    return True


def get_most_constrained_variable(CSP, variables_left, values_left):
    locked_values = CSP.generate_empty_variables()
    max_locked = -1
    most_constrained = None
    for variable in sorted(variables_left):
        for value in sorted(values_left[variable]):
            if not CSP.is_safe(value, variable):
                locked_values[variable].append(value)
        if len(locked_values[variable]) > max_locked:
            max_locked = len(locked_values[variable])
            most_constrained = variable
    return most_constrained


def get_less_constrained_variable(CSP, variables_left, values_left):
    locked_values = CSP.generate_empty_variables()
    min_locked = len(CSP.get_values())
    less_constrained = None
    for variable in variables_left:
        for value in values_left[variable]:
            if not CSP.is_safe(value, variable):
                locked_values[variable].append(value)
        if len(locked_values[variable]) < min_locked:
            min_locked = len(locked_values[variable])
            less_constrained = variable
    return less_constrained

def solve(CSP, algorithm, variable_heuristic=1, value_heuristic=1):
    locked_values = CSP.generate_empty_variables()
    variables_left = CSP.generate_variables()
    values_left = CSP.generate_values()

    if algorithm == 'BT':
        return CSP, backtracking(CSP, variables_left)
    elif algorithm == 'FC':
        return CSP, forward_checking(CSP, variable_heuristic, value_heuristic, deepcopy(locked_values), variables_left, values_left)

    return None
