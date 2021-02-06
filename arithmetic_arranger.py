def arithmetic_arranger(problems, condition = bool):
    problems_list = []
    width_list = []
    height = 3
    format_list = []
    x = []
    # Check for too many problems
    if len(problems) > 5:
        return 'Error: Too many problems.'
    # Loop through all the given problems
    for i in range(len(problems)):
        # Simplify the parts of the equations
        split_problems = problems[i].split()
        top, operator, bottom = split_problems[:]
        # Check that the numbers are digits
        if not top.isnumeric() or not bottom.isnumeric():
            return 'Error: Numbers must only contain digits.'
        # Create the design layout   
        width = len(max(split_problems, key=len)) + 2
        width_list.append(width)
        dashes = width*'-'
        arranged_problem = top.rjust(width) + '\n' + operator + ' ' + bottom.rjust(width-2) + '\n' + dashes + '\n'
        # Create error for max length
        if width > 6:
            return 'Error: Numbers cannot be more than four digits.'
        # Create answer condition and check operator error condition
        if operator == '+':
            answer = int(top) + int(bottom)
        elif operator == '-':
            answer = int(top) - int(bottom)
        else:
            return 'Error: Operator must be \'+\' or \'-\'.'
        if condition == True:
            arranged_problem += str(answer).rjust(width) + '\n'
            height = 4
        # Add each answer to the list of answers
        problems_list.append(arranged_problem)
    # Make everything a formatted string
    joined_list = ''.join(problems_list)
    for i in range(height):
        format_list.append(joined_list.splitlines()[i::height])
    for i in format_list:
        lines = '    '.join(i)
        x.append(lines + '\n')
    final = ''.join(x).rstrip()
    return final

print(arithmetic_arranger(["5434 - 12", '34 + 5', '17 - 27', '432 + 5423', '1 + 4'], True))
print(arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]))
