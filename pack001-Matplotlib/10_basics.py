"""Summary of matplotlib basics.

Aytekin Kaplan, Aug 2024."""

# NumPy ve Matplotlib kütüphanelerini içe aktardığımızı varsayıyoruz
import numpy as np
import matplotlib.pyplot as plt

# Farklı standart sapmalara sahip normal dağılımlardan veri oluşturuyoruz
data = [np.random.normal(0, std, 100) for std in range(1, 4)]

# Oluşturulan veriyi kullanarak bir kutu grafiği (box plot) çiziyoruz
plt.boxplot(data)

# Oluşturulan grafiği ekranda gösteriyoruz
plt.show()


