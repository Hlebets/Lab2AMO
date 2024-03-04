import math
import matplotlib.pyplot as plt

def f(x, a):
    return math.exp(a * x) * (1 + x * x) * math.sin(x) / (x + 2)


def simpson(a, b, n, ai):
    h = 0.001
    summ = f(a, a) + f(b, a)
    for i in range(1, n):
        k = 2 + 2 * (i % 2)
        summ += k * f(a + i * h, ai)
    summ *= h / 3
    return summ


a = [0.019, 0.127, 0.346, 0.417, 0.527, 0.696]
print("a\t     integral")
for i in range(6):
    ai = a[i]
    result = simpson(0, 1, 1000, ai)
    print(ai, "\t", result)

plt.plot(a, [simpson(0, 1, 1000, ai) for ai in a])
plt.show()
