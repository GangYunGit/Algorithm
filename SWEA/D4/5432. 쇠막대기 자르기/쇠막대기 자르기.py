for test_case in range(1, int(input()) + 1):
    info = input()
    left_bracket = 0
    right_bracket = 0
    stick = 0
    result = 0
    former_bracket = ''
    for bracket in info:
        if bracket == '(':
            if former_bracket == '(':
                stick += 1
            former_bracket = '('

        if bracket == ')':
            if former_bracket == '(':
                result += stick
            else:
                stick -= 1
                result += 1
            former_bracket = ')'

    print(f'#{test_case} {result}')