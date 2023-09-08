def rosalind_input(text):
    tmp = [int(x) for x in text[1:-2].split(" ")]
    
    return tmp


def chromosome_to_cycle(chromosome):
    cycle = []
    for x in chromosome:
        if x > 0:
            cycle.extend([2 * x - 1, 2 * x])
        if x < 0:
            x = abs(x)
            cycle.extend([2 * x, 2 * x - 1])
    return cycle


def rosalind_print(cycle):
    return "(" + " ".join([str(x) for x in cycle]) + ")"

with open("C:/Users/kmart/Downloads/rosalind_ba6f.txt") as file:
   inlines=[line for line in file]
chromosome=rosalind_input(inlines[0])

print(rosalind_print(chromosome_to_cycle(chromosome)))
