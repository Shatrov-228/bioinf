def reverse_complement(dna_string):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    reverse_complement = ''.join(complement[nucl] for nucl in reversed(dna_string))
    return reverse_complement

dna_sequence = "ATCGATTGCG"
print(reverse_complement(dna_sequence))
