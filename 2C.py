
def FindAllKmersBezPonavljanja(text,k):
    kmers=[]
    for i in range(0,len(text)-k+1):
        if text[i:(i+k)] not in kmers:
            kmers.append(text[i:(i+k)])
    return kmers

def Index(slovo):
    if slovo=='A':
        return 0
    if slovo=='C':
        return 1
    if slovo=='G':
        return 2
    else:
        return 3
def KmerProbability(profile,kmer):
    prob=1
    for k in enumerate(kmer):
        prob=prob * profile[Index(k[1])][k[0]]
    return prob

def ProfileMostProbableKmer(text,k,profile):
    rj=""
    prob=0
    for kmer in FindAllKmersBezPonavljanja(text,k):
        if KmerProbability(profile,kmer)>prob:
            prob=KmerProbability(profile,kmer)
            rj=kmer
    return rj

text='TGAGACGAGAGACACAAAGGACGTATTCGAATTGAGTCAGCAATCCTGGAGCCTCACGTCCATCGACCTCAGTGCGAATAGTGGGTCTTCAGTGACGTTGAGGAGGTACTCGTGCCACGTACCCCCGATATGCCTCGACCGTGCATCAAGTAAGTCGAGATAAGGACTCAAGTTCTACGGTAGCCAACCCCTGACGTCTG'
k=8
profile=[[0.16 ,0.12, 0.36, 0.16, 0.36, 0.16, 0.36, 0.32],[0.24, 0.28, 0.2, 0.32, 0.2, 0.24, 0.24, 0.16],[0.24, 0.32, 0.32, 0.16, 0.2, 0.36, 0.24, 0.28],[0.36, 0.28, 0.12, 0.36, 0.24, 0.24 ,0.16 ,0.24]]
print(ProfileMostProbableKmer(text,k,profile))