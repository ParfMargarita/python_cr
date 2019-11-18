import random
import datetime
import prettytable
import matplotlib.pyplot as plt

def selection_sort(A):
    for i in range(len(A)):
        current_val = A[i]
        index_min = i
        j = i + 1
        while j < len(A):
            if A[j] < A[index_min]:
                index_min = j
            j += 1
        A[i] = A[index_min];
        A[index_min] = current_val


def insertion_sort(A):
    for i in range(len(A)):
        min = A[i]
        j = i
        while j > 0:
            if A[j - 1] > min:
                A[j] = A[j - 1]
                A[j - 1] = min
            j -= 1

A = []
B = []

table = prettytable.PrettyTable(['Array size', 'Selection time', 'Insertion time'])
x = []
y1 = []
y1 = []


for n in range(10, 50, 10):
    x.append(n)
    for i in range(random.randint(5, 50)):
        a = random.randint(0, 1000)
        A.append(a)

    B = A.copy()

    print('Before sorting:\n',A)

    t1 = datetime.datetime.now()
    selection_sort(A)
    t2 = datetime.datetime.now()
    y1.append((t2 - t1).total_seconds())

    print('\nAfter selection sorting :\n', A)


    t3 = datetime.datetime.now()
    insertion_sort(B)
    t4 = datetime.datetime.now()
    y1.append((t4 - t3).total_seconds())

    print('\nAfter insertion sorting :\n',B)

    table.add_row([str(n), str((t2 - t1).total_seconds()), str((t4 - t3).total_seconds()) ])
print(table)

plt.plot(x, y1, 'C0')
plt.plot(x, y2, 'C1')
plt.show()