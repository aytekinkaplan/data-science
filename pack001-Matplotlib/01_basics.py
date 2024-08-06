"""Summary of matplotlib basics.

Aytekin Kaplan, Aug 2024."""

# Gerekli kütüphaneleri içe aktarıyoruz
import matplotlib.pyplot as plt
import numpy as np

# 0'dan 20'ye kadar 200 eşit aralıklı nokta oluşturuyoruz (x ekseni)
x = np.linspace(0, 20, 200)

# x değerlerinin sinüsünü alarak y değerlerini hesaplıyoruz (y ekseni)
y = np.sin(x)

# x ve y değerlerini kullanarak bir çizgi grafiği oluşturuyoruz
plt.plot(x, y)

# Oluşturulan grafiği ekranda gösteriyoruz
plt.show()

