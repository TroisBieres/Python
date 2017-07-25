a=eval(input("Nombre 1: "))
b=eval(input("Nombre 2: "))
c=eval(input("Nombre 3: "))


if (b>a and b>c):
    a,b,c = b,a,c
elif (c>a and c>a):
    a,b,c = c,a,b

if (a**2==b**2+c**2):
    print("Le triangle est rectangle")
else:
    print("Le triangle n'est pas rectangle")
