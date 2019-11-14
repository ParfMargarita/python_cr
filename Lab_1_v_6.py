run_program = 'y'
flag = 0
while run_program == 'Y' or run_program == 'y':
#    number = int(input('Enter a three-digit number:\n'))
    number = str(input('Enter a three-digit number:\n'))
#    while len(str(number)) != 3 or type(number) != str:
    while len(number) != 3:
        print('Failed! Please, try again.\n')
        number = input('Enter a three-digit number:\n')

#    number = str(number)
    for i in range(3):
        if number[i] == '0' or number[i] == '9':
            flag += 1
    if flag > 0:
        print('True: there are 0 or 9 among the entered numbers.\n')
    else:
        print('False: there are not  0 or 9 among the entered numbers.\n')
    run_program = str(input('Do you want to repeat the program?\n Yes - press Y or y\n No - press any character.\n'))
