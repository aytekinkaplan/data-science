"""Summary of matplotlib basics.

Aytekin Kaplan, Aug 2024."""

# NumPy ve Matplotlib kütüphanelerini içe aktardığımızı varsayıyoruz
import numpy as np
import matplotlib.pyplot as plt

# x eksenindeki değerleri oluşturuyoruz
# 0'dan 10'a kadar 100 eşit aralıklı nokta
x = np.linspace(0, 10, 100)

# y eksenindeki değerleri hesaplıyoruz
# x değerlerinin karesini alarak
y = x**2

# x ve y değerlerini kullanarak bir saçılım grafiği oluşturuyoruz
plt.scatter(x, y)

# Oluşturulan grafiği ekranda gösteriyoruz
plt.show()

