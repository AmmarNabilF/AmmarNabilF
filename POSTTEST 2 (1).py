print("Selamat anda diterima sebagai mahasiswa baru di Universitas Mulawarman. Anda dimohon untuk mengisi biodata anda berikut untuk melengkapi data dan berkenalan dengan anda:")

nama_lengkap = str(input("Nama Lengkap: "))
nama_pendek = str(input("Nama Pendek: "))
jenis_kelamin = str(input("Jenis kelamin: "))
nim = (input("NIM: "))
asal_sekolah = input("Asal Sekolah: ")
alamat = input("Alamat Sekarang: ")
tinggi_badan = float(input("Tinggi Badan:  (harus desimal!) "))
berat_badan = float(input("Berat badan: (harus desimal!) "))

modulus = nim[7:10]
modulus2 = str(modulus)
pembilang = int(modulus2)
pembagi = 4
hasil = pembilang % pembagi

perkenalan_dalam_kalimat = f"Hai. Nama saya {nama_lengkap} biasa dipanggil {nama_pendek}, saya merupakan {jenis_kelamin} dengan NIM {nim}, saya berasal dari  {asal_sekolah}, dan sekarang saya tinggal di {alamat}. Saya memiliki tinggi {tinggi_badan} cm dengan berat {berat_badan} kg {hasil}."
print(perkenalan_dalam_kalimat)