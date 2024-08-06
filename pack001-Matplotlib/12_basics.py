"""Summary of matplotlib basics.

Aytekin Kaplan, Aug 2024."""

# NumPy ve Matplotlib kütüphanelerini içe aktarıyoruz
import numpy as np
import matplotlib.pyplot as plt

# 3D grafik çizimi için gerekli modülü içe aktarıyoruz
from mpl_toolkits.mplot3d import Axes3D

# x ve y eksenlerinde -5'ten 5'e kadar 100 nokta oluşturuyoruz
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

# x ve y değerlerinden 2D ızgara (grid) oluşturuyoruz
X, Y = np.meshgrid(x, y)

# Z değerlerini hesaplıyoruz: sin(sqrt(x^2 + y^2))
Z = np.sin(np.sqrt(X**2 + Y**2))

# Kontur grafiği çiziyoruz
plt.contourf(X, Y, Z)

# Renk çubuğu (colorbar) ekliyoruz
plt.colorbar()

# Oluşturulan grafiği ekranda gösteriyoruz
plt.show()