from library import tet#, alt_tet
import matplotlib.pyplot as plt
from numpy import e, sqrt
import numpy as np

if __name__=='__main__':
    x = np.linspace(0, e**(1/e), 1000)
    plt.plot(x, [tet(i, 5000) for i in x], alpha=0.75, label='b = even')
    plt.plot(x, [tet(i, 5001) for i in x], alpha=0.75, label='b = odd')
    plt.title(r'$y=\lim_{b\rightarrow\infty} (a\uparrow\uparrow b)$')
    plt.xlabel(r'$a$, where $a \in [0, e^{\frac{1}{e}}]$')
    plt.legend()
    plt.show()