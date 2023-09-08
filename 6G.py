def rosalind_input(text):
    tmp = [int(x) for x in text[1:-2].split(" ")]
    return tmp


def cycle_to_chromosome(cycle):
    chromosome = []
    for i in range(0, len(cycle), 2):
        if cycle[i] < cycle[i + 1]:
            chromosome.append(cycle[i + 1] // 2)
        if cycle[i] > cycle[i + 1]:
            chromosome.append(-1 * cycle[i] // 2)
    return chromosome


def f(x):
    if x >= 0:
        return f"+{x}"
    else:
        return f"{x}"


def rosalind_print(cycle):
    return "(" + " ".join([f(x) for x in cycle]) + ")"


with open("C:/Users/kmart/Downloads/rosalind_ba6g.txt") as file:
   inlines=[line for line in file]

cycle=rosalind_input(inlines[0])
print(rosalind_print(cycle_to_chromosome(cycle)))