def SymbolToNumber(slovo):
    if slovo=="A":
        return 0
    if slovo=="C":
        return 1
    if slovo=="G":
        return 2
    if slovo=="T":
        return 3
    
def PatternToNumber(pattern):
    if len(pattern)==0:
        return 0
    else:
        return 4*PatternToNumber(pattern[0:len(pattern)-1])+SymbolToNumber(pattern[-1])
    
pattern=input()
print(PatternToNumber(pattern))