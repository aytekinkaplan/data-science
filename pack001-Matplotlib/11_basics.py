"""Summary of matplotlib basics.

Aytekin Kaplan, Aug 2024."""

# NumPy ve Matplotlib kütüphanelerini içe aktarıyoruz
import numpy as np
import matplotlib.pyplot as plt

# 3D grafik çizimi için gerekli modülü içe aktarıyoruz
from mpl_toolkits.mplot3d import Axes3D

# Yeni bir figure (şekil) oluşturuyoruz
fig = plt.figure()

# 3D projeksiyon ile bir alt grafik (subplot) ekliyoruz
ax = fig.add_subplot(111, projection='3d')

# 0 ile 1 arasında rastgele 100 sayı oluşturuyoruz (x, y ve z eksenleri için)
x = np.random.rand(100)
y = np.random.rand(100)
z = np.random.rand(100)

# 3D saçılım grafiği çiziyoruz
ax.scatter(x, y, z)

# Oluşturulan grafiği ekranda gösteriyoruz
plt.show()
