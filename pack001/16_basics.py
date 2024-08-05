"""Summary of matplotlib basics.

Aytekin Kaplan, Aug 2024."""

import numpy as np  # Numpy kütüphanesini import ediyoruz
import matplotlib.pyplot as plt  # Matplotlib kütüphanesini import ediyoruz

# 0 ile 10 arasında 100 eşit aralıkta nokta oluşturan bir dizi oluşturuyoruz
x = np.linspace(0, 10, 100)

# x dizisinin sinüsünü alarak y dizisini oluşturuyoruz
y = np.sin(x)

# x ve y dizilerini kullanarak bir çizgi grafiği çiziyoruz
# Çizginin stili kesik çizgi ('--'), rengi kırmızı ('r') ve noktalar ('o') ile gösteriliyor
plt.plot(x, y, linestyle='--', color='r', marker='o')

# Grafiği gösteriyoruz
plt.show()

