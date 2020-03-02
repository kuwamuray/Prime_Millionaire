
import math
import sys
import itertools
import sympy

print("")
sys.stdout.write("CARD NUMBER : ")
hand_string = str(input())
joker_flag = 0
hand_string_list = list(map(str, hand_string))

hand_int = []
for i in range(len(hand_string_list)) :
    if hand_string_list[i] == "t" :
        hand_int.append("10")
    elif hand_string_list[i] == "j" :
        hand_int.append("11")
    elif hand_string_list[i] == "q" :
        hand_int.append("12")
    elif hand_string_list[i] == "k" :
        hand_int.append("13")
    elif hand_string_list[i] == "x" :
        joker_flag += 1
    else :
        hand_int.append(hand_string_list[i])

if sum(list(map(int, hand_int))) % 3 == 0 and "x" not in hand_string_list :
    print()
    print("  THIS COMBINATION IS MULTIPLE OF 3 !!!")
    print()
    sys.exit()

cards_string_list = []
if joker_flag == 0 :
    cards_string_list = list(map(lambda x : "".join(x), list(set(list(itertools.permutations(hand_int, len(hand_string_list)))))))
elif joker_flag == 1 :
    if len(hand_int) > 7 :
        for i in range(10,14) :
            hand_int.append(str(i))
            if sum(list(map(int, hand_int))) % 3 != 0 :
                print("i = " + str(i))
                L = list(set(list(map(lambda x : "".join(x), list(itertools.permutations(hand_int))))))
                print("length A = " + str(len(L)))
                cards_string_list += L
                if len(cards_string_list) > 30000 :
                    cards_string_list.sort(reverse=True)
                    cards_string_list = cards_string_list[:30000]
                print("length B = " + str(len(cards_string_list)))
            hand_int.remove(str(i))
    else :
        for i in range(14) :
            hand_int.append(str(i))
            if sum(list(map(int, hand_int))) % 3 != 0 :
                L = list(set(list(map(lambda x : "".join(x), list(itertools.permutations(hand_int))))))                               
                cards_string_list += L
            hand_int.remove(str(i))
else:
    for i in range(10, 14) :
        for j in range(10, 14) :
            print("i = " + str(i) + " : j = " + str(j))
            hand_int.append(str(i))
            hand_int.append(str(j))
            if sum(list(map(int, hand_int))) % 3 != 0 :
                L = list(map(lambda x : "".join(x), list(set(list(itertools.permutations(hand_int, len(hand_string_list)))))))
                cards_string_list += L
            hand_int.remove(str(i))
            hand_int.remove(str(j))
            
prime_flag = 0
print("")
cards_int_list = list(map(int, cards_string_list))
cards_int_list.sort(reverse=True)
for candidate in cards_int_list :
    d = sympy.factorint(candidate)
    if candidate in d :
        print()
        print(" max prime is " + str(candidate))
        prime_flag = 1
        break
    elif 2 not in d and 3 not in d and 5 not in d :
        print(str(candidate) + " = " + str(d))

if prime_flag == 0 :
    print("")
    print("can't make prime number.")
print("")
