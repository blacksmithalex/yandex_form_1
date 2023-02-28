def f(x, y, A):
    l1 = x <= 9
    l2 = x * x <= A
    l3 = y * y <= A
    l4 = y <= 10
    return (l1 <= l2) and (l3 <= l4)

for A in range(200):
    flag = True
    for x in range(200):
        for y in range(200):
            if f(x, y, A) == False:
                flag = False
    if flag == True:
        print(A)
#Ответ: 120



