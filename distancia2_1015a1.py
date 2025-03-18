import sqrt. from math
p1 = []
p2 = []
i = 0
c = 0
for i in range(i, 2):
    num = float(input(f"x{i+1} "))
    p1.append(num)
    i=+1
i=+1
for c in range(c, 2):
    num = float(input(f"y{c+1} "))
    p2.append(num)
    c=+1
c=+1
print(p1)
print(p2)
resultado = sqrt((p1[1]-p1[0])**2 + (p2[1]-p2[0])**2)
print(round(resultado, 4))