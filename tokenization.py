
paragraph = "But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful. Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because occasionally circumstances occur in which toil and pain can procure him some great pleasure. To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it? But who has any right to find fault with a man who chooses to enjoy a pleasure that has no annoying consequences, or one who avoids a pain that produces no resultant pleasure?"
pattern = r'[A-Za-z0-9]+'

def white_space(text):
    tokens = text.split()
    return tokens

def bigram(text):
    words = text.split()
    bigrams = [(words[i], words[i + 1]) for i in range(len(words) - 1)]
    return bigrams

def trigram(text):
    words = text.split()
    trigrams = [(words[i], words[i + 1],  words[i + 2]) for i in range(len(words) - 2)]
    return trigrams

def findmatch(pattern, text):
    matches = []
    i = 0
    while i < len(text):
        match = ''
        j = i
        while j < len(text) and text[j].isalnum():
            match += text[j]
            j += 1
        if match:
            matches.append(match)
        i = j + 1
    return matches

def regex(text):
    tokens = findmatch(pattern, text)
    return tokens


print('----- White Space -----')
tokens = white_space(paragraph)
print(tokens)
print('------------------------')
print('\n')

print('----- Bigram -----')
bigrams = bigram(paragraph)
print(bigrams)
print('------------------------')
print('\n')

print('----- Trigram -----')
trigrams = trigram(paragraph)
print(trigrams)
print('------------------------')
print('\n')

print('----- RegEx -----')
tokens = regex(paragraph)
print(tokens)
print('------------------------')
print('\n')