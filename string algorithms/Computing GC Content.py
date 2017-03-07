# ROSALIND
# Bioinformatics Stronghold
# String Algorithms
# Computing GC Content
# Kofi E. Gyan
# Dec. 24th, 2016

"""
Problem

The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content. DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.

In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

Sample Dataset:
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT

Sample Output:
Rosalind_0808
60.919540
"""


## Implement the function

import operator # this module exports a set of efficient functions corresponding to the intrinsic operators of Python

# Function to calculate GC content
def GC_calc(q):
    q = q.replace('\n', '') # replace all occurences of \n with ''
    q = q.strip() # return a copy of the string with leading and trailing characters removed
    length = float(len(q)) # determine the length of the read
    count_G = float(q.count('G')) # total count of G's in the sequence
    count_C = float(q.count('C')) # total count of C's in the sequence
    result = float(((count_G + count_C) / length) * 100) # calculate GC content
    return result

# Function to parse FASTA inputs and return read sequence with the highest GC content
def GC_content(w):
    w = w.strip() # return a copy of the string with leading and trailing characters removed
    start = [] # empty list
    readID_GC = {} # empty dictionary
    total_reads = w.count('>')
    start = [pos for pos, char in enumerate(w) if char == '>'] # find all positions of > in the string
    for i in range(total_reads):
        if i == (total_reads - 1): # determine the final read
            k = w[start[i] + 1:start[i] + 14] # index read ID information
            k = k.strip() # return a copy of the string with leading and trailing characters removed
            q = w[start[i] + 14:] # index read sequence
            q = q.strip() # return a copy of the string with leading and trailing characters removed
            v = GC_calc(q) # calculate GC content
            readID_GC.update({k:v}) # set-up dictionary for final entry
        else:
            k = w[start[i] + 1:start[i] + 14] # index read ID information
            k = k.strip() # return a copy of the string with leading and trailing characters removed
            q = w[start[i] + 14:start[i + 1]] # index read sequence
            q = q.strip() # return a copy of the string with leading and trailing characters removed
            v = GC_calc(q) # calculate GC content
            readID_GC.update({k:v}) # set-up dictionary for enteries
    # return readID_GC   
    sorted_GClist = sorted(readID_GC.items(), key = operator.itemgetter(1), reverse = True) # create a list of tuples sorted by the second element in each tuple, highest to lowest
    # print sorted_GClist
    # sorted_GCdict = dict(sorted_GClist) # convert list of tuples into a dictionary
    # return sorted_GCdict
    for key, value in sorted_GClist:
        print key # display each read ID and its GC content
        print value
        print ' ' # insert a space for aesthetic


# Test the function
w = '''
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT
'''
print GC_content(w)


# EOL string literal erorr solved using ''' quotes
p = '''
>Rosalind_8125
ACCATTCGGGCAAATGTACAGTCATGACAGACAGTCTCGCTTGGTTGTCTACTCGTGCAC
GTAACGCTCCATTCCCATCCCACACCTGCCCGTTCTACTTTAGAAACACTAGTCCGACAC
CGAGAGCTTTCAATCAGCTTAAGGAGTTATGTAGGCTTCGTATGGTACGATTAGCTGTAT
ATTTTCTGTTCATCACTGCGATCACAAGCATCTCGGTCTACCTTCTGAGAGGCTGTACCC
GGTACGGCATCGCCCTGAAAAAATATTCTCATCGTAGCGCGTAAGCCCTCTGACGACGCA
ACCATTGTGTGGCCAAGACTGCGAGTGTATCTTCACAACATCGCTCTACGAGCATAGTTG
AAGCCTCGTTAAACGCCAACACGTCCCAAGTGTCTTAGCTGTGTGGCCACGATTATAGCC
GCACGTGGGTACCCATTCGGGGCTCTTAACCTCTGCTTACCAGCTACATGGCGTTATCGA
ATCTCTGTAATAACTTAACTGGTATACGACGGTAGAGTCTTATAAGGAGTAATATGACGT
GGTAGAGAATTTATGCTCGATAGCACTAACTTGGACTACTTACTTTAGTGTCAGCCGGCA
ATTCACGGGGACGGCATAAGCGTAGCCGCCGAAAATGGTGCCCTTTCTGCAAGCCTGGAT
GCCAGTATACTGGACTTTATGGCCCCGCAGGTTTTTGGTGCCGTGCTTGGCGCACCGTAG
ATGCTAGTTTCGTGTGGCCAGGGGAAGAGCCGCAGGCTTTCGAACCACATTGTGTCTTTC
GGTACCTCGGGTGGGATCTGTAGGCAATGTAGGGCCCACGGCTTACTG
>Rosalind_9897
ACTACGTGTCTGTAGCGTTGCCATAATAGTATGCCCATTGGAAACTGACGGTCCCCTCTG
CTAGGGACAATACTGAGGTAGACTAAGTTTGGTGCGGAGGCTGCATCCCCGAGGTTATAG
CACGATTCGCAAGGCGCATCTGTGAGGGAGGTATTACCCGATATAATTGTTTGAAGTCCG
TGCCGTTTGCTGTACTTGTGGTCGCGTCTTATGAGAGCCTTCCACGTGTAACGATGATCA
GTCCAATAGAAAAATGGAACTCAGAATAGACCTTCTTATTGTGAATAGGCCAGCCGCTCT
CGTAAGTACCTGACGCGCTGTGAACCTGGGTGTTTGTTAACGCACCGCGTTATTGTCTTA
TGACCAGGTGTGGTACGATTCCCTCACGCGTCTAAGTCATGTTTCAGGAGCATCGACATA
GTAATCGTAACTATATCTCAGGTCGTCTTCAATTACACAGCCCCTGCCTGTGAGGAGGTT
TTCTCCCACGGGATACAGGCGCACGTAATGAGGGACTCGCCTCAGCCTACGTCTGCGGTA
AAATGTCCGGTGCCGGTTCAAGTAACGAAAGCACCACATACGGTCAAATTTTTTAATACG
GGCCGCGAGAAATATGTGATTATCGCTAGTTGTGTGTAAGTAGTGGGAAACAAGATCACG
ATCTCGCTCACAAGAGTTATCAAGCGAAATGTTGCTCCGAAAGCAGAGCCAAAAGCGCAC
CATGCGCAGGCCCCCATGCTACGGGCTTAAAGCATATTACTCATGAAGAAGTCCTGTAGA
CTTGGGACAGGATAACAGTTAAGTTAGCCGCCTGCCTCCCATGCTTTGGCATCATTACTG
CTTTTTTGGCGCACCAGCGTTCTACATCAGTTACAGACTATATTCCTCTCAGATATAAAG
CGACCTTGGGCAAATTCTCTTGAGATCTTGTTGTGTCGAGAGTGAGACT
>Rosalind_9951
GTGCAGAGCGCCCCCCGCTCAGACGGTCCAAAACGAAAAAGGGCAGGTCCCGAGAATCCA
GTCGCCGCATGGTTTTCAGTTTAGACTATGCTTTGCTTGGGCAGAGACTACCTTTCCAGA
GGTGAACGCAACAGGGAGACCCACAGCACAATTCGATGAGTTTCTCGCCAACAAAGTCAG
ACCAAAAGCAGGTCTTAGCGTAACGGTCTGTCATCTCTAAGTTTTCACACACCTAAGGCG
CTCAAGGAACGTCCGTGATCCCTGATGAGGAGGTATGCGCTTAGCCGGGAGGGTCGTACT
AGAAGCTGAGACCGTATACATGATCACGGATTTAAGCATCATCCTAAGCGTTACTGAGGC
TTGAGCGTTCGGCAAATCAACGGTGCTTATCAGACAGTGTAGGTTCAGATTACTATGTTT
CTGTTTCGGCTAATGTTACTCATGTTTTTACTACTCTGGAATGTTAGTCAATAGGCGTCA
TAATGTTGCCGCCGTGCCTCACGTATCAACTTTATCTGCAACAGGCGCAATATTCGATCC
CCATCCAAAATCCCCGGCCAGCCGGCGTCTGCAGATTATTCGCTTTTAAGCCGGGAGGGG
CAAGTTTTTAGGGTATCATCGCAGTTCTTAATGGCATAAGACAGGGAGTCCCAAAGCCAT
GCCTTTCTCGTGTGACTTCGATGGGTCAGTATTTAGATCACTATCGACTGGACGAAGACA
CAACCACGTCAGCGTGCTGACACGGACCTGTCATCGCATGAATGACTGCCAGTGACGGCT
GTTCTATAATGAAAGGGTGACTGTGTTATCGGGTTATGGATACACAGCACCTCTCCATTG
AATCATCCCATAACCCCCAACTCAAATGAACGTCTACCCGTGCGTTCGCTCCCTCGAGTC
ATCCACCTAAATTGCCTGGATCAGCGGTTCTCTTTACCGCGAACGCTGGC
>Rosalind_3959
CAATCTAAAACGTAATGGCGAGACTCTAATTGGACGCATCGACCGTTAATTTTCATTTGG
AGTGAATAGGCAGACTGGAATCCCAGCGTGCCAAAAAGTCGTCAGACCAATTAATGGACC
TACGCTGGCCGTGAAGGCTATACTTAAGACAGCGCGGCGGGGTTGGACTGATTCGTCATT
GCCAATGGGTCGCCCCCAGACCAATCAGGGGTGTTTCGTTGTGTTGTTATCAATCCTACG
CCTCTAATTGGGGTAGACGCATCATTCACATCGAAGAACAGTACGGGCCGGTCTAATCTA
GCTCCGCAGTTAGTCGAGCGTAGTGTATAGTGATAAGAGGTACTAGCTCTGAATAGGTTT
TGGCGGGACCGAGGGTCCCAAGGAAGGTGACAATTAGTTTTCCCGGAGACGAGCGTGTGG
GGACCGACTACTCCGATATAGGTTACAACATCCTGATCGTGACAAGGTGCGCGCGGTACC
AGACACTACCCTCACTTACTTCTCAGATTGAAGCGCGTCAGCACCGGGTTGACGTGCTCT
CCTATTTCCTATGCTTGACTGGCGCCAAAGACCCCCGAGGGCCTAATTCAGCTTCGGAAG
GACCCAGCACCGCTGTTCAGCAACCCTTGAAACCAATAATAAATGAATAAGCCCGCTCTA
ACAAACCACCGTCCAGGCTCTATATCTGGAAATCAGGTCCCAACTTATCCTCCTAGCATT
ATCGCATACGCGTTTTGGAAGCTAATAGTTAGAACTTGCCTGTCCTCCTCGTTCGCGTGC
TTTAACTGGCCGGCGGATATATT
>Rosalind_2832
AGGCCGCTCCGTAACAATGTGTCCCACACCTCCAACCAGCTTAAATGACTCCTTTCTTCC
GTCGAGAGGATGCGACGCCAGGTGACAGTTGGTATTATATGGTACACCAAGCGGTATCAC
CTACCCTAGAAGAAAAACTTCCGTTCAGAGCGGTCTACCAGCAGCATTCGGTTCACCCAC
GACCTGCTTTAAACCCATCACCGCCGTATGAAAGTTTAGCGCACCGTGGAGTAACTATAG
ATCGTGTGATAAACCCTGAATCCAGTAAGATGGGCAACTCGTATCCTAGGGCCGTCGAAC
GTCGAGAACTTACATCTTCCCCTGGGCGCAACTTACCAGGGCTACGCAGCAACCAAGCTC
GCTCGACACCAAGCGATTGACTAGGAAGCCAAGCCGCAGTTGGTTGGCGACGGGCGGGCT
AAGTAGGCTCCAGCATGGCTATAATGAGGGTTGAATCAACGGCGCCAGGAGCTCCGAACC
CGTTAGACAACATGGAACGCTTTTGCTCCATACTGCTGGTATCTTTCTCTAATTGTATGA
CCGTCCCCACCATGGTTGAATATTGAGTTGAGGAACGCTGGCAACTGAGCACACGACTTA
GCGATATTTCAGAAATGTTGGTCTATTTTCTTGAGCCCTGACTATTAGTAGCCTGCGTAT
CCCAGTCGGAAGCATGCTGGAAGCTTCGACCCCCCATAGACGTGGTCCCGAGGGTTGCGG
GTCCCGTCTCCGGCGGAATAAAGCCGCTTACCCCCTGTGGGTAGTGAACCAGTAAAGAAA
TCCTTACATCCAATCGCATCCATGGTATCTGGAGATGCTCCAGCGCAGTTCAAGTAAGTC
AAAAGTAGCTACCTACAACCCGCAATCAGGACCTTATTAACTTTTGGCGGGAGCTGCCTA
AAGCCTAGCAACTC
>Rosalind_8906
GCTACGCCCAGGGTTGGGGGTCATTATGACTCGATGATGTTGAATCCTAGGAAGCTTCAA
GTGCACTAAGCGGGCACGGCACCGAGTAATTGTATTCGTTTTTGTGCTGTAACTTCCCGT
TAACGATCCGAATAAAAAGAACGCAATTGAACTAACTGAGATTCACAGATGAACCAGTAA
TGAGGTTTTCTCGCGGTAGGGCCATAACCATTCCAACTCTGGGTACAGCACCGAGGGCCG
GGAAGTCCATAGGACTATGGAGTTGACTCCAGAGACCCATTAATCGAAACATACGTAAGA
ACAGCCGGACCTGCTGCCAAGTATCAGAGCCGCCTTTGGTATGCGGTTGCAAGGGCAGAG
GTGGGTTCATGGCCTATGCCACCTAAGCATTGTCCCTCTCTGGATTCTGGTCAGTCGTTT
CGTAATAGCCCTCCACTAGCCAGCCCATCCGCCAACACGCTAATCCGTGCAGTCTGAAAC
AGAACGAGTGTTGGGACTGAGCGTAGTTGACAGTGCGCAGCGTGTAAGGATACTTGGCGG
ACTTTAGATATCTCCGATCAATATGTGCTGGATGTAAGGTCATGGGAAAAAAGGCTCGTA
TGCTGTATCGGGTGGCATGCTGAAACCCGTCTTGTCGATGTCCGCACGGTCGACTACGCG
GGCCCGGACCATTCGGGGGCGTGGGCTGCTGAGAAGAAACTGCCTGTCTATACGGGCGGA
TGAAACTAGCGTGGAAGACGGCCGTTCGGACAAAAGCTAGCTTCTCTAGCACAGCGCTAC
CACGCTCAAGATGCAGGTTCCTACCAGCCATTTCAATATAGGACTAAATTGAATTATTTC
GAATCTCTACTTCACCGCCAACGCCATTGGAGTCGGTGCATGCATCTTAAGG
>Rosalind_4473
GCAAGCGCAAGGTTGCCGCGAGCTTGTGTAGATGACGGAGCATTTTGACTTCCAAACGCA
TAAGAGCTAGATTCCAGCACTAGGAACAGATAACAGTGGGGGTGCTGTACACGTTCAACC
CAACGCTGCCGTGGCTCGTATTACGCCGTTCCGTGTAGCTGCATGGCTTCCATTGGAGTC
TTGCTCCGTAGATTCCGCTAGAACATTCGATCCGTATACGCTCTGGACCCCACTCGCCCT
AGTGCCGTTCTATATTTTGTGTCATCCATAACTCATCCGTAACCCTGGCAACCTGCGGAG
TGCTCCATGAAATGTGCACTCATGCCTGTCGGGGTGTAGACATACACGTCGACAATTTAC
CGGATCCCCGCGTCACATTGGTCGGTCTACAGTCTGGAGCCTATGTCAACCGAAGCATAT
GTTGACGTTGGTACGGCTCCAGATGGGTACGGCGTTCACGTACAGATCATGAGCAGGCGG
TGCTGGTTGTACGTCTATCGATCCCTACTTTACATCGGGCGTTAGGACAATTTGGTACAC
ATACCTGGCTCGGACTCCTACATACTTAATTATCGGAACGGACTGCATGTAAAGGATGAT
TTCCTCGATGTTTATGAATGAACCATCAACCCTTCTCAATGAGCACTAAGACTGCAGTTG
ACCGGGCTAGCCGATTACATCCGTTAACGCGCAAGCTGAAGGGCCCGGGTTTGAAATCCT
GGTAACTTCATGGCCAACATAACAATACATTTACTGAGCAGGTATCACGCACTGCCTGAC
TGGGCGAACGGCTAGTGCACAGAACGAACACTCACGCGCCTTGCTGCACGTAATTGCTCT
TAGTTATACCAACAACATCGCGGGCGACCTATATGTTTACATGATATTGTACGAGGTATA
TTCTAATAAATAAATGGGGGGTGCC
>Rosalind_6848
GGTCTGGGCAAGTAATCCCAGTCTAATTGTTCGTCAGGCGGCAGATTTTGAAAACATACC
ACCGCCTTGCTTTTAGCAGGACACCCCTTCGCGATTACTCCCCGTCCTGGTTTCTCAAAA
AGAGGACCGAGTAATGCTTCGAGCCTTTATCCCGCCTGCTGCGGGGAGGCGCTGTGATGG
TAACAGTATGCTCCCCGGAGTGCGGCACACAAACAAGAAGGCTGAGAATGATCGCCATTC
AATCTGAGACATAAAGTGACAAGTTCTACTTATAGAGGCCTGTATGTAGCGTTAGCAATG
TCGCTGTTTGCCATTGAAACTAAATGAGTCGCCCTTGGCGTGCCTGATGCATCCTAGCAC
CCATTAGGACTACCTACTAAGGTAGGCACAGTCGTGACTGGAATTTATACGGAAAAGATA
AAAGAGTTCAAAATCTAAAACGCTCTGCTGGTCACTAGGCCCACACTTTGATGGGGCAGT
CGGCGCGAATACGACTTGACTGCTCGTGGTGCTGTCCCTGGTAATAAACCGGCTAAGGAC
TTCATTTAAACAGCCAGCGCTAAACAAAGCCTGGCGCATCTATTCGGGTTTGCACCAATT
TAGTAAGTTTCCGGCGAGATATGCTTCTAAGTATACTTTTGCCATATCAACTTGCGAACA
AACCTTCCACGAAGCATATGGACCTACAGATGTTCGCCCCCAGCTATTTTTAGTTGGTCT
AAAGAAGTTCACACCTGGGGAAAGTCGGCAAAATTCAACCCTCCACTGAGCCAAGGGTGG
GAGTAGTGTTTCCCTAGCTCGTCCAACCATGGCCACGGGATTCACGCATAGGATCCGGCT
TCTTACGCATCAGGTGGCACACTT
>Rosalind_6391
GTGTAAACAGGTAGCCACCTTCTCTTTTAACAGATATCTTCTGGATATGACGAGATATGG
TCGCGAGACCTTACCCCGCATAATTAGATTCTGGGTCGTCTTCATGTCTAGACTAGCTCT
ACGCACACCACGGAAGAGACAAGTTATATAACCCTTATAGATAGATCACGAGGAGCCATA
GGCTTAAAATGACCCGATGAAGACCTGTGCGATGAGGGCTAGGGCAACCATATACTTTCT
TCGCACAAACCTAGCTATAAAGGGTGATACAAACTAAGCTTTGTCGCACAGTCGCGCTCG
GGAACAAACAACGGCCATGCCGAGACACGAAGCCGATCATAGTACATGAGTATCCCGCTA
TATTTAACTTTTCCACTAGCAGAGTACACGCCGATGTGTTACAGAGCGACCGATACCTCA
GCAGGTACCGCATGCACAGCGTGTTGAAAGGCATCGGTTATAACGCAATCATCGAAGATG
CGGTCCTTTTCCTATATGGTTGTAACCAGATCCACGACTAACACTATCAACACCGGAGGA
AGGGATGCCCTTCACATTCACAAATGTAACTTGCCCCCCAATAAGGGTTCCCCGTCATCC
TAGCGTTGAATAACCCTTGTCCATCGGGGGCAGCGTGTTTTGCCTTGGGCCACGCGCCTG
TTAGGGTTCCCGTGGGCCGTTGGGTGATCCTCGCTTAGGGACTAAACTAGGGATGCCGTC
GCAGCAAGTCAAGCCTCGTTGTCGGAGACGCTTAGTCGGAGGCTATCGATCAACCCAGGC
CTGTAACAGCACGAACATAATTAGCTGCTTAGGGTCGCCACCCAAGTTAACTCTTTGCTA
CGCCGACAGG
'''
print GC_content(p)

