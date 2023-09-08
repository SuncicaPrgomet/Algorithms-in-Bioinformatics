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

def FindAllKmers(peptide,k):
  kmers_list = []
  i = 0
  while i + k - 1 <= len(peptide)-1:
    kmers_list.append(peptide[i:i+k])
    i = i + 1
  return kmers_list
     

def GenerateAllSubpeptides(peptide):
  subpeptides = []
  for subpeptide_length in range(1,len(peptide)+1):
    subpeptides.extend(FindAllKmers(peptide,subpeptide_length))
  subpeptides.append(peptide)
  return subpeptides
     

def SubpeptideMass(subpeptide):
  mass = 0
  masses=get_amino_acid_mass()
  for aminoacid in subpeptide:
    mass = mass + masses[aminoacid]
  return mass
     

def LinearSpectrum(peptide):
  theoretical_linear_spectrum = [0]
  for subpeptide in GenerateAllSubpeptides(peptide):
    theoretical_linear_spectrum.append(SubpeptideMass(subpeptide))
  return theoretical_linear_spectrum
     

from collections import Counter

def LinearPeptideScoring(peptide,spectrum): #the score is computed for spectrum against peptide's theoretical spectrum --> spectrum is experimental spectrum
  peptide_theoretical_spectrum = LinearSpectrum(peptide)
  peptide_theoretical_spectrum_counter_dict = Counter(peptide_theoretical_spectrum)
  spectrum_counter_dict = Counter(spectrum)
  score = 0
  scored_aminoacid_integer_masses = []
  for aminoacid_integer_mass in spectrum:
    if aminoacid_integer_mass not in scored_aminoacid_integer_masses:
      if spectrum_counter_dict[aminoacid_integer_mass] == peptide_theoretical_spectrum_counter_dict[aminoacid_integer_mass]:
        score = score + spectrum_counter_dict[aminoacid_integer_mass]
        scored_aminoacid_integer_masses.append(aminoacid_integer_mass)
      elif spectrum_counter_dict[aminoacid_integer_mass] > peptide_theoretical_spectrum_counter_dict[aminoacid_integer_mass]:
        if peptide_theoretical_spectrum_counter_dict[aminoacid_integer_mass] > 0: #if peptide_theoretical_spectrum_counter_dict[aminoacid_integer_mass] > 0 then there are surpluss occurences of same mass in experimental spectrum
          score = score + peptide_theoretical_spectrum_counter_dict[aminoacid_integer_mass]
          scored_aminoacid_integer_masses.append(aminoacid_integer_mass)
      else: #spectrum_counter_dict[aminoacid_integer_mass] < peptide_theoretical_spectrum_counter_dict[aminoacid_integer_mass] --> there are surpluss occurences of same mass in theoretical spectrum
        score = score + spectrum_counter_dict[aminoacid_integer_mass]
        scored_aminoacid_integer_masses.append(aminoacid_integer_mass)
  return score


def Trim(leaderboard,linear_spectrum,N):
  leaderboard_scores_dict = {}
  for linear_peptide in leaderboard:
    leaderboard_scores_dict.update({linear_peptide:LinearPeptideScoring(linear_peptide,linear_spectrum)}) #LinearPeptideScoring(linear_peptide,linear_spectrum) --> score of linear_peptide's spectrum against linear_spectrum
  sorted_linear_peptides = sorted(leaderboard_scores_dict.keys(), key=leaderboard_scores_dict.get, reverse=True) #peptides sorted by scores
  top_n_peptides = sorted_linear_peptides[0:N] #last index is N-1, next index is N
  i = N
  for i in range(N,len(sorted_linear_peptides)):
    if leaderboard_scores_dict[sorted_linear_peptides[i]] == leaderboard_scores_dict[top_n_peptides[len(top_n_peptides)-1]]:
      top_n_peptides.append(sorted_linear_peptides[i])
    else:
      break
  return top_n_peptides

with open("C:/Users/kmart/Downloads/rosalind_ba4l.txt") as file:
  inlines = [line.rstrip() for line in file]

leaderboard=inlines[0].split(' ')
linear_spectrum=inlines[1].split(' ')
N=int(inlines[2])

f = open("task_result_L.txt","w")
for solution in Trim(leaderboard,linear_spectrum,N):
  f.write(solution + '\n')
f.close()