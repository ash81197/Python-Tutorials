def counter(word, letter):
    index = 0
    count = 0
    for eachLetter in word: #eachLetter can not be written as letter
    #while index < len(word):  -- this can be used
        if word[index] == letter:
            count+=1
        index+=1
    print(count)

counter("Hello banana", 'a')
