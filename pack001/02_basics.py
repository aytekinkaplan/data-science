"""Summary of matplotlib basics.

Aytekin Kaplan, Aug 2024."""

# Matplotlib kütüphanesinden pyplot modülünü içe aktarıyoruz
import matplotlib.pyplot as plt

# x eksenindeki değerleri tanımlıyoruz
x = [1, 2, 3, 4]

# y eksenindeki değerleri tanımlıyoruz
y = [1, 4, 2, 3]

# x ve y değerlerini kullanarak bir çizgi grafiği oluşturuyoruz
plt.plot(x, y)

# Oluşturulan grafiği ekranda gösteriyoruz
plt.show()
