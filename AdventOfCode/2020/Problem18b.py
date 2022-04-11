import re
# expression = '1 + (2 * 3) + (4 * (5 + 6))'
# expression = expression.replace(' ', '')

def evaluate_expression2(expr):
    """Recursively evaluates a subexpression"""
    # 54*210+6 sign at index 6
    # print('Evaluating: ', expr)
    nums = re.findall(r'\b\d+\b', expr, re.M)
    signs = re.findall(r'[*+]', expr, re.M)
    term_number = len(nums)
    if term_number == 2:
        sign = '*' if expr.find('*') != -1 else '+'
        if sign == '*':
            return str(int(nums[0]) * int(nums[1]))
        if sign == '+':
            return str(int(nums[0]) + int(nums[1]))
    else:
        # find the left most addition sign if none use left most mult sign
        found = expr.find('+')
        if found != -1:
            # find the result of the left most + expression and replace it
            for i, sign in enumerate(signs):
                if sign == '+':
                    sub_expr = nums[i] + sign + nums[i + 1]
                    sub_ans = evaluate_expression2(sub_expr)
                    expr = expr.replace(sub_expr, sub_ans, 1)
                    # Iterate recursively until one sub_expr remains
                    return evaluate_expression2(expr)
        else:
            # evaluate the left most * sign
            sub_expr = nums[0] + '*' + nums[1]
            sub_ans = evaluate_expression2(sub_expr)
            expr = expr.replace(sub_expr, sub_ans, 1)
            # Iterate recursively until one sub_expr remains
            return evaluate_expression2(expr)


def parse_expression(expression: str, part=1):
    # Base case 1
    if expression.isnumeric():
        return expression
    # Base case 2
    if expression.find('(') == -1:
        sub_ans = evaluate_expression2(expression)
        # print('Returned: ', sub_ans)
        return sub_ans
    count = 0
    found = False
    lp_index = -1  # Index of left most parenthesis
    for index, item in enumerate(expression):
        if item == '(':
            lp_index = index if lp_index == -1 else lp_index
            found = True
            count += 1
        if item == ')':
            count -= 1
        if count == 0 and found:
            # Get a subexpression and call recursively on it
            sub_expr = expression[lp_index + 1:index]
            sub_expr_par = expression[lp_index:index + 1]
        # print('Sub: ', sub_expr_par)
        # print('sub without par', sub_expr)
            sub_ans = parse_expression(sub_expr)
            expression = expression.replace(sub_expr_par, sub_ans)
        # print(expression)
            return parse_expression(expression)



expressions = list()
with open('Problem18.txt') as file:
    data = file.read()
    data = data.replace(' ', '')
    for line in data.splitlines():
        line = line.rstrip()
        expressions.append(line)

# print(expressions[0])
# print(evaluate_expression('1 + 2 * 3 + 4 * 5 + 6'))
# print(parse_expression(expressions[0]))

result = sum(int(parse_expression(expr)) for expr in expressions)
print('Part 2 answer: ', result)






