import numpy as np
import matplotlib.pyplot as plt

#2
#Gr.A

x1 = np.arange(0, 10, 0.1)
x2 = np.arange(0, 10, 0.1)
x3 = np.arange(0, 10, 0.1)
y1 = (x1**2)-(4 * x1)+2
y2 = (x2**3)-(2 ** x2)-(4 * x2)
plt.subplot(1, 3, 1)
plt.plot(x1, y1, 'b-', label='x^2-4*x+2')
plt.title('Pierwszy wykres')
plt.grid()
plt.legend(loc='lower left')
plt.axis([0, 10, -10, 50])
plt.subplot(1, 3, 2)
plt.plot(x2, y2, 'g:', label='x^3-2^x-4*x')
plt.title('Drugi wykres')
plt.grid()
plt.legend(loc='lower center')
plt.axis([0, 10, -50, 200])
plt.subplot(1, 3, 3)
plt.plot(x1, y1, 'b-', label='x^2-4*x+2')
plt.plot(x2, y2, 'g:', label='x^3-2^x-4*x')
plt.title('Trzeci wykres')
plt.grid()
plt.axis([0, 10, -10, 50])
plt.legend(loc='upper center')
plt.show()