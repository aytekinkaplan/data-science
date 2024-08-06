"""Summary of matplotlib basics.

Aytekin Kaplan, Aug 2024."""

import numpy as np  # Numpy kütüphanesini import ediyoruz
import matplotlib.pyplot as plt  # Matplotlib kütüphanesini import ediyoruz

x = np.arange(5)
y = np.random.randint(1, 10, 5)

plt.barh(x, y)
plt.show()
