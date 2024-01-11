s1 = 'GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGAAGTACGGGCATCAACCCAGTT'
s2 = 'TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGCGGTACGAGTGTTCCTTTGGGT'
dna_dict = {'AG': 'transition', 'CT': 'transition', 'AC': 'transversion', 'GT': 'transversion', 'AT': 'transversion', 'CG': 'transversion'}
    transition = 0
    transvertion = 0
    for nucl in range(0, len(s1)):
        if s1[nucl] != s2[nucl]:
            identifier = ''.join(sorted([s1[nucl], s2[nucl]]))
            if dna_dict[identifier] == 'transition':
                transition += 1
            else:
                transvertion += 1
print(f'Кол-во транзиций = {transition}, кол-во трансверсий = {transversion}, коэффициент = {transition / transvertion}')
