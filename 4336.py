
import itertools
import sympy
import sys

def String2List(L):
    LL = []
    for s in L :
        if s == "t" :
            LL.append(10)
        elif s == "j" :
            LL.append(11)
        elif s == "q" :
            LL.append(12)
        elif s == "k" :
            LL.append(13)
        else :
            LL.append(int(s))
    return LL

print()

top_string = input("TOP : ")
bot_string = input("BOT : ")

top_list = String2List(list(top_string))
bot_list = String2List(list(bot_string))

if (sum(top_list) + sum([4,3,3,6]) + sum(bot_list)) % 3 == 0 :
    print()
    print("  THIS COMBINATION IS MULTIPLE OF 3 !!!")
    print()
    sys.exit()

top_roll_list = list(map(int, (map(lambda x : "".join(x), list(itertools.permutations(list(map(str, top_list))))))))
bot_roll_list = list(map(int, (map(lambda x : "".join(x), list(itertools.permutations(list(map(str, bot_list))))))))

top_roll_list.sort(reverse=True)
bot_roll_list.sort(reverse=True)

print(top_roll_list)
print(bot_roll_list)

i,j,k = 0,0,0

while k == 0 :
    N = int(str(top_roll_list[i]) + "4336" + str(bot_roll_list[j]))
    D = sympy.factorint(N)
    print(str(N) + " = " + str(D))
    if N in D :
        k = 1
    else :
        j += 1
        if j == len(bot_roll_list) :
            i += 1
            j  = 0
            if i == len(top_roll_list) :
                print()
                print("  NOTHING 4336 PRIME ....")
                print()
                k = - 1
