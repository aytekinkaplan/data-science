"""Summary of matplotlib basics.

Aytekin Kaplan, Aug 2024."""


import numpy as np  # Numpy kütüphanesini import ediyoruz
import matplotlib.pyplot as plt  # Matplotlib kütüphanesini import ediyoruz

# 0 ile 2 arasında 0.01 aralıklarla bir dizi oluşturuyoruz
r = np.arange(0, 2, 0.01)

# r dizisinin her bir elemanının 2π ile çarpılmasını sağlayarak theta dizisini oluşturuyoruz
theta = 2 * np.pi * r

# Polar koordinatlarda theta ve r dizilerini kullanarak bir polar grafiği çiziyoruz
plt.polar(theta, r)

# Grafiği gösteriyoruz
plt.show()
