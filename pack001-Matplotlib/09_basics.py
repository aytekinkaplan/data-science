"""Summary of matplotlib basics.

Aytekin Kaplan, Aug 2024."""

# NumPy ve Matplotlib kütüphanelerini içe aktarıyoruz
import numpy as np
import matplotlib.pyplot as plt

# Pasta dilimlerinin büyüklüklerini tanımlıyoruz
sizes = [30, 20, 25, 25]

# Her dilimin etiketini tanımlıyoruz
labels = ['Ahmed', 'Salih', 'Yusuf', 'Deniz']

# Pasta grafiği oluşturuyoruz
plt.pie(sizes, labels=labels)

# Oluşturulan grafiği ekranda gösteriyoruz
plt.show()


