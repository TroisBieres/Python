n = eval(input("Entrez valeur: "))
res = 0

while n > 0:
    res += n%10
    n //= 10
    print(res, n)

print(res)
