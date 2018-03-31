import math
import sys
import itertools



def synthesis_break(s) :
    N = math.sqrt(s) + 2
    i = 2
    first_flag = 0
    while s != 1 and i != N :
        if s % i == 0 :
            s = s / i
            if first_flag == 0 :
                sys.stdout.write(str(i))
                first_flag = 1
            else :
                sys.stdout.write(" * " + str(i))
        else :
            i += 1
        if i == N :
            sys.stdout.write(" * " + str(i))
    print("")



print("")
sys.stdout.write("all number : ")
num_of_hand=int(input())
sys.stdout.write("field number : ")
use_number=int(input())
print("")

cards = []
string_cards = []

for num in range(num_of_hand):
    sys.stdout.write("card"+str(num+1)+" : ")
    input_value = input()
    cards.append(int(input_value))
    string_cards.append(input_value)

cards_string_list = []

cards_combination_lists = list(itertools.permutations(string_cards, use_number))
for cards_list in cards_combination_lists:
    cards_string = ''.join(cards_list)
    cards_string_list.append(cards_string)

cards_int_list = list(map(int, cards_string_list))

cards_int_list.sort(reverse=False)
i = 0
while i + 1 < len(cards_int_list) :
    if cards_int_list[i] == cards_int_list[i+1] :
        del cards_int_list[i+1]
    else :
        i += 1

NG_count = 1

print("")
for s in cards_int_list :
    hold_cards = list(cards)
    hold_s = s
    while s != 0 :
        cards.remove(s % 10)
        s = int(s / 10)
    s = hold_s
    prime_factor = []
    use_cards = []
    N = math.sqrt(s) + 2
    i = 2
    while s != 1 and i != N :
        if s % i == 0 :
            s = s / i
            prime_factor.append(i)
            # print(prime_factor)
        else :
            i += 1
    if i == N :
        prime_factor.append(s)
    while len(prime_factor) > 0 :
        if len(prime_factor) > 1 and prime_factor[0] == prime_factor[1] :
            same_count = 1
            while same_count < len(prime_factor) and prime_factor[0] == prime_factor[same_count] :
                same_count += 1
            move_number = prime_factor[0]
            for loop in range(same_count) :
                prime_factor.remove(move_number)
            while move_number > 9 :
                add_number = move_number % 10
                use_cards.append(add_number)
                move_number = int(move_number / 10)
            use_cards.append(move_number)
            use_cards.append(same_count)
        else :
            move_number = prime_factor[0]
            prime_factor.remove(move_number)
            while move_number > 9 :
                add_number = move_number % 10
                use_cards.append(add_number)
                move_number = int(move_number / 10)
            use_cards.append(move_number)
    hold_use_cards = list(use_cards)
    # print(use_cards)
    for i in range(len(cards)) :
        if cards[i] in use_cards :
            use_cards.remove(cards[i])
    if len(use_cards) == 0 :
        print("")
        sys.stdout.write(" " + str(hold_s) + " = ")
        synthesis_break(hold_s)
        print("")
    else :
        print(" " + str(hold_s) + " NG MAKING " + str("{0:05d}".format(NG_count)))
        NG_count += 1
    # print(hold_cards)
    cards = list(hold_cards)
print("")

if NG_count == len(cards_int_list) + 1 :
    print(" NO MAKE SYNTHESIS NUMBER")
    print("")
