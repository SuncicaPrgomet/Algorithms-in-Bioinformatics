def NumberToPattern(number,k):
    pattern=list()
    D={0:"A",1:"C",2:"G",3:"T"}
    q=number
    for i in range(0,k):
        r=q%4
        q=q//4
        pattern.append(D[r])
    return "".join(pattern[::-1])

number=int(input())
k=int(input())
print(NumberToPattern(number,k))
