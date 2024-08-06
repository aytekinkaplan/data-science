"""Summary of matplotlib basics.

Aytekin Kaplan, Aug 2024."""

# NumPy ve Matplotlib kütüphanelerini içe aktarıyoruz
import numpy as np
import matplotlib.pyplot as plt

# x eksenindeki değerleri oluşturuyoruz
# 1'den 10'a kadar olan tam sayıları içeren bir dizi
x = np.arange(1, 11)

# y eksenindeki değerleri hesaplıyoruz
# x değerlerinin karesini alarak
y = x * x

# x ve y değerlerini kullanarak bir sütun grafiği oluşturuyoruz
plt.bar(x, y)

# Oluşturulan grafiği ekranda gösteriyoruz
plt.show()


