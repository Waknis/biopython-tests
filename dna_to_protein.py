from Bio.Seq import Seq

# Example DNA sequence
dna_sequence = "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"

# Creating a sequence object
seq = Seq(dna_sequence)

# Translating DNA to Protein
protein_sequence = seq.translate()

# Print the protein sequence
print("DNA Sequence: ", dna_sequence)
print("Protein Sequence: ", protein_sequence)

# This would be the output:
# DNA Sequence:  ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG
# Protein Sequence:  MAIVMGR*KGAR*
#In the protein sequence, each letter corresponds to an amino acid (e.g., 'M' for Methionine, 'A' for Alanine),
# and the '*' symbol represents a stop codon, indicating where the protein sequence ends.