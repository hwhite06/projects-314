import re 

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
def dna_check(data):
    valid_entries = "atcg\n"
    global errors
    errors = ""
    for index, x in enumerate(data):
        if x not in valid_entries:
            errors += (f"\nError location: {index} invalid nucleotide: {x}")
    if errors:
        return True
    else:
        return False

def transcription(data):
    rna_String = ""
    for x in data:
        if x.find("t") < 0:
            rna_String += x
        else:
            rna_String += "u"
    return rna_String

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

def main(file_path):
    test_rna = ""
    try:
        with open(file_path) as file:
            data = file.read()
        if dna_check(data):
            return (f"Please fix errors within DNA sample. {errors}")
        else:
            sample_rna = transcription(data)
            Up_sample_rna = sample_rna.upper()
            sample_Aa = translation(sample_rna)
            return f"DNA sample is valid. \n RNA sample: {Up_sample_rna} \nAmino acid chain: {sample_Aa}"
    except FileNotFoundError: 
        return f"File not found: {file_path}"

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
        return None


def compare_Aa(AA1, AA2):
    if AA1 == AA2:
        return "The amino acid chains are identical."
    else:
        codon_match = r'\b\w{3}\b'
        match_1 = re.findall(codon_match,AA1)
        match_2 = re.findall(codon_match, AA2)
        matches = set(match_1) & set(match_2)
        return f"The matching amino acids bewteen the two samples are: {matches}"


DNA_sample_1 = main("DNA_Random_Sample_1.txt")
DNA_sample_2 = main("DNA_Random_Sample_2.txt")
DNA_sample_3 = main("DNA_Random_Sample_3.txt")
print("Random sample 1:\n", DNA_sample_1)
print("Random sample 2:\n", DNA_sample_2)
print("Random sample 3:\n", DNA_sample_3)

AA_sample_1 = main_Aa("DNA_Random_Sample_1.txt")
AA_sample_2 = main_Aa("DNA_Random_Sample_2.txt")

AA_compare_1 = compare_Aa(AA_sample_1, AA_sample_2)
AA_compare_2 = compare_Aa(AA_sample_1, AA_sample_1)

print(AA_compare_1)
print(AA_compare_2)

