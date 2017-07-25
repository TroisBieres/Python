x = eval(input("Entre une valeur pour x: "))
y = (x%2)+(x%3)+(x%5)

if y == 0 :
    print(x, "est un multiple de 2, 3 et 5")
else:
    print(x, "n'est pas un multiple de 2, 3 ou 5")
