with open('/home/kodolamacz/Downloads/text_sample.txt', 'r') as readfile:
    dane = readfile.read()
print(dane)


import string

def word_stats(filename, words):
    stats = {}
    with open(filename, 'r') as f:
        words = f.read().split()
    for word in words:
        word = word.lower().strip(string.punctuation)
        stats.setdefault(word, 0)
        stats[word] +=1
    return stats


def word_stats2(filename, words):
    stats = {}
    with open(filename, 'r') as f:
        words = f.read().split()
    for word in words:
        word = word.lower().strip(string.punctuation)
        if word not in stats:
            stats[word] = 0
        stats[word] += 1
    return stats


print(word_stats('/home/kodolamacz/Downloads/text_sample.txt', ["the", "off"]))
