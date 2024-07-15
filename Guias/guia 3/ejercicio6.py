h=0
m=0
s=0
while h!=24:
    if m==60:
        h+=1
        m=0
    else:
        if s!=60:
            print(f"{h}:{m}:{s}")
            s+=1
        else:
            m+=1
            s=0