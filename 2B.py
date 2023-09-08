from itertools import product

def HammingDistance(str1,str2):
    udalj=0
    for i in range(len(str1)):
        if str1[i]!=str2[i]:
            udalj+=1
    return udalj

def FindAllKmers(text,k):
    kmers=[]
    for i in range(len(text)-k+1):
        kmers.append(text[i:(i+k)])
    return kmers

def GenerateAllKmers(k):
    set=k*[['A','C','G','T']]
    return list(product(*set))

def Udaljenost1(pattern,text):
    niz_udaljenosti=[]
    for el in FindAllKmers(text,len(pattern)):
        niz_udaljenosti.append(HammingDistance(el,pattern))
    return min(niz_udaljenosti)

def Udaljenost2(pattern,dnas):
    niz_udaljenosti=[]
    for dna in dnas:
        niz_udaljenosti.append(Udaljenost1(pattern,dna))
    return sum(niz_udaljenosti)

def MedianString(k, dnas):
    min_distance = float("inf")
    median = ""

    for pattern in GenerateAllKmers(k):
            distance = Udaljenost2(pattern, dnas)
            if distance < min_distance:
                min_distance = distance
                median = pattern
                
    return median

k = 6
dnas=['TGTTGGTTGTGATCACGTGGCGTAGGGGCAGTTCTGGAAGCC','CGTAATGCATTCCCTTGTTCCTTTATGTTGGAGGCATACGAA','GCCTTAGCTATATCAGGGTTTTTCATAAAGGTGGCACTTTTC','GAGGCACCAATTTGAAGTAAAGATTCATAGCTGATGATCCGT','TGGTCTGAAGGACTATATACTTGACCACGCGCGGCACCAAAT','GCTCTTCATAGAGTACGCAAGCATGGGGCATACTATAGGACA','AGATCGTCCGTAGGGGCAATCCTACTCTTTCCGCTCCTGCGG','GGAGTGCCTCATCCTGTTTAAGAAGTGGCATCACGTCGGGCC','GCGGGAGATATCGAGGCAGATAATTTTCTTCGCTATTGTCTG','TCAGACATATATGTGATCTTAACCGGGGCAATTGACGGAACG']
result = MedianString(k, dnas)
print(result)
