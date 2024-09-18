library = {
    "Edukasi": [
        {"id": "E001", "judul": "Belajar Python", "pengarang": "John Doe", "status": "Tersedia", "peminjam": None},
        {"id": "E002", "judul": "Matematika Terapan", "pengarang": "Jane Doe", "status": "Tersedia", "peminjam": None},
        {"id": "E003", "judul": "Fisika untuk Pemula", "pengarang": "Albert", "status": "Tersedia", "peminjam": None},
        {"id": "E004", "judul": "Kimia Dasar", "pengarang": "Isaac", "status": "Tersedia", "peminjam": None},
        {"id": "E005", "judul": "Sejarah Dunia", "pengarang": "Herodotus", "status": "Tersedia", "peminjam": None}
    ],
    "Fiksi": [
        {"id": "F001", "judul": "Harry Potter", "pengarang": "J.K. Rowling", "status": "Tersedia", "peminjam": None},
        {"id": "F002", "judul": "Lord of the Rings", "pengarang": "J.R.R. Tolkien", "status": "Tersedia", "peminjam": None},
        {"id": "F003", "judul": "Hobbit", "pengarang": "J.R.R. Tolkien", "status": "Tersedia", "peminjam": None},
        {"id": "F004", "judul": "Percy Jackson", "pengarang": "Rick Riordan", "status": "Tersedia", "peminjam": None},
        {"id": "F005", "judul": "Sherlock Holmes", "pengarang": "Arthur Conan Doyle", "status": "Tersedia", "peminjam": None}
    ],
    "Religi": [
        {"id": "R001", "judul": "Tafsir Al-Quran", "pengarang": "Ibn Kathir", "status": "Tersedia", "peminjam": None},
        {"id": "R002", "judul": "Bimbingan Shalat", "pengarang": "Ustadz Ahmad", "status": "Tersedia", "peminjam": None},
        {"id": "R003", "judul": "Hadits Sahih Bukhari", "pengarang": "Imam Bukhari", "status": "Tersedia", "peminjam": None},
        {"id": "R004", "judul": "Tafsir Jalalain", "pengarang": "Jalaluddin", "status": "Tersedia", "peminjam": None},
        {"id": "R005", "judul": "Fikih Ibadah", "pengarang": "Ustadz Abdul", "status": "Tersedia", "peminjam": None}
    ]
}

def tampilkan_menu():
    print("\n=== Aplikasi Perpustakaan ===")
    print("1. Pilih Kategori dan Lihat Buku")
    print("2. Pinjam Buku")
    print("3. Kembalikan Buku")
    print("4. Cek Status Buku")
    print("5. Keluar")
    pilihan = input("Pilih opsi (1-5): ")
    return pilihan

def admin_menu():
    print("\n=== Menu Admin ===")
    print("1. Tambah Buku")
    print("2. Hapus Buku")
    print("3. Lihat Daftar Buku")
    print("4. Keluar")
    pilihan = input("Pilih opsi (1-4): ")
    return pilihan

def daftar_kategori():
    print("\n=== Pilih Kategori Buku ===")
    print("1. Edukasi")
    print("2. Fiksi")
    print("3. Religi")
    kategori_input = input("Pilih kategori (1-3): ").strip().lower()
    
    if kategori_input == "1":
        daftar_buku("Edukasi")
    elif kategori_input == "2":
        daftar_buku("Fiksi")
    elif kategori_input == "3":
        daftar_buku("Religi")
    else:
        print("Kategori tidak valid!")

def daftar_buku(kategori):
    kategori = kategori.capitalize()  
    if kategori not in library:
        print("Kategori tidak valid!")
        return
    
    print(f"\n=== Daftar Buku {kategori} ===")
    for buku in library[kategori]:
        status = buku['status']
        peminjam = f"(Dipinjam oleh {buku['peminjam']})" if buku['peminjam'] else ""
        print(f"ID: {buku['id']}, Judul: {buku['judul']}, Status: {status} {peminjam}")
    print()

def tambah_buku():
    kategori = input("\nMasukkan kategori buku (Edukasi, Fiksi, Religi): ").strip().capitalize()
    if kategori not in library:
        print("Kategori tidak valid!")
        return
    daftar_buku(kategori)
    
    while True:
        id_buku = input("Masukkan ID buku baru: ").strip()
        if any(buku['id'].lower() == id_buku.lower() for buku in library[kategori]):
            print("ID Buku telah tersedia, buatkan ID Buku baru")
        else:
            break

    judul_buku = input("Masukkan judul buku: ").strip()
    pengarang = input("Masukkan nama pengarang: ").strip()
    library[kategori].append({
        "id": id_buku,
        "judul": judul_buku,
        "pengarang": pengarang,
        "status": "Tersedia",
        "peminjam": None
    })
    print(f"Buku '{judul_buku}' berhasil ditambahkan ke kategori {kategori}.")
    
def hapus_buku():
    kategori = input("\nMasukkan kategori buku (Edukasi, Fiksi, Religi): ").strip().capitalize()
    if kategori not in library:
        print("Kategori tidak valid!")
        return
    daftar_buku(kategori)

    id_buku = input("Masukkan ID buku yang ingin dihapus: ").strip()
    for buku in library[kategori]:
        if buku['id'].lower() == id_buku.lower():
            library[kategori].remove(buku)
            print(f"Buku '{buku['judul']}' berhasil dihapus dari kategori {kategori}.")
            return
    print("Buku dengan ID tersebut tidak ditemukan.")

def pinjam_buku():
    kategori = input("\nMasukkan kategori buku (Edukasi, Fiksi, Religi): ").strip().capitalize()
    if kategori not in library:
        print("Kategori tidak valid!")
        return

    daftar_buku(kategori)

    id_buku = input("Masukkan ID buku yang ingin dipinjam: ").strip()
    for buku in library[kategori]:
        if buku['id'].lower() == id_buku.lower():
            if buku['status'] == "Tersedia":
                nama_peminjam = input("Masukkan nama peminjam: ")
                buku['status'] = "Dipinjam"
                buku['peminjam'] = nama_peminjam
                print(f"Buku '{buku['judul']}' berhasil dipinjam oleh {nama_peminjam}.")
                return
            else:
                print(f"Buku '{buku['judul']}' sedang dipinjam oleh {buku['peminjam']}.")
                return
    print("Buku dengan ID tersebut tidak ditemukan.")

def kembalikan_buku():
    kategori = input("\nMasukkan kategori buku (Edukasi, Fiksi, Religi): ").strip().capitalize()
    if kategori not in library:
        print("Kategori tidak valid!")
        return

    id_buku = input("Masukkan ID buku yang ingin dikembalikan: ").strip()
    for buku in library[kategori]:
        if buku['id'].lower() == id_buku.lower():
            if buku['status'] == "Dipinjam":
                nama_peminjam = input("Masukkan nama peminjam: ")
                if buku['peminjam'] == nama_peminjam:
                    buku['status'] = "Tersedia"
                    buku['peminjam'] = None
                    print(f"Buku '{buku['judul']}' berhasil dikembalikan.")
                    return
                else:
                    print("Nama peminjam tidak sesuai!")
                    return
            else:
                print(f"Buku '{buku['judul']}' belum dipinjam.")
                return
    print("Buku dengan ID tersebut tidak ditemukan.")

def cek_status_buku():
    kategori = input("\nMasukkan kategori buku (Edukasi, Fiksi, Religi): ").strip().capitalize()
    if kategori not in library:
        print("Kategori tidak valid!")
        return

    id_buku = input("Masukkan ID buku: ").strip()
    for buku in library[kategori]:
        if buku['id'].lower() == id_buku.lower():
            status = buku['status']
            if status == "Tersedia":
                print(f"Buku '{buku['judul']}' tersedia untuk dipinjam.")
            else:
                print(f"Buku '{buku['judul']}' sedang dipinjam oleh {buku['peminjam']}.")
            return
    print("Buku dengan ID tersebut tidak ditemukan.")

def main():
    role = input("Masukkan peran Anda (admin/peminjam): ").strip().lower()
    if role == "admin":
        while True:
            pilihan = admin_menu()
            if pilihan == "1":
                tambah_buku()
            elif pilihan == "2":
                hapus_buku()
            elif pilihan == "3":
                daftar_kategori()
            elif pilihan == "4":
                print("Terima kasih telah menggunakan Aplikasi Perpustakaan.")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
    elif role == "peminjam":
        while True:
            pilihan = tampilkan_menu()
            if pilihan == "1":
                daftar_kategori()
            elif pilihan == "2":
                pinjam_buku()
            elif pilihan == "3":
                kembalikan_buku()
            elif pilihan == "4":
                cek_status_buku()
            elif pilihan == "5":
                print("Terima kasih telah menggunakan Aplikasi Perpustakaan.")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
    else:
        print("Tidak valid.")

main()
