"""
This module is a simple DNA analyzer that will convert a DNA sample from a text file to RNA and an amino acid chain. 

Author: Holly White 
Version: 1.5
Date: 12-13-2024
"""
import re 
import matplotlib.pyplot as plt

# First I created a dictionary that defines the matching amino acid associated with 
# every codon possibility in an RNA sequence. There are some codons that will result 
# in the end of the amino acid chain, those are denoted with the key "stop". 
codon_chart = {
    'aug': 'Met ', 
    'uuu': 'Phe ', 'uuc': 'Phe ',
    'uua': 'Leu ', 'uug': 'Leu ',
    'ucu': 'Ser ', 'ucc': 'Ser ', 'uca': 'Ser ', 'ucg': 'Ser ',
    'uau': 'Tyr ', 'uac': 'Tyr ',
    'ugu': 'Cys ', 'ugc': 'Cys ',
    'ugg': 'Trp ',
    'uaa': 'Stop', 'uag': 'Stop', 'uga': 'Stop',
    'cuu': 'Leu ', 'cuc': 'Leu ', 'cua': 'Leu ', 'cug': 'Leu ',
    'ccu': 'Pro ', 'ccc': 'Pro ', 'cca': 'Pro ', 'ccg': 'Pro ',
    'cau': 'His ', 'cac': 'His ',
    'caa': 'Gln ', 'cag': 'Gln ',
    'cgu': 'Arg ', 'cgc': 'Arg ', 'cga': 'Arg ', 'cgg': 'Arg ',
    'auu': 'Ile ', 'auc': 'Ile ', 'aua': 'Ile ',
    'aca': 'Thr ', 'acc': 'Thr ', 'acu': 'Thr ', 'acg': 'Thr ',
    'aau': 'Asn ', 'aac': 'Asn ',
    'aaa': 'Lys ', 'aag': 'Lys ',
    'agu': 'Ser ', 'agc': 'Ser ',
    'aga': 'Arg ', 'agg': 'Arg ',
    'guu': 'Val ', 'guc': 'Val ', 'gua': 'Val ', 'gug': 'Val ',
    'gcu': 'Ala ', 'gcc': 'Ala ', 'gca': 'Ala ', 'gcg': 'Ala ',
    'gau': 'Asp ', 'gac': 'Asp ',
    'gaa': 'Glu ', 'gag': 'Glu ',
    'ggu': 'Gly ', 'ggc': 'Gly ', 'gga': 'Gly ', 'ggg': 'Gly ',
}

#The menu function will display options for the user to test one or two samples. The menu will loop until 
# it is exited by the user. 
def menu(): 
    while True:
        print ("1. Analyze one sample with graph")
        print ("2. Compare two samples")
        print ("Q. Exit")
        choice = input("Please choose from the options above: ")
        if choice == "1":
            Sample_1_1 = input("Please enter file path:")
            main_one(Sample_1_1)
        elif choice == "2":
         Sample_1_2 = input("Please enter file path for sample 1:")
         Sample_2_2 = input("Please enter file path for sample 2:")
         Sam1 = main_two(Sample_1_2)
         Sam2 = main_two(Sample_2_2)
         compare(Sam1, Sam2)
        elif choice == "Q":
            break
        else:
            print ("Invalid choice, please enter 1, 2, or Q.")

#The dna_check function will verify that the DNA sample from the text file is valid
# and contains no errors. It utilizes a valid entries string to ensure that all entries
# are valid.  
def dna_check(data):
    valid_entries = "atcgATCG\n" 
    global errors  
    errors = "" 
    for index, x in enumerate(data):
        if x not in valid_entries:
            errors += (f"\nError location: {index} invalid nucleotide: {x}")
    if errors:
        return True 
    else:
        return False

# The transcription function performs the transcription of the DNA in which every thymine (t) nucleotide is 
# converted into uracil (u).
def transcription(data):
    rna_String = ""
    for x in data:
        if x.find("t") < 0:
            rna_String += x
        else:
            rna_String += "u"
    return rna_String

# The translation function performs translation on the RNA sample which will return an amino acid chain. 
# The RNA string will be read three characters at a time and those three character sequences will be matched
# with the associated amino acid using the codon dictionary. 
def translation(rna_String):
    Aa_chain = ""
    for i in range(0, len(rna_String),3):  
        codon = rna_String[i:i+3]
        if codon in codon_chart:
            amino_acid = codon_chart[codon]
            if amino_acid == "Stop":
                break 
            Aa_chain += amino_acid
    return Aa_chain

#The main_one function contains all the calls necessary to analyze a single DNA sample. It will return information from every step
# as well as a line graph that represents the RNA sample. The RNA sample will be dsplayed in uppercase for readability. 
# The file error messages will be returned in this function if errors are present. 
def main_one(file_path):
    test_rna = ""
    try:
        with open(file_path) as file:
            data = file.read()
        if dna_check(data):
            print (f"\nSample extracted from: {file_path}\nPlease fix errors within DNA sample. {errors}")
        else:
            sample_rna = transcription(data)
            Up_sample_rna = sample_rna.upper() 
            sample_Aa = translation(sample_rna)
            sample_values = nucleotide_value(sample_rna)
            sample_graph = graph(sample_values)
            print (f"\nSample extracted from: {file_path}\nDNA sample is valid. \n RNA sample: {Up_sample_rna} \nAmino acid chain: {sample_Aa}\n{sample_graph}")
    except FileNotFoundError: 
        print (f"File not found: {file_path}") 

# The main_two function is similar to the main_one function, however it will only return a sample's amino acid chain
#  as opposed to all of the information from the steps. This was designed to allow two amino acid chains to be compared. 
def main_two(file_path):
    test_rna = ""
    try:
        with open(file_path) as file:
            data = file.read()
        if dna_check(data):
            print ("Please fix errors within DNA sample.")
        else:
            sample_rna = transcription(data)
            Up_sample_rna = sample_rna.upper()
            sample_Aa = translation(sample_rna)
            return (sample_Aa)
    except FileNotFoundError: 
        print (f"File not found: {file_path}")

# The compare function will compare two amino acid chains. This function will read through both chains and collect
# the same amino acid in the same locations of both chains. 
def compare(AA1, AA2):
    if AA1 == AA2:
        print (f"\nThe amino acid chains are identical.")
    else:
        codon_match = r'\b\w{3}\b'
        match_1 = re.findall(codon_match,AA1) 
        match_2 = re.findall(codon_match, AA2)
        matches = set(match_1) & set(match_2) 
        print (f"\nThe matching amino acids bewteen the two samples are: {matches}")

# The nucleotide_value function will convert an RNA sample into the values 1, 2, 3, and 4 for the purpose 
# of graphing the RNA string. 
def nucleotide_value(rna):
    values = []
    for x in rna:
        if x == "a":
            values.append(1)
        if x == "u":
            values.append(2)
        if x == "c":
            values.append(3)
        if x == "g":
            values.append(4)
    return values
    
# The graph function will take the ennumerated values of the RNA string from the nucleotide_value function 
# and put them in a line graph with the indexed location of each of the nucleotides. 
def graph(rna):
    x = range(1, len(rna)+1)
    y = rna
    plt.plot(x, y)
    plt.xlabel("Nucleotide Position")
    plt.ylabel("Nucleotide Value:\n a = 1, u = 2, c = 3, g = 4")
    plt.show()

menu()
