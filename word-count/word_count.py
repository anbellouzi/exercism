import enchant


def count_words(sentence):
    hist = {}
    for c in sentence:
        if not c.isalnum():
            sentence = sentence.replace(c, " ")

    for word in sentence.split():
        word = word.lower()

        if word not in hist.keys():
            hist[word] = 1
        else:
            hist[word] += 1

    return hist


print(count_words("one fish two fish red fish blue fish"))

