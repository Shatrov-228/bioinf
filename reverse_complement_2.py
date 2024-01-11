def reverse_complement(dna_string):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    reverse_string = dna_string[::-1]
    reverse_complement = ''
    for nucl in reverse_string:
        reverse_complement += complement[nucl]
    return reverse_complement

dna_sequence = "ATCGATTGCG"
print(reverse_complement(dna_sequence))
