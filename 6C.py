def StringToIntRepr(text):
    return [int(x) for x in text.split(" ")]
     

def RosalindInput(text):
    chromosomes = text.split(")")
    chromosomes = [StringToIntRepr(chrom[1:]) for chrom in chromosomes[:-1]]
    return chromosomes

def ChromosomeToCycle(chromosome):
    cycle = []
    for x in chromosome:
      if x > 0:
        cycle.extend([2*x-1, 2*x])
      if x < 0:
        x = abs(x)
        cycle.extend([2*x, 2*x-1])
    return cycle
     

def GetColoredEdges(chromosomes):
    edges = []
    for chrom in chromosomes:
        nodes = ChromosomeToCycle(chrom)
        for j in range(1, len(nodes) - 1, 2):
            edges.append((nodes[j], nodes[j + 1]))
        edges.append((nodes[-1], nodes[0]))
    return edges
     
def GetNCycles(edges):
    edges = edges.copy()
    n_cycles = 0
    starting = edges[0][1]
    del edges[0]
    while True:
      found = False
      for i in range(0,len(edges)):
          if starting == edges[i][0]:
              starting = edges[i][1]
              found = True
              break
          if starting == edges[i][1]:
              starting = edges[i][0]
              found = True
              break
      if found:
        del edges[i]
      else:
        # cycle done
        n_cycles += 1
        if len(edges) == 0:
            break
        starting = edges[0][1]
        del edges[0]

    return n_cycles
def TwoBreakDistance(genome_P,genome_Q):
  chromosomes_P = RosalindInput(genome_P)
  chromosomes_Q = RosalindInput(genome_Q)

  colored_edges_P = GetColoredEdges(chromosomes_P)
  colored_edges_Q = GetColoredEdges(chromosomes_Q)

  colored_edges_breakpoint_PQ = colored_edges_P + colored_edges_Q

  n_cycles = GetNCycles(colored_edges_breakpoint_PQ)

  n_syn_blocks = 0
  for chrom in chromosomes_P:
      n_syn_blocks += len(chrom)

  print(n_syn_blocks - n_cycles)

with open("C:/Users/kmart/Downloads/rosalind_ba6c.txt") as file:
   inlines=[line for line in file]

genome_P=inlines[0]
genome_Q=inlines[1]
TwoBreakDistance(genome_P,genome_Q)