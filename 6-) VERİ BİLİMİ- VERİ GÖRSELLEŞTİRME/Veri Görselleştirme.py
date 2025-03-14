import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# 📌 1. Örnek Veri Seti Oluşturma
np.random.seed(42)  # Rastgele sayılar her seferinde aynı olsun
data = pd.DataFrame({
    "Gün": np.arange(1, 11),  # 1'den 10'a kadar günler
    "Satış": np.random.randint(100, 500, 10),  # Günlük satış rakamları
    "Müşteri Sayısı": np.random.randint(50, 200, 10),  # Günlük müşteri sayıları
    "Mağaza": np.random.choice(["A", "B", "C"], 10)  # 3 farklı mağaza
})

# 📌 2. Çizgi Grafiği (Satışların Günlere Göre Değişimi)
plt.figure(figsize=(8, 5))
plt.plot(data["Gün"], data["Satış"], marker="o", linestyle="-", color="b", label="Satış")
plt.xlabel("Gün")
plt.ylabel("Satış Miktarı")
plt.title("Günlük Satış Grafiği")
plt.legend()
plt.grid()
plt.show()

# 📌 3. Histogram (Satış Dağılımı)
plt.figure(figsize=(8, 5))
plt.hist(data["Satış"], bins=5, color="purple", edgecolor="black")
plt.xlabel("Satış Miktarı")
plt.ylabel("Frekans")
plt.title("Satış Dağılımı Histogramı")
plt.show()

# 📌 4. Dağılım Grafiği (Satış vs. Müşteri Sayısı)
plt.figure(figsize=(8, 5))
sns.scatterplot(x=data["Müşteri Sayısı"], y=data["Satış"], hue=data["Mağaza"], palette="coolwarm", s=100)
plt.xlabel("Müşteri Sayısı")
plt.ylabel("Satış Miktarı")
plt.title("Müşteri Sayısı ve Satış Arasındaki İlişki")
plt.legend(title="Mağaza")
plt.show()

# 📌 5. Isı Haritası (Korelasyon Matrisi)
plt.figure(figsize=(6, 4))
sns.heatmap(data.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Korelasyon Matrisi")
plt.show()

# 📌 6. Etkileşimli Çubuk Grafiği (Plotly ile)
fig = px.bar(data, x="Gün", y="Satış", color="Mağaza", title="Günlük Satış Miktarı (Mağazalara Göre)")
fig.show()
