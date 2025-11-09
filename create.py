from prettytable import PrettyTable
import pandas as pd
from data import judul
import inquirer
import os
from read import lihatproduk

pesanan = {}

def tambahpesanan():
    global pesanan
    try:
        df = pd.read_csv('produk.csv')
    except FileNotFoundError:
        print("File tidak ditemukan.")
        return

    filtered_df = lihatproduk()
    if filtered_df is None:
        return

    try:
        pesan_id = int(input("masukkan ID pesanan anda: "))
    except ValueError:
        print("Input harus berupa angka.")
        return

    if pesan_id not in filtered_df['id'].values:
        print("ID produk tidak valid.")
        return

    produk = df[df['id'] == pesan_id]

    stok = produk['stok'].values[0]
    if stok <= 0:
        print("Stok produk habis.")
        return

    nama = produk['nama'].values[0]
    harga = produk['harga'].values[0]
    kategori = produk['kategori'].values[0]
    gender = produk['gender'].values[0]

    try:
        jumlah_input = int(input(f"Masukkan jumlah untuk '{nama}': "))
    except ValueError:
        print("Input jumlah harus berupa angka.")
        return

    if jumlah_input <= 0:
        print("Jumlah harus lebih dari 0.")
        return

    if jumlah_input > stok:
        print("Jumlah melebihi stok tersedia.")
        return

    produk_ada = False
    for key, item in pesanan.items():
        if item['id'] == pesan_id:
            item['jumlah'] += jumlah_input
            produk_ada = True
            break

    if not produk_ada:
        pesanan_len = len(pesanan) + 1
        pesanan[pesanan_len] = {
            'id': pesan_id,
            'nama': nama,
            'kategori': kategori,
            'harga': harga,
            'gender': gender,
            'jumlah': jumlah_input
        }

    df.loc[df['id'] == pesan_id, 'stok'] -= jumlah_input
    df.to_csv('produk.csv', index=False)

    os.system("cls || clear")
    table = PrettyTable()
    table.field_names = ["No", "Nama Produk", "Kategori", "Harga", "Gender", "Jumlah"]
    for no, item in pesanan.items():
        table.add_row([no, item['nama'], item['kategori'], item['harga'], item['gender'], item['jumlah']])
    print(table)
    print(f"Pesanan '{nama}' telah ditambahkan.")