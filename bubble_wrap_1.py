
import random
import sympy

def card2number(J,S):
    j = 0
    SS = ""
    for i in range(len(S)):
        if S[i] == "A" :
            SS += "1"
        elif S[i] == "T" :
            SS += "10"
        elif S[i] == "J" :
            SS += "11"
        elif S[i] == "Q" :
            SS += "12"
        elif S[i] == "K" :
            SS += "13"
        elif S[i] == "X" :
            if J[j] == "A" :
                SS += "1"
            elif J[j] == "T" :
                SS += "10"
            elif J[j] == "J" :
                SS += "11"
            elif J[j] == "Q" :
                SS += "12"
            elif J[j] == "K" :
                SS += "13"
            else :
                SS += J[j]
            j += 1
        else :
            SS += S[i]
    return int(SS)

def index2card(A):
    B = list(A)
    B.sort()
    C = []
    for i in range(len(B)):
        if B[i] == 1 :
            C.append("A")
        elif B[i] == 10 :
            C.append("T")
        elif B[i] == 11 :
            C.append("J")
        elif B[i] == 12 :
            C.append("Q")
        elif B[i] == 13 :
            C.append("K")
        elif B[i] == 99 :
            C.append("X")
        else :
            C.append(str(B[i]))
    return C

def ResetField(J,A,B,C):
    j = 0
    for i in range(len(A)):
        if A[i] == "A" :
            N = 1
        elif A[i] == "T" :
            N = 10
        elif A[i] == "J" :
            N = 11
        elif A[i] == "Q" :
            N = 12
        elif A[i] == "K" :
            N = 13
        elif A[i] == "X" :
            N = 99
        else :
            N = int(A[i])
        B.remove(A[i])
        C.append(N)
    return B,C

first_card_num = 11

card_list = list(range(54))
card_list = random.sample(card_list,len(card_list))

print()

for i in range(54):
    if card_list[i] > 51 :
        card_list[i] = 99
    else :
        card_list[i] += 1
        while card_list[i] > 13 :
            card_list[i] -= 13

print(card_list)
print()

hold_number_list = card_list[:first_card_num]
del card_list[:first_card_num]
hold_card_list = index2card(hold_number_list)

while len(hold_card_list) != 0 :

    print(hold_card_list)
    print()

    field_card = input("FIELD CARD : ")
    joker_list = []

    if field_card.count("X") == 1 :
        x_card = input("X = ")
        joker_list.append(x_card)
    elif field_card.count("X") == 2 :
        x_card_1 = input("X_1 = ")
        joker_list.append(x_card_1)
        x_card_2 = input("X_2 = ")
        joker_list.append(x_card_2)

    N = card2number(joker_list, field_card)
    D = sympy.factorint(N)
    print(str(N) + " = " + str(D))
    print()

    if N in D or N == 57 or N == 1729 :
        hold_card_list, card_list = ResetField(joker_list, field_card, list(hold_card_list), list(card_list))
        print(hold_card_list)
        print(card_list)
        print()
