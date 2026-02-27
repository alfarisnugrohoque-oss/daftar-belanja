import database
import logger   


def tambah_item(nama):
    daftar = database.baca_data()
    daftar.append(nama)
    database.tulis_data(daftar)

    logger.tulis_log(f"Tambah item: {nama}")
    return f"✅ '{nama}' berhasil ditambahkan."


def semua_item():
    logger.tulis_log("Melihat semua item")
    return database.baca_data()


def hapus_item(no):
    daftar = database.baca_data()
    if 1 <= no <= len(daftar):
        item = daftar.pop(no - 1)
        database.tulis_data(daftar)

        logger.tulis_log(f"Hapus item: {item}")
        return f"❌ '{item}' dihapus."
    else:
        logger.tulis_log("Gagal hapus item: nomor tidak valid")
        return "⚠️ Nomor tidak valid."


def edit_item(no, nama_baru):
    """Mengedit item pada nomor urut tertentu"""
    daftar = database.baca_data()
    if 1 <= no <= len(daftar):
        item_lama = daftar[no - 1]
        daftar[no - 1] = nama_baru
        database.tulis_data(daftar)

        logger.tulis_log(f"Edit item: {item_lama} → {nama_baru}")
        return f"✏️ '{item_lama}' diubah menjadi '{nama_baru}'."
    else:
        logger.tulis_log("Gagal edit item: nomor tidak valid")
        return "⚠️ Nomor tidak valid."


def cari_item(kata_kunci):
    """mengembalikan daftar item yang mengandung kata kunci"""
    daftar = database.baca_data()
    hasil = [item for item in daftar if kata_kunci.lower() in item.lower()]

    logger.tulis_log(f"Cari item dengan kata kunci: {kata_kunci}")
    import backend
import logger


def tampilkan_daftar(daftar):
    for i, item in enumerate(daftar, start=1):
        print(f"{i}. {item}")


def tambah_item_handler():
    item = input("Nama item: ")

    if item.strip() == "":
        print("⚠ Nama item tidak boleh kosong.")
        logger.tulis_log("Peringatan: input item kosong")
    else:
        pesan = backend.tambah_item(item)
        print(pesan)
        logger.tulis_log(f"Menambah item: {item}")


def lihat_item_handler():
    daftar = backend.semua_item()

    if not daftar:
        print("🛒 Daftar belanja kosong.")
        logger.tulis_log("Melihat daftar (kosong)")
    else:
        print("\n📋 Daftar Belanja:")
        tampilkan_daftar(daftar)
        logger.tulis_log("Melihat daftar item")
    return hasil