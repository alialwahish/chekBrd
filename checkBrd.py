chk="* * * *"
s=1
print(chk)

for c in range(0,7):
    if s %2!=0:
        chk=" "+chk
        
    else:
        chk= chk[1:]
    print(chk)
    s+=1