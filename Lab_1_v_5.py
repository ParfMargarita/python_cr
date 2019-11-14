'''Определить, есть ли среди заданных целых чисел A, B, C, D хотя бы одно нечётное.'''
run_program = 'y'
flag = 0
while run_program == 'Y' or run_program == 'y':
    A = int(input('Введите число A:\n'))
    B = int(input('Введите число B:\n'))
    C = int(input('Введите число C:\n'))
    if A % 2 == 1 or B % 2 == 1 or C % 2 == 1:
        print('Среди чисел есть нечетное!\n')
    else:
        print('Все числа чётные!\n')
    run_program = str(input('Повторить выполнение программы?\n Да - нажмите Y or y\n Нет - нажмите любой символ.\n'))