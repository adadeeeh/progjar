import random
import time

z = 1
listsoal = []
listhasil = []
skor = 0

while (z <= 10):
    ops = ['+', '-', '*', '/']

    loop = random.randint(4, 6)
    i = 0
    soal = []


    # membuat soal dan memasukkan soal ke list maths
    while (i < loop):
        num1 = random.randint(1, 10)
        num1 = str(num1)
        soal.append(num1)
        operation = random.choice(ops)
        operation = str(operation)
        soal.append(operation)
        i = i + 1
    num2 = random.randint(1, 10)
    num2 = str(num2)
    soal.append(num2)
    soal = ''.join(soal)
    soal = soal+'\n'
    #print(soal)
    listsoal.append(soal)
    listsoal = listsoal
    #print(listsoal)
    hasil = eval(soal)
    #print (hasil)
    listhasil.append(hasil)
    print (listhasil)
    z = z + 1
for a in range(10):
    print (listsoal[a])
    print (listhasil[a])
    jawab = input("jawaban : ")
    #if(time.sleep(5)):
    #    continue
    for z in listhasil:
        if (jawab == z):
            skor = skor + 5
print (skor)