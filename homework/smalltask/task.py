def find_letter_occurrences(list_of_strings, letter):
    letter = letter.lower()
    return sum(1 for string in list_of_strings if letter in string.lower())