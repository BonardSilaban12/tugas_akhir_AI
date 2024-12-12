import numpy as np
import matplotlib.pyplot as plt

# Fungsi keanggotaan untuk Permintaan
def permintaan(x):
    if x < 2000:
        return (2000 - x) / 2000
    elif 2000 <= x <= 3000:
        return 1
    elif 3000 < x < 4000:
        return (4000 - x) / 1000
    else:
        return 0

# Fungsi keanggotaan untuk Persediaan
def persediaan(y):
    if y < 200:
        return (200 - y) / 200
    elif 200 <= y <= 400:
        return 1
    elif 400 < y < 600:
        return (600 - y) / 200
    else:
        return 0

# Fungsi untuk menghitung produksi berdasarkan fuzzy rules
def fuzzy_inference(per, pers):
    rules = []
    
    # Aturan Fuzzy
    if per == "turun":
        if pers == "sedikit":
            rules.append(1)  # Produksi Bertambah
        elif pers == "sedang" or pers == "banyak":
            rules.append(0)  # Produksi Berkurang
    elif per == "tetap":
        if pers == "sedikit":
            rules.append(1)  # Produksi Bertambah
        else:
            rules.append(0)  # Produksi Berkurang
    elif per == "naik":
        if pers == "sedikit" or pers == "sedang":
            rules.append(1)  # Produksi Bertambah
        else:
            rules.append(0)  # Produksi Berkurang
    
    return rules

# Contoh Input
permintaan_input = "turun"
persediaan_input = "sedikit"

# Menghitung keanggotaan
keanggotaan_permintaan = permintaan(1500)  # contoh permintaan
keanggotaan_persediaan = persediaan(100)    # contoh persediaan

# Menghitung produksi
produksi = fuzzy_inference(permintaan_input, persediaan_input)

# Output
print("Keanggotaan Permintaan:", keanggotaan_permintaan)
print("Keanggotaan Persediaan:", keanggotaan_persediaan)
print("Produksi berdasarkan aturan:", produksi)

# Visualisasi
x = np.linspace(0, 6000, 100)
y_permintaan = [permintaan(i) for i in x]
y_persediaan = [persediaan(i) for i in x]

plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(x, y_permintaan, label='Permintaan', color='orange')
plt.title('Fungsi Keanggotaan Permintaan')
plt.xlabel('Jumlah Permintaan')
plt.ylabel('Keanggotaan')
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(x, y_persediaan, label='Persediaan', color='purple')
plt.title('Fungsi Keanggotaan Persediaan')
plt.xlabel('Jumlah Persediaan')
plt.ylabel('Keanggotaan')
plt.grid()

plt.tight_layout()
plt.show()
