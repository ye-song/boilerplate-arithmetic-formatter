def arithmetic_arranger(problems, A='default'):

    # Check for the number of problems submitted
    number_of_problems = len(problems)
    if number_of_problems > 5:
        return 'Error: Too many problems.'

    # Check for other rules and generate lists for formatting
    # and calculation
    n1 = []  # The first number in the string
    op = []  # op stand for operator
    n2 = []  # The second number in the string
    line = []  # The formatting line
    for i in range(number_of_problems):
        a, b, c = problems[i].strip().split()
        n1.append(a)
        op.append(b)
        n2.append(c)
        line.append('-')
        if len(n1[i]) > 4 or len(n2[i]) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        d1 = n1[i].isdigit()
        d2 = n2[i].isdigit()
        if d1 != True or d2 != True:
            return 'Error: Numbers must only contain digits.'

    if any(x == '*' for x in op):
        return "Error: Operator must be '+' or '-'."
    if any(x == '/' for x in op):
        return "Error: Operator must be '+' or '-'."

    # Calculating the sums
    ans_lst = []
    for i in range(number_of_problems):
        result = 0
        if op[i] == '+':
            result = int(n1[i]) + int(n2[i])
            ans_lst.append(result)
        elif op[i] == '-':
            result = int(n1[i]) - int(n2[i])
            ans_lst.append(result)

    # Formatting the output
    for i in range(number_of_problems):
        if len(n1[i]) == len(n2[i]):
            n1[i] = n1[i].rjust(len(n1[i]) + 2)
            n2[i] = op[i] + ' ' + n2[i].rjust(len(n2[i]))
            line[i] = line[i] * len(n1[i])
            ans_lst[i] = str(ans_lst[i]).rjust(len(n1[i]))

        elif len(n1[i]) > len(n2[i]):
            n2[i] = op[i] + ' ' + n2[i].rjust(len(n1[i]))
            n1[i] = n1[i].rjust(len(n1[i]) + 2)
            line[i] = line[i] * len(n1[i])
            ans_lst[i] = str(ans_lst[i]).rjust(len(n1[i]))

        elif len(n1[i]) < len(n2[i]):
            n1[i] = n1[i].rjust(len(n2[i]) + 2)
            n2[i] = op[i] + ' ' + n2[i]
            line[i] = line[i] * len(n2[i])
            ans_lst[i] = str(ans_lst[i]).rjust(len(n2[i]))

    x = '    '.join(n1)
    y = '    '.join(n2)
    z = '    '.join(line)
    w = '    '.join(ans_lst)

    # Returning the output
    if A == 'default':
        return ("%s\n%s\n%s" % (x, y, z))
    elif A == True :
        return ("%s\n%s\n%s\n%s" % (x, y, z, w))
