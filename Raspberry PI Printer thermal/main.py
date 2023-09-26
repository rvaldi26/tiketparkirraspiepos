from escpos import *
import datetime

sekarang = datetime.datetime.now()

format_tanggal = sekarang.strftime("%Y-%m-%d")
format_waktu = sekarang.strftime("%H:%M:%S")

def run():
    p = printer.Usb (0x4b43,0x3830 , 
    timeout=0, in_ep=0x81, out_ep=0x03)
    # Print text
    p.set(align='Left')
    p.text("\nRSU IMELDA PEKERJA INDONESIA\n")
    p.text("Jl. Bilal No.24, Pulo Brayan Darat I, Kec.Medan Tim., Kota Medan, Sumatera Utara 20239\n")
    p.set(align='Center')
    p.text("-------------------------------------------\n\n")
    #p.qr('halo valdi di sini', size=10, native=True)
    p.set(align='Left')
    p.text(format_tanggal)
    p.text("\nUmum\n\n")
    p.barcode(format_waktu,"CODE128", function_type="B", height=80, width=4, pos='BELOW'"\n\n\n\n")
    p.text("\n HARAP TIDAK MENINGGALKAN TIKET DI KENDARAAN. TIKET HILANG AKAN DIKENAKAN DENDA\n")
    p.text("KUNCI KENDARAAN ANDA, JANGAN TINGGALKAN BARANG BERHARGA DI KENDARAAN, SEGALA BENTUK KEHILANGAN BUKAN TANGGUNG JAWAB PENGELOLA PARKIR\n")
    p.text("TERIMA KASIH\n\n\n")

    # Print image
    #p.image("logo.gif") 
    # Cut paper
    p.cut()
    #p.close()

run()
