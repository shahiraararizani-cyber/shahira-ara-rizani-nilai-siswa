# Menentukan kelulusan siswa lulus/tidak

nama = input("Masukkan nama siswa: ")
kelas = input("Masukkan kelas: ")

matematika = int(input("Nilai Matematika: "))
informatika = int(input("Nilai Informatika: "))
b_indonesia = int(input("Nilai Bahasa Indonesia: "))
b_inggris = int(input("Nilai Bahasa Inggris: "))
ekonomi = int(input("Nilai Ekonomi: "))

# Logika OR
lulus = (matematika >= 85) or (informatika >= 80) or (b_indonesia >= 87) or (b_inggris >= 80) or (ekonomi >= 82)

print(" HASIL KELULUSAN ")
print("Nama:", nama)
print("kelas:", kelas)
print("Hasil:", lulus)

if lulus:
    print("SISWA DINYATAKAN LULUS")
else:
    print("SISWA DINYATAKAN TIDAK LULUS")
