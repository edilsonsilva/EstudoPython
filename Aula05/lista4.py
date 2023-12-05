n1 = [20,15,3,48,21]
n2 = [2,51,17,6,20]
p = 0
n3 = []
for i in n1:
    el = i + n2[p]
    n3.append(el)
    p+=1

print(n1)
print(n2)
print(n3)

