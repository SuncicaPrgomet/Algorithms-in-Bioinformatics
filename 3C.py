def Prefix(pattern):
    return pattern[0:len(pattern)-1]
def Sufix(pattern):
    return pattern[1:len(pattern)]
def OverlapGraph(patterns):
    for pattern in patterns:
        for pattern_ in patterns:
            if Sufix(pattern)==Prefix(pattern_):
                print(pattern,"->",pattern_)

with open("C:/Users/1/Downloads/rosalind_ba3c.txt") as file:
    patterns=[line.rstrip() for line in file]
OverlapGraph(patterns)