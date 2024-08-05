"""Summary of matplotlib basics.

Aytekin Kaplan, Aug 2024."""

import matplotlib.pyplot as plt  # Matplotlib kütüphanesini import ediyoruz
import numpy as np  # Numpy kütüphanesini import ediyoruz

# 10x10 boyutunda rastgele sayılardan oluşan bir matris oluşturuyoruz
data = np.random.rand(10, 10)

# Bu veriyi görselleştirmek için imshow fonksiyonunu kullanıyoruz ve sıcaklık haritası (cmap='hot') stilini seçiyoruz
plt.imshow(data, cmap='hot')

# Yanında renk skalası (colorbar) ekliyoruz
plt.colorbar()

# Grafiği gösteriyoruz
plt.show()
