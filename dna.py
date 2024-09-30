from csv import DictReader
from sys import argv


def main():

    rows = []
    keys = []
    flag = False

    # TODO: Check for command-line usage
    if len(argv) != 3:
        print("INVALID input")
        return

    # TODO: Read database file into a variable
    with open(argv[1]) as known_info_csv:
        reader = DictReader(known_info_csv)
        for row in reader:
            rows.append(row)
            if flag == False:
                flag = True
                keys.append(row.keys())
                keys = list(keys[0])
                keys.pop(0)

    # TODO: Read DNA sequence file into a variable
    dna = ""
    f = open(argv[2], 'r')
    read = f.read(1)
    while read != '':
        dna += read
        read = f.read(1)

    # TODO: Find longest match of each STR in DNA sequence
    str_seq = []
    for seq in keys:
        str_seq.append(str(longest_match(dna, seq)))

    # TODO: Check database for matching profiles
    for row in rows:
        value = list(row.values())
        value.pop(0)
        if value == str_seq:
            print(list(row.values())[0])
            return

    print("No match")
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
