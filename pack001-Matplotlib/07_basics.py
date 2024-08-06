"""Summary of matplotlib basics.

Aytekin Kaplan, Aug 2024."""

# NumPy ve Matplotlib kütüphanelerini içe aktarıyoruz
import numpy as np
import matplotlib.pyplot as plt

# Rastgele 1000 adet standart normal dağılımlı veri oluşturuyoruz
data = np.random.randn(1000)

# Oluşturulan veriyi kullanarak bir histogram grafiği çiziyoruz
# 'bins' parametresi histogramın kaç aralığa bölüneceğini belirler
plt.hist(data, bins=30)

# Oluşturulan grafiği ekranda gösteriyoruz
plt.show()


