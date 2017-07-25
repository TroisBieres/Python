x = eval(input("Nombre 1: "))
y = eval(input("Nombre 2: "))

if x < y:
    x,y = y,x

print ("x:", x, " y:", y)
