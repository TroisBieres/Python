a = eval(input("Nombre a: "))
n = eval(input("Nombre n: "))

for i in range(1, n):
    print(a, "**", i, "%", n, "=", a**i % n)
