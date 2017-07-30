for i in range(1, 101):
    for j in range(i, 101):
        k=(i**2+j**2)**0.5
        if k==int(k):
            print("(", i, j, int(k), ") forme un trio")
