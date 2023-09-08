def Kmer(text,i,k):
    return text[i:(i+k)]

def fja(text,k):
    d=dict()
    for i in range(0,len(text)-k+1):
        temp=Kmer(text,i,k)
        try:
            d[temp]+=1
        except KeyError:
            d[temp]=1
    return d

def rjesenje(text,k):
    d=fja(text,k)
    maksimum=max(d.values())
    return ' '.join([x[0] for x in d.items() if x[1]==maksimum])

text=input()
k=int(input())
print(rjesenje(text,k))