import math

# List untuk menyimpan jari-jari lingkaran
jari_jari_list = []

# Mengambil input dari pengguna
n = int(input("Masukkan jumlah lingkaran: "))

for i in range(n):
    jari_jari = float(input(f"Masukkan jari-jari lingkaran ke-{i+1}: "))
    jari_jari_list.append(jari_jari)

# Tuple untuk menyimpan hasil perhitungan luas lingkaran
luas_tuple = tuple(math.pi * (r ** 2) for r in jari_jari_list)

# Dictionary untuk menyimpan pasangan jari-jari dan luas lingkaran
lingkaran_dict = {jari_jari_list[i]: luas_tuple[i] for i in range(n)}

# Menampilkan hasil
print("\nLuas lingkaran untuk masing-masing jari-jari:")
for jari_jari, luas in lingkaran_dict.items():
    print(f"Jari-jari: {jari_jari} -> Luas: {luas}")
