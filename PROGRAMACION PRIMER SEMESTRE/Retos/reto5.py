n=int(input("Ingrese un valor : "))
if n==0:
    print([0])
elif n==1:
    print([0,1,1])
else:
    l_fib=[0,1,1]
    l_final=[]
    for i in range(n):
        l_fib.append(l_fib[-1] + l_fib[-2])
    for k in range(len(l_fib)):
        if l_fib[k]<=n:
            l_final.append(l_fib[k])
    print(l_final)