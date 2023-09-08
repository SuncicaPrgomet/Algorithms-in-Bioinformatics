from itertools import product
def GenerateAllKmers(k):
    set=k*[['A','T','G','C']]
    return list(product(*set))
def FindAllKmers(pattern,k):
    kmers=[]
    for i in range(0,len(pattern)-k+1):
        if pattern[i:(i+k)] not in kmers:
            kmers.append(pattern[i:(i+k)])
    return kmers
def HammingDistance(p,q):
    ham_dist=0
    for i in range(len(p)):
        if p[i]!=q[i]:
            ham_dist+=1
    return ham_dist
def DNeighbourhood(pattern,d):
    neighbours=[]
    for kmer in GenerateAllKmers(len(pattern)):
        kmer=''.join(kmer)
        if HammingDistance(kmer,pattern)<=d and kmer not in neighbours:
            neighbours.append(kmer)
    return neighbours
def RemoveDuplicate(patterns):
    removedduplicates=[]
    for el in patterns:
        if el not in removedduplicates:
            removedduplicates.append(el)
    return removedduplicates




def MotifEnumeration(list_dna,k,d):
    patterns=[]
    for dna in list_dna:
        for kmer in FindAllKmers(dna,k):
            for kmer_neighbour in DNeighbourhood(kmer,d):
                kmer_neighbour=''.join(kmer_neighbour)
                counter=0
                for dna in list_dna:
                    for comparison_kmer in FindAllKmers(dna,k):
                        if HammingDistance(comparison_kmer,kmer_neighbour)<=d:
                            counter+=1
                            break
                if counter==len(list_dna):
                    patterns.append(kmer_neighbour)
        return RemoveDuplicate(patterns)



dna = ['ATTTGGC', 'TGCCTTA', 'CGGTATC', 'GAAAATT']
k=3
d=1
print(MotifEnumeration(dna,k,d))


dna_=['GGGTCTGACGGTGCCATGCAATTGT','GCTATGTAGTATTATGCGCTGGCCT','AGCTTCGGGAATTCTTTGCCTCTAC','CGTCATTGCTATTTTTGGTGCACCA','ATGAGTACGGCGTCGAGATTATTTT','TCGCCGCAGCAATTATTTTGATTAT','TATGATAAAACCTAGCAACCATTTT','ACATTGGTGCATTGTGGGTACAACT','ATTATTGCCGATCTGCCAGCTTCCG','GATATCATTGCCGGCATTCTAATGA']
res=MotifEnumeration(dna_,5,1)
for el in res:
    print(el)