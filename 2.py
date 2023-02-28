def f(x, A):
    l1 = x % A == 0
    l2 = x % 16 == 0
    l3 = x % 16 != 0
    l4 = x % 24 == 0
    return (l1 <= l2) <= (l3 <= l4)

for A in range(1, 200):
    flag = True
    for x in range(1, 200):
        if f(x, A) == False:
            flag = False
    if flag == True:
        print(A)
#Ответ: 1



