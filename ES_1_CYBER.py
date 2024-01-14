a = 3
b = 4
c = 5
ca = 0
cb = 0
cc = 0
cta = 0
ctb = 0
ctc = 0
for _ in range(0, 2000):
    a -= 1
    b -= 1
    c -= 1
    if (a == 0 && cta = 0):
        ca += 1
    elif(b == 0):
        cb += 1
    elif(c == 0):
        cc += 1
    else:
        ca += 1
    
    if (a == 0):
        ca -= 1
        a = 3
    if (b == 0):
        b = 4
        cb -= 1
    if (c == 0):
        c = 5
        cc -= 1
    
print(f"ca: {ca}")
print(f"cb: {cb}")
print(f"cc: {cc}")

tot = ca - (2000/3)
print(tot)


