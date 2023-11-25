'''
INPUTS : DNA sequence in string format, cDNA sequence in string format
OUTPUT : List of introns and exons
'''

def intronExon(dna, cdna):
  g, c = dna, cdna
  intron, exon = [], []

  exon_index = 0  #index of the last element of the exon found in g
  limit = 5   # minimum length of an exon

  while len(c) > 0:
    limit = 5   # Reset limit to 5 after every iteration

    # This loop finds the total length of the exon
    while c[:limit] in g and limit <= len(c):
      limit += 1

    exon_index = g.find(c[:limit-1])  #This finds the starting index of the exon in the DNA string

    # Add the respective intron and exon to their lists
    exon.append(g[exon_index:(exon_index + limit -1)])
    intron.append(g[:exon_index])

    # Remove the exon found from the DNA and cDNA sequence; remove intron from DNA sequence
    c = c.replace(exon[-1], "", 1)
    g = g.replace(exon[-1], "", 1)
    g = g.replace(intron[-1], "", 1)

  # This makes sure any intron isn't left
  if len(g)>0:
    intron.append(g)

  print(f'Exons : {exon}')
  print(f'Introns : {intron}')

#Example
intronExon("ACTACTTTGACTCGACTGCATTATCGGACTCTCTCTGGACTTACTCT", "TTGACTTTATCGGGGACTT")

'''
Example's Output :
Exons : ['TTGACT', 'TTATCGG', 'GGACTT']
Introns : ['ACTACT', 'CGACTGCA', 'ACTCTCTCT', 'ACTCT']
'''
