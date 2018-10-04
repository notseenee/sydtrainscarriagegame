import sys
import itertools
import random

OPERATIONS = ['+', '-', '*', '/']
solutions = []

def test_seq(permutations, op, one_ans_only=False):
    for perm in permutations:
        result = perm[0]

        for i in range(1, 4):
            if (op[i - 1] == '+'):
                result += perm[i]
            if (op[i - 1] == '-'):
                result -= perm[i]
            if (op[i - 1] == '*'):
                result *= perm[i]
            if (op[i - 1] == '/'):
                if (perm[i] != 0):
                    result /= perm[i]

        if result == 10:
            output = []
            for i in range(3):
                output.append(str(perm[i]))
                output.append(op[i])
            output.append(str(perm[3]))
            solutions.append(' '.join(output))

            if one_ans_only:
                return True

def test_10(num):
    str_num = str(num)
    digits = [int(digit) for digit in str_num]
    permutations = list(itertools.permutations(digits))

    for op1 in OPERATIONS:
        for op2 in OPERATIONS:
            for op3 in OPERATIONS:
                result = test_seq(permutations, [op1, op2, op3])
                if result:
                    return

def generate_number():
    number = random.randint(1000, 9999)
    return number

def main():
    while len(solutions) == 0:
        number = generate_number()
        test_10(number)

    print('{:d} has {:d} solutions:'.format(number, len(solutions)))

    for solution in solutions:
        print(solution)

if __name__ == '__main__':
    main()
