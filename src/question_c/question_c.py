#write functions here, don't add input('') statements here!

def get_most_likely_ancestor_consensus(dna_string1, dna_string2):
    positions = []
    start = 0
    while True:
        pos = dna_string1.find(dna_string2, start)
        if pos == -1:
            break
        positions.append(pos + 1)  # 1-based position
        start = pos + 1
    return tuple(positions)