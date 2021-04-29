def _sum(N1, D1, N2, D2):
    numerator = (N1*D2 + N2*D1)
    denominator = (D1*D2)
    return '{}/{}'.format(numerator, denominator)


def _subtraction(N1, D1, N2, D2):
    numerator = (N1*D2 - N2*D1)
    denominator = (D1*D2)
    return '{}/{}'.format(numerator, denominator)


def _multiplication(N1, D1, N2, D2):
    numerator = (N1*N2)
    denominator = (D1*D2)
    return '{}/{}'.format(numerator, denominator)


def _division(N1, D1, N2, D2):
    numerator = (N1*D2)
    denominator = (N2*D1)
    return '{}/{}'.format(numerator, denominator)


# dictionary relating operators with functions
oper_functions = {'+': _sum,
                  '-': _subtraction,
                  '*': _multiplication,
                  '/': _division}


def _simplifier(fraction):
    numerator, denominator = fraction.split(sep='/')
    min_value = min(abs(int(numerator)), abs(int(denominator)))
    if min_value == 0:
        numerator = 0
        denominator = 1
    else:
        for i in range(min_value, 0, -1):
            if (int(numerator) % i == 0) and (int(denominator) % i == 0):
                break

        numerator = int(numerator) // i
        denominator = int(denominator) // i
    return '{}/{}'.format(numerator, denominator)


def rational(expression):
    N1, _, D1, operation, N2, _, D2 = expression.split()
    first_fraction = oper_functions[operation](
        int(N1), int(D1), int(N2), int(D2))
    second_fraction = _simplifier(first_fraction)
    return ' = '.join([first_fraction, second_fraction])


if __name__ == "__main__":
    N = eval(input())
    for _ in range(N):
        expression = input()
        print(rational(expression))