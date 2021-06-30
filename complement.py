def rev_function(dna):
    if dna == "A":
        dna_complement = "T"
        return(dna_complement)
    elif dna == "T":
        dna_complement = "A"
        return(dna_complement)
    elif dna == "C":
        dna_complement = "G"
        return(dna_complement)
    elif dna == "G":
        dna_complement = "C"
        return(dna_complement)

dna = input("Enter a DNA sequence: ")
dna_complement = ""
for i in dna:
    dna_complement = dna_complement + rev_function(i)


s_reverse = ""
i = 0


while i < len(dna):
    s_reverse = s_reverse + dna_complement[3-i]
    i = i + 1


print(dna_complement)
print(s_reverse)
