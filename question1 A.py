L1=['HTTP','HTTPS','FTP','DNS']
L2=[80,443,21,53]
d={}
for key in L1 :
    for value in L2 :
        d[key]= value
        L2.remove(value)
        break
print(d)
