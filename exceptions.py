# print(1 + 'hi')
# print('we will never get here')

# def print_sum(num1, num2):
#     try:
#         print('Sum:', num1 + num2)
#     except Exception:
#         print('Could not add those numbers.')

def print_sum(num1, num2):
    if type(num1) != int or type(num2) != int:
        raise Exception('Inputs to the print_sum function must be ints')
    print('Sum:', num1 + num2)

print_sum(1, 3)

try:
    print_sum(1, 'hi')
except Exception as e:
    print(f'Something went wrong: {e}')