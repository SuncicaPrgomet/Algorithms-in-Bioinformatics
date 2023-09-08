def Prefix(pattern):
    return pattern[:len(pattern)-1]
def SUffix(pattern):
    return pattern[1:len(pattern)]
def DeBrujiGraph(patterns):
    D=dict()
    for kmer in patterns:
        if Prefix(kmer) not in D.keys():
            D[Prefix(kmer)]=[SUffix(kmer)]
        else:
            D[Prefix(kmer)].append(SUffix(kmer))
    return D

def PrintResultToFile(D):
    f = open("result.txt","w")
  
    for key in D.keys():
        st = key+'->'
        for i in range(len(D[key])):
            if i>0:
                st+=','+D[key][i]
            else:
                st+=D[key][i]
        f.write(st+'\n')
    f.close()

with open("C:/Users/kmart/OneDrive/Radna površina/ABI/rosalind_ba3e (1).txt") as file:
    patterns=[line.rstrip() for line in file]

D=DeBrujiGraph(patterns)
PrintResultToFile(D)