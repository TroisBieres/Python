print("Question A")

n = eval(input("Entrez une valeur : "))
a = 180*(n-2)/n
print("Chaque angle d'un polygone régulier a", n, "angle de", a, "degre")

print ("Question B")
a2 = eval(input("Entrez la valeur d'un angle en degre: "))
n2 = 360/(180-a2)
if n2 == int(n2):
    print(a2, "est un angle pouvant être d'un polygone régulier à", n, "côtés")
else:
    print(a2, "ne peut pas être un angle d'un polygone régulier")
