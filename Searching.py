def find(word, letter, index):
    #index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
    return 'Letter is not present in the string...'
