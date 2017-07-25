x = eval(input("Entrez une année: "))
if (x%4==0 and x%100!=0 or x%400==0):
    print(x, "est une année bisextile")
else:
    print(x, "n'est pas une année bisextile")
