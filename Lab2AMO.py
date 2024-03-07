import math
import numpy as np
import matplotlib.pyplot as plt

def f(x, a):
    return np.exp(a * x) * (1 + x * x) * np.sin(x) / (x + 2)


def simpson_integral(a, b, n, ai):
    h = 0.001
    summ = f(a, a) + f(b, a)
    for i in range(1, n):
        k = 2 + 2 * (i % 2)
        summ += k * f(a + i * h, ai)
    summ *= h / 3
    return summ


a = [0.019, 0.127, 0.346, 0.417, 0.527, 0.696]
wavalues = [0.2581540067158702, 0.2779425229697118, 0.3234648726721269, 0.3399509191810630, 0.3673539787612951, 0.4143086261231443]
print("a     | integral     | wavalues")
for i in range(6):
    ai = a[i]
    waivalues = wavalues[i]
    result = simpson_integral(0, 1, 1000, ai)
    print("{:<4} | {:<12} | {:<10}".format(ai, round(result, 9), round(waivalues, 9)))

x = np.linspace(0, 1, int((1 - 0) / 0.001) + 1)
plt.figure(figsize=(10, 7))
plt.title("Інтеграли функції при кожному а")

for ai in a:
    y = f(x, ai)
    integral = simpson_integral(0, 1, 1000, ai)
    plt.plot(x, y, label=f"а = {ai:.3f}, Int = {integral:.9f}")
    plt.fill_between(x, y, color='pink', alpha=0.4)

plt.legend()
plt.show()