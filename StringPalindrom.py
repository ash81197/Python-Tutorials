def is_reverse(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    if len(word1) != len(word2):
        return False
    i = 0
    j = len(word2) - 1
    while j > 0:
        if word1[i] != word2[j]:
            return False
        i+=1
        j-=1
    return True

is_reverse('pots', 'stop')

