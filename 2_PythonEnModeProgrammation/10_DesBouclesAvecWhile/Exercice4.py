n = eval(input("Entrez une valeur: "))

while n != 1:
    if n%2 == 0:
        n //= 2
    else:
        n = 3*n+1
    print(n)
