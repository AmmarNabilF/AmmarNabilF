print("Masukkan akun anda   dengan USERNAME dan PASSWORD yang sama")

# username: Ammar Nabil Fauzan
# password: 6
username = input()
benar = "Ammar Nabil Fauzan"
password = int(input())
benar2 = 6
if username == benar and password == benar2:
    print("selamat datang")
else:
    salah = 0
    while username != benar or password != benar2 and salah <= 3:
        print("coba lagi")
        salah = salah + 1
        for kesalahan in range(1, salah + 1, 1):
            if username == benar and password == benar2:
                pass
            else:
                salah = kesalahan + 1
                if username == benar and password == benar2 or salah > 3:
                    print("Akun anda diBLOKIR!!")
                print("Masukkan username anda lagi: ")
                username = input()
                benar = "Ammar Nabil Fauzan"
                print("Masukkan password anda lagi: ")
                password = int(input())
                benar2 = 6
                print("kesalahan: " + str(salah))
    print("selamat datanggg")
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
else:
    if 18.5 <= bmi and bmi < 24.9:
        print("nilai BMI anda: " + str(bmi) + ", anda termasuk normal")
    else:
        if 24.9 <= bmi and bmi <= 29.9:
            print("nilai BMI anda: " + str(bmi) + ", anda termasuk Overweight")
        else:
            print("nilai BMI anda: " + str(bmi) + ", anda termasuk Obesitas")
