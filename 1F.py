def Skew(skew_value,citamo):
    if citamo=="C":
        return skew_value-1
    elif citamo=="G":
        return skew_value+1
    else:
        return skew_value

def MinSkew(text):
    skew=[0]
    for i in range(0,len(text)):
        skew.append(Skew(skew[len(skew)-1],text[i]))
    
    return skew

text=input()
min=min(MinSkew(text))
niz=MinSkew(text)
rj=" "
for i in range(len(niz)):
    if niz[i]==min:
        rj+=str(i)+" "
print(rj)
