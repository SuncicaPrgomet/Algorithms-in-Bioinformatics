from itertools import product

def FindAllKmers(text,k):
    kmers=[]
    for i in range(len(text)-k+1):
        kmers.append(text[i:(i+k)])
    return kmers

def GenerateAllKmers(k):
    set=k*[['A','T','C','G']]
    return list(product(*set))

def HammingDistance(str1,str2):
    udalj=0
    for i in range(len(str1)):
        if str1[i]!=str2[i]:
            udalj+=1
    return udalj

def Reverse(rijec):
    nova=""
    if rijec=="A":
        nova+="T"
    if rijec=="T":
        nova+="A"
    if rijec=="C":
        nova+="G"
    if rijec=="G":
        nova+="C"
    
    return nova[::-1]

def Mismatches(text,k,greska):
    dict={}
    for el in GenerateAllKmers(k):
        kmer=''.join(el)
        dict.update({kmer:0})
        kmer_reverse=Reverse(kmer)
        for kmer_text in FindAllKmers(text,k):
            if HammingDistance(kmer,kmer_text)<=greska:
                dict[kmer]+=1
            if HammingDistance(kmer_reverse,kmer_text)<=greska:
                dict[kmer]+=1
    return ' '.join([x[0] for x in dict.items() if x[1]==max(dict.values())])

text=input()
k=int(input())
greska=int(input())
print(Mismatches(text,k,greska))