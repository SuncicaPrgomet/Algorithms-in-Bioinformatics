def ReverseComplement(string):
    novi=""
    for i in range(0,len(string)):
        if string[i]=="A":
            novi+="T"
        if string[i]=="T":
            novi+="A"
        if string[i]=="C":
            novi+="G"
        if string[i]=="G":
            novi+="C"
    return novi[::-1]
string=input()
print(ReverseComplement(string))