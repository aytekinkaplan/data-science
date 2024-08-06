"""Summary of matplotlib basics.

Aytekin Kaplan, Aug 2024."""

# Matplotlib kütüphanesinden pyplot modülünü içe aktarıyoruz
import matplotlib.pyplot as plt

# x eksenindeki değerleri tanımlıyoruz
x = [1, 2, 3, 4]

# İlk y ekseni değerlerini tanımlıyoruz (y1)
y1 = [1, 4, 2, 3]

# İkinci y ekseni değerlerini tanımlıyoruz (y2)
y2 = [1, 2, 4, 1]

# x ve y1 değerlerini, ardından x ve y2 değerlerini kullanarak iki çizgi grafiği oluşturuyoruz
plt.plot(x, y1, x, y2)

# Oluşturulan grafiği ekranda gösteriyoruz
plt.show()