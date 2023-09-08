from itertools import product

def FindAllKmers(text,k):
    kmers=[]
    for i in range(len(text)-k+1):
        kmers.append(text[i:(i+k)])
    return kmers

def GenerateAllKmers(k):
    set=k*[['A','T','C','G']]
    return sorted(list(product(*set)))

def HammingDistance(str1,str2):
    udalj=0
    for i in range(len(str1)):
        if str1[i]!=str2[i]:
            udalj+=1
    return udalj

def Mismatches(text,k,d):
    dict={}
    for el in GenerateAllKmers(k):
        kmer=''.join(el)
        dict.update({kmer:0})
        for kmer_text in FindAllKmers(text,k):
            if HammingDistance(kmer,kmer_text)<=d:
                dict[kmer]+=1 
    return dict
text=input()
k=int(input())
d=int(input())
dict=Mismatches(text,k,d)
print(' '.join(x[0] for x in dict.items() if x[1]==max(dict.values())))