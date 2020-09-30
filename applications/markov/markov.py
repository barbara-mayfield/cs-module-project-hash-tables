import random
from collections import defaultdict

# Read in all the words in one go

# Read the file input.txt and split it into words
with open("input.txt") as f:
    words = f.read().split()

# TODO: analyze which words can follow other words
# Your code here
start = []
stop = []
punct = ".?!"
word_dict = defaultdict(list)

for index, word in enumerate(words):
    if word[0].isupper():
        start.append(word)

    if word[-1] in punct:
        stop.append(word[:-1])

    if index < len(words) - 1:
        word_dict[word].append(words[index + 1])

for key, val in word_dict.items():
    print(f"key: {key}: {index} \n")


# TODO: construct 5 random sentences
# Your code here

for line in range(10):
    s = random.choice(start)

    if s not in stop:
        next_word = random.choice(word_dict[s])

        while next_word not in stop:
            s += " " + next_word
            next_word = random.choice(word_dict[next_word])

        s += " " + next_word

    s += random.choice(punct)
    print(f"Sentence: {s}")
