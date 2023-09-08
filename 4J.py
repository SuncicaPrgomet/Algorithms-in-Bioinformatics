def get_amino_acid_mass():
    mass = {
        "G": 57,
        "A": 71,
        "S": 87,
        "P": 97,
        "V": 99,
        "T": 101,
        "C": 103,
        "I": 113,
        "L": 113,
        "N": 114,
        "D": 115,
        "K": 128,
        "Q": 128,
        "E": 129,
        "M": 131,
        "H": 137,
        "F": 147,
        "R": 156,
        "Y": 163,
        "W": 186,
    }

    return mass


     

def ReturnPeptidePrefixes(peptide):
  peptide_prefixes = []
  i = 1
  while i <= len(peptide):
    peptide_prefixes.append(peptide[0:i])
    i = i + 1
  return peptide_prefixes
     

def ReturnPeptideIntegerMass(peptide):
  peptide_mass = 0
  D=get_amino_acid_mass()
  for aminoacid in peptide:
    peptide_mass = peptide_mass + D[aminoacid]
  return peptide_mass

def FindAllKmers(peptide,k):
  kmers_list = []
  i = 0
  while i + k - 1 <= len(peptide)-1:
    kmers_list.append(peptide[i:i+k])
    i = i + 1
  return kmers_list
     

def GenerateAllSubpeptides(peptide):
  subpeptides = []
  for subpeptide_length in range(1,len(peptide)):
    subpeptides.extend([[' '] + FindAllKmers(peptide,subpeptide_length)])
  subpeptides.append([' '] + [peptide])
  return subpeptides
     

def LinearSpectrum(peptide):
  peptide_prefixes_masses = [0] #mass of empty peptide
  theoretical_linear_spectrum = [0]
  for peptide_prefix in ReturnPeptidePrefixes(peptide):
    peptide_prefixes_masses.append(ReturnPeptideIntegerMass(peptide_prefix))
  subpeptides = GenerateAllSubpeptides(peptide)
  for subpeptide_group in enumerate(subpeptides):
    for i in range(1,len(subpeptide_group[1])):
      theoretical_linear_spectrum.append(peptide_prefixes_masses[i+(subpeptide_group[0]+1)-1]-peptide_prefixes_masses[i-1]) #k = (subpeptide_group[0] + 1)
  return sorted(theoretical_linear_spectrum)
     
with open("C:/Users/kmart/Downloads/rosalind_ba4j.txt") as file:
  inlines=[line.rstrip() for line in file]

peptide=inlines[0]
def rosalindprint(res):
    return " ".join([str(x) for x in res])
print(rosalindprint(LinearSpectrum(peptide)))