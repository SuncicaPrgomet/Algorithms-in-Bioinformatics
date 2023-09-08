from collections import Counter
     

def Convolution(spectrum):
  positive_differences = []
  i = 0
  while i <= len(spectrum) - 1:
    for aminoacid_integer_mass in spectrum[0:i]:
      if spectrum[i] - aminoacid_integer_mass > 0:
        positive_differences.append(spectrum[i]-aminoacid_integer_mass)
    i = i + 1
  positive_differences_counter_dict = Counter(positive_differences)
  positive_differences_sorted = sorted(positive_differences_counter_dict,key=positive_differences_counter_dict.get,reverse=True)
  positive_differences = []
  for key in positive_differences_sorted:
    for i in range(positive_differences_counter_dict[key]):
      positive_differences.append(key)
  return positive_differences

with open("C:/Users/kmart/Downloads/rosalind_ba4h (4).txt") as file:
  inlines=[line.rstrip() for line in file][0]

spectrum=inlines.split(' ')
for i in range(len(spectrum)):
  spectrum[i] = int(spectrum[i])
spectrum = sorted(spectrum)
f = open("task_result.txt", "w")
for solution in Convolution(spectrum):
  f.write(str(solution) + ' ')
f.close()