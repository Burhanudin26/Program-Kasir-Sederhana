#masukan harga barang
harga_barang= int(input("\nBerapa harga barangnya? :"))
#harga barang didiskon
harga_barang= harga_barang - harga_barang/10
#pelanggan membayar
print("\nSilahkan bayar sejumlah RP.",harga_barang,)
uang_dibayar= int(input("\nmasukan jumlah uang anda: "))
#Selesai membayar
if uang_dibayar >= harga_barang :
    uang_kembalian = uang_dibayar-harga_barang
    print("terima kasih telah berbelanja\n silakan ambil uang kembalian anda sebesar : RP.", uang_kembalian)
else:
    print("terima kasih telah berbelanja")