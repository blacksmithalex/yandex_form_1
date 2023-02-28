def f(t, m, A):
    l1 = 3 * t + 8 * m > 89
    l2 = m < A
    l3 = t <= A
    return l1 or (l2 and l3)

for A in range(200):
    flag = True
    for t in range(200):
        for m in range(200):
            if f(t, m, A) == False:
                flag = False
    if flag == True:
        print(A)
        break
#Ответ: 29