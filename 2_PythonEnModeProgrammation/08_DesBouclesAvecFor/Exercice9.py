for i in range(10):
    for j in range(10):
        for k in range(10):
            n=i*100+j*10+k
            if (i**3+j**3+k**3==n and n>99):
                print(n)
