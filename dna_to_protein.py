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
