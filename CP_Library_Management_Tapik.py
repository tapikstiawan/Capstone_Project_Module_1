# Inisialisasi data buku
books = {
    "001": {"title": "Eloquent Data Script", "author": "Marijn Haverbeke", "stock": 5, "harga_sewa": 12000},
    "002": {"title": "JavaScript for Cats", "author": "Max Ogden", "stock": 3, "harga_sewa": 15000},
    "003": {"title": "JavaScript Uncover", "author": "Andre Pratama", "stock": 1, "harga_sewa": 17000}
}


# Fungsi menampilkan menu utama
def display_menu():
    print("\n=== Menu Utama ===")
    print("1. Laporan Buku")
    print("2. Tambah Buku")
    print("3. Perbarui Buku")
    print("4. Hapus Buku")
    print("5. Sewa Buku")
    print("6. Keluar")

# Fungsi menampilkan menu laporan
def show_report_menu():
    print("\n=== Menu Laporan ===")
    print("1. Tampilkan Semua Buku")
    print("2. Cari Buku Berdasarkan ISBN")
    print("3. Kembali ke Menu Utama")

# Fungsi untuk validasi input angka
def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Input tidak valid! Harap masukkan angka.")

# Fungsi untuk menampilkan semua buku
def display_books():
    if not books:
        print("Tidak ada buku dalam database.")
        return
    print("\n=== Daftar Buku ===")
    for isbn, data in books.items():
        print(f"ISBN: {isbn}, Judul: {data['title']}, Penulis: {data['author']}, Stok: {data['stock']}, Harga Sewa: Rp{data['harga_sewa']}")

# Fungsi untuk mencari buku berdasarkan ISBN
def show_book_by_isbn():
    code = input("Masukkan ISBN Buku: ")
    if code in books:
        book = books[code]
        print(f"Judul: {book['title']}, Penulis: {book['author']}, Stok: {book['stock']}, Harga Sewa: Rp{book['harga_sewa']}")
    else:
        print("Buku dengan ISBN tersebut tidak ditemukan.")

# Fungsi untuk menambah buku
def add_book():
    code = input("Masukkan ISBN Buku: ")
    if code in books:
        print("Buku dengan ISBN tersebut sudah ada. Silahkan memilih Menu Perbarui Buku")
    else:
        title = input("Judul Buku: ")
        author = input("Penulis: ")
        stock = get_integer_input("Stok: ")
        harga_sewa = get_integer_input("Harga Sewa: ")
        books[code] = {"title": title, "author": author, "stock": stock, "harga_sewa": harga_sewa}
        print("Buku berhasil ditambahkan.")

# Fungsi untuk memperbarui buku
def update_book():
    code = input("Masukkan ISBN Buku: ")
    if code in books:
        title = input("Masukkan judul buku: ")
        author = input("Masukkan nama penulis: ")
        stock = get_integer_input("Masukkan jumlah stok: ")
        harga_sewa = get_integer_input("Harga Sewa: ")
        books[code] = {"title": title, "author": author, "stock": stock, "harga_sewa": harga_sewa}
        print("Data buku berhasil diperbarui!")
    else:
        print("Data buku tidak ditemukan! Silahkan merekam data buku baru di Menu Tambah Buku")

# Fungsi untuk menghapus buku
def delete_book():
    code = input("Masukkan ISBN Buku: ")
    if code in books:
        del books[code]
        print("Data buku berhasil dihapus!")
    else:
        print("Data buku tidak ditemukan!")

# Fungsi untuk menyewa buku
def rent_book():
    code = input("Masukkan ISBN Buku: ")
    if code not in books:
        print("Buku dengan ISBN tersebut tidak ditemukan.")
    else:
        if books[code]["stock"] > 0:
            books[code]["stock"] -= 1  # Stok dikurangi sebelum menampilkan pesan
            harga_sewa = books[code]["harga_sewa"]
            print(f"Buku '{books[code]['title']}' berhasil disewa dengan harga sewa Rp{harga_sewa}.")
            print(f"Stok tersisa: {books[code]['stock']}")
        else:
            print("Maaf, stok buku habis.")

# Fungsi untuk menangani menu laporan
def handle_report_menu():
    while True:
        show_report_menu()
        report_choice = input("Pilih menu report: ")

        report_actions = {
            "1": display_books,
            "2": show_book_by_isbn
        }

        if report_choice in report_actions:
            report_actions[report_choice]()
        elif report_choice == "3":
            break
        else:
            print("Pilihan tidak valid, silakan pilih menu yang tersedia.")

# Fungsi utama program
def main():
    menu_options = {
        "2": add_book,
        "3": update_book,
        "4": delete_book,
        "5": rent_book
    }

    while True:
        display_menu()
        choice = input("Masukkan pilihan menu: ")

        if choice == "1":
            handle_report_menu()
        elif choice == "6":
            print("Terima kasih telah menggunakan Purwadhika Library")
            break
        elif choice in menu_options:
            menu_options[choice]()
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

# Menjalankan program
if __name__ == "__main__":
    main()