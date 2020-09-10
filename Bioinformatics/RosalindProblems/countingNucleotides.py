#countingNucleotides.py

# Author: J Cooper Hopkin
# Problem Source: http://rosalind.info/problems/dna/
# Problem: A string is simply an ordered collection of symbols selected from some alphabet and formed into
# a word; the length of a string is the number of symbols that it contains.
# An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."
#     Given: A DNA string s of length at most 1000 nt.
#     Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s

def countNucleotides(dataset):
    a= 0
    g= 0
    c= 0
    t= 0
    for char in dataset:
        if char=='A':
            a+=1
        elif char=='G':
            g+=1
        elif char=='T':
            t+=1
        elif char=='C':
            c+=1
        else:
            raise ValueError("Invalid Character Found")
    for nt in [a,c,g,t]:
        print(nt, end=' ')
    print()

    return [a,c,g,t]

if __name__ == "__main__":
    countNucleotides("GTTGCACCCCTACTGATAGGGATCGCGTTATACAGTCTTCGATTAGCTCAAAACCTCCTATTTATGAAGAGCCCGAGAATCAAATTACTGCGCGGGTAGGACCGTAAGTGCGTGGGCTACCCAGCATTAAGGTAAAGAGCCGTGATATCTGGATCATTATACGCAGTTTGTATACCTAGAAGCCAATCTGCTGTGGTCCCCGGCCGGCTCGTATTTTGCGCAACCTTCTCTTCCATGAAGATTACGGGGTCAGCCCACCGACGTGGGTCCCGCTTGACTTGCTTGTATTTGCAGCGGTTGAGAACAAAAGGGCGGTATACAAGTTTGACACATGTGGCTTATATTGCGCGCTATTCGGGTAACTTAGTGTGCTAACCCCGATATAGTCCAGGACCGTTGCGCGGCTCGTCTGGGGCGCACGAGTGTTTTCCCAAGTATTCTGAGGGGGGACTATGTAGGGGTGTTGTCTACGCAGATTAGATTAATGTCTTGGTACAACAGATTCCGACAATCAATGTCGCTAGACGCAGCATGAGCGTAAGAGCCTTGACTAGCCACCCAAGTGTGGACCGGTTGTAGAACCGAAAAGGCGATCATACAACGCCGGCAGGCGGTATATAGGTGACCGAGGCTTAGATCGTCCTGGGGTTGGGCGGGCTAAGCACGTACGACCCCGCCATTAGACGTAGTACATCGCGGAGACCATGCGCTTTGTAGGGCGACCCCCGGTTTGGCATATTATCACCTTGAACGCACGAGGCGTAATTGGTCCCTGTCCGTCTAACTGATCCTGGAAATGG")

