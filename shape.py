import matplotlib.pyplot as plt
import numpy as np

def sgn(angle):
    if angle < 0:
        return -1
    elif angle == 0:
        return 0
    elif angle > 0:
        return 1

n = 0
for p in range(1, 78):
    i = 0
    r = 100
    a = 1
    b = 1
    if p < 40:
        n += 0.1
    elif p > 39:
        n -= 0.1
        if n <= 0:
            break
    na = 2/n
    x, y = [], []
    while i < np.pi*2+1:
        i += 0.1
        x.append(pow(abs(np.cos(i)), na) * a * sgn(np.cos(i)))
        y.append(pow(abs(np.sin(i)), na) * b * sgn(np.sin(i)))
    plt.axis('equal')
    plt.axis('off')
    plt.plot(x, y)
    plt.savefig('img/foo{0}'.format(p))
    plt.clf()

