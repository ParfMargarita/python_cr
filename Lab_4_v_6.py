run_program = 'y'
while run_program == 'Y' or run_program == 'y':
    import numpy
    import random
    n = int(input('Enter the size of array: \n'))
    M = []

    for i in range(n):
        m = random.randint(0, 99)
        M.append(m)

    print('Array:')
    print(M)

    number = int(input('Enter the item to be deleted: \n'))
    i = 0
    while i < len(M):
        if M[i] == number:
            M.pop(i)
        else:
            i += 1

    print('Array:')
    print(M)
    run_program = str(input('Do you want to repeat the program?\n Yes - press Y or y\n No - press any character.\n'))
