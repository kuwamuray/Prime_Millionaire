import sympy

L = ["9","8","7","2","11"]

for i in range(1,14):
    M = list(L)
    M.insert(2,str(i))
    M.insert(1,str(i))
    M.insert(0,str(i))
    S = ""
    for j in range(len(M)):
        S += M[j]
    N = int(S)
    D = sympy.factorint(N)
    print(str(N) + " = " + str(D))
