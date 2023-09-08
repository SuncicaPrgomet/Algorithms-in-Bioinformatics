def fja(patterns):
    text=patterns[0]
    for i in range(1,len(patterns)):
        text+=patterns[i][-1]
    return text


with open("C:/Users/1/Downloads/rosalind_ba2h (1).txt") as file:
  inlines=[line.rstrip() for line in file]

kmer=inlines[0]
collection=inlines[1:len(inlines)]
print(fja(inlines))