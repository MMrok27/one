import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
#1
# t = np.arange(1, 21, 1)
# print(t)
# plt.plot(t,1/t, label='f(x) = 1/x')
# print()
# plt.xlabel('x')
# plt.ylabel("f(x)")
# plt.title("wykres funkcji f(x) = 1 / x dla x ϵ[1, 20]")
#
# plt.axis([0,max(t),0,1])
# plt.legend()
# plt.show()
#2
# t = np.arange(1, 21, 1)
# print(t)
# plt.plot(t,1/t,'g:>', label='f(x) = 1/x' )
#
# print()
# plt.xlabel('x')
# plt.ylabel("f(x)")
# plt.title("wykres funkcji f(x) = 1 / x dla x ϵ[1, 20]")
#
# plt.axis([0,max(t),0,1])
# plt.legend()
# plt.show()
#3
x1 = np.arange(0, 31, 0.1)
x2 = np.arange(0, 31, 0.1)
y1 = np.sin(2 * np.pi * x1)
y2 = np.cos(2 * np.pi * x2)
fig, axs = plt.subplots(2)
axs[0].plot(x1, y1, '-', label="sin(x)")
axs[0].set_title('wykres sin(x)')
axs[0].set_xlabel('x')
axs[0].set_ylabel('sin(x)')
axs[1].plot(x2, y2, 'r-',label="sin(y)")
axs[1].set_title('wykres cos(x)')
axs[1].set_xlabel('x')
axs[1].set_ylabel('cos(x)')
lines_labels = [ax.get_legend_handles_labels() for ax in fig.axes]
lines, labels = [sum(lol, []) for lol in zip(*lines_labels)]
fig.legend(lines, labels)
plt.subplots_adjust(hspace=0.5)
plt.show()