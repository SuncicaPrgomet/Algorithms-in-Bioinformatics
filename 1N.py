from itertools import product

def HammingDistance(str1,str2):
    udalj=0
    for i in range(len(str1)):
        if str1[i]!=str2[i]:
            udalj+=1
    return udalj

def GenerateAllKmers(k):
    set=k*[['A','C','G','T']]
    return list(product(*set))

def fja(dna,greska):
    k=len(dna)
    niz=[]
    for el in GenerateAllKmers(k):
        kmer=''.join(el)
        if HammingDistance(kmer,dna)<=greska:
            niz.append(kmer)
    return " ".join(niz)

dna=input()
greska=int(input())
print(fja(dna,greska))