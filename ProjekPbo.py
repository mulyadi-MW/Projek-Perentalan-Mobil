# ======================================
# Program Perentalan Mobil
# Menggunakan Konsep OOP dan Function
# ======================================

# Class Induk
class Orang:
    def _init_(self, nama):
        self.nama = nama


# Class Pelanggan (Inheritance)
class Pelanggan(Orang):
    def _init_(self, nama, no_hp):
        super()._init_(nama)
        self.no_hp = no_hp


# Class Mobil
class Mobil:
    def _init_(self, merk, plat):
        self.merk = merk
        self.plat = plat
        self.status = "Tersedia"

    def sewa(self):
        self.status = "Disewa"

    def kembali(self):
        self.status = "Tersedia"


# Class Rental
class RentalMobil:
    def _init_(self):
        self.data_sewa = []

    def tambah_sewa(self, pelanggan, mobil, lama):
        mobil.sewa()
        self.data_sewa.append((pelanggan, mobil, lama))

    def tampilkan_sewa(self):
        print("\n=== Data Rental Mobil ===")
        for p, m, l in self.data_sewa:
            print(f"Nama: {p.nama} | HP: {p.no_hp} | Mobil: {m.merk} | Plat: {m.plat} | Lama: {l} hari | Status: {m.status}")


# ===== Function =====
def input_sewa(rental):
    nama = input("Nama Pelanggan   : ")
    hp = input("No HP            : ")
    merk = input("Merk Mobil       : ")
    plat = input("Plat Mobil       : ")
    lama = int(input("Lama Sewa (hari) : "))

    pelanggan = Pelanggan(nama, hp)
    mobil = Mobil(merk, plat)

    rental.tambah_sewa(pelanggan, mobil, lama)
    print("Data sewa berhasil disimpan!\n")


# ===== Program Utama =====
rental = RentalMobil()

while True:
    print("=== MENU RENTAL MOBIL ===")
    print("1. Input Sewa Mobil")
    print("2. Tampilkan Data Rental")
    print("3. Keluar")

    pilih = input("Pilih menu (1/2/3): ")

    if pilih == "1":
        input_sewa(rental)
    elif pilih == "2":
        rental.tampilkan_sewa()
    elif pilih == "3":
        print("Terima kasih telah menggunakan jasa rental.")
        break
    else:
        print("Pilihan tidak valid!\n")