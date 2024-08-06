"""Summary of matplotlib basics.

Aytekin Kaplan, Aug 2024."""

import numpy as np  # Numpy kütüphanesini import ediyoruz
import matplotlib.pyplot as plt  # Matplotlib kütüphanesini import ediyoruz

# 0 ile 10 arasında 10 eşit aralıkta nokta oluşturan bir dizi oluşturuyoruz
x = np.linspace(0, 10, 10)

# x dizisinin sinüsünü alarak y1 dizisini oluşturuyoruz
y1 = np.sin(x)

# x dizisinin kosinüsünü alarak y2 dizisini oluşturuyoruz
y2 = np.cos(x)

# x ve y1 dizilerini kullanarak bir bar grafiği çiziyoruz
plt.bar(x, y1, label='sin(x)')

# y1 dizisini 'bottom' argümanı olarak kullanarak x ve y2 dizilerini kullanarak bir başka bar grafiği çiziyoruz
plt.bar(x, y2, bottom=y1, label='cos(x)')

# Grafiği gösteriyoruz
plt.show()
