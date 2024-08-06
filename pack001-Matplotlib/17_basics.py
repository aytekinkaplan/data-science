"""Summary of matplotlib basics.

Aytekin Kaplan, Aug 2024."""

import numpy as np  # Numpy kütüphanesini import ediyoruz
import matplotlib.pyplot as plt  # Matplotlib kütüphanesini import ediyoruz

# 0 ile 10 arasında 100 eşit aralıkta nokta oluşturan bir dizi oluşturuyoruz
x = np.linspace(0, 10, 100)

# x dizisinin sinüsünü alarak y1 dizisini oluşturuyoruz
y1 = np.sin(x)

# x dizisinin kosinüsünü alarak y2 dizisini oluşturuyoruz
y2 = np.cos(x)

# x ve y1, y2 dizilerini kullanarak iki eğri arasındaki alanı dolduruyoruz
plt.fill_between(x, y1, y2)

# Grafiği gösteriyoruz
plt.show()


