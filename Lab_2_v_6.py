import numpy
print('Введите значениие ')
b = -5.4
m = 4
u = 0.05E-4

v = u + b - 2 * pow((0.7*k+m),0.5)
w = 100 * numpy.exp(-0.2 * u) - numpy.log(8.1 * u)

for k in numpy.arange(6, 4, 0.3, -7):
    v = u + b - 2 * pow((0.7 * k + m), 0.5)
    w = 100 * numpy.exp(-0.2 * u) - numpy.log(8.1 * u)
