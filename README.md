# 6--VERI-BILIMI-VERI-GORSELLESTIRME

# 📊 Veri Görselleştirme (Data Visualization) README

## 📌 Giriş (Introduction)

Veri görselleştirme, veriyi anlaşılabilir ve etkili bir şekilde sunmak için grafikler, tablolar ve diyagramlar kullanma sanatıdır. Bu sayede büyük veri setleri üzerinde sezgisel çıkarımlar yapabiliriz.

Bu repo, Python'da veri görselleştirme için kullanılan popüler kütüphaneleri ve temel grafik çizim tekniklerini içermektedir. 📈📉

---

## 🚀 Kurulum (Installation)

Veri görselleştirme kütüphanelerini yüklemek için aşağıdaki komutları çalıştırabilirsin:

```bash
pip install matplotlib seaborn plotly pandas numpy
```

---

## 🎨 Kullanılan Kütüphaneler (Libraries Used)

1. **Matplotlib** 📊 - Temel grafikler, ç1. **Matplotlib** 📊 - Temel grafikler, \xe7izgi grafikleri ve histogramlar iç1. **Matplotlib** 📊 - Temel grafikler, \xe7izgi grafikleri ve histogramlar i\xe7in.
2. **Seaborn** 🎨 - Daha estetik ve istatistiksel analiz iç2. **Seaborn** 🎨 - Daha estetik ve istatistiksel analiz i\xe7in.
3. **Plotly** 🚀 - Etkileşimli grafikler oluşturmak içturmak i\xe7in.
4. **Pandas & NumPy** 📚 - Veriyi yö4. **Pandas & NumPy** 📚 - Veriyi y\xf6netmek ve dö4. **Pandas & NumPy** 📚 - Veriyi y\xf6netmek ve d\xf6nü4. **Pandas & NumPy** 📚 - Veriyi y\xf6netmek ve d\xf6n\xfcştüt\xfcrmek içt\xfcrmek i\xe7in.

---

## 🏗️ Örnek Kullanım (Examples)

### 📌 Basit Bir Çizgi Grafiği

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y, label='Sinüs Fonksiyonu', color='blue')
plt.xlabel('X Ekseni')
plt.ylabel('Y Ekseni')
plt.title('Sin Grafiği')
plt.legend()
plt.show()
```

### 🎨 Seaborn ile Histogram

```python
import seaborn as sns
import numpy as np

data = np.random.randn(1000)

sns.histplot(data, kde=True, color='purple')
plt.title('Histogram Örneği')
plt.show()
```

### 🚀 Plotly ile Etkileşimli Grafik

```python
import plotly.express as px
import pandas as pd

df = pd.DataFrame({'X Ekseni': [1, 2, 3, 4, 5], 'Y Ekseni': [10, 20, 30, 40, 50]})
fig = px.line(df, x='X Ekseni', y='Y Ekseni', title='Plotly Etkileşimli Grafik')
fig.show()
```

---

## 📚 Ek Kaynaklar (Additional Resources)

- [Matplotlib Resmi Dokümanı](https://matplotlib.org/stable/contents.html)
- [Seaborn Resmi Dokümanı](https://seaborn.pydata.org/)
- [Plotly Resmi Dokümanı](https://plotly.com/python/)
- [Pandas Dokümanı](https://pandas.pydata.org/docs/)

---

## 📌 Katkı Yapma (Contributing)

Katkı yapmak ister misin? Forkla, geliştir ve bir PR gönder! 🚀

---

## 📜 Lisans (License)

Bu proje MIT lisansı altında sunulmaktadır. Serbestçe kullanabilirsiniz! 😊

