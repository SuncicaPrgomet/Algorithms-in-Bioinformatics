def FindAllKmersBezPonavljanja(text,k):
    kmers=[]
    for i in range(0,len(text)-k+1):
        if text[i:(i+1)] not in kmers:
            kmers.append(text[i:(i+k)])
    return kmers

def PatternCount(text,pattern):
    count=0
    for i in range(0,len(text)-len(pattern)+1):
        if text[i:(i+len(pattern))]==pattern:
            count+=1
    return count

def fja(text,k,L,t):
    niz=[]
    prozori=FindAllKmersBezPonavljanja(text,L)
    for prozor in prozori:
        kmerovi=FindAllKmersBezPonavljanja(prozor,k)
        for kmer in kmerovi:
            if PatternCount(prozor,kmer)>=t and kmer not in niz:
                niz.append(kmer)
    return niz

text=input()
k=int(input())
L=int(input())
t=int(input())
niz=' '.join([str(el) for el in fja(text,k,L,t)])
print(niz)