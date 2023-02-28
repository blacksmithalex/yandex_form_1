def f(x, A):
    l1 = x & 41  == 0
    l2 = x & 119 != 0
    l3 = x & A != 0
    return l1 <= (l2 <= l3)

for A in range(200):
    flag = True
    for x in range(200):
        if f(x, A) == False:
            flag = False
    if flag == True:
        print(A)
#Ответ: 86

