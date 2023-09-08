from posixpath import split


def string_to_int_repr(text):
    return [int(x) for x in text.strip("(, ").split(",")]


def rosalind_input(text):
    edges = text.split(")")[:-1]
    edges = [string_to_int_repr(edge) for edge in edges]
    return edges




def split_edges_to_chromosomes(edges):
    final_pairs = []
    for i, pair in enumerate(edges):
        if pair[0] > pair[1]:
            final_pairs.append(i)

    chromosomes = []
    previous = 0
    for end in final_pairs:
        chromosomes.append(edges[previous : (end + 1)])
        previous = end + 1
    return chromosomes


def colored_edges_to_cycle(edges):
    cycle = []
    for i in range(len(edges) - 1):
        cycle.extend([edges[i][1], edges[i + 1][0]])
    final = [edges[-1][1], edges[0][0]]
    final.extend(cycle)
    return final


def cycle_to_chromosome(cycle):
    chromosome = []
    for i in range(0, len(cycle), 2):
        if cycle[i] < cycle[i + 1]:
            chromosome.append(cycle[i + 1] // 2)
        if cycle[i] > cycle[i + 1]:
            chromosome.append(-1 * cycle[i] // 2)
    return chromosome


def graph_to_genome(colored_edges):
    chromosomes = []
    chromosome_edges = split_edges_to_chromosomes(colored_edges)
    for chrom_edge in chromosome_edges:
        cycle = colored_edges_to_cycle(chrom_edge)
        chromosome = cycle_to_chromosome(cycle)
        chromosomes.append(chromosome)
    return chromosomes


def f(x):
    if x >= 0:
        return f"+{x}"
    else:
        return f"{x}"


def rosalind_print_one(cycle):
    return "(" + " ".join([f(x) for x in cycle]) + ")"


def rosalind_print(chromosomes):
    final = ""
    for chrom in chromosomes:
        final += rosalind_print_one(chrom)
    return final

with open("C:/Users/kmart/Downloads/rosalind_ba6i.txt") as file:
   inlines=[line for line in file]

print(rosalind_print(graph_to_genome(rosalind_input(inlines[0]))))