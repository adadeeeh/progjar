import random
import time

z = 1
while (z <= 10):
    ops = ['+', '-', '*', '/']

    loop = random.randint(4, 6)
    i = 0
    numx = []
    numy = []
    op = []
    maths = []
    mathsss = []
    # membuat soal dan memasukkan soal ke list maths
    while (i < loop):
        num1 = random.randint(1, 10)
        numx.append(num1)
        num2 = random.randint(1, 10)
        numy.append(num2)
        operation = random.choice(ops)
        op.append(operation)
        if i == 0:
            # print('{}{}{}'.format(numx[i],op[i],numy[i]))
            math = numx[i], op[i], numy[i]
        else:
            # print('{}{}'.format(op[i],numy[i]))
            math = op[i], numy[i]
        maths.append(math)
        i = i + 1

    # masukkan soal ke list-of-list
    mathss = (str(maths[0][0]) + maths[0][1] + str(maths[0][2]))
    # print(mathss)
    mathsss.append(mathss)

    for i in xrange(1, loop):
        matha = (maths[i][0] + str(maths[i][1]))
        mathsss.append(matha)
        # print(matha)
        # print maths[i][0]
        # print maths[i]

    if (loop == 4):
        hitung = eval(str(maths[0][0]) + maths[0][1] + str(maths[0][2]) + maths[1][0] +
                      str(maths[1][1]) + maths[2][0] + str(maths[2][1]) + maths[3][0] +
                      str(maths[3][1]))
        print(hitung)

    # menghitung soal
    if (loop == 5):
        hitung = eval(str(maths[0][0]) + maths[0][1] + str(maths[0][2]) + maths[1][0] +
                      str(maths[1][1]) + maths[2][0] + str(maths[2][1]) + maths[3][0] +
                      str(maths[3][1]) + maths[4][0] + str(maths[4][1]))
        print(hitung)
    if (loop == 6):
        hitung = eval(str(maths[0][0]) + maths[0][1] + str(maths[0][2]) + maths[1][0] +
                      str(maths[1][1]) + maths[2][0] + str(maths[2][1]) + maths[3][0] +
                      str(maths[3][1]) + maths[4][0] + str(maths[4][1]) + maths[5][0] +
                      str(maths[5][1]))
        print(hitung)
    # print(maths[0])
    # print(mathsss)
    # menghapus atribut-aitribut dalam list
    print ''.join(map(str, mathsss))
    #print ''.join(mathsss)

    # mathsss = (maths[1][0] + str(maths[1][1]))
    # print(maths)
    z = z+1
    time.sleep(10)