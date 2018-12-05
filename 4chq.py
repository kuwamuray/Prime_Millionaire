import random
import sympy
import sys

DIGIT = 5

COUNT = 0
MIN = pow(10, DIGIT - 1)
MAX = pow(10, DIGIT)
NG = 0

while NG == 0 :
    C = 0
    COUNT += 1
    L = []
    while C < 3 :
        N = random.randrange(MIN,MAX)
        D = sympy.factorint(N)
        if N not in D and 2 not in D and 3 not in D and 5 not in D :
            check_list = list(map(int, str(N)))
            if 0 not in check_list :
                L.append(N)
                C += 1
            else :
                not_good = 0
                for i in range(DIGIT - 1) :
                    if check_list[i+1] == 0 and check_list[i] != 1 :
                        not_good = 1
                if not_good == 0 :
                    L.append(N)
                    C += 1
    while C < 4 :
        N = random.randrange(MIN,MAX)
        D = sympy.factorint(N)
        if N in D :
            check_list = list(map(int, str(N)))
            if 0 not in check_list :
                L.append(N)
                C += 1
            else :
                not_good = 0
                for i in range(DIGIT - 1) :
                    if check_list[i+1] == 0 and check_list[i] != 1 :
                        not_good = 1
                if not_good == 0 :
                    L.append(N)
                    C += 1
    L.sort(reverse=False)
    if COUNT < 10 :
        print("0" + str(COUNT) + " QUESTION")
    else :
        print(str(COUNT) + " QUESTION")
    print("   A : " + str(L[0]))
    print("   B : " + str(L[1]))
    print("   C : " + str(L[2]))
    print("   D : " + str(L[3]))
    sys.stdout.write("PRIME NUMBER IS ... ")
    ANSWER = input()
    if ANSWER == "A" :
        D = sympy.factorint(L[0])
        if L[0] in D :
            print("   " + str(D))
        else :
            print("   " + str(D))
            NG = 1
    elif ANSWER == "B" :
        D = sympy.factorint(L[1])
        if L[1] in D :
            print("   " + str(D))
        else :
            print("   " + str(D))
            NG = 1
    elif ANSWER == "C" :
        D = sympy.factorint(L[2])
        if L[2] in D :
            print("   " + str(D))
        else :
            print("   " + str(D))
            NG = 1
    else :
        D = sympy.factorint(L[3])
        if L[3] in D :
            print("   " + str(D))
        else :
            print("   " + str(D))
            NG = 1
