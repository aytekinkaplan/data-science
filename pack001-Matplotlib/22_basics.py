"""Summary of matplotlib basics.

Aytekin Kaplan, Aug 2024."""


import numpy as np  # Numpy kütüphanesini import ediyoruz
import matplotlib.pyplot as plt  # Matplotlib kütüphanesini import ediyoruz

# Kategoriler için isimler tanımlıyoruz
categories = ['A', 'B', 'C', 'D', 'E']

# Her bir kategori için değerler tanımlıyoruz
values = [4, 3, 5, 2, 4]

# Kategoriler kadar açılar oluşturarak polar koordinatlarda kullanılacak açıları hesaplıyoruz
angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False)

# İlk ve son değerlerin aynı noktada birleşmesini sağlamak için values dizisini döngüye ekliyoruz
values = np.concatenate((values, [values[0]]))

# İlk ve son açıların aynı noktada birleşmesini sağlamak için angles dizisini döngüye ekliyoruz
angles = np.concatenate((angles, [angles[0]]))

# Polar koordinat sisteminde açıları ve değerleri kullanarak bir grafik çiziyoruz
plt.polar(angles, values)

# Grafiği gösteriyoruz
plt.show()

