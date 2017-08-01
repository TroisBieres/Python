s = 1200
n = eval(input("Entrez nombre de mensualités: "))
for i in range(1, n):
    s *= 1.15
print("Au bout de", n, "mensualités, le capital est à", int(s))
