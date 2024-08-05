"""Summary of matplotlib basics.

Aytekin Kaplan, Aug 2024."""

# Gerekli kütüphaneleri içe aktarıyoruz
import matplotlib.pyplot as plt
import numpy as np

# x eksenindeki değerleri oluşturuyoruz
# 0'dan 10'a kadar 100 eşit aralıklı nokta
x = np.linspace(0, 10, 100)

# y eksenindeki değerleri hesaplıyoruz
# x değerlerinin sinüsünü alarak
y = np.sin(x)

# x ve y değerlerini kullanarak bir çizgi grafiği oluşturuyoruz
# 'label' parametresi ile grafiğe bir etiket ekliyoruz
plt.plot(x, y, label='Sin Graph')

# Grafiğe bir açıklama (legend) ekliyoruz
# Bu, 'label' parametresi ile eklediğimiz etiketi gösterecek
plt.legend()

# Oluşturulan grafiği ekranda gösteriyoruz
plt.show()

