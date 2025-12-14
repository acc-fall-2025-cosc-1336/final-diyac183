#add import
from question_c import get_most_likely_ancestor_consensus

while True:
    # Prompt for DNA string
    while True:
        dna_string1 = input("Enter a DNA string (9-16 characters): ")
        if 8 < len(dna_string1) <= 16:
            break
        else:
            print("Invalid length. Must be greater than 8 and less than or equal to 16 characters.")
    
    # Prompt for DNA substring
    while True:
        dna_string2 = input("Enter a DNA substring (exactly 4 characters): ")
        if len(dna_string2) == 4:
            break
        else:
            print("Invalid length. Must be exactly 4 characters.")
    
    # Call the function
    positions = get_most_likely_ancestor_consensus(dna_string1, dna_string2)
    
    # Display the result
    if positions:
        print(f"Positions: {' '.join(map(str, positions))}")
    else:
        print("No occurrences found.")
    
    # Ask to continue
    choice = input("Do you want to continue? (y/n): ")
    if choice.lower() != 'y':
        break