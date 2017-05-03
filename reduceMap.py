n = open("nature.txt", "r")
info = n.read().split()
n.close()

text = [word.strip('()",.') for word in info]

def add(a, b):
    return a + b

def frequency(word):
    word = word.lower()
    words = filter(lambda letter: word in letter.lower(), text)
    times = map(lambda x: 1, words)
    num = reduce(add, times)
    return num

print "frequency of 'the':"
print frequency("the")

def totalFreq(words):
    words = map(lambda x: x.lower(), words)
    freq = map(lambda x: frequency(x), words)
    total = reduce(add, freq)
    return total

print "total frequency of 'the', 'it', 'they':"
print totalFreq(['the','it','they'])

def mostFreq():
    answer = sorted([(w, text.count(w)) for w in set(text)], key = lambda x:x[1], reverse=True)[:1][0]
    return answer

print "most frequent word:"
print mostFreq()
