# Holly White- Genome Seqeuncer 1.5
This project will accept samples of DNA as text files and return 
RNA strings as well as the amino acid chain that is produced from 
the RNA chain. The DNA sample will undergo a series of functions for conversion. 

##Menu will display a menu of options for the user tho choose from when 
analyzing one or two DNA samples. 

##Graph will put the values of an RNA sequence on a line graph to visualize the data. 

##nucleotide_value will assign a value 1-4 to each of the RNA nucleotides (a, u, c, and g)
doing so will allow the data to be visualized in a graph. 

##Error Check 
The DNA sample will first be checked for invalid nucleotide values. 
In other words it will ensure that all values are either a, c, t, or g. 

##Trancription 
The DNA sample will then be turned into an RNA string by converting 
all t values, or thymine nucleotines to u (uracil). 

##Translation 
The RNA string will then be converted to an amino acid chain by 
reading the codons within the RNA string. 

##main_one is the main function that runs when analuzing one sample. 
all information from each step of the process will be printed, and a graph 
of the RNA sequence will be created. 

##main_two is a function that will run everything from main_one but only return 
the amino acid chain. This is so that the amino acid chains can be compared. 

##Compare is a function that will compare two amino acid chains and return a list 
of amino acids that are present in both chains. 