print("Apakah ingin meneruskan program, ketik[Takn nak] jika ingin berhenti")
lanjut = input()
while lanjut != "Tak nak":
    
    print("Masukkan akun anda   dengan USERNAME dan PASSWORD yang sama")

# username: "Ammar Nabil Fauzan"
# password: 6

    data_username = "Ammar Nabil Fauzan"
    data_password = "6"

    salah = 0

    while salah < 3:
        username = str(input("username: "))
        password = str(input("password: "))
    
        if username == data_username and password == data_password:
            print("Selamat Datang, ",username)
            break
        else:
            salah += 1
            print("Kesalahan ke- ", salah)
        
    if salah == 3:
        print("ANDA DIBLOKIR")
        break
    else:
        print("Berapa berat badan anda (mg): ")
        beratbadan = float(input())
        print("berapa tinggi badan anda (km): ")
        tinggibadan = float(input())
        beratbadan2 = beratbadan / 1000000
        tinggibadan2 = tinggibadan * 1000
        tinggibadan3 = tinggibadan2 * tinggibadan2
        print("berikut data anda: " + str(beratbadan2) + " kg dan " + str(tinggibadan3) + " m")
        bmi = beratbadan2 / tinggibadan3
        if 0 <= bmi and bmi < 18.5:
            print("nilai BMI anda: " + str(bmi) + ", anda termasuk underweight")
        elif 18.5 <= bmi and bmi < 24.9:
            print("nilai BMI anda: " + str(bmi) + ", anda termasuk normal")
        elif 24.9 <= bmi and bmi <= 29.9:
            print("nilai BMI anda: " + str(bmi) + ", anda termasuk Overweight")
        else:
            print("nilai BMI anda: " + str(bmi) + ", anda termasuk Obesitas")

        lanjut = str(input("Apakah mau lanjut lagi? ketik [Tak nak] bila nak stop:"))
else:
    print("program akan terus berjalan")
            
        
