"""Summary of matplotlib basics.

Aytekin Kaplan, Aug 2024."""

import matplotlib.pyplot as plt  # Matplotlib kütüphanesini import ediyoruz
import numpy as np  # Numpy kütüphanesini import ediyoruz

# 0 ile 5 arasında 11 eşit aralıkta nokta oluşturan bir dizi oluşturuyoruz
x = np.linspace(0, 5, 11)

# x dizisinin her bir elemanının karesini alarak y dizisini oluşturuyoruz
y = x ** 2

# x ve y dizilerini kullanarak bir çizgi grafiği çiziyoruz
plt.plot(x, y)

# Y eksenini logaritmik ölçeğe çeviriyoruz
plt.yscale('log')

# Grafiği gösteriyoruz
plt.show()


