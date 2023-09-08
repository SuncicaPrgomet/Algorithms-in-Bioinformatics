def Decompose(k,string):
    rjesenje=[]
    for i in range(0,len(string)-k+1):
        rjesenje.append(string[i:(i+k)])
    return sorted(rjesenje)

k=int(input())
string=input()
niz=Decompose(k,string)
for i in range(len(niz)):
    print(niz[i])

