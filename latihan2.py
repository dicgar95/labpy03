max = 0

while True:
    angka = int (raw_input("Masukan Bilangan : "))
    if max < angka:
        max = angka
    if angka == 0:
        break

print ("Bilangan terbesarnya adalah :",max)
