import re 
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

# First I created a funciton that would verify the validity of the DNA sample. 
# This would catch any incorrectly entered nucleotides and return a message asking for the errors
# to be corrected before continuing. 
def dna_check(data):
    valid_entries = "atcgATCG\n" # This string is used to check the validity of the nucleotide entries. 
    global errors # I chose to make the error message a global variable so it could be accessed by the main funciton. 
    errors = ""
    # Because I chose to use strings throughout most of this program, I did have to use
    # the enumerate function in order to discern the location of the erros in the string. 
    for index, x in enumerate(data):
        if x not in valid_entries:
            errors += (f"\nError location: {index} invalid nucleotide: {x}")
    if errors:
        return True 
    else:
        return False

# This function performed the transcription of the data in which every thymine (t) nucleotide is 
# converted into uracil (u).
def transcription(data):
    rna_String = ""
    for x in data:
        if x.find("t") < 0:
            rna_String += x
        else:
            rna_String += "u"
    return rna_String

# This function performs the actual translation of the data by matching every 3 letters in the string 
# it is given to the keys of the codon chart above and adds the value of the codon to a new string.
def translation(rna_String):
    Aa_chain = ""
    for i in range(0, len(rna_String),3): # I needed to use range and len functions to count the string in sets of 3 characters. 
        codon = rna_String[i:i+3]
        if codon in codon_chart:
            amino_acid = codon_chart[codon]
            if amino_acid == "Stop":
                break # The stop codon will stop the amino acid chain construstion.
            Aa_chain += amino_acid
    return Aa_chain

# This main function takes a text file and runs all of the necessary functions at once. 
# This function will return all of the information about each sample at once. 
def main(file_path):
    test_rna = ""
    try:
        with open(file_path) as file:
            data = file.read()
        if dna_check(data):
            return (f"\nSample extracted from: {file_path}\nPlease fix errors within DNA sample. {errors}")
        else:
            sample_rna = transcription(data)
            Up_sample_rna = sample_rna.upper() # This will turn the rna sample to uppercase for display purposes. 
            sample_Aa = translation(sample_rna)
            return f"\nSample extracted from: {file_path}\nDNA sample is valid. \n RNA sample: {Up_sample_rna} \nAmino acid chain: {sample_Aa}"
    except FileNotFoundError: 
        return f"File not found: {file_path}" # This is an error I included for if the file is not found. 

# I created a function similar to main that will only return the amino acid chain, I did this in order
# to compare two amino acid chains directly, while still keeping a main function that will return everything with a single call. 
def main_Aa(file_path):
    test_rna = ""
    try:
        with open(file_path) as file:
            data = file.read()
        if dna_check(data):
            return ("Please fix errors within DNA sample.")
        else:
            sample_rna = transcription(data)
            Up_sample_rna = sample_rna.upper()
            sample_Aa = translation(sample_rna)
            return sample_Aa
    except FileNotFoundError: 
        return f"File not found: {file_path}"


# This function uses regular expressions to compare 2 amino acid chains produced from the main AA function. 
def compare_Aa(AA1, AA2):
    if AA1 == AA2:
        return f"\nThe amino acid chains are identical."
    else:
        codon_match = r'\b\w{3}\b' # This is the regular expression that will check for exactly 3 characters within both of the AA chains that match. 
        match_1 = re.findall(codon_match,AA1) # This will automatically catch all of the amino acids in the chain.
        match_2 = re.findall(codon_match, AA2)
        matches = set(match_1) & set(match_2) # This will combine the matches that are within both chains to be displayed in one set.
        return f"\nThe matching amino acids bewteen the two samples are: {matches}"


DNA_sample_1 = main("DNA_Random_Sample_1.txt")
DNA_sample_2 = main("DNA_Random_Sample_2.txt")
DNA_sample_3 = main("DNA_Random_Sample_3.txt")
print(DNA_sample_1) # This sample is random with no errors. 
print(DNA_sample_2) # This sample is random with no errors. 
print(DNA_sample_3) # This sample is random with 3 errors. 

AA_sample_1 = main_Aa("DNA_Random_Sample_1.txt") 
AA_sample_2 = main_Aa("DNA_Random_Sample_2.txt")
AA_compare_1 = compare_Aa(AA_sample_1, AA_sample_2)
AA_compare_2 = compare_Aa(AA_sample_1, AA_sample_1)
print("\nAA chain 1 compared to AA chain 2:", AA_compare_1) # Comparison of amino acid chains 1 and 2.
print("\nAA chain 1 compared to AA chain 1:", AA_compare_2) # Comparison of amino acid chains 1 and 1. 

