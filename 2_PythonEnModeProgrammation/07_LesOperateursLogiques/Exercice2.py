x = eval(input("Entrez une valeur: "))
if (x%3==0 and x%5!=0):
    print(x, "est divisible par 3")
elif (x%3!=0 and x%5==0):
    print(x, "est divisible par 5")
elif (x%3==0 and x%5==0):
    print(x, "est divisible par 3 et par 5")
else:
    print(x, "n'est pas divisible ni par 3 ni par 5")
