"""Summary of matplotlib basics.

Aytekin Kaplan, Aug 2024."""

# 0. Numpy'ı içe aktarma
import numpy as np

# 1. Pandas'ı içe aktarma
import pandas as pd

# 2. Series oluşturma
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print("Series örneği:")
print(s)

# 3. DataFrame oluşturma
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
print("\nDataFrame örneği:")
print(df)

# 4. CSV dosyasından veri okuma (yorumda, çünkü dosya yok)
# df = pd.read_csv('data.csv')
# print(df.head())

# 5. Excel dosyasından veri okuma (yorumda, çünkü dosya yok)
# df = pd.read_excel('data.xlsx')
# print(df.head())

# 6. DataFrame'in ilk birkaç satırını görüntüleme
print("\nİlk birkaç satır:")
print(df.head())

# 7. DataFrame'in son birkaç satırını görüntüleme
print("\nSon birkaç satır:")
print(df.tail())

# 8. DataFrame hakkında genel bilgi alma
print("\nDataFrame bilgisi:")
print(df.info())

# 9. DataFrame'in istatistiksel özetini alma
print("\nİstatistiksel özet:")
print(df.describe())

# 10. Belirli bir sütunu seçme
print("\n'A' sütunu:")
print(df['A'])

# 11. Birden fazla sütun seçme
print("\n'A' ve 'B' sütunları:")
print(df[['A', 'B']])

# 12. Belirli satırları seçme
print("\nİlk iki satır:")
print(df.loc[0:1])

# 13. Belirli satır ve sütunları seçme
print("\nİlk iki satır, 'A' ve 'B' sütunları:")
print(df.loc[0:1, ['A', 'B']])

# 14. Koşullu seçim
print("\n'A' > 1 olan satırlar:")
print(df[df['A'] > 1])

# 15. Yeni bir sütun ekleme
df['C'] = df['A'] + df['B']
print("\nYeni 'C' sütunu eklenmiş DataFrame:")
print(df)

# 16. Sütun silme
df = df.drop('C', axis=1)
print("\n'C' sütunu silinmiş DataFrame:")
print(df)

# 17. NaN değerleri doldurma
df_with_nan = pd.DataFrame({'A': [1, 2, np.nan], 'B': [4, np.nan, 6]})
print("\nNaN değerler doldurulmuş DataFrame:")
print(df_with_nan.fillna(0))

# 18. NaN değerleri olan satırları silme
print("\nNaN değerleri olan satırlar silinmiş DataFrame:")
print(df_with_nan.dropna())

# 19. Gruplama ve toplama
df_group = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar'], 'B': [1, 2, 3, 4]})
print("\nGruplanmış ve toplanmış DataFrame:")
print(df_group.groupby('A').sum())

# 20. Sıralama
print("\n'B' sütununa göre azalan şekilde sıralanmış DataFrame:")
print(df.sort_values('B', ascending=False))

# 21. Veri tiplerini değiştirme
df['A'] = df['A'].astype(float)
print("\nVeri tipleri değiştirilmiş DataFrame:")
print(df.dtypes)

# 22. Pivot tablo oluşturma
df_pivot = pd.DataFrame({'A': ['foo', 'foo', 'bar', 'bar'],
                         'B': ['one', 'two', 'one', 'two'],
                         'C': [1, 2, 3, 4]})
print("\nPivot tablo:")
print(pd.pivot_table(df_pivot, values='C', index='A', columns='B'))

# 23. Zaman serisi verisi oluşturma
dates = pd.date_range('20230101', periods=6)
df_time = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print("\nZaman serisi DataFrame'i:")
print(df_time)

# 24. Veriyi yeniden şekillendirme (reshape)
df_melt = pd.DataFrame({'A': ['a', 'b', 'c'], 'B': [1, 3, 5], 'C': [2, 4, 6]})
melted = pd.melt(df_melt, id_vars=['A'], value_vars=['B', 'C'])
print("\nYeniden şekillendirilmiş (melted) DataFrame:")
print(melted)

# 25. İki DataFrame'i birleştirme (concat)
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
result = pd.concat([df1, df2])
print("\nBirleştirilmiş DataFrame'ler (concat):")
print(result)

# 26. İki DataFrame'i birleştirme (merge)
df1 = pd.DataFrame({'key': ['K0', 'K1', 'K2'], 'A': ['A0', 'A1', 'A2']})
df2 = pd.DataFrame({'key': ['K0', 'K1', 'K2'], 'B': ['B0', 'B1', 'B2']})
result = pd.merge(df1, df2, on='key')
print("\nBirleştirilmiş DataFrame'ler (merge):")
print(result)

# 27. Veriyi CSV dosyasına yazma (yorumda, çünkü dosya yazma işlemi)
# df.to_csv('output.csv', index=False)

# 28. Veriyi Excel dosyasına yazma (yorumda, çünkü dosya yazma işlemi)
# df.to_excel('output.xlsx', index=False)

# 29. Betimleyici istatistikler
print("\nBetimleyici istatistikler:")
print(df.agg(['min', 'max', 'mean', 'std']))

# 30. Korelasyon matrisi
print("\nKorelasyon matrisi:")
print(df.corr())
