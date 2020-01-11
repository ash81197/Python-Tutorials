# Printing the content of a file
fin = open('words.txt')
for line in fin:
    word = line.strip()
    #print(word)

# Printing word that has greater than 20 characters
fin = open('words.txt')
for line in fin:
    word = line.strip()
    if len(word) >= 20:
        print(word)

# Seaching for letter 'e'
def has_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
    return True
    
    
