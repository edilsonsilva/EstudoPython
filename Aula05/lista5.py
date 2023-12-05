n1 = [1,2,5,90,45,12,8,15]
n2 = [21,35,2,48,9,8,12,67,15,45]
n3 = []
n4 = []
for i in n1:
    for j in n2:
        if i == j:
            # print(i)
            n3.append(i)
        if i % j == 0:
            n4.append(i)
       

print(n3)
print(n4)
