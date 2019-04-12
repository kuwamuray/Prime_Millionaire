import math
import sys
import itertools
import sympy

def CheckPrime(x,y):
    n = x * 10 + y
    d = sympy.factorint(n)
    if n in d :
        return 1
    else :
        return 0

print("")
sys.stdout.write("FIELD NUMBER : ")
fn = int(input())
sys.stdout.write(" CARD NUMBER : ")
hand_string = str(input())
hand_string_list = list(hand_string)

hand_int = []
for i in range(len(hand_string_list)) :
    if hand_string_list[i] == "t" :
        hand_int.append(10)
    elif hand_string_list[i] == "j" :
        hand_int.append(11)
    elif hand_string_list[i] == "q" :
        hand_int.append(12)
    elif hand_string_list[i] == "k" :
        hand_int.append(13)
    else :
        hand_int.append(int(hand_string_list[i]))

cards_string_list = []
cards_combination_lists = list(itertools.permutations(hand_int, fn - 1))
print(cards_combination_lists)

cards_int_list = list(set(cards_combination_lists))
cards_int_list.sort(reverse=True)
print(cards_int_list)

quad_count = 0
for candidate in cards_int_list:
    if sum(candidate) % 3 == 1 :
        N = 0
        for i in range(len(candidate)):
            if candidate[i] < 10 :
                N = N * 10 + candidate[i]
            else :
                N = N * 100 + candidate[i]
        if CheckPrime(N,1) == 1 :
            if CheckPrime(N,3) == 1 :
                if CheckPrime(N,7) == 1 :
                    if CheckPrime(N,9) == 1 :
                        S = ""
                        quad_count += 1
                        for i in range(len(candidate)):
                            if candidate[i] == 10 :
                                S += "T"
                            elif candidate[i] == 11 :
                                S += "J"
                            elif candidate[i] == 12 :
                                S += "Q"
                            elif candidate[i] == 13 :
                                S += "K"
                            else :
                                S += str(candidate[i])
                        print("No." + str(quad_count) + " : " + str(S) + "X is quad prime.")

if quad_count == 0 :
    print("Quad prime is nothing.")
