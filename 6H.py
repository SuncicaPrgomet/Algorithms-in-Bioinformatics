def string_to_int_repr(text):
    return [int(x) for x in text.split(" ")]


def rosalind_input(text):
    chromosomes = text.split(")")
    chromosomes = [string_to_int_repr(chrom[1:]) for chrom in chromosomes[:-1]]
    return chromosomes


def chromosome_to_cycle(permutation):
    cycle = []
    for x in permutation:
        if x > 0:
            cycle.extend([2 * x - 1, 2 * x])
        if x < 0:
            x = abs(x)
            cycle.extend([2 * x, 2 * x - 1])
    return cycle


def get_colored_edges(chromosomes):
    edges = []
    for chrom in chromosomes:
        nodes = chromosome_to_cycle(chrom)
        for j in range(1, len(nodes) - 1, 2):
            edges.append((nodes[j], nodes[j + 1]))
        edges.append((nodes[-1], nodes[0]))
    return edges


def rosalind_print(edges):
    return repr(edges)[1:-1]

with open("C:/Users/kmart/Downloads/rosalind_ba6h.txt") as file:
   inlines=[line for line in file]

chromosomes=rosalind_input(inlines[0])
print(rosalind_print(get_colored_edges(chromosomes)))