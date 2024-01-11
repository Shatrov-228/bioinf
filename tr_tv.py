def transition_transversion_ratio(s1, s2):
    transition_transversion_dict = {'AG': 'transition', 'CT': 'transition', 'AC': 'transversion', 'GT': 'transversion', 'AT': 'transversion', 
                                    'CG': 'transversion'}
    transition = 0
    transversion = 0
    for nucl in range(0, len(s1)):
        if s1[nucl] != s2[nucl]:
            current_key = ''.join(sorted([s1[nucl], s2[nucl]]))
            if transition_transversion_dict[current_key] == 'transition':
                transition += 1
            else:
                transversion += 1
    print(f'Кол-во транзиций = {transition}, кол-во трансверсий = {transversion}, коэффициент = {transition / transversion}')

s1 = 'GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGAAGTACGGGCATCAACCCAGTT'
s2 = 'TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGCGGTACGAGTGTTCCTTTGGGT'
transition_transversion_ratio(s1, s2)
