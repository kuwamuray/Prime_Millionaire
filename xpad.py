import random
import sympy
import sys

N = 3

count = 0
NG = 0
while NG == 0 :

    count += 1
    x = random.randrange(N)
    num_l = ["0" for i in range(N)]
    num_n = [ 0  for i in range(N)]

    for i in range(N - 1) :
        n = random.randrange(13) + 1
        num_n[i] = n
        if n == 10 :
            num_l[i] = "T"
        elif n == 11 :
            num_l[i] = "J"
        elif n == 12 :
            num_l[i] = "Q"
        elif n == 13 :
            num_l[i] = "K"
        else :
            num_l[i] = str(n)
    num_l[N-1] = random.sample(["1","3","7","9"],k=1)[0]
    num_n[N-1] = int(num_l[N-1])
    num_l[x] = "X"

    NUM_L = ""
    for i in range(N) :
        NUM_L += num_l[i]

    sys.stdout.write(str(count) + " QUESTION : " + str(NUM_L) + " : X = ")
    pad_number = int(input())

    num_n[x] = pad_number
    NUM_N = 0
    for i in range(N) :
        if num_n[i] < 10 :
            NUM_N = NUM_N *  10 + num_n[i]
        else :
            NUM_N = NUM_N * 100 + num_n[i]

    NUM_D = sympy.factorint(NUM_N)
    if len(NUM_D) == 1 and NUM_N in NUM_D :
        print(NUM_D)
    else :
        print(NUM_D)
        NG = 1
