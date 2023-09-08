def Kmer(text,i,k):
    return text[i:(i+k)]

def fja(pattern,text):
    niz=[]
    for i in range(len(text)-len(pattern)+1):
        if(pattern==Kmer(text,i,len(pattern))):
            niz.append(i)

    return niz

pattern=input()
text=input()
niz=' '.join([str(el) for el in fja(pattern,text)])
print(niz)

