print('Hi!', 'Esra', 've', 'İbrahim.')
print('')

other_print = print
other_print('This is just print with a new name')
print('')


def do_math(num1, num2):
    result = num1 * num2
    result = result + 10
    result = result / 1.5
    result = result - num1
    return result


print(do_math(5, 7))
print(do_math(8, 10))
print('')

import operator

print(operator.add(2, 2))  # 2 + 2
print(operator.not_(True))  # not True
print('')


def do_math(num1, num2=7):
    result = num1 * num2
    result = result + 10
    result = result / 1.5
    result = result - num1
    return result


print(do_math(5))
print(do_math(8))
print('')


def other_function(arg1, arg2='a', arg3=None, arg4=True, arg5='hello'):
    print(arg4)
    print(arg1)
    pass

other_function(1, arg4=False)
