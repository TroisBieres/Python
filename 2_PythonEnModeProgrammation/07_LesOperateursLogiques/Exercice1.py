p = eval(input("Poids (kg) "))
t = eval(input("Taille (m) "))
imc = p/(t**2)

if imc < 25 :
    print("Poids moyen")
elif (imc>=25 and imc<30) :
    print("Surpoids")
else :
    print("obésité sévère")
