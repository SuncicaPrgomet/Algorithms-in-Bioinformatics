def HammingDistance(str1,str2):
    count=0
    for i in range(0,len(str1)):
        if str1[i]!=str2[i]:
            count+=1
    return count

def Kmer(text,i,k):
    return text[i:(i+k)]

def fja(pattern,text,greska):
    niz=[]
    for i in range(0,len(text)-len(pattern)+1):
        if HammingDistance(pattern,Kmer(text,i,len(pattern)))<=greska:
            niz.append(i)

    return niz

pattern=input()
text=input()
greska=int(input())
niz=' '.join([str(el) for el in fja(pattern,text,greska)])
print(niz)