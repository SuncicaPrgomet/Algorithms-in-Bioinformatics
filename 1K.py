from itertools import product
from collections import Counter
def FindAllKmers(text,k):
    kmers=[]
    for i in range(0,len(text)-k+1):
        kmers.append(text[i:(i+k)])
    return kmers

def GenerateAllKmers(k):
    set=k*[['A','T','C','G']]
    return sorted(list(product(*set)))

def FreqArray(text,k):
    freq_arr=[]
    dict=Counter(FindAllKmers(text,k))
    for el in GenerateAllKmers(k):
        kmer=''.join(el)
        freq_arr.append(dict[kmer])

    return freq_arr

text=input()
k=input()
niz=' '.join([str(el) for el in FreqArray(text,k)])
print(niz)